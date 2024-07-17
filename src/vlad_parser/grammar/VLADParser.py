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
        4,1,35,195,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,4,0,52,8,0,11,0,
        12,0,53,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,84,
        8,6,10,6,12,6,87,9,6,1,7,1,7,1,8,1,8,1,8,5,8,94,8,8,10,8,12,8,97,
        9,8,1,9,4,9,100,8,9,11,9,12,9,101,1,9,3,9,105,8,9,1,10,1,10,3,10,
        109,8,10,1,10,1,10,3,10,113,8,10,3,10,115,8,10,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,5,12,124,8,12,10,12,12,12,127,9,12,1,13,4,13,130,
        8,13,11,13,12,13,131,1,13,3,13,135,8,13,1,14,1,14,1,14,3,14,140,
        8,14,1,14,1,14,3,14,144,8,14,3,14,146,8,14,1,15,1,15,1,16,1,16,1,
        16,3,16,153,8,16,1,17,1,17,1,17,1,17,3,17,159,8,17,1,18,1,18,1,18,
        1,18,3,18,165,8,18,1,19,1,19,1,19,1,19,5,19,171,8,19,10,19,12,19,
        174,9,19,1,19,1,19,1,20,1,20,1,20,3,20,181,8,20,1,21,1,21,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,2,
        2,0,22,23,25,25,2,0,6,6,33,33,194,0,51,1,0,0,0,2,58,1,0,0,0,4,60,
        1,0,0,0,6,65,1,0,0,0,8,71,1,0,0,0,10,77,1,0,0,0,12,80,1,0,0,0,14,
        88,1,0,0,0,16,90,1,0,0,0,18,104,1,0,0,0,20,114,1,0,0,0,22,116,1,
        0,0,0,24,120,1,0,0,0,26,134,1,0,0,0,28,145,1,0,0,0,30,147,1,0,0,
        0,32,152,1,0,0,0,34,158,1,0,0,0,36,164,1,0,0,0,38,166,1,0,0,0,40,
        180,1,0,0,0,42,182,1,0,0,0,44,184,1,0,0,0,46,188,1,0,0,0,48,192,
        1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,
        53,54,1,0,0,0,54,1,1,0,0,0,55,59,3,4,2,0,56,59,3,6,3,0,57,59,3,8,
        4,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,60,61,
        5,33,0,0,61,62,5,10,0,0,62,63,3,10,5,0,63,64,5,13,0,0,64,5,1,0,0,
        0,65,66,5,9,0,0,66,67,5,33,0,0,67,68,5,10,0,0,68,69,3,10,5,0,69,
        70,5,13,0,0,70,7,1,0,0,0,71,72,5,8,0,0,72,73,5,33,0,0,73,74,5,10,
        0,0,74,75,3,14,7,0,75,76,5,13,0,0,76,9,1,0,0,0,77,78,5,6,0,0,78,
        79,3,12,6,0,79,11,1,0,0,0,80,85,3,26,13,0,81,82,5,26,0,0,82,84,3,
        26,13,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,13,1,0,0,0,87,85,1,0,0,0,88,89,3,16,8,0,89,15,1,0,0,0,90,95,3,
        18,9,0,91,92,5,26,0,0,92,94,3,18,9,0,93,91,1,0,0,0,94,97,1,0,0,0,
        95,93,1,0,0,0,95,96,1,0,0,0,96,17,1,0,0,0,97,95,1,0,0,0,98,100,3,
        20,10,0,99,98,1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,
        0,0,102,105,1,0,0,0,103,105,1,0,0,0,104,99,1,0,0,0,104,103,1,0,0,
        0,105,19,1,0,0,0,106,108,3,32,16,0,107,109,3,30,15,0,108,107,1,0,
        0,0,108,109,1,0,0,0,109,115,1,0,0,0,110,112,3,22,11,0,111,113,3,
        30,15,0,112,111,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,106,
        1,0,0,0,114,110,1,0,0,0,115,21,1,0,0,0,116,117,5,14,0,0,117,118,
        3,16,8,0,118,119,5,15,0,0,119,23,1,0,0,0,120,125,3,26,13,0,121,122,
        5,26,0,0,122,124,3,26,13,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,25,1,0,0,0,127,125,1,0,0,0,128,130,3,
        28,14,0,129,128,1,0,0,0,130,131,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,135,1,0,0,0,133,135,1,0,0,0,134,129,1,0,0,0,134,133,
        1,0,0,0,135,27,1,0,0,0,136,139,3,34,17,0,137,140,3,30,15,0,138,140,
        1,0,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,146,1,0,0,0,141,143,
        3,44,22,0,142,144,3,30,15,0,143,142,1,0,0,0,143,144,1,0,0,0,144,
        146,1,0,0,0,145,136,1,0,0,0,145,141,1,0,0,0,146,29,1,0,0,0,147,148,
        7,0,0,0,148,31,1,0,0,0,149,153,3,40,20,0,150,153,3,48,24,0,151,153,
        3,36,18,0,152,149,1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,33,
        1,0,0,0,154,159,3,40,20,0,155,159,3,48,24,0,156,159,3,42,21,0,157,
        159,3,36,18,0,158,154,1,0,0,0,158,155,1,0,0,0,158,156,1,0,0,0,158,
        157,1,0,0,0,159,35,1,0,0,0,160,161,5,32,0,0,161,165,3,40,20,0,162,
        163,5,32,0,0,163,165,3,38,19,0,164,160,1,0,0,0,164,162,1,0,0,0,165,
        37,1,0,0,0,166,167,5,14,0,0,167,172,3,40,20,0,168,169,5,26,0,0,169,
        171,3,40,20,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,
        173,1,0,0,0,173,175,1,0,0,0,174,172,1,0,0,0,175,176,5,15,0,0,176,
        39,1,0,0,0,177,181,5,33,0,0,178,181,5,6,0,0,179,181,3,46,23,0,180,
        177,1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,41,1,0,0,0,182,183,
        5,33,0,0,183,43,1,0,0,0,184,185,5,14,0,0,185,186,3,24,12,0,186,187,
        5,15,0,0,187,45,1,0,0,0,188,189,5,6,0,0,189,190,5,28,0,0,190,191,
        5,6,0,0,191,47,1,0,0,0,192,193,7,1,0,0,193,49,1,0,0,0,20,53,58,85,
        95,101,104,108,112,114,125,131,134,139,143,145,152,158,164,172,180
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
    RULE_ruleAltList = 6
    RULE_lexerRuleBlock = 7
    RULE_lexerAltList = 8
    RULE_lexerAlt = 9
    RULE_lexerElement = 10
    RULE_lexerBlock = 11
    RULE_altList = 12
    RULE_alternative = 13
    RULE_element = 14
    RULE_ebnfSuffix = 15
    RULE_lexerAtom = 16
    RULE_atom = 17
    RULE_notSet = 18
    RULE_blockSet = 19
    RULE_setElement = 20
    RULE_ruleref = 21
    RULE_block = 22
    RULE_characterRange = 23
    RULE_terminalDef = 24

    ruleNames =  [ "rules", "rule", "tokenRule", "specialRule", "fragmentRule", 
                   "ruleBlock", "ruleAltList", "lexerRuleBlock", "lexerAltList", 
                   "lexerAlt", "lexerElement", "lexerBlock", "altList", 
                   "alternative", "element", "ebnfSuffix", "lexerAtom", 
                   "atom", "notSet", "blockSet", "setElement", "ruleref", 
                   "block", "characterRange", "terminalDef" ]

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
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.rule_()
                self.state = 53 
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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.tokenRule()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.specialRule()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
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
            self.state = 60
            self.match(VLADParser.ID)
            self.state = 61
            self.match(VLADParser.COLON)
            self.state = 62
            self.ruleBlock()
            self.state = 63
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
            self.state = 65
            self.match(VLADParser.SPECIAL)
            self.state = 66
            self.match(VLADParser.ID)
            self.state = 67
            self.match(VLADParser.COLON)
            self.state = 68
            self.ruleBlock()
            self.state = 69
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

        def lexerRuleBlock(self):
            return self.getTypedRuleContext(VLADParser.LexerRuleBlockContext,0)


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
            self.state = 71
            self.match(VLADParser.FRAGMENT)
            self.state = 72
            self.match(VLADParser.ID)
            self.state = 73
            self.match(VLADParser.COLON)
            self.state = 74
            self.lexerRuleBlock()
            self.state = 75
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

        def ruleAltList(self):
            return self.getTypedRuleContext(VLADParser.RuleAltListContext,0)


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
            self.state = 77
            self.match(VLADParser.STRING_LITERAL)
            self.state = 78
            self.ruleAltList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleAltListContext(ParserRuleContext):
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
            return VLADParser.RULE_ruleAltList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleAltList" ):
                listener.enterRuleAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleAltList" ):
                listener.exitRuleAltList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAltList" ):
                return visitor.visitRuleAltList(self)
            else:
                return visitor.visitChildren(self)




    def ruleAltList(self):

        localctx = VLADParser.RuleAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ruleAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.alternative()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 81
                self.match(VLADParser.OR)
                self.state = 82
                self.alternative()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerRuleBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAltList(self):
            return self.getTypedRuleContext(VLADParser.LexerAltListContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_lexerRuleBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerRuleBlock" ):
                listener.enterLexerRuleBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerRuleBlock" ):
                listener.exitLexerRuleBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerRuleBlock" ):
                return visitor.visitLexerRuleBlock(self)
            else:
                return visitor.visitChildren(self)




    def lexerRuleBlock(self):

        localctx = VLADParser.LexerRuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lexerRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.lexerAltList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAltListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAlt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VLADParser.LexerAltContext)
            else:
                return self.getTypedRuleContext(VLADParser.LexerAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(VLADParser.OR)
            else:
                return self.getToken(VLADParser.OR, i)

        def getRuleIndex(self):
            return VLADParser.RULE_lexerAltList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAltList" ):
                listener.enterLexerAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAltList" ):
                listener.exitLexerAltList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAltList" ):
                return visitor.visitLexerAltList(self)
            else:
                return visitor.visitChildren(self)




    def lexerAltList(self):

        localctx = VLADParser.LexerAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lexerAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.lexerAlt()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 91
                self.match(VLADParser.OR)
                self.state = 92
                self.lexerAlt()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VLADParser.LexerElementContext)
            else:
                return self.getTypedRuleContext(VLADParser.LexerElementContext,i)


        def getRuleIndex(self):
            return VLADParser.RULE_lexerAlt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAlt" ):
                listener.enterLexerAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAlt" ):
                listener.exitLexerAlt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAlt" ):
                return visitor.visitLexerAlt(self)
            else:
                return visitor.visitChildren(self)




    def lexerAlt(self):

        localctx = VLADParser.LexerAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lexerAlt)
        self._la = 0 # Token type
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 14, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 98
                    self.lexerElement()
                    self.state = 101 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12884918336) != 0)):
                        break

                pass
            elif token in [13, 15, 26]:
                self.enterOuterAlt(localctx, 2)

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


    class LexerElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAtom(self):
            return self.getTypedRuleContext(VLADParser.LexerAtomContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(VLADParser.EbnfSuffixContext,0)


        def lexerBlock(self):
            return self.getTypedRuleContext(VLADParser.LexerBlockContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_lexerElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerElement" ):
                listener.enterLexerElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerElement" ):
                listener.exitLexerElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerElement" ):
                return visitor.visitLexerElement(self)
            else:
                return visitor.visitChildren(self)




    def lexerElement(self):

        localctx = VLADParser.LexerElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lexerElement)
        self._la = 0 # Token type
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.lexerAtom()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 46137344) != 0):
                    self.state = 107
                    self.ebnfSuffix()


                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.lexerBlock()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 46137344) != 0):
                    self.state = 111
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


    class LexerBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(VLADParser.LPAREN, 0)

        def lexerAltList(self):
            return self.getTypedRuleContext(VLADParser.LexerAltListContext,0)


        def RPAREN(self):
            return self.getToken(VLADParser.RPAREN, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_lexerBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerBlock" ):
                listener.enterLexerBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerBlock" ):
                listener.exitLexerBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerBlock" ):
                return visitor.visitLexerBlock(self)
            else:
                return visitor.visitChildren(self)




    def lexerBlock(self):

        localctx = VLADParser.LexerBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lexerBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(VLADParser.LPAREN)
            self.state = 117
            self.lexerAltList()
            self.state = 118
            self.match(VLADParser.RPAREN)
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
        self.enterRule(localctx, 24, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.alternative()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 121
                self.match(VLADParser.OR)
                self.state = 122
                self.alternative()
                self.state = 127
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
        self.enterRule(localctx, 26, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 14, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 128
                    self.element()
                    self.state = 131 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12884918336) != 0)):
                        break

                pass
            elif token in [13, 15, 26]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 28, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.atom()
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22, 23, 25]:
                    self.state = 137
                    self.ebnfSuffix()
                    pass
                elif token in [6, 13, 14, 15, 26, 32, 33]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.block()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 46137344) != 0):
                    self.state = 142
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
        self.enterRule(localctx, 30, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
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


    class LexerAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def setElement(self):
            return self.getTypedRuleContext(VLADParser.SetElementContext,0)


        def terminalDef(self):
            return self.getTypedRuleContext(VLADParser.TerminalDefContext,0)


        def notSet(self):
            return self.getTypedRuleContext(VLADParser.NotSetContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_lexerAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAtom" ):
                listener.enterLexerAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAtom" ):
                listener.exitLexerAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAtom" ):
                return visitor.visitLexerAtom(self)
            else:
                return visitor.visitChildren(self)




    def lexerAtom(self):

        localctx = VLADParser.LexerAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lexerAtom)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.terminalDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.notSet()
                pass


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

        def setElement(self):
            return self.getTypedRuleContext(VLADParser.SetElementContext,0)


        def terminalDef(self):
            return self.getTypedRuleContext(VLADParser.TerminalDefContext,0)


        def ruleref(self):
            return self.getTypedRuleContext(VLADParser.RulerefContext,0)


        def notSet(self):
            return self.getTypedRuleContext(VLADParser.NotSetContext,0)


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
        self.enterRule(localctx, 34, self.RULE_atom)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.terminalDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.ruleref()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.notSet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(VLADParser.NOT, 0)

        def setElement(self):
            return self.getTypedRuleContext(VLADParser.SetElementContext,0)


        def blockSet(self):
            return self.getTypedRuleContext(VLADParser.BlockSetContext,0)


        def getRuleIndex(self):
            return VLADParser.RULE_notSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotSet" ):
                listener.enterNotSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotSet" ):
                listener.exitNotSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotSet" ):
                return visitor.visitNotSet(self)
            else:
                return visitor.visitChildren(self)




    def notSet(self):

        localctx = VLADParser.NotSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_notSet)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(VLADParser.NOT)
                self.state = 161
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(VLADParser.NOT)
                self.state = 163
                self.blockSet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(VLADParser.LPAREN, 0)

        def setElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VLADParser.SetElementContext)
            else:
                return self.getTypedRuleContext(VLADParser.SetElementContext,i)


        def RPAREN(self):
            return self.getToken(VLADParser.RPAREN, 0)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(VLADParser.OR)
            else:
                return self.getToken(VLADParser.OR, i)

        def getRuleIndex(self):
            return VLADParser.RULE_blockSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockSet" ):
                listener.enterBlockSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockSet" ):
                listener.exitBlockSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockSet" ):
                return visitor.visitBlockSet(self)
            else:
                return visitor.visitChildren(self)




    def blockSet(self):

        localctx = VLADParser.BlockSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_blockSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(VLADParser.LPAREN)
            self.state = 167
            self.setElement()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 168
                self.match(VLADParser.OR)
                self.state = 169
                self.setElement()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
            self.match(VLADParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetElementContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return VLADParser.RULE_setElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetElement" ):
                listener.enterSetElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetElement" ):
                listener.exitSetElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetElement" ):
                return visitor.visitSetElement(self)
            else:
                return visitor.visitChildren(self)




    def setElement(self):

        localctx = VLADParser.SetElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_setElement)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(VLADParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(VLADParser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.characterRange()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RulerefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VLADParser.ID, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_ruleref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleref" ):
                listener.enterRuleref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleref" ):
                listener.exitRuleref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleref" ):
                return visitor.visitRuleref(self)
            else:
                return visitor.visitChildren(self)




    def ruleref(self):

        localctx = VLADParser.RulerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ruleref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(VLADParser.ID)
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
        self.enterRule(localctx, 44, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(VLADParser.LPAREN)
            self.state = 185
            self.altList()
            self.state = 186
            self.match(VLADParser.RPAREN)
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
        self.enterRule(localctx, 46, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(VLADParser.STRING_LITERAL)
            self.state = 189
            self.match(VLADParser.RANGE)
            self.state = 190
            self.match(VLADParser.STRING_LITERAL)
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
        self.enterRule(localctx, 48, self.RULE_terminalDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not(_la==6 or _la==33):
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





