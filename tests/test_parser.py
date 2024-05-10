import unittest

from vlad_parser import TransformerParser, Grammar, ParseResult, NewRuleResult, MatchResult, ParseResultType, CompletionType
from vlad_parser.matchers import LiteralTokenMatcher


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

    def test_multiple_match_three_levels(self):
        rm1 = LiteralTokenMatcher(token_ids={1: None}, is_optional=False, matches_multiple=True)
        root_matchers = [rm1]
        m1 = LiteralTokenMatcher(token_ids={2: None}, is_optional=False, matches_multiple=True)
        m2 = LiteralTokenMatcher(token_ids={3: None}, is_optional=False, matches_multiple=True)
        m3 = LiteralTokenMatcher(token_ids={4: None}, is_optional=False, matches_multiple=True)
        m4 = LiteralTokenMatcher(token_ids={5: None}, is_optional=False, matches_multiple=True)
        m5 = LiteralTokenMatcher(token_ids={6: None}, is_optional=False, matches_multiple=True)
        m6 = LiteralTokenMatcher(token_ids={7: None}, is_optional=False, matches_multiple=True)
        grammar = Grammar(root_rule=root_matchers, rules={1: [m1, m4], 2: [m2, m3], 5: [m5, m6]})
        parser = TransformerParser(grammar)

        # According to the grammar, this parser will accept the token sequence (regex notation used, kinda): (1, (2, 3+, 4+)+, (5, 6+, 7+)+)+.

        for i in range(2):
            results = parser.test_token(1)
            if i == 0:
                self.assertEqual(len(results), 2)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1 for x in range(i+1)], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=1))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
            else:
                self.assertEqual(len(results), 4)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=5, matched_token_ids=[6, 6, 7, 7], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertParseResultsEqual(results[1], MatchResult(is_valid=False, cur_rule_id=1, matched_token_ids=[2, 2, 5, 5], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertParseResultsEqual(results[2], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1 for x in range(i+1)], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertParseResultsEqual(results[3], NewRuleResult(is_valid=True, new_rule_id=1))
                self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
            parser.apply_token(1, results)

            for j in range(2):
                results = parser.test_token(2)
                if j == 0:
                    self.assertEqual(len(results), 2)
                    self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
                    self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=2))
                else:
                    self.assertEqual(len(results), 3)
                    self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=2, matched_token_ids=[3, 3, 4, 4], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                    self.assertParseResultsEqual(results[1], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2 for x in range(j+1)], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
                    self.assertParseResultsEqual(results[2], NewRuleResult(is_valid=True, new_rule_id=2))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(2, results)

                expected_tokens = [3]
                results = parser.test_token(3)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=expected_tokens, matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(3, results)

                expected_tokens.append(3)
                results = parser.test_token(3)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=expected_tokens, matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(3, results)

                expected_tokens.append(4)
                results = parser.test_token(4)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=expected_tokens, matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(4, results)

                expected_tokens.append(4)
                results = parser.test_token(4)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=expected_tokens, matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(4, results)

            for j in range(2):
                results = parser.test_token(5)
                if j == 0:
                    self.assertEqual(len(results), 3)
                    self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=2, matched_token_ids=[3, 3, 4, 4], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                    self.assertParseResultsEqual(results[1], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2, 2] + [5 for x in range(j+1)], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                    self.assertParseResultsEqual(results[2], NewRuleResult(is_valid=True, new_rule_id=5))
                    self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                else:
                    self.assertEqual(len(results), 3)
                    self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=5, matched_token_ids=[6, 6, 7, 7], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                    self.assertParseResultsEqual(results[1], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2, 2] + [5 for x in range(j+1)], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                    self.assertParseResultsEqual(results[2], NewRuleResult(is_valid=True, new_rule_id=5))
                    # The parser is maybe complete before token 5 is applied because this isn't the first match of this rule.
                    self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                parser.apply_token(5, results)

                expected_tokens = [6]
                results = parser.test_token(6)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=expected_tokens, matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(6, results)

                expected_tokens.append(6)
                results = parser.test_token(6)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=expected_tokens, matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(6, results)

                expected_tokens.append(7)
                results = parser.test_token(7)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=expected_tokens, matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
                parser.apply_token(7, results)

                expected_tokens.append(7)
                results = parser.test_token(7)
                self.assertEqual(len(results), 1)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=expected_tokens, matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                parser.apply_token(7, results)
                self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)

    def test_optional_three_levels(self):
        # Iterates through token ids that should be left out.
        for token_id_to_ignore in range(2, 8):
            with self.subTest():
                rm1 = LiteralTokenMatcher(token_ids={1: None}, is_optional=True, matches_multiple=False)
                root_matchers = [rm1]
                m1 = LiteralTokenMatcher(token_ids={2: None}, is_optional=True, matches_multiple=False)
                m2 = LiteralTokenMatcher(token_ids={3: None}, is_optional=True, matches_multiple=False)
                m3 = LiteralTokenMatcher(token_ids={4: None}, is_optional=True, matches_multiple=False)
                m4 = LiteralTokenMatcher(token_ids={5: None}, is_optional=True, matches_multiple=False)
                m5 = LiteralTokenMatcher(token_ids={6: None}, is_optional=True, matches_multiple=False)
                m6 = LiteralTokenMatcher(token_ids={7: None}, is_optional=True, matches_multiple=False)
                grammar = Grammar(root_rule=root_matchers, rules={1: [m1, m4], 2: [m2, m3], 5: [m5, m6]})
                parser = TransformerParser(grammar)

                # According to the grammar, this parser will accept the token sequence (regex notation used, kinda): (1, (2, 3?, 4?)?, (5, 6?, 7?)?)?.

                self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                results = parser.test_token(1)
                self.assertEqual(len(results), 2)
                self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1], matched_matcher_index=0, rule_completion=CompletionType.COMPLETE))
                self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=1))
                self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                parser.apply_token(1, results)
                self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)

                tier_2_tokens = []
                tier_A3_tokens = []
                if token_id_to_ignore != 2:
                    tier_2_tokens.append(2)
                    results = parser.test_token(2)
                    self.assertEqual(len(results), 2)
                    self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=tier_2_tokens, matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
                    self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=2))
                    self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                    parser.apply_token(2, results)

                    if token_id_to_ignore != 3:
                        tier_A3_tokens.append(3)
                        results = parser.test_token(3)
                        self.assertEqual(len(results), 1)
                        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=tier_A3_tokens, matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
                        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                        parser.apply_token(3, results)

                    if token_id_to_ignore != 4:
                        tier_A3_tokens.append(4)
                        results = parser.test_token(4)
                        self.assertEqual(len(results), 1)
                        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=2, matched_token_ids=tier_A3_tokens, matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))
                        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                        parser.apply_token(4, results)

                if token_id_to_ignore != 5:
                    tier_2_tokens.append(5)
                    results = parser.test_token(5)
                    if token_id_to_ignore == 4:
                        # token_id 4 is optional, so we get a false match before falling back to the next rule node.
                        self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=2, matched_token_ids=[3], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
                        self.assertParseResultsEqual(results[1], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=tier_2_tokens, matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))
                        self.assertParseResultsEqual(results[2], NewRuleResult(is_valid=True, new_rule_id=5))
                    else:
                        self.assertEqual(len(results), 2)
                        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=tier_2_tokens, matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))                    
                        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=5))
                    self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                    parser.apply_token(5, results)

                    tier_B3_tokens = []
                    if token_id_to_ignore != 6:
                        tier_B3_tokens.append(6)
                        results = parser.test_token(6)
                        self.assertEqual(len(results), 1)
                        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=tier_B3_tokens, matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
                        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                        parser.apply_token(6, results)

                    if token_id_to_ignore != 7:
                        tier_B3_tokens.append(7)
                        results = parser.test_token(7)
                        self.assertEqual(len(results), 1)
                        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=5, matched_token_ids=tier_B3_tokens, matched_matcher_index=1, rule_completion=CompletionType.COMPLETE))
                        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                        parser.apply_token(7, results)
                        self.assertEqual(parser.is_complete(), CompletionType.COMPLETE)
                    else:
                        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
                else:
                    self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
    def test_multiple_tokens_matches_multiple_three_levels(self):
        rm1 = LiteralTokenMatcher(token_ids={1: None, 6: None}, is_optional=False, matches_multiple=True)
        root_matchers = [rm1]
        m1 = LiteralTokenMatcher(token_ids={2: None, 3: None}, is_optional=False, matches_multiple=True)
        m2 = LiteralTokenMatcher(token_ids={4: None, 5: None}, is_optional=False, matches_multiple=True)
        m3 = LiteralTokenMatcher(token_ids={7: None, 8: None}, is_optional=False, matches_multiple=True)
        m4 = LiteralTokenMatcher(token_ids={9: None, 12: None}, is_optional=False, matches_multiple=True)
        m5 = LiteralTokenMatcher(token_ids={10: None, 11: None}, is_optional=False, matches_multiple=True)
        grammar = Grammar(root_rule=root_matchers, rules={1: [m1, m2], 6: [m3, m4], 9: [m5]})
        parser = TransformerParser(grammar)

        # According to the grammar, this parser will accept the token sequence: (1, (2, 3), (4, 5), 6, (7, 8), (9, (10, 11), 12))

        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        results = parser.test_token(1)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=1))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(1, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(2)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(2, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(3)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2, 3], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(3, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(4)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2, 3, 4], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(4, results)
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)

        results = parser.test_token(5)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=1, matched_token_ids=[2, 3, 4, 5], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
        parser.apply_token(5, results)
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)

        results = parser.test_token(6)
        self.assertEqual(len(results), 3)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=1, matched_token_ids=[2, 3, 4, 5], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertParseResultsEqual(results[1], MatchResult(is_valid=True, cur_rule_id=None, matched_token_ids=[1, 6], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertParseResultsEqual(results[2], NewRuleResult(is_valid=True, new_rule_id=6))
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
        parser.apply_token(6, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(7)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=6, matched_token_ids=[7], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(7, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(8)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=6, matched_token_ids=[7, 8], matched_matcher_index=0, rule_completion=CompletionType.INCOMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(8, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(9)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=6, matched_token_ids=[7, 8, 9], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertParseResultsEqual(results[1], NewRuleResult(is_valid=True, new_rule_id=9))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(9, results)
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)

        results = parser.test_token(10)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=9, matched_token_ids=[10], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.INCOMPLETE)
        parser.apply_token(10, results)
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)

        results = parser.test_token(11)
        self.assertEqual(len(results), 1)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=True, cur_rule_id=9, matched_token_ids=[10, 11], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
        parser.apply_token(11, results)
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)

        results = parser.test_token(12)
        self.assertEqual(len(results), 2)
        self.assertParseResultsEqual(results[0], MatchResult(is_valid=False, cur_rule_id=9, matched_token_ids=[10, 11], matched_matcher_index=0, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertParseResultsEqual(results[1], MatchResult(is_valid=True, cur_rule_id=6, matched_token_ids=[7, 8, 9, 12], matched_matcher_index=1, rule_completion=CompletionType.MAYBE_COMPLETE))
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)
        parser.apply_token(12, results)
        self.assertEqual(parser.is_complete(), CompletionType.MAYBE_COMPLETE)


if __name__ == '__main__':
    unittest.main()
