from .parser import Grammar

from antlr4 import *
from typing import Dict, Tuple

from .grammar.VLADLexer import VLADLexer
from .grammar.VLADParser import VLADParser
from .grammar.VLADParserVisitor import VLADParserVisitor, Rule
from vlad.parser.translator import TokenTranslator


def load_grammar(
    filename: str, translator: TokenTranslator
) -> Tuple[Grammar, Dict[str, Rule]]:
    with open(filename) as file:
        input_stream = InputStream(file.read())
        lexer = VLADLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = VLADParser(token_stream)
        tree = parser.rules()
        visitor = VLADParserVisitor(translator)
        visitor.visit(tree)

        return (visitor.build_grammar(), visitor.get_rules())
