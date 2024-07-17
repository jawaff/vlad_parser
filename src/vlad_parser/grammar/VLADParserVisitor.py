# Generated from ./grammar/VLADParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VLADParser import VLADParser
else:
    from VLADParser import VLADParser

# This class defines a complete generic visitor for a parse tree produced by VLADParser.

from typing import List, Dict, Optional, Union
from enum import Enum
from dataclasses import dataclass
import re

from vlad_parser.parser import Grammar, TokenMatcher
from vlad_parser.matchers import LiteralTokenMatcher
from vlad_parser.translator import TokenTranslator
 
class RuleType(Enum):
    TOKEN = 1
    SPECIAL = 2
    FRAGMENT = 3

@dataclass(init=False)
class Rule:
    # Identifies the type of the rule, which specifies how it is to be used.
    type: RuleType
    # This should be the id of the rule that appears in the parsed grammar.
    id: str
    # This is the id of the token that represents the rule.
    token_id: int
    matchers: List[TokenMatcher]

    def __init__(self, type: RuleType, id: str):
        self.type = type
        self.id = id
        self.token_id = -1
        self.matchers = []

class VLADParserVisitor(ParseTreeVisitor):
    def __init__(self, translator: TokenTranslator):
        self._cur_rule_id: Optional[str] = None
        self._token_rules: Dict[str, Rule] = {}
        self._special_rule_ids: List[str] = []
        self._translator: TokenTranslator = translator

    def build_grammar(self) -> Grammar:
        assert 'SELECT' in self._token_rules
        assert len(self._token_rules['SELECT'].matchers) == 1
        root_matcher = self._token_rules['SELECT'].matchers[0]
        del self._token_rules['SELECT']
        rules = {rule.token_id: rule.matchers for rule in self._token_rules}
        return Grammar(root_rule=[root_matcher], rules=rules)

    # Visit a parse tree produced by VLADParser#rules.
    def visitRules(self, ctx:VLADParser.RulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#rule.
    def visitRule(self, ctx:VLADParser.RuleContext):
        # Resets the current rule id becaue it should be replaced in the next visit*.
        self._cur_rule_id = None

        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#tokenRule.
    def visitTokenRule(self, ctx:VLADParser.TokenRuleContext):
        print("Visit Token Rule: " + ctx.ID().getText())
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.TOKEN, id = self._cur_rule_id)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#specialRule.
    def visitSpecialRule(self, ctx:VLADParser.SpecialRuleContext):
        print("Visit Special Rule: " + ctx.ID().getText())
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.SPECIAL, id = self._cur_rule_id)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#fragmentRule.
    def visitFragmentRule(self, ctx:VLADParser.FragmentRuleContext):
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.FRAGMENT, id = self._cur_rule_id)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#ruleBlock.
    def visitRuleBlock(self, ctx:VLADParser.RuleBlockContext):
        # Here we are going to be saving the token id that is to be associated with the current rule.
        token = ctx.STRING_LITERAL().getText()[1:-1]
        cur_rule = self._token_rules[self._cur_rule_id]

        # If the token id for the provided token does not exist in our model's vocabulary, then it must be added to the vocabulary as a new token so that we can
        # associate it with a single token id.
        self._translator.add_new_token(token)
        token_ids = self._translator.translate(token)
        assert len(token_ids) == 1
        cur_rule.token_id = token_ids[0]

        print("Rule Block Literal:" + token)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#ruleAltList.
    def visitRuleAltList(self, ctx:VLADParser.RuleAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#lexerRuleBlock.
    def visitLexerRuleBlock(self, ctx:VLADParser.LexerRuleBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#lexerAltList.
    def visitLexerAltList(self, ctx:VLADParser.LexerAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#lexerAlt.
    def visitLexerAlt(self, ctx:VLADParser.LexerAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#lexerElement.
    def visitLexerElement(self, ctx:VLADParser.LexerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#lexerBlock.
    def visitLexerBlock(self, ctx:VLADParser.LexerBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#altList.
    def visitAltList(self, ctx:VLADParser.AltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#alternative.
    def visitAlternative(self, ctx:VLADParser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#element.
    def visitElement(self, ctx:VLADParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#ebnfSuffix.
    def visitEbnfSuffix(self, ctx:VLADParser.EbnfSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#lexerAtom.
    def visitLexerAtom(self, ctx:VLADParser.LexerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#atom.
    def visitAtom(self, ctx:VLADParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#notSet.
    def visitNotSet(self, ctx:VLADParser.NotSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#blockSet.
    def visitBlockSet(self, ctx:VLADParser.BlockSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#setElement.
    def visitSetElement(self, ctx:VLADParser.SetElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#ruleref.
    def visitRuleref(self, ctx:VLADParser.RulerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#block.
    def visitBlock(self, ctx:VLADParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#characterRange.
    def visitCharacterRange(self, ctx:VLADParser.CharacterRangeContext):
        # This is for matching a range of characters and should probably only work on literals with a single character!
        start = ctx.STRING_LITERAL()[1:-1]
        assert len(start) == 1
        end = ctx.STRING_LITERAL()[1:-1]
        assert len(end) == 1

        # TODO Make a matcher that matches all characters between the start and end. Use the ordinal values of the characters and make sure that the end has a greater ordinal value!

        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#terminalDef.
    def visitTerminalDef(self, ctx:VLADParser.TerminalDefContext):
        # TODO This is going to be an ID or STRING_LITERAL. Either way, return a matcher that matches the sequence of token ids that make up the id or literal.
        #ctx.ID
        #ctx.STRING_LITERAL
        return self.visitChildren(ctx)



del VLADParser