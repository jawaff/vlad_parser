import unittest
import os

from vlad_parser.translator import TokenTranslator
from vlad_parser.grammar_factory import load_grammar

class TestGrammarFactory(unittest.TestCase):
    def test_load_grammar(self):
        file_path = os.path.dirname(__file__)
        sql_grammar_path = os.path.join(file_path, '../src/vlad_parser/grammars/postgres.vlad')
        tokenizer_path = '../text2sql4j/raw-files/flan-t5-large/tokenizer.json'
        translator = TokenTranslator(tokenizer_path, [])
        grammar = load_grammar(sql_grammar_path, translator)

if __name__ == '__main__':
    unittest.main()
