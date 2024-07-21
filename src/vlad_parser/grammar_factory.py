from .parser import Grammar

from antlr4 import *
from .grammar.VLADLexer import VLADLexer
from .grammar.VLADParser import VLADParser
from .grammar.VLADParserVisitor import VLADParserVisitor
from vlad_parser.translator import TokenTranslator


def load_grammar(filename: str, translator: TokenTranslator) -> Grammar:
    with open(filename) as file:
        input_stream = InputStream(file.read())
        lexer = VLADLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = VLADParser(token_stream)
        tree = parser.rules()
        visitor = VLADParserVisitor(translator)
        visitor.visit(tree)
    
        return visitor.build_grammar()
