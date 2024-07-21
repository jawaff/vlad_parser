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
        # This will be used to make fragment rule tokens unique.
        self._fragment_rule_index = 1

    def build_grammar(self) -> Grammar:
        assert 'SELECT' in self._token_rules
        root_matcher = LiteralTokenMatcher({self._token_rules['SELECT'].token_id: None}, False, False)
        rules = {rule.token_id: rule.matchers for rule in self._token_rules.values()}
        return Grammar(root_rule=[root_matcher], rules=rules)

    def _create_new_token(self, token: str) -> int:
        # Tokens should not exist within with the existing vocabulary.
        self._translator.add_new_token(self._prepare_token_id(token), error_on_exists=True)
        token_ids = self._translator.translate(self._prepare_token_id(token))
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
            self._junction_rule_index += 1
            token_id = self._create_new_token(token)
            junction_token_ids[token_id] = None
            self._token_rules[token] = Rule(RuleType.JUNCTION, token, token_id, partial_rule.matchers)
        
        # Optional and matchesMultiple will default to false for junctions, but can be updated for where they're used.
        return LiteralTokenMatcher(junction_token_ids, False, False)
    
    def _prepare_token_id(self, id: str) -> str:
        return f':{id}:'

    def _literal_to_rule(self, literal: str) -> PartialRule:
        matchers: List[TokenMatcher]
        # Just in case the literal doesn't match a rule, then we're going to need to treat it like some arbitrary literal which would be matched by a list of matchers.
        # Remember that token ids have special characters added around them.
        if literal in self._token_rules:
            target_rule = self._token_rules[literal]
            # Fragment rules must have their matchers copied to the place they are referenced.
            if target_rule.type == RuleType.FRAGMENT:
                matchers = target_rule.matchers
            else:
                matchers = [LiteralTokenMatcher({self._token_rules[literal].token_id: None}, False, False)]
        else:
            if not (literal.startswith('\'') and literal.endswith('\'')):
                raise Exception(f'Rule reference must come after rule definition: {literal}')
            # We need to cut off the last id because it should be a 1.
            ids = self._translator.translate(literal)
            assert ids[-1] == 1
            matchers = [LiteralTokenMatcher({id: None}, False, False) for id in ids[0:-1]]
        return PartialRule(matchers)
    
    def _regex_literal_to_rule(self, regex: str) -> PartialRule:
        # Strips the r'' from the regex string.
        pattern_str = regex[2:-1]
        pattern = re.compile(pattern_str)
        token_ids: Dict[int, None] = {}
        for key, value in  self._translator.get_vocab().items():
            if pattern.match(key):
                token_ids[value] = None

        if len(token_ids) == 0:
            raise Exception(f'Regex did not match a single token in the model\'s vocabulary: {regex}')
        return PartialRule([LiteralTokenMatcher(token_ids, False, False)])

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
        #print("Visit Token Rule: " + ctx.ID().getText())
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.TOKEN, id = self._cur_rule_id, token_id = -1, matchers = [])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#specialRule.
    def visitSpecialRule(self, ctx:VLADParser.SpecialRuleContext):
        #print("Visit Special Rule: " + ctx.ID().getText())
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.SPECIAL, id = self._cur_rule_id, token_id = -1, matchers = [])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#fragmentRule.
    def visitFragmentRule(self, ctx:VLADParser.FragmentRuleContext):
        self._cur_rule_id = ctx.ID().getText()
        self._token_rules[self._cur_rule_id] = Rule(type = RuleType.FRAGMENT, id = self._cur_rule_id, token_id = -1, matchers = [])

        # TODO Fragment rules are really special. The places that reference these FRAGMENT rules will need to copy their matchers instead of referencing the
        # FRAGMENT's token id. In addition, these fragment rules may be stored alongside the other rules, but should not make themselves into the grammar
        # as a standalone rule. These rules are only able to be used by other rules.

        return self.visitChildren(ctx)


    # Visit a parse tree produced by VLADParser#ruleBlock.
    def visitRuleBlock(self, ctx:VLADParser.RuleBlockContext):
        # Here we are going to be saving the token id that is to be associated with the current rule.
        token = ctx.STRING_LITERAL().getText()[1:-1]
        cur_rule = self._token_rules[self._cur_rule_id]

        # The token does not exist in our model's vocabulary, so it must be added to the vocabulary as a new token so that we can
        # associate it with a single token id.
        cur_rule.token_id = self._create_new_token(token)

        #print("Rule Block Literal: " + token)
        cur_rule.matchers = self.visitAltList(ctx.altList()).matchers


    # Visit a parse tree produced by VLADParser#fragmentRuleBlock.
    def visitFragmentRuleBlock(self, ctx:VLADParser.FragmentRuleBlockContext):
        token = f'FRAGMENT{self._fragment_rule_index}'
        self._fragment_rule_index += 1
        cur_rule = self._token_rules[self._cur_rule_id]

        # The token does not exist in our model's vocabulary, so it must be added to the vocabulary as a new token so that we can
        # associate it with a single token id.
        cur_rule.token_id = self._create_new_token(token)

        #print("Fragment Block Literal: " + token)
        cur_rule.matchers = self.visitAltList(ctx.altList()).matchers


    # Visit a parse tree produced by VLADParser#altList.
    def visitAltList(self, ctx:VLADParser.AltListContext) -> PartialRule:
        # In the alt list there will be some number of conditional paths. This means that the alt list will translate to a conditional junction rule.
        sub_rules: List[PartialRule] = []
        for alt_ctx in ctx.alternative():
            sub_rules.append(self.visitAlternative(alt_ctx))
        
        rule: PartialRule
        if len(sub_rules) == 1:
            rule = sub_rules[0]
        elif len(sub_rules) > 1:
            matcher: TokenMatcher = self._create_junction_rule(sub_rules)
            rule = PartialRule([matcher])
        else:
            raise Exception('Alt list requires at least one alternative')

        return rule


    # Visit a parse tree produced by VLADParser#alternative.
    def visitAlternative(self, ctx:VLADParser.AlternativeContext) -> PartialRule:
        rule: PartialRule = PartialRule([])
        for element_ctx in ctx.element():
            sub_rule = self.visitElement(element_ctx)
            rule.matchers.extend(sub_rule.matchers)
        return rule


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
                raise Exception('An ebnf suffix must be applied to a matcher, but there is none')
            elif len(rule.matchers) == 1:
                self.visitEbnfSuffix(suffix, rule.matchers[0])
            else:
                # If there are multiple matchers that this ebnf applies to, then we need a junction rule to apply the ebnf suffix to the list of matchers.
                matcher: TokenMatcher = self._create_junction_rule([rule])
                self.visitEbnfSuffix(suffix, matcher)
                # We need a new rule for representing the junction.
                rule = PartialRule([matcher])
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


    # Visit a parse tree produced by VLADParser#block.
    def visitBlock(self, ctx:VLADParser.BlockContext) -> PartialRule:
        # A block consists of parenthesis and some alt list within them. We're just going to delegate and pass up the matchers
        return self.visitAltList(ctx.altList())


    # Visit a parse tree produced by VLADParser#atom.
    def visitAtom(self, ctx:VLADParser.AtomContext) -> PartialRule:
        terminal_def = ctx.terminalDef()
        if terminal_def is not None:
            return self.visitTerminalDef(terminal_def)
        else:
            raise Exception(f'Unsupported atom: {ctx.getText()}')
        

    # Visit a parse tree produced by VLADParser#terminalDef.
    def visitTerminalDef(self, ctx:VLADParser.TerminalDefContext) -> PartialRule:
        id = ctx.ID()
        literal = ctx.STRING_LITERAL()
        regex_literal = ctx.REGEX_LITERAL()
        range = ctx.characterRange()
        if id is not None:
            return self._literal_to_rule(id.getText())
        elif literal is not None:
            return self._literal_to_rule(literal.getText())
        elif regex_literal is not None:
            return self._regex_literal_to_rule(regex_literal.getText())
        elif range is not None:
            return self.visitCharacterRange(range)
        else:
            raise Exception(f'Unsupported terminalDef: {ctx.getText()}')


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



del VLADParser