import unittest

from transformer_parser.parser import TransformerParser, Grammar, ParseResult, NewRuleResult, MatchResult, ParseResultType, CompletionType
from transformer_parser.token_matchers import LiteralTokenMatcher


class TestParser(unittest.TestCase):
    def assertParseResultsEqual(self, result1: ParseResult, result2: ParseResult):
        self.assertEqual(result1.type, result2.type)
        if result1.type == ParseResultType.MATCH_RESULT:
            self.assertEqual(result1.is_valid, result2.is_valid)
            self.assertEqual(result1.cur_rule_id, result2.cur_rule_id)
            self.assertEqual(result1.matched_token_ids, result2.matched_token_ids)
            self.assertEqual(result1.matched_matcher_index, result2.matched_matcher_index)
            self.assertEqual(result1.rule_completion, result2.rule_completion)
        elif result1.type == ParseResultType.NEW_RULE_RESULT:
            self.assertEqual(result1.is_valid, result2.is_valid)
            self.assertEqual(result1.new_rule_id, result2.new_rule_id)
        else:
            raise Exception(f'Unsupported parse result type: {result1.type}')

    def test_simple_three_levels(self):
        rm1 = LiteralTokenMatcher(token_ids={1: None}, is_optional=False, matches_multiple=False)
        root_matchers = [rm1]
        m1 = LiteralTokenMatcher(token_ids={2: None}, is_optional=False, matches_multiple=False)
        m2 = LiteralTokenMatcher(token_ids={3: None}, is_optional=False, matches_multiple=False)
        m3 = LiteralTokenMatcher(token_ids={4: None}, is_optional=False, matches_multiple=False)
        m4 = LiteralTokenMatcher(token_ids={5: None}, is_optional=False, matches_multiple=False)
        m5 = LiteralTokenMatcher(token_ids={6: None}, is_optional=False, matches_multiple=False)
        m6 = LiteralTokenMatcher(token_ids={7: None}, is_optional=False, matches_multiple=False)
        grammar = Grammar(root_rule=root_matchers, rules={1: [m1, m4], 2: [m2, m3], 5: [m5, m6]})
        parser = TransformerParser(grammar)

        # According to the grammar, this parser will only accept the token sequence: 1, 2, 3, 4, 5, 6.

        results = parser.test_token(1)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1], matched_matcher_index=0, rule_completion=CompletionType.COMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=1))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(1, results)

        results = parser.test_token(2)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=2))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(2, results)

        results = parser.test_token(3)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=[3], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(3, results)

        results = parser.test_token(4)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=[3, 4], matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(4, results)

        results = parser.test_token(5)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2, 5], matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=5))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(5, results)

        results = parser.test_token(6)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=[6], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(6, results)

        results = parser.test_token(7)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=[6, 7], matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(7, results)
        self.assertEqual(parser.is_complete(), CompletionType.COMPLETE)

    def test_simple_one_level(self):
        rm1 = LiteralTokenMatcher(token_ids={1: None}, is_optional=False, matches_multiple=False)
        rm2 = LiteralTokenMatcher(token_ids={2: None}, is_optional=False, matches_multiple=False)
        rm3 = LiteralTokenMatcher(token_ids={3: None}, is_optional=False, matches_multiple=False)
        root_matchers = [rm1, rm2, rm3]
        grammar = Grammar(root_rule=root_matchers, rules={})
        parser = TransformerParser(grammar)

        # According to the grammar, this parser will only accept the token sequence: 1, 2, 3

        results = parser.test_token(1)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(1, results)

        results = parser.test_token(2)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1, 2], matched_matcher_index=1, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(2, results)

        results = parser.test_token(3)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1, 2, 3], matched_matcher_index=2, rule_completion=CompletionType.COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(3, results)
        self.assertEqual(parser.is_complete(), CompletionType.COMPLETE)

    def test_simple_two_levels(self):
        rm1 = LiteralTokenMatcher(token_ids={1: None}, is_optional=False, matches_multiple=False)
        rm2 = LiteralTokenMatcher(token_ids={3: None}, is_optional=False, matches_multiple=False)
        rm3 = LiteralTokenMatcher(token_ids={5: None}, is_optional=False, matches_multiple=False)
        root_matchers = [rm1, rm2, rm3]
        m1 = LiteralTokenMatcher(token_ids={2: None}, is_optional=False, matches_multiple=False)
        m2 = LiteralTokenMatcher(token_ids={4: None}, is_optional=False, matches_multiple=False)
        m3 = LiteralTokenMatcher(token_ids={6: None}, is_optional=False, matches_multiple=False)
        grammar = Grammar(root_rule=root_matchers, rules={1: [m1], 3: [m2], 5: [m3]})
        parser = TransformerParser(grammar)

        # According to the grammar, this parser will only accept the token sequence: 1, 2, 3, 4, 5, 6.

        results = parser.test_token(1)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=1))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(1, results)

        results = parser.test_token(2)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2], matched_matcher_index=0, rule_completion=CompletionType.COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(2, results)

        results = parser.test_token(3)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1, 3], matched_matcher_index=1, rule_completion=CompletionType.INCOMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=3))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(3, results)

        results = parser.test_token(4)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=3, matched_token_ids=[4], matched_matcher_index=0, rule_completion=CompletionType.COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(4, results)

        results = parser.test_token(5)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1, 3, 5], matched_matcher_index=2, rule_completion=CompletionType.COMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=5))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(5, results)

        results = parser.test_token(6)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=[6], matched_matcher_index=0, rule_completion=CompletionType.COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(6, results)
        self.assertEqual(parser.is_complete(), CompletionType.COMPLETE)


if __name__ == '__main__':
    unittest.main()
