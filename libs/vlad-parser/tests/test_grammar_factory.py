import unittest
import os
import re

from vlad.parser.translator import TokenTranslator
from vlad.parser.grammar_factory import load_grammar
from vlad.parser.grammar.VLADParserVisitor import RuleType


class TestGrammarFactory(unittest.TestCase):
    def test_load_grammar(self):
        file_path = os.path.dirname(__file__)
        sql_grammar_path = os.path.join(file_path, "../assets/test.vlad")
        tokenizer_path = os.path.join(file_path, "../assets/tokenizer.json")
        translator = TokenTranslator(tokenizer_path, [])
        grammar, rules = load_grammar(sql_grammar_path, translator)

        for matchers in grammar.rules.values():
            assert len(matchers) > 0

        print(len(rules))
        rule_pattern = re.compile(r"(special |root )?(\w+)\s*:\s*(\'\w+\').*")
        with open(sql_grammar_path, "r") as file:
            for line in file:
                m = rule_pattern.match(line)
                if m is not None:
                    id = m.group(2)
                    print(id)
                    token = m.group(3)
                    rule = rules.pop(id)
                    assert rule.type == RuleType.TOKEN or rule.type == RuleType.SPECIAL

                    # This is the expected token that should have been added to the vocab for the rule.
                    token_ids = translator.translate(f":{token[1:-1]}:")

                    # All of the rules in our grammar should be in the grammar and have at least one matcher.
                    assert len(token_ids) == 2 and token_ids[1] == 1
                    token_id = token_ids[0]
                    assert rule.token_id == token_id
                    assert token_id in grammar.rules
                    rule_matchers = grammar.rules[token_id]
                    assert len(rule_matchers) > 0

        # Token and special rules should have been removed from the rules. We checked that they match a rule in the grammar and so only
        # junction and fragment rules should remain.
        for rule in rules.values():
            assert rule.type == RuleType.FRAGMENT or rule.type == RuleType.JUNCTION

            # Fragment rules should not exist as a standalone rule in the grammar.
            if rule.type == RuleType.FRAGMENT:
                assert rule.token_id not in grammar.rules
            else:
                assert rule.token_id in grammar.rules


if __name__ == "__main__":
    unittest.main()
