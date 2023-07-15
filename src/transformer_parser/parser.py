# https://peps.python.org/pep-0563/
from __future__ import annotations
from enum import Enum
from typing import List, Dict, Optional, Union
from abc import ABC, abstractmethod
from dataclasses import dataclass

class TokenMatcher(ABC):
    @abstractmethod
    def is_optional(self) -> bool:
        '''
        Returns true if the current matcher is optional and whether the next matcher should be consulted.
        '''
        pass

    @abstractmethod
    def matches_multiple(self) -> bool:
        '''
        Returns true if the current matcher matches multiple tokens.
        '''
        pass

    @abstractmethod
    def test_token(self, token_id: int) -> bool:
        '''
        Tests the provided token id to see if it are considered valid for this matcher.
        Returns true if the token is valid and false if invalid.
        '''
        pass

class ParseResultType(Enum):
    NEW_RULE_RESULT = 1
    MATCH_RESULT = 2

@dataclass
class ParseResult:
    type: ParseResultType
    # This field is the only one meant to be updated outside of the parser for results!
    # Update this field to deny tokens which are valid by the grammar and invalid according to the context as witnessed by the application using this parser.
    is_valid: bool

@dataclass(init=False)
class NewRuleResult(ParseResult):
    new_rule_id: int

    def __init__(self, is_valid: bool, new_rule_id: int):
        ParseResult.__init__(self, type=ParseResultType.NEW_RULE_RESULT, is_valid=is_valid)
        self.new_rule_id = new_rule_id

    def __eq__(self, obj):
        return isinstance(obj, NewRuleResult) and obj.is_valid == self.is_valid and obj.new_rule_id == self.new_rule_id

class CompletionType(Enum):
    INCOMPLETE = 1
    MAYBE_COMPLETE = 2
    COMPLETE = 3

@dataclass(init=False)
class MatchResult(ParseResult):
    '''
    This is the most common result, which will provide information about the current rule and the matched token literals.
    This type of result should be for simple literals such as a column name, table alias or a long list of arbitrary text.

    The completion flag will specify the state of the matching within the current rule.
    '''
    cur_rule_id: int
    matched_token_ids: List[int]
    matched_matcher_index: int
    rule_completion: CompletionType

    def __init__(self, is_valid: bool, cur_rule_id: int, matched_token_ids: List[int], matched_matcher_index: int, rule_completion: CompletionType):
        ParseResult.__init__(self, type=ParseResultType.MATCH_RESULT, is_valid=is_valid)
        self.cur_rule_id = cur_rule_id
        self.matched_token_ids = matched_token_ids
        self.matched_matcher_index = matched_matcher_index
        self.rule_completion = rule_completion

    def __eq__(self, obj):
        return isinstance(obj, MatchResult) \
            and obj.is_valid == self.is_valid \
            and obj.cur_rule_id == self.cur_rule_id \
            and obj.matched_token_ids == self.matched_token_ids \
            and obj.matched_matcher_index == self.matched_matcher_index \
            and obj.rule_completion == self.rule_completion

    def __repr__(self):
        return f'MatchResult(is_valid={self.is_valid}, cur_rule_id={self.cur_rule_id}, matched_token_ids={self.matched_token_ids}, matched_matcher_index={self.matched_matcher_index}, rule_completion={self.rule_completion})'
    
class RuleNode(ABC, list):
    def __init__(self, parent: Optional[RuleNode], id: Optional[int], token_matchers: List[TokenMatcher]):
        # The list's contents will be the ordered child rule nodes.
        list.__init__(self, [])
        assert len(token_matchers) > 0
        self.parent = parent
        self.id = id
        self._token_matchers = token_matchers
        self._matcher_index = 0
        self._cur_multiple_matcher_has_match = False
    
    @abstractmethod
    def is_branch(self) -> bool:
        pass

    @abstractmethod
    def test_token(self, token_id: int) -> ParseResult:
        pass
    
    @abstractmethod
    def apply_token(self, token_id: int, parse_result: MatchResult):
        pass

    def is_complete(self) -> bool:
        return self._matcher_index >= len(self._token_matchers)
    
    def is_maybe_complete(self, start_matcher_index: Optional[int]) -> bool:
        '''
        Returns True if this rule is maybe complete starting at the current matcher index or the one that is provided and Fac lse otherwise.
        '''
        if start_matcher_index == None:
            start_matcher_index = self._matcher_index

        maybe_complete = True
        # If the rest of the matchers are considered optional, then we'll say that this rule is maybe complete.
        for opt_matcher_index in range(start_matcher_index, len(self._token_matchers)):
            # Again, if the current multiple matcher has a match, then it is considered optional
            if not self._token_matchers[opt_matcher_index].is_optional():
                maybe_complete = False
                break
        return maybe_complete

