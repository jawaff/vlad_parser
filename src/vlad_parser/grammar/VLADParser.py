# Generated from ./grammar/VLADParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,1,1,3,1,39,8,1,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,66,8,7,10,7,12,7,69,9,7,1,8,
        4,8,72,8,8,11,8,12,8,73,1,9,1,9,1,9,3,9,79,8,9,1,9,1,9,3,9,83,8,
        9,3,9,85,8,9,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,
        13,1,13,3,13,99,8,13,1,14,1,14,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,0,1,2,0,22,23,25,25,100,0,31,1,0,0,0,
        2,38,1,0,0,0,4,40,1,0,0,0,6,45,1,0,0,0,8,51,1,0,0,0,10,57,1,0,0,
        0,12,60,1,0,0,0,14,62,1,0,0,0,16,71,1,0,0,0,18,84,1,0,0,0,20,86,
        1,0,0,0,22,88,1,0,0,0,24,92,1,0,0,0,26,98,1,0,0,0,28,100,1,0,0,0,
        30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,
        0,0,0,34,1,1,0,0,0,35,39,3,4,2,0,36,39,3,6,3,0,37,39,3,8,4,0,38,
        35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,5,33,0,
        0,41,42,5,10,0,0,42,43,3,10,5,0,43,44,5,13,0,0,44,5,1,0,0,0,45,46,
        5,9,0,0,46,47,5,33,0,0,47,48,5,10,0,0,48,49,3,10,5,0,49,50,5,13,
        0,0,50,7,1,0,0,0,51,52,5,8,0,0,52,53,5,33,0,0,53,54,5,10,0,0,54,
        55,3,12,6,0,55,56,5,13,0,0,56,9,1,0,0,0,57,58,5,6,0,0,58,59,3,14,
        7,0,59,11,1,0,0,0,60,61,3,14,7,0,61,13,1,0,0,0,62,67,3,16,8,0,63,
        64,5,26,0,0,64,66,3,16,8,0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,
        0,0,67,68,1,0,0,0,68,15,1,0,0,0,69,67,1,0,0,0,70,72,3,18,9,0,71,
        70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,17,1,0,0,
        0,75,78,3,24,12,0,76,79,3,20,10,0,77,79,1,0,0,0,78,76,1,0,0,0,78,
        77,1,0,0,0,79,85,1,0,0,0,80,82,3,22,11,0,81,83,3,20,10,0,82,81,1,
        0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,75,1,0,0,0,84,80,1,0,0,0,85,
        19,1,0,0,0,86,87,7,0,0,0,87,21,1,0,0,0,88,89,5,14,0,0,89,90,3,14,
        7,0,90,91,5,15,0,0,91,23,1,0,0,0,92,93,3,26,13,0,93,25,1,0,0,0,94,
        99,5,33,0,0,95,99,5,6,0,0,96,99,3,28,14,0,97,99,5,5,0,0,98,94,1,
        0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,27,1,0,0,0,100,
        101,5,6,0,0,101,102,5,28,0,0,102,103,5,6,0,0,103,29,1,0,0,0,8,33,
        38,67,73,78,82,84,98
    ]

