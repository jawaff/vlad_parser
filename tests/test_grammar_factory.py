import unittest
import os
import re

from vlad_parser.translator import TokenTranslator
from vlad_parser.grammar_factory import load_grammar

class TestGrammarFactory(unittest.TestCase):
    def test_load_grammar(self):
        file_path = os.path.dirname(__file__)
        sql_grammar_path = os.path.join(file_path, '../src/vlad_parser/grammars/postgres.vlad')
        tokenizer_path = '../text2sql4j/raw-files/flan-t5-large/tokenizer.json'
        translator = TokenTranslator(tokenizer_path, [])
        grammar = load_grammar(sql_grammar_path, translator)

        for matchers in grammar.rules.values():
            assert len(matchers) > 0

        rule_pattern = re.compile(r'(special )?\w+\s*:\s*(\'\w+\').*')
        with open(sql_grammar_path, 'r') as file:
            for line in file:
                m = rule_pattern.match(line)
                if m is not None:
                    token = m.group(2)

                    # This is the expected token that should have been added to the vocab for the rule.
                    token_ids = translator.translate(f':{token[1:-1]}:')
                    
                    # All of the rules in our grammar should be in the grammar and have at least one matcher.
                    assert len(token_ids) == 2 and token_ids[1] == 1
                    token_id = token_ids[0]
                    assert token_id in grammar.rules
                    rule_matchers = grammar.rules[token_id]
                    assert len(rule_matchers) > 0

if __name__ == '__main__':
    unittest.main()
