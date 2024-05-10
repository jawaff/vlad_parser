from typing import List
from .parser import Grammar, TokenMatcher

from antlr4 import *
from parser.grammar.VLADLexer import VLADLexer
from parser.grammar.VLADParser import VLADParser
from parser.grammar.VLADParserListener import VLADParserListener

# TODO This needs a lot of work too convert from the rule text to the token matchers.

def is_root_rule(rule_line: str) -> bool:
    return rule_line.startswith('ROOT = ')

def is_other_rule(rule_line: str) -> bool:
    return not is_root_rule(rule_line)

def build_matchers(rule: str) -> List[TokenMatcher]:
    return []

def load_grammar(filename: str) -> Grammar:
    listener = VLADParserListener()
    with open(filename) as file:
        input_stream = InputStream(file)
        lexer = VLADLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = VLADParser(token_stream)
        parser.addParseListener(listener)
    
    return Grammar()

        # Collects the nonempty rule lines
        #rule_lines = [line.strip() for line in file if not line.strip()]

#    root_rule_line = next(filter(is_root_rule, rule_lines), None)
#    assert root_rule_line is not None
#    root_rule = build_matchers(root_rule_line)
#
#    other_rule_lines = list(filter(is_other_rule, rule_lines))
#    # TODO Figure out what the maximum number of special token ids we can use and subtract the offset for the first token.
#    # TODO Figure outranslator
#    # There needs to be a certain offset that we use for the first rule's token id.
#    other_rules = {i+2: build_matchers(other_rule_lines[i]) for i in range(0, len(other_rule_lines))}
#
#    return Grammar(root_rule, other_rules)
#