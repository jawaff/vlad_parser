# Generated from ./grammar/vladparser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .vladparser import vladparser
else:
    from vladparser import vladparser

# This class defines a complete listener for a parse tree produced by vladparser.
class vladparserListener(ParseTreeListener):

    # Enter a parse tree produced by vladparser#tokenRule.
    def enterTokenRule(self, ctx:vladparser.TokenRuleContext):
        pass

    # Exit a parse tree produced by vladparser#tokenRule.
    def exitTokenRule(self, ctx:vladparser.TokenRuleContext):
        pass


    # Enter a parse tree produced by vladparser#specialRule.
    def enterSpecialRule(self, ctx:vladparser.SpecialRuleContext):
        pass

    # Exit a parse tree produced by vladparser#specialRule.
    def exitSpecialRule(self, ctx:vladparser.SpecialRuleContext):
        pass


    # Enter a parse tree produced by vladparser#fragmentRule.
    def enterFragmentRule(self, ctx:vladparser.FragmentRuleContext):
        pass

    # Exit a parse tree produced by vladparser#fragmentRule.
    def exitFragmentRule(self, ctx:vladparser.FragmentRuleContext):
        pass


    # Enter a parse tree produced by vladparser#ruleBlock.
    def enterRuleBlock(self, ctx:vladparser.RuleBlockContext):
        pass

    # Exit a parse tree produced by vladparser#ruleBlock.
    def exitRuleBlock(self, ctx:vladparser.RuleBlockContext):
        pass


    # Enter a parse tree produced by vladparser#ruleAltList.
    def enterRuleAltList(self, ctx:vladparser.RuleAltListContext):
        pass

    # Exit a parse tree produced by vladparser#ruleAltList.
    def exitRuleAltList(self, ctx:vladparser.RuleAltListContext):
        pass


    # Enter a parse tree produced by vladparser#lexerRuleBlock.
    def enterLexerRuleBlock(self, ctx:vladparser.LexerRuleBlockContext):
        pass

    # Exit a parse tree produced by vladparser#lexerRuleBlock.
    def exitLexerRuleBlock(self, ctx:vladparser.LexerRuleBlockContext):
        pass


    # Enter a parse tree produced by vladparser#lexerAltList.
    def enterLexerAltList(self, ctx:vladparser.LexerAltListContext):
        pass

    # Exit a parse tree produced by vladparser#lexerAltList.
    def exitLexerAltList(self, ctx:vladparser.LexerAltListContext):
        pass


    # Enter a parse tree produced by vladparser#lexerAlt.
    def enterLexerAlt(self, ctx:vladparser.LexerAltContext):
        pass

    # Exit a parse tree produced by vladparser#lexerAlt.
    def exitLexerAlt(self, ctx:vladparser.LexerAltContext):
        pass


    # Enter a parse tree produced by vladparser#lexerElement.
    def enterLexerElement(self, ctx:vladparser.LexerElementContext):
        pass

    # Exit a parse tree produced by vladparser#lexerElement.
    def exitLexerElement(self, ctx:vladparser.LexerElementContext):
        pass


    # Enter a parse tree produced by vladparser#lexerBlock.
    def enterLexerBlock(self, ctx:vladparser.LexerBlockContext):
        pass

    # Exit a parse tree produced by vladparser#lexerBlock.
    def exitLexerBlock(self, ctx:vladparser.LexerBlockContext):
        pass


    # Enter a parse tree produced by vladparser#altList.
    def enterAltList(self, ctx:vladparser.AltListContext):
        pass

    # Exit a parse tree produced by vladparser#altList.
    def exitAltList(self, ctx:vladparser.AltListContext):
        pass


    # Enter a parse tree produced by vladparser#alternative.
    def enterAlternative(self, ctx:vladparser.AlternativeContext):
        pass

    # Exit a parse tree produced by vladparser#alternative.
    def exitAlternative(self, ctx:vladparser.AlternativeContext):
        pass


    # Enter a parse tree produced by vladparser#element.
    def enterElement(self, ctx:vladparser.ElementContext):
        pass

    # Exit a parse tree produced by vladparser#element.
    def exitElement(self, ctx:vladparser.ElementContext):
        pass


    # Enter a parse tree produced by vladparser#ebnfSuffix.
    def enterEbnfSuffix(self, ctx:vladparser.EbnfSuffixContext):
        pass

    # Exit a parse tree produced by vladparser#ebnfSuffix.
    def exitEbnfSuffix(self, ctx:vladparser.EbnfSuffixContext):
        pass


    # Enter a parse tree produced by vladparser#lexerAtom.
    def enterLexerAtom(self, ctx:vladparser.LexerAtomContext):
        pass

    # Exit a parse tree produced by vladparser#lexerAtom.
    def exitLexerAtom(self, ctx:vladparser.LexerAtomContext):
        pass


    # Enter a parse tree produced by vladparser#atom.
    def enterAtom(self, ctx:vladparser.AtomContext):
        pass

    # Exit a parse tree produced by vladparser#atom.
    def exitAtom(self, ctx:vladparser.AtomContext):
        pass


    # Enter a parse tree produced by vladparser#notSet.
    def enterNotSet(self, ctx:vladparser.NotSetContext):
        pass

    # Exit a parse tree produced by vladparser#notSet.
    def exitNotSet(self, ctx:vladparser.NotSetContext):
        pass


    # Enter a parse tree produced by vladparser#blockSet.
    def enterBlockSet(self, ctx:vladparser.BlockSetContext):
        pass

    # Exit a parse tree produced by vladparser#blockSet.
    def exitBlockSet(self, ctx:vladparser.BlockSetContext):
        pass


    # Enter a parse tree produced by vladparser#setElement.
    def enterSetElement(self, ctx:vladparser.SetElementContext):
        pass

    # Exit a parse tree produced by vladparser#setElement.
    def exitSetElement(self, ctx:vladparser.SetElementContext):
        pass


    # Enter a parse tree produced by vladparser#ruleref.
    def enterRuleref(self, ctx:vladparser.RulerefContext):
        pass

    # Exit a parse tree produced by vladparser#ruleref.
    def exitRuleref(self, ctx:vladparser.RulerefContext):
        pass


    # Enter a parse tree produced by vladparser#block.
    def enterBlock(self, ctx:vladparser.BlockContext):
        pass

    # Exit a parse tree produced by vladparser#block.
    def exitBlock(self, ctx:vladparser.BlockContext):
        pass


    # Enter a parse tree produced by vladparser#characterRange.
    def enterCharacterRange(self, ctx:vladparser.CharacterRangeContext):
        pass

    # Exit a parse tree produced by vladparser#characterRange.
    def exitCharacterRange(self, ctx:vladparser.CharacterRangeContext):
        pass


    # Enter a parse tree produced by vladparser#terminalDef.
    def enterTerminalDef(self, ctx:vladparser.TerminalDefContext):
        pass

    # Exit a parse tree produced by vladparser#terminalDef.
    def exitTerminalDef(self, ctx:vladparser.TerminalDefContext):
        pass



del vladparser