class GrammarRule(RuleNode):
    def __init__(self, parent: Optional[RuleNode], id: Optional[int], token_matchers: List[TokenMatcher]):
        RuleNode.__init__(self, parent, id, token_matchers)
        self._token_ids: List[int] = []

    def is_branch(self) -> bool:
        return False

    def test_token(self, token_id: int) -> ParseResult:
        # Note: While testing tokens we cannot save any state! Multiple tokens will be tested to check for validity and then one will be chosen.

        found_match = False
        matched_matcher_index = self._matcher_index
        # Iterate the matchers starting at the current matcher.
        # The first matcher that matches against the token will receive priority. If we have no match and the matcher is optional or a multiple matcher with a match, then
        # we will move to the next matcher to check against it.
        for matcher_index in range(self._matcher_index, len(self._token_matchers)):
            if self._token_matchers[matcher_index].test_token(token_id):
                matched_matcher_index = matcher_index
                found_match = True
                break
            # Priority is given to the current matcher, which is why we only move to the next matcher on the condition that the current matcher doesn't have a match.
            elif self._token_matchers[matcher_index].is_optional():
                continue
            # If we're still on the first matcher and this multiple matcher already has a match, then we can move to the next matcher to check for a match.
            # TODO The matches multiple check may not be necessary due to cur_multiple_matcher_has_match only being true for multiple matchers.
            elif matcher_index == self._matcher_index and self._cur_multiple_matcher_has_match and self._token_matchers[matcher_index].matches_multiple():
                continue
        
        matched_token_ids = self._token_ids[:]
        if found_match:
            matched_token_ids.append(token_id)

        completion = CompletionType.INCOMPLETE
        # We only enter a complete state when all of the matchers are undoubtedly matched.
        # If the final matcher allows for multiple matches, then we'll have to rely on an explicit rule change.
        if found_match and matched_matcher_index == (len(self._token_matchers) - 1) and not self._token_matchers[matched_matcher_index].matches_multiple():
            completion = CompletionType.COMPLETE
        # If we found a match, then the matched matcher is maybe complete regardless if it matches multiple, is optional, or required.
        elif found_match and self.is_maybe_complete(matched_matcher_index + 1):
            completion = CompletionType.MAYBE_COMPLETE
        elif self.is_maybe_complete(matched_matcher_index):
            completion = CompletionType.MAYBE_COMPLETE

        return MatchResult(found_match, self.id, matched_token_ids, matched_matcher_index, completion)


    def apply_token(self, token_id: int, parse_result: MatchResult):
        assert parse_result.type == ParseResultType.MATCH_RESULT

        # Only matched tokens should be applied.
        if parse_result.is_valid:
            self._token_ids.append(token_id)
            if self._token_matchers[parse_result.matched_matcher_index].matches_multiple():
                # This matcher (new or old) matches multiple, so we need to save that we've already matched a token with it.
                self._cur_multiple_matcher_has_match = True
                self._matcher_index = parse_result.matched_matcher_index
            else:
                self._cur_multiple_matcher_has_match = False
                # We only move the matcher index if we've confirmed that the matcher is complete.
                # This matcher doesn't match multiple.
                self._matcher_index = parse_result.matched_matcher_index + 1
        
@dataclass(frozen=True)
class Grammar:
    root_rule: List[TokenMatcher]
    # Maps rule ids to the relevant token matchers.
    rules: Dict[int, List[TokenMatcher]]

