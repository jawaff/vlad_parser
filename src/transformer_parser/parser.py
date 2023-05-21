# https://peps.python.org/pep-0563/
from __future__ import annotations
from enum import Enum
from typing import List, Dict, Optional, Union
from abc import ABC, abstractmethod
 
class SpecialTokenTypes(Enum):
    END_BRANCH = 1
    
class Vocabulary:
    def __init__(self, token_id_types: Dict[int, int]):
        '''
        A token id can only map to a single type. The mapping must not have any ambiguity. All of the grammar rules that refer to a branch will need to be special token ids that
        are not used in literal expressions.
        '''
        self._token_id_types = token_id_types

class MatchResult(Enum):
    INVALID = 1
    VALID_NOT_DONE = 2
    VALID_DONE = 3
    DONE_RETRY_NEXT_MATCHER = 4

class TokenMatcher(ABC):
    @abstractmethod
    def get_id(self) -> int:
        ''''
        Returns the id of this token matcher.
        '''
        pass

    @abstractmethod
    def is_optional(self) -> bool:
        '''
        Returns true if the current matcher is optional and whether the next matcher should be consulted.

        TODO Do we need this since there will be optional matchers? We probably need to skip optional and backtrack to them if necessary.
        '''
        pass

    @abstractmethod
    def test(self, token_ids: List[int]) -> MatchResult:
        '''
        Tests the provided token ids to see if they are considered valid.
        Returns a match result that gives instructions on what to do with the token.
        '''
        pass

class GrammarRule:
    def __init__(self, id: int, rule_type: int, token_matchers: List[TokenMatcher]):
        assert len(token_matchers) > 0
        self.rule_type = rule_type
        self._token_matchers = token_matchers
        self._matcher_index = 0
    
    def test_tokens(self, token_ids: List[int]):
        pass

    def complete_matcher(self) -> bool:
        '''
        Moves to the next matcher and returns true if there are no more matchers in this rule.
        '''
        self._matcher_index += 1

        # TODO Check if there are no more matchers.
        return False

class Grammar:
    def __init__(self, root_rule: GrammarRule, rules: List[GrammarRule]):
        self._root_rule = root_rule
        self._rules = rules

    def get_root_rule(self) -> GrammarRule:
        return self._root_rule

class ParseResultType(Enum):
    NEW_RULE_RESULT = 1
    END_RULE_RESULT = 2
    MATCH_RESULT = 3

class ParseResult:
    def __init__(self, type: ParseResultType, is_valid: bool):
        self.type = type
        self.is_valid = is_valid

class NewRuleResult(ParseResult):
    '''
    This specifies that the current rule should be paused while a sub-rule is being processed.
    '''
    def __init__(self, new_rule: GrammarRule):
        ParseResult.__init__(ParseResultType.NEW_RULE_RESULT, True)
        self.new_rule = new_rule

class EndRuleResult(ParseResult):
    '''
    This specifies that a rule has been fully matched and that the parent rule can resume its matching.
    This is different than the completion of a matcher, because a rule can contain multiple matchers.
    Matchers allow us to get the values of something within a rule, like a table's column. A rule is a combination of matchers.
    '''
    def __init__(self):
        ParseResult.__init__(ParseResultType.END_RULE_RESULT, True)

class MatchResult(ParseResult):
    '''
    This is the most common result, which will provide information about the current matcher and matched token ids within the current rule.
    A WHERE clause in SQL might have a column matcher and this result will specify which token ids make up the matched column and whether the match can 
    be considered complete.

    It's unsure if the completion flag is able to be definitive or just a suggestion. It depends on how well the matchers turn out. There might be additional
    tokens that can be applied to the current matcher. There might be a need for a maybe complete flag and a definitively complete flag. For the maybe complete
    case we'll attempt to see if it applies to the current matcher and if not valid it will be applied to the next matcher.
    '''
    def __init__(self, is_valid: bool, cur_rule_type: int, cur_matcher_id: int, matched_ids: List[int], is_match_complete: bool):
        ParseResult.__init__(ParseResultType.MATCH_RESULT, is_valid)
        self.cur_rule_type = cur_rule_type
        self.cur_matcher_id = cur_matcher_id
        self.matched_ids = matched_ids
        self.is_match_complete = is_match_complete
        