class VLADParser ( Parser ):

    grammarFileName = "VLADParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'fragment'", "'special'" ]

    symbolicNames = [ "<INVALID>", "DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "INT", "REGEX_LITERAL", "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", 
                      "FRAGMENT", "SPECIAL", "COLON", "COLONCOLON", "COMMA", 
                      "SEMI", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "RARROW", 
                      "LT", "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", 
                      "PLUS", "OR", "DOLLAR", "RANGE", "DOT", "AT", "POUND", 
                      "NOT", "ID", "WS", "ERRCHAR" ]

    RULE_rules = 0
    RULE_rule = 1
    RULE_tokenRule = 2
    RULE_specialRule = 3
    RULE_fragmentRule = 4
    RULE_ruleBlock = 5
    RULE_fragmentRuleBlock = 6
    RULE_altList = 7
    RULE_alternative = 8
    RULE_element = 9
    RULE_ebnfSuffix = 10
    RULE_block = 11
    RULE_atom = 12
    RULE_terminalDef = 13
    RULE_characterRange = 14

    ruleNames =  [ "rules", "rule", "tokenRule", "specialRule", "fragmentRule", 
                   "ruleBlock", "fragmentRuleBlock", "altList", "alternative", 
                   "element", "ebnfSuffix", "block", "atom", "terminalDef", 
                   "characterRange" ]

    EOF = Token.EOF
    DOC_COMMENT=1
    BLOCK_COMMENT=2
    LINE_COMMENT=3
    INT=4
    REGEX_LITERAL=5
    STRING_LITERAL=6
    UNTERMINATED_STRING_LITERAL=7
    FRAGMENT=8
    SPECIAL=9
    COLON=10
    COLONCOLON=11
    COMMA=12
    SEMI=13
    LPAREN=14
    RPAREN=15
    LBRACE=16
    RBRACE=17
    RARROW=18
    LT=19
    GT=20
    ASSIGN=21
    QUESTION=22
    STAR=23
    PLUS_ASSIGN=24
    PLUS=25
    OR=26
    DOLLAR=27
    RANGE=28
    DOT=29
    AT=30
    POUND=31
    NOT=32
    ID=33
    WS=34
    ERRCHAR=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RulesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VLADParser.RuleContext)
            else:
                return self.getTypedRuleContext(VLADParser.RuleContext,i)


        def getRuleIndex(self):
            return VLADParser.RULE_rules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRules" ):
                listener.enterRules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRules" ):
                listener.exitRules(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRules" ):
                return visitor.visitRules(self)
            else:
                return visitor.visitChildren(self)




    def rules(self):

        localctx = VLADParser.RulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.rule_()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8589935360) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tokenRule(self):
            return self.getTypedRuleContext(VLADParser.TokenRuleContext,0)


        def specialRule(self):
            return self.getTypedRuleContext(VLADParser.SpecialRuleContext,0)


        def fragmentRule(self):
            return self.getTypedRuleContext(VLADParser.FragmentRuleContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = VLADParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.tokenRule()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.specialRule()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.fragmentRule()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VLADParser.ID, 0)

        def COLON(self):
            return self.getToken(VLADParser.COLON, 0)

        def ruleBlock(self):
            return self.getTypedRuleContext(VLADParser.RuleBlockContext,0)


        def SEMI(self):
            return self.getToken(VLADParser.SEMI, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_tokenRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTokenRule" ):
                listener.enterTokenRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTokenRule" ):
                listener.exitTokenRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenRule" ):
                return visitor.visitTokenRule(self)
            else:
                return visitor.visitChildren(self)




    def tokenRule(self):

        localctx = VLADParser.TokenRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tokenRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(VLADParser.ID)
            self.state = 41
            self.match(VLADParser.COLON)
            self.state = 42
            self.ruleBlock()
            self.state = 43
            self.match(VLADParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPECIAL(self):
            return self.getToken(VLADParser.SPECIAL, 0)

        def ID(self):
            return self.getToken(VLADParser.ID, 0)

        def COLON(self):
            return self.getToken(VLADParser.COLON, 0)

        def ruleBlock(self):
            return self.getTypedRuleContext(VLADParser.RuleBlockContext,0)


        def SEMI(self):
            return self.getToken(VLADParser.SEMI, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_specialRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecialRule" ):
                listener.enterSpecialRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecialRule" ):
                listener.exitSpecialRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecialRule" ):
                return visitor.visitSpecialRule(self)
            else:
                return visitor.visitChildren(self)




    def specialRule(self):

        localctx = VLADParser.SpecialRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_specialRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(VLADParser.SPECIAL)
            self.state = 46
            self.match(VLADParser.ID)
            self.state = 47
            self.match(VLADParser.COLON)
            self.state = 48
            self.ruleBlock()
            self.state = 49
            self.match(VLADParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FragmentRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRAGMENT(self):
            return self.getToken(VLADParser.FRAGMENT, 0)

        def ID(self):
            return self.getToken(VLADParser.ID, 0)

        def COLON(self):
            return self.getToken(VLADParser.COLON, 0)

        def fragmentRuleBlock(self):
            return self.getTypedRuleContext(VLADParser.FragmentRuleBlockContext,0)


        def SEMI(self):
            return self.getToken(VLADParser.SEMI, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_fragmentRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFragmentRule" ):
                listener.enterFragmentRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFragmentRule" ):
                listener.exitFragmentRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFragmentRule" ):
                return visitor.visitFragmentRule(self)
            else:
                return visitor.visitChildren(self)




    def fragmentRule(self):

        localctx = VLADParser.FragmentRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fragmentRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(VLADParser.FRAGMENT)
            self.state = 52
            self.match(VLADParser.ID)
            self.state = 53
            self.match(VLADParser.COLON)
            self.state = 54
            self.fragmentRuleBlock()
            self.state = 55
            self.match(VLADParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(VLADParser.STRING_LITERAL, 0)

        def altList(self):
            return self.getTypedRuleContext(VLADParser.AltListContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_ruleBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleBlock" ):
                listener.enterRuleBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleBlock" ):
                listener.exitRuleBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleBlock" ):
                return visitor.visitRuleBlock(self)
            else:
                return visitor.visitChildren(self)




    def ruleBlock(self):

        localctx = VLADParser.RuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ruleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(VLADParser.STRING_LITERAL)
            self.state = 58
            self.altList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FragmentRuleBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def altList(self):
            return self.getTypedRuleContext(VLADParser.AltListContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_fragmentRuleBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFragmentRuleBlock" ):
                listener.enterFragmentRuleBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFragmentRuleBlock" ):
                listener.exitFragmentRuleBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFragmentRuleBlock" ):
                return visitor.visitFragmentRuleBlock(self)
            else:
                return visitor.visitChildren(self)




    def fragmentRuleBlock(self):

        localctx = VLADParser.FragmentRuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fragmentRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.altList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AltListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VLADParser.AlternativeContext)
            else:
                return self.getTypedRuleContext(VLADParser.AlternativeContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(VLADParser.OR)
            else:
                return self.getToken(VLADParser.OR, i)

        def getRuleIndex(self):
            return VLADParser.RULE_altList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAltList" ):
                listener.enterAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAltList" ):
                listener.exitAltList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAltList" ):
                return visitor.visitAltList(self)
            else:
                return visitor.visitChildren(self)




    def altList(self):

        localctx = VLADParser.AltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.alternative()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 63
                self.match(VLADParser.OR)
                self.state = 64
                self.alternative()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VLADParser.ElementContext)
            else:
                return self.getTypedRuleContext(VLADParser.ElementContext,i)


        def getRuleIndex(self):
            return VLADParser.RULE_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternative" ):
                listener.enterAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternative" ):
                listener.exitAlternative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternative" ):
                return visitor.visitAlternative(self)
            else:
                return visitor.visitChildren(self)




    def alternative(self):

        localctx = VLADParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.element()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8589951072) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(VLADParser.AtomContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(VLADParser.EbnfSuffixContext,0)


        def block(self):
            return self.getTypedRuleContext(VLADParser.BlockContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = VLADParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.atom()
                self.state = 78
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22, 23, 25]:
                    self.state = 76
                    self.ebnfSuffix()
                    pass
                elif token in [5, 6, 13, 14, 15, 26, 33]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.block()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 46137344) != 0):
                    self.state = 81
                    self.ebnfSuffix()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EbnfSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(VLADParser.QUESTION, 0)

        def STAR(self):
            return self.getToken(VLADParser.STAR, 0)

        def PLUS(self):
            return self.getToken(VLADParser.PLUS, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_ebnfSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEbnfSuffix" ):
                listener.enterEbnfSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEbnfSuffix" ):
                listener.exitEbnfSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEbnfSuffix" ):
                return visitor.visitEbnfSuffix(self)
            else:
                return visitor.visitChildren(self)




    def ebnfSuffix(self):

        localctx = VLADParser.EbnfSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 46137344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(VLADParser.LPAREN, 0)

        def altList(self):
            return self.getTypedRuleContext(VLADParser.AltListContext,0)


        def RPAREN(self):
            return self.getToken(VLADParser.RPAREN, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = VLADParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(VLADParser.LPAREN)
            self.state = 89
            self.altList()
            self.state = 90
            self.match(VLADParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminalDef(self):
            return self.getTypedRuleContext(VLADParser.TerminalDefContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = VLADParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.terminalDef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VLADParser.ID, 0)

        def STRING_LITERAL(self):
            return self.getToken(VLADParser.STRING_LITERAL, 0)

        def characterRange(self):
            return self.getTypedRuleContext(VLADParser.CharacterRangeContext,0)


        def REGEX_LITERAL(self):
            return self.getToken(VLADParser.REGEX_LITERAL, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_terminalDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminalDef" ):
                listener.enterTerminalDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminalDef" ):
                listener.exitTerminalDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminalDef" ):
                return visitor.visitTerminalDef(self)
            else:
                return visitor.visitChildren(self)




    def terminalDef(self):

        localctx = VLADParser.TerminalDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_terminalDef)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(VLADParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(VLADParser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.characterRange()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.match(VLADParser.REGEX_LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(VLADParser.STRING_LITERAL)
            else:
                return self.getToken(VLADParser.STRING_LITERAL, i)

        def RANGE(self):
            return self.getToken(VLADParser.RANGE, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_characterRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterRange" ):
                listener.enterCharacterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterRange" ):
                listener.exitCharacterRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacterRange" ):
                return visitor.visitCharacterRange(self)
            else:
                return visitor.visitChildren(self)




    def characterRange(self):

        localctx = VLADParser.CharacterRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(VLADParser.STRING_LITERAL)
            self.state = 101
            self.match(VLADParser.RANGE)
            self.state = 102
            self.match(VLADParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





