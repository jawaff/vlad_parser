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
    JUNCTION = 4

@dataclass(init=False)
class Rule:
    # Identifies the type of the rule, which specifies how it is to be used.
    type: RuleType
    # This should be the id of the rule that appears in the parsed grammar.
    id: str
    # This is the id of the token that represents the rule.
    token_id: int
    matchers: List[TokenMatcher]

    def __init__(self, type: RuleType, id: str, token_id: int, matchers: List[TokenMatcher]):
        self.type = type
        self.id = id
        self.token_id = token_id
        self.matchers = matchers

@dataclass
class PartialRule:
    '''
    A partial rule is what is returned by the visit* functions that are within a rule.
    We will build up matchers for the rule using partial rules.

    A conditional junction within a rule is going to require us to create rules for each of the conditional paths and then a junction matcher will
    need to match the token ids for these conditional path rules. The token id of the conditional paths will need to be completely unique.
    However, in the case of the conditional paths already being a rule, then an additional rule will not have to be created for that path!
    '''
    matchers: List[TokenMatcher]

class VLADParserVisitor(ParseTreeVisitor):
    def __init__(self, translator: TokenTranslator):
        self._cur_rule_id: Optional[str] = None
        self._token_rules: Dict[str, Rule] = {}
        self._special_rule_ids: List[str] = []
        self._translator: TokenTranslator = translator
        # This will be used to make junction rule tokens unique.
        self._junction_rule_index = 1

    def build_grammar(self) -> Grammar:
        assert 'SELECT' in self._token_rules
        assert len(self._token_rules['SELECT'].matchers) == 1
        root_matcher = self._token_rules['SELECT'].matchers[0]
        del self._token_rules['SELECT']
        rules = {rule.token_id: rule.matchers for rule in self._token_rules}
        return Grammar(root_rule=[root_matcher], rules=rules)

    def _create_new_token(self, token: str) -> int:
        # Tokens should not exist within with the existing vocabulary.
        self._translator.add_new_token(f':{token}:', error_on_exists=True)
        token_ids = self._translator.translate(token)
        # The token_ids should have one id and an "end" id
        assert len(token_ids) == 2 and token_ids[1] == 1
        return token_ids[0]

    def _create_junction_rule(self, partial_rules: List[PartialRule]) -> TokenMatcher:
        '''
        When creating a junction rule for the provided partial rules, we will be filling in
        arbitrary data for the rule because it doesn't really matter. That means we need to
        add new tokens for each partial rule to identify their start and ensure that the
        returned matcher matches each of these new tokens.
        '''
        assert len(partial_rules) > 0
        junction_token_ids = {}
        for partial_rule in partial_rules:
            token = f'JUNCTION{self._junction_rule_index}'
            token_id = self._create_junction_rule(token)
            junction_token_ids[token_id] = None
            self._token_rules[token] = Rule(RuleType.JUNCTION, token, token_id, partial_rule.matchers)
            self._junction_rule_index += 1
        
        # Optional and matchesMultiple will default to false for junctions, but can be updated for where they're used.
        return LiteralTokenMatcher(junction_token_ids, False, False)
    
    def _prepare_token_id(self, id: str) -> str:
        return f':{id}:'

    def _literal_to_rule(self, literal: str) -> PartialRule:
        matchers: List[TokenMatcher]
        token_id = self._prepare_token_id(literal)
        # Just in case the literal doesn't match a rule, then we're going to need to treat it like some arbitrary literal which would be matched by a list of matchers.
        # Remember that token ids have special characters added around them.
        if token_id in self._token_rules:
            matchers = [LiteralTokenMatcher({self._token_rules[token_id].token_id: None}, False, False)]
        else:
            # We need to cut off the last id because it should be a 1.
            ids = self._translator.translate(literal)
            assert ids[-1] == 1
            matchers = [LiteralTokenMatcher({id: None}) for id in ids[0:-1]]
        return PartialRule(matchers)

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
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.TOKEN, id = self._cur_rule_id, token_id = -1, matchers = [])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#specialRule.
    def visitSpecialRule(self, ctx:VLADParser.SpecialRuleContext):
        print("Visit Special Rule: " + ctx.ID().getText())
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.SPECIAL, id = self._cur_rule_id, token_id = -1, matchers = [])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#fragmentRule.
    def visitFragmentRule(self, ctx:VLADParser.FragmentRuleContext):
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.FRAGMENT, id = self._cur_rule_id, token_id = -1, matchers = [])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#ruleBlock.
    def visitRuleBlock(self, ctx:VLADParser.RuleBlockContext):
        # Here we are going to be saving the token id that is to be associated with the current rule.
        token = ctx.STRING_LITERAL().getText()[1:-1]
        cur_rule = self._token_rules[self._cur_rule_id]

        # If the token id for the provided token does not exist in our model's vocabulary, then it must be added to the vocabulary as a new token so that we can
        # associate it with a single token id.
        cur_rule.token_id = self._create_new_token(token)

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
    def visitElement(self, ctx:VLADParser.ElementContext) -> PartialRule:
        atom = ctx.atom()
        block = ctx.block()
        rule: PartialRule
        if atom is not None:
            rule = self.visitAtom(atom)
        else:
            rule = self.visitBlock(block)
        
        # This ebnf suffix will affect the provided partial rule by making it optional and/or match multiple times.
        suffix = ctx.ebnfSuffix()
        if suffix is not None:
            if len(rule.matchers) == 0:
                return rule
            elif len(rule.matchers) == 1:
                self.visitEbnfSuffix(suffix, rule.matchers[0])
            else:
                # If there are multiple matchers that this ebnf applies to, then we need a junction rule to apply the ebnf suffix to the list of matchers.
                rule = self._create_junction_rule([rule])
                self.visitEbnfSuffix(suffix, rule.matchers[0])
        return rule

    # Visit a parse tree produced by VLADParser#ebnfSuffix.
    def visitEbnfSuffix(self, ctx:VLADParser.EbnfSuffixContext, matcher: TokenMatcher):
        # This will need to modify the provided matcher by setting whether is conditional or matches multiple.
        if ctx.PLUS() is not None:
            matcher.is_optional = False
            matcher.matches_multiple = True
        elif ctx.STAR() is not None:
            matcher.is_optional = True
            matcher.matches_multiple = True
        elif ctx.QUESTION() is not None:
            matcher.is_optional = True
            matcher.matches_multiple = False
        else:
            raise Exception('The ebnf suffix must be a *, + or ?')

    # Visit a parse tree produced by VLADParser#lexerAtom.
    def visitLexerAtom(self, ctx:VLADParser.LexerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#atom.
    def visitAtom(self, ctx:VLADParser.AtomContext) -> PartialRule:
        set_element = ctx.setElement()
        terminal_def = ctx.terminalDef()
        rule_ref = ctx.ruleref()
        # TODO Remove support for notSet! I'm not sure how I would even support that unless we do some complex modification of some other matcher.
        if set_element is not None:
            return self.visitSetElement(set_element)
        elif terminal_def is not None:
            return self.visitTerminalDef(terminal_def)
        elif rule_ref is not None:
            return self.visitRuleref(rule_ref)
        else:
            raise Exception(f'Unsupported atom: {ctx.getText()}')

    # Visit a parse tree produced by VLADParser#notSet.
    def visitNotSet(self, ctx:VLADParser.NotSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#blockSet.
    def visitBlockSet(self, ctx:VLADParser.BlockSetContext) -> PartialRule:
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#setElement.
    def visitSetElement(self, ctx:VLADParser.SetElementContext) -> PartialRule:
        id = ctx.ID()
        literal = ctx.STRING_LITERAL()
        range = ctx.characterRange()
        if id is not None:
            return self._literal_to_rule(id.getText())
        elif literal is not None:
            return self._literal_to_rule(literal.getText())
        elif range is not None:
            return self.visitCharacterRange(range)
        else:
            raise Exception(f'Unsupported setElement: {ctx.getText()}')


    # Visit a parse tree produced by VLADParser#ruleref.
    def visitRuleref(self, ctx:VLADParser.RulerefContext) -> PartialRule:
        id = ctx.ID()
        if id is not None:
            return self._literal_to_rule(id.getText())
        else:
            raise Exception(f'Unsupported ruleRef: {ctx.getText()}')

    # Visit a parse tree produced by VLADParser#block.
    def visitBlock(self, ctx:VLADParser.BlockContext):
        # A block consists of parenthesis and some elements within it, maybe child blocks.
        # TODO We're going to need a matcher around blocks to support conditions (in parent visits) and the "multiple" cases.
        # We might need to find a way to optimize all these rules so that we don't have to make unnecessary matchers.

        # Since the "ebnfSuffix" exists at the element level (which is the parent of a block), then maybe that's definitely where a matcher should be defined,
        # but for a block specifically we probably need subrules.

        # Matchers support the optional/multiple cases and a list of valid ids. This handles the simple cases for sure.
        # Conditional matches are going to require a junction rule which delegates to the rules defined for each case of the condition.
        # Maybe we should start at the root of this parse tree and move down to the leaves so that we know what is expected of the leaf visits.
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#characterRange.
    def visitCharacterRange(self, ctx:VLADParser.CharacterRangeContext) -> PartialRule:
        # This is for matching a range of characters and should probably only work on literals with a single character!
        # The ordinals for the characters also must go from a lower number to a higher number.
        start = ctx.STRING_LITERAL().getText()[1:-1]
        assert len(start) == 1
        end = ctx.STRING_LITERAL().getText()[1:-1]
        assert len(end) == 1
        assert ord(start) < ord(end)

        token_ids: Dict[int, None] = {}
        for ordinal in range(ord(start), ord(end)+1):
            ids = self._translator.translate(chr(ordinal))
            assert len(ids) == 2 and ids[1] == 1
            token_ids[ids[0]] = None

        # The returned matcher will allow any of the characters in the range to be matched before the next matcher is processed.
        return PartialRule([LiteralTokenMatcher(token_ids, False, False)])


    # Visit a parse tree produced by VLADParser#terminalDef.
    def visitTerminalDef(self, ctx:VLADParser.TerminalDefContext) -> PartialRule:
        id = ctx.ID()
        literal = ctx.STRING_LITERAL()
        if id is not None:
            return self._literal_to_rule(id.getText())
        elif literal is not None:
            return self._literal_to_rule(literal.getText())
        else:
            raise Exception(f'Unsupported terminalDef: {ctx.getText()}')


del VLADParser