class TransformerParser:
    def __init__(self, grammar: Grammar):
        self._grammar = grammar
        self.reset()

    def test_token(self, token_id: int) -> List[ParseResult]:
        '''
        This tests the provided token id against the current history of tokens in the parse tree.
        Returns the result of the current matcher and possibly a second result if a new rule node has been reached.
        '''
        # Design Note: We start at the current node and move along the parent nodes testing each of them for as long as they are maybe complete.
        # If a rule node has been matched, then we stop.

        results = []
        done = False
        target_rule_node = self._cur_rule_node
        while not done:
            result = target_rule_node.test_token(token_id)
            results.append(result)

            # If the token matched, then we're done.
            if result.is_valid:
                done = True
            # If the token didn't match the current rule while that rule is maybe complete, then we can check the next rule.
            # If the next rule is maybe complete, then we can continue checking the next rules until we've found a match.
            elif target_rule_node.is_maybe_complete(None):
                target_rule_node = target_rule_node.parent
            # If the token didn't match and the rule node isn't maybe complete, then we're done.
            else:
                done = True

        # If this token id is a rule id, then we should add a new rule result to the results so that the grammar rule can be added to the stack.
        if results[-1].is_valid and token_id in self._grammar.rules:
            results.append(NewRuleResult(True, token_id))

        return results
        
    def get_next_possible_tokens(self) -> List[int]:
        '''
        Based on the current matcher being used in the parse tree, this will return all of the possible tokens that are valid.
        This could be used to restrict the vocabulary to help train a transformer to only take into consideration the valid tokens.
        '''
        # We can get these tokens from the current matcher.
        pass
        
    def apply_token(self, token_id: int, parse_results: List[ParseResult]):
        '''
        After testing to see if a token is valid and what matcher it applies to, this will save the token to the parse tree.
        This should be used when a valid token has been selected for the current beam and before a subsequent token is tested.
        '''
        target_rule_node = self._cur_rule_node
        # Parse results start at the current rule node and each successive one applies to the parent if it's a match result.
        # New rule results will result in a new rule node being added to whatever is the target node in this loop.
        for index, parse_result in enumerate(parse_results):
            if parse_result.type == ParseResultType.NEW_RULE_RESULT:
                # Add the new rule as a child to the current rule node and set that new rule node as the current node.
                new_node = GrammarRule(target_rule_node, parse_result.new_rule_id, self._grammar.rules[parse_result.new_rule_id])

                # The new node should be added to the end of the current rule node.
                target_rule_node.append(new_node)
                self._cur_rule_node = new_node
                break
            elif parse_result.type == ParseResultType.MATCH_RESULT:
                if parse_result.is_valid:
                    target_rule_node.apply_token(token_id, parse_result)
                    # If we've completed the current rule and this is the last match result, then we go down the parent tree until we find an incomplete rule or None.
                    # We can't do this if the next result is a new rule result, because that one will be added to the current rule node.
                    if index == len(parse_results) - 1:
                        while target_rule_node != None and target_rule_node.is_complete():
                            target_rule_node = target_rule_node.parent
                        # The next incomplete rule node will be our current rule node.
                        self._cur_rule_node = target_rule_node
                # Invalid results will be ignored because their rule nodes are maybe complete. In that case, we skip to the next
                # parent node.
                else:
                    target_rule_node = self._cur_rule_node.parent
            else:
                raise Exception(f'Unsupported result type: {parse_result.type}')

    def reset(self):
        self._rule_tree = GrammarRule(None, None, self._grammar.root_rule)
        self._cur_rule_node = self._rule_tree

    def is_complete(self) -> CompletionType:
        if self._cur_rule_node == None:
            return CompletionType.COMPLETE
        elif self._cur_rule_node.parent == None:
            if self._cur_rule_node.is_complete():
                return CompletionType.COMPLETE
            elif self._cur_rule_node.is_maybe_complete(None):
                return CompletionType.MAYBE_COMPLETE
            else:
                return CompletionType.INCOMPLETE
        else:
            return CompletionType.INCOMPLETE