class RuleNode(list):
    def __init__(self, parent: Optional[RuleNode], rule: GrammarRule):
        # The list's contents will be the ordered child rule nodes.
        list.__init__(self, [])
        # The rule node starts with no children, so the index is -1.
        self.cur_child_index = -1
        self.parent = parent
        self._token_ids: List[int] = []
        self._rule = rule
        self._cur_matched_ids: List[int] = []
    
    def test_token(self, token_id: int) -> ParseResult:
        tmp_tokens = self._cur_matched_ids[:]
        tmp_tokens.append(token_id)
        return self._rule.test_tokens(tmp_tokens)
    
    def apply_token(self, token_id: int, parse_result: MatchResult) -> bool:
        assert parse_result.type == ParseResultType.MATCH_RESULT

        self._token_ids.append(token_id)

        is_rule_done = False
        # If the parse result specifies that the previous matcher was complete, then we reset the matched ids.
        if (parse_result.is_match_complete):
            self.reset_matched_ids
            is_rule_done = self.rule.complete_matcher()
        self._cur_matched_ids.append(token_id)
        return is_rule_done

    def reset_matched_ids(self):
        del self._cur_matched_ids[:]

    def get_next_child(self) -> RuleNode:
        '''
        Increments the current child index and retrieves the relevant child of this rule node.
        '''
        self.cur_child_index += 1
        # TODO I'm pretty sure we don't have to deal with navigating down this child's tree to the first branch...
        # Also, we should make sure there's a plan for appending children to this rule's list of children so that this actually works.
        return self[self.cur_child_index]
    
    def has_next_child(self) -> bool:
        '''
        Returns true if there is a next child.
        '''
        return self.cur_child_index + 1 < self.length

class TransformerParser:
    def __init__(self, vocabulary: Vocabulary, grammar: Grammar):
        self._vocabulary = vocabulary
        self._grammar = grammar
        self.reset()

    def test_token(self, token_id: int) -> ParseResult:
        '''
        This tests the provided token id against the current history of tokens in the parse tree. It will only account for the matching of the grammar and will return
        results relating to the current matcher and whether the match is incomplete or not.
        '''
        if token_id == SpecialTokenTypes.END_BRANCH:
            # Check if an end branch completes the current RuleNode (for is_valid) and then move self._cur_rule_node up one node.
            return EndRuleResult()
        else:
            return self._cur_rule_node.test_token(token_id)
        
    def get_next_possible_tokens(self) -> List[int]:
        '''
        Based on the current matcher being used in the parse tree, this will return all of the possible tokens that are valid.
        This could be used to restrict the vocabulary to help train a transformer to only take into consideration the valid tokens.
        '''
        # We can get these tokens from the current matcher.
        pass
        
    def apply_token(self, token_id: int, parse_result: Union[NewRuleResult, EndRuleResult, MatchResult]):
        '''
        After testing to see if a token is valid and what matcher it applies to, this will save the token to the parse tree.
        This should be used when a valid token has been selected for the current beam and before a subsequent token is tested.
        '''
        assert parse_result.is_valid
        if (parse_result.type == ParseResultType.END_RULE_RESULT):
            # The current rule node's matched_ids should be reset because that matcher has completed.
            self._cur_rule_node.reset_matched_ids()

            # Move cur_rule_node to its parent because the current rule is done.
            self._cur_rule_node = self._cur_rule_node.parent

        elif (parse_result.type == ParseResultType.NEW_RULE_RESULT):
            # The current rule node's matched_ids should be reset because that matcher has completed.
            self._cur_rule_node.reset_matched_ids()

            # Add the new rule as a child to the current rule node and set that new rule node as the current node.
            new_node = RuleNode(self._cur_rule_node, parse_result.new_rule)
            self._cur_rule_node.append(new_node)
            self._cur_rule_node = new_node

        else:
            is_rule_done = self._cur_rule_node.apply_token(token_id, parse_result)
            # TODO TODO TODO Are we sure that having the list of rules here is going to be possible? Our NEW_RULE_RESULT currently only provides a single rule that is appended to the
            # current node. Maybe that should be a list? Or maybe we can simplify things by only dealing with a single rule instead of a list of children for each node.
            if is_rule_done:
                if self._cur_rule_node.parent != None and self._cur_rule_node.parent.has_next_child():
                    next_node = self._cur_rule_node.parent.get_next_child()
                else:
                    pass


    def reset(self):
        del self._rule_tree
        del self._cur_rule_node
        self._rule_tree = RuleNode(None, self._grammar.get_root_rule())
        self._cur_rule_node = self._rule_tree
