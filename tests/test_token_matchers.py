import unittest
import random

from vlad.parser.matchers import LiteralTokenMatcher


class TestTokenMatchers(unittest.TestCase):
    def test_literal_token_matcher(self):
        token_ids = {1: None, 2: None, 3: None}
        for is_optional in [True, False]:
            for matches_multiple in [True, False]:
                matcher = LiteralTokenMatcher(token_ids=token_ids, is_optional=is_optional, matches_multiple=matches_multiple)
                self.assertEqual(matcher.is_optional(), is_optional)
                self.assertEqual(matcher.matches_multiple(), matches_multiple)
                for token_id in token_ids.keys():
                    self.assertEqual(matcher.test_token(token_id=token_id), True)
                    self.assertEqual(matcher.test_token(token_id=random.randint(4, 10000)), False)

if __name__ == '__main__':
    unittest.main()
