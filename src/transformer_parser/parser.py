from enum import Enum
from typing import List, Dict
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
    def test(self, token_ids: List[int]) -> MatchResult:
        '''
        Tests the provided token ids to see if they are considered valid.
        Returns a match result that gives instructions on what to do with the token.
        '''
        pass

class GrammarRule:
    def __init__(self, id: int, rule_type: int, token_matchers: List[TokenMatcher]):
        self.rule_type = rule_type
        self.token_matchers = token_matchers

class Grammar:
    def __init__(self, rules: List[GrammarRule]):
        self._rules = rules

    def get_root_rule(self) -> GrammarRule:
        pass

# TODO This works great for the result of a matcher, but maybe we need to use inheritance so that we can express other things, like an end of branch or new rule result.
class ParseResult:
    def __init__(self, is_valid: bool, cur_rule_type: int, cur_matcher_id: int, matched_ids: List[int], is_match_complete: bool):
        self.is_valid = is_valid
        self.cur_rule_type = cur_rule_type
        self.cur_matcher_id = cur_matcher_id
        self.matched_ids = matched_ids
        self.is_match_complete = is_match_complete

class RuleNode:
    def __init__(self, rule: GrammarRule):
        self._token_ids: List[int] = []
        self._rule = rule
        self._cur_matched_ids: List[int] = []
    
    def test_token(self, token_id: int) -> ParseResult:
        # The grammar rules need to be consulted to check if this token is valid according to the matchers.
        self._token_ids.append(token_id)
        self._cur_matched_ids.append(token_id)

        return ParseResult(True, 1, 2, self._cur_matched_ids, True)
    
    def apply_token(self, token_id: int, parse_result: ParseResult):
        pass

class TransformerParser:
    def __init__(self, vocabulary: Vocabulary, grammar: Grammar):
        self._vocabulary = vocabulary
        self._grammar = grammar
        self.reset()


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # TODO For beam searching we need to support the ability to test a few different tokens. 


    def test_token(self, token_id: int) -> ParseResult:
        '''
        This tests the provided token id against the current history of tokens in the parse tree. It will only account for the matching of the grammar and will return
        results relating to the current matcher and whether the match is incomplete or not.
        '''
        if token_id == SpecialTokenTypes.END_BRANCH:
            # Check if an end branch completes the current RuleNode (for is_valid) and then move self._cur_rule_node up one node.
            return ParseResult(is_valid = True, cur_rule_type = -1, cur_matcher_id = -1, matched_ids = [token_id], is_match_complete = True)
        else:
            return self._cur_rule_node.test_token(token_id)
        
    def get_next_possible_tokens(self) -> List[int]:
        '''
        Based on the current matcher being used in the parse tree, this will return all of the possible tokens that are valid.
        This could be used to restrict the vocabulary to help train a transformer to only take into consideration the valid tokens.
        '''
        # We can get these tokens from the current matcher.
        pass
        
    def apply_token(self, token_id: int, parse_result: ParseResult):
        '''
        After testing to see if a token is valid and what matcher it applies to, this will save the token to the parse tree.
        This should be used when a valid token has been selected for the current beam and before a subsequent token is tested.
        '''
        assert parse_result.is_valid
    
    def reset(self):
        self._rule_tree = RuleNode(self._grammar.get_root_rule())
        self._cur_rule_node = self._rule_tree
