# Generated from ./grammar/vladparser.g4 by ANTLR 4.13.1
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
        4,1,37,180,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,5,4,70,8,4,10,
        4,12,4,73,9,4,1,5,1,5,1,6,1,6,1,6,5,6,80,8,6,10,6,12,6,83,9,6,1,
        7,4,7,86,8,7,11,7,12,7,87,1,7,3,7,91,8,7,1,8,1,8,3,8,95,8,8,1,8,
        1,8,3,8,99,8,8,3,8,101,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,110,
        8,10,10,10,12,10,113,9,10,1,11,4,11,116,8,11,11,11,12,11,117,1,11,
        3,11,121,8,11,1,12,1,12,1,12,3,12,126,8,12,1,12,1,12,3,12,130,8,
        12,3,12,132,8,12,1,13,1,13,1,14,1,14,1,14,3,14,139,8,14,1,15,1,15,
        1,15,3,15,144,8,15,1,16,1,16,1,16,1,16,3,16,150,8,16,1,17,1,17,1,
        17,1,17,5,17,156,8,17,10,17,12,17,159,9,17,1,17,1,17,1,18,1,18,1,
        18,3,18,166,8,18,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,0,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,0,2,2,0,24,25,27,27,2,0,1,1,8,8,177,0,46,
        1,0,0,0,2,51,1,0,0,0,4,57,1,0,0,0,6,63,1,0,0,0,8,66,1,0,0,0,10,74,
        1,0,0,0,12,76,1,0,0,0,14,90,1,0,0,0,16,100,1,0,0,0,18,102,1,0,0,
        0,20,106,1,0,0,0,22,120,1,0,0,0,24,131,1,0,0,0,26,133,1,0,0,0,28,
        138,1,0,0,0,30,143,1,0,0,0,32,149,1,0,0,0,34,151,1,0,0,0,36,165,
        1,0,0,0,38,167,1,0,0,0,40,169,1,0,0,0,42,173,1,0,0,0,44,177,1,0,
        0,0,46,47,5,2,0,0,47,48,5,12,0,0,48,49,3,6,3,0,49,50,5,15,0,0,50,
        1,1,0,0,0,51,52,5,11,0,0,52,53,5,2,0,0,53,54,5,12,0,0,54,55,3,6,
        3,0,55,56,5,15,0,0,56,3,1,0,0,0,57,58,5,10,0,0,58,59,5,1,0,0,59,
        60,5,12,0,0,60,61,3,10,5,0,61,62,5,15,0,0,62,5,1,0,0,0,63,64,5,8,
        0,0,64,65,3,8,4,0,65,7,1,0,0,0,66,71,3,22,11,0,67,68,5,28,0,0,68,
        70,3,22,11,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,
        0,0,72,9,1,0,0,0,73,71,1,0,0,0,74,75,3,12,6,0,75,11,1,0,0,0,76,81,
        3,14,7,0,77,78,5,28,0,0,78,80,3,14,7,0,79,77,1,0,0,0,80,83,1,0,0,
        0,81,79,1,0,0,0,81,82,1,0,0,0,82,13,1,0,0,0,83,81,1,0,0,0,84,86,
        3,16,8,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,
        88,91,1,0,0,0,89,91,1,0,0,0,90,85,1,0,0,0,90,89,1,0,0,0,91,15,1,
        0,0,0,92,94,3,28,14,0,93,95,3,26,13,0,94,93,1,0,0,0,94,95,1,0,0,
        0,95,101,1,0,0,0,96,98,3,18,9,0,97,99,3,26,13,0,98,97,1,0,0,0,98,
        99,1,0,0,0,99,101,1,0,0,0,100,92,1,0,0,0,100,96,1,0,0,0,101,17,1,
        0,0,0,102,103,5,16,0,0,103,104,3,12,6,0,104,105,5,17,0,0,105,19,
        1,0,0,0,106,111,3,22,11,0,107,108,5,28,0,0,108,110,3,22,11,0,109,
        107,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,
        21,1,0,0,0,113,111,1,0,0,0,114,116,3,24,12,0,115,114,1,0,0,0,116,
        117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,121,1,0,0,0,119,
        121,1,0,0,0,120,115,1,0,0,0,120,119,1,0,0,0,121,23,1,0,0,0,122,125,
        3,30,15,0,123,126,3,26,13,0,124,126,1,0,0,0,125,123,1,0,0,0,125,
        124,1,0,0,0,126,132,1,0,0,0,127,129,3,40,20,0,128,130,3,26,13,0,
        129,128,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,122,1,0,0,0,
        131,127,1,0,0,0,132,25,1,0,0,0,133,134,7,0,0,0,134,27,1,0,0,0,135,
        139,3,42,21,0,136,139,3,44,22,0,137,139,3,32,16,0,138,135,1,0,0,
        0,138,136,1,0,0,0,138,137,1,0,0,0,139,29,1,0,0,0,140,144,3,44,22,
        0,141,144,3,38,19,0,142,144,3,32,16,0,143,140,1,0,0,0,143,141,1,
        0,0,0,143,142,1,0,0,0,144,31,1,0,0,0,145,146,5,34,0,0,146,150,3,
        36,18,0,147,148,5,34,0,0,148,150,3,34,17,0,149,145,1,0,0,0,149,147,
        1,0,0,0,150,33,1,0,0,0,151,152,5,16,0,0,152,157,3,36,18,0,153,154,
        5,28,0,0,154,156,3,36,18,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,157,1,0,0,0,160,161,
        5,17,0,0,161,35,1,0,0,0,162,166,5,1,0,0,163,166,5,8,0,0,164,166,
        3,42,21,0,165,162,1,0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,37,
        1,0,0,0,167,168,5,2,0,0,168,39,1,0,0,0,169,170,5,16,0,0,170,171,
        3,20,10,0,171,172,5,17,0,0,172,41,1,0,0,0,173,174,5,8,0,0,174,175,
        5,30,0,0,175,176,5,8,0,0,176,43,1,0,0,0,177,178,7,1,0,0,178,45,1,
        0,0,0,18,71,81,87,90,94,98,100,111,117,120,125,129,131,138,143,149,
        157,165
    ]

class vladparser ( Parser ):

    grammarFileName = "vladparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'fragment'", "'special'" ]

    symbolicNames = [ "<INVALID>", "FRAGMENT_REF", "RULE_REF", "DOC_COMMENT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "INT", "REGEX_LITERAL", 
                      "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", "FRAGMENT", 
                      "SPECIAL", "COLON", "COLONCOLON", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "RARROW", 
                      "LT", "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", 
                      "PLUS", "OR", "DOLLAR", "RANGE", "DOT", "AT", "POUND", 
                      "NOT", "ID", "WS", "ERRCHAR" ]

    RULE_tokenRule = 0
    RULE_specialRule = 1
    RULE_fragmentRule = 2
    RULE_ruleBlock = 3
    RULE_ruleAltList = 4
    RULE_lexerRuleBlock = 5
    RULE_lexerAltList = 6
    RULE_lexerAlt = 7
    RULE_lexerElement = 8
    RULE_lexerBlock = 9
    RULE_altList = 10
    RULE_alternative = 11
    RULE_element = 12
    RULE_ebnfSuffix = 13
    RULE_lexerAtom = 14
    RULE_atom = 15
    RULE_notSet = 16
    RULE_blockSet = 17
    RULE_setElement = 18
    RULE_ruleref = 19
    RULE_block = 20
    RULE_characterRange = 21
    RULE_terminalDef = 22

    ruleNames =  [ "tokenRule", "specialRule", "fragmentRule", "ruleBlock", 
                   "ruleAltList", "lexerRuleBlock", "lexerAltList", "lexerAlt", 
                   "lexerElement", "lexerBlock", "altList", "alternative", 
                   "element", "ebnfSuffix", "lexerAtom", "atom", "notSet", 
                   "blockSet", "setElement", "ruleref", "block", "characterRange", 
                   "terminalDef" ]

    EOF = Token.EOF
    FRAGMENT_REF=1
    RULE_REF=2
    DOC_COMMENT=3
    BLOCK_COMMENT=4
    LINE_COMMENT=5
    INT=6
    REGEX_LITERAL=7
    STRING_LITERAL=8
    UNTERMINATED_STRING_LITERAL=9
    FRAGMENT=10
    SPECIAL=11
    COLON=12
    COLONCOLON=13
    COMMA=14
    SEMI=15
    LPAREN=16
    RPAREN=17
    LBRACE=18
    RBRACE=19
    RARROW=20
    LT=21
    GT=22
    ASSIGN=23
    QUESTION=24
    STAR=25
    PLUS_ASSIGN=26
    PLUS=27
    OR=28
    DOLLAR=29
    RANGE=30
    DOT=31
    AT=32
    POUND=33
    NOT=34
    ID=35
    WS=36
    ERRCHAR=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TokenRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(vladparser.RULE_REF, 0)

        def COLON(self):
            return self.getToken(vladparser.COLON, 0)

        def ruleBlock(self):
            return self.getTypedRuleContext(vladparser.RuleBlockContext,0)


        def SEMI(self):
            return self.getToken(vladparser.SEMI, 0)

        def getRuleIndex(self):
            return vladparser.RULE_tokenRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTokenRule" ):
                listener.enterTokenRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTokenRule" ):
                listener.exitTokenRule(self)




    def tokenRule(self):

        localctx = vladparser.TokenRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tokenRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(vladparser.RULE_REF)
            self.state = 47
            self.match(vladparser.COLON)
            self.state = 48
            self.ruleBlock()
            self.state = 49
            self.match(vladparser.SEMI)
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
            return self.getToken(vladparser.SPECIAL, 0)

        def RULE_REF(self):
            return self.getToken(vladparser.RULE_REF, 0)

        def COLON(self):
            return self.getToken(vladparser.COLON, 0)

        def ruleBlock(self):
            return self.getTypedRuleContext(vladparser.RuleBlockContext,0)


        def SEMI(self):
            return self.getToken(vladparser.SEMI, 0)

        def getRuleIndex(self):
            return vladparser.RULE_specialRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecialRule" ):
                listener.enterSpecialRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecialRule" ):
                listener.exitSpecialRule(self)




    def specialRule(self):

        localctx = vladparser.SpecialRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_specialRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(vladparser.SPECIAL)
            self.state = 52
            self.match(vladparser.RULE_REF)
            self.state = 53
            self.match(vladparser.COLON)
            self.state = 54
            self.ruleBlock()
            self.state = 55
            self.match(vladparser.SEMI)
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
            return self.getToken(vladparser.FRAGMENT, 0)

        def FRAGMENT_REF(self):
            return self.getToken(vladparser.FRAGMENT_REF, 0)

        def COLON(self):
            return self.getToken(vladparser.COLON, 0)

        def lexerRuleBlock(self):
            return self.getTypedRuleContext(vladparser.LexerRuleBlockContext,0)


        def SEMI(self):
            return self.getToken(vladparser.SEMI, 0)

        def getRuleIndex(self):
            return vladparser.RULE_fragmentRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFragmentRule" ):
                listener.enterFragmentRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFragmentRule" ):
                listener.exitFragmentRule(self)




    def fragmentRule(self):

        localctx = vladparser.FragmentRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fragmentRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(vladparser.FRAGMENT)
            self.state = 58
            self.match(vladparser.FRAGMENT_REF)
            self.state = 59
            self.match(vladparser.COLON)
            self.state = 60
            self.lexerRuleBlock()
            self.state = 61
            self.match(vladparser.SEMI)
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
            return self.getToken(vladparser.STRING_LITERAL, 0)

        def ruleAltList(self):
            return self.getTypedRuleContext(vladparser.RuleAltListContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_ruleBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleBlock" ):
                listener.enterRuleBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleBlock" ):
                listener.exitRuleBlock(self)




    def ruleBlock(self):

        localctx = vladparser.RuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ruleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(vladparser.STRING_LITERAL)
            self.state = 64
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
                return self.getTypedRuleContexts(vladparser.AlternativeContext)
            else:
                return self.getTypedRuleContext(vladparser.AlternativeContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(vladparser.OR)
            else:
                return self.getToken(vladparser.OR, i)

        def getRuleIndex(self):
            return vladparser.RULE_ruleAltList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleAltList" ):
                listener.enterRuleAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleAltList" ):
                listener.exitRuleAltList(self)




    def ruleAltList(self):

        localctx = vladparser.RuleAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ruleAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.alternative()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 67
                self.match(vladparser.OR)
                self.state = 68
                self.alternative()
                self.state = 73
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
            return self.getTypedRuleContext(vladparser.LexerAltListContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_lexerRuleBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerRuleBlock" ):
                listener.enterLexerRuleBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerRuleBlock" ):
                listener.exitLexerRuleBlock(self)




    def lexerRuleBlock(self):

        localctx = vladparser.LexerRuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lexerRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
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
                return self.getTypedRuleContexts(vladparser.LexerAltContext)
            else:
                return self.getTypedRuleContext(vladparser.LexerAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(vladparser.OR)
            else:
                return self.getToken(vladparser.OR, i)

        def getRuleIndex(self):
            return vladparser.RULE_lexerAltList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAltList" ):
                listener.enterLexerAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAltList" ):
                listener.exitLexerAltList(self)




    def lexerAltList(self):

        localctx = vladparser.LexerAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lexerAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.lexerAlt()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 77
                self.match(vladparser.OR)
                self.state = 78
                self.lexerAlt()
                self.state = 83
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
                return self.getTypedRuleContexts(vladparser.LexerElementContext)
            else:
                return self.getTypedRuleContext(vladparser.LexerElementContext,i)


        def getRuleIndex(self):
            return vladparser.RULE_lexerAlt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAlt" ):
                listener.enterLexerAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAlt" ):
                listener.exitLexerAlt(self)




    def lexerAlt(self):

        localctx = vladparser.LexerAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lexerAlt)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8, 16, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 84
                    self.lexerElement()
                    self.state = 87 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17179934978) != 0)):
                        break

                pass
            elif token in [15, 17, 28]:
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
            return self.getTypedRuleContext(vladparser.LexerAtomContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(vladparser.EbnfSuffixContext,0)


        def lexerBlock(self):
            return self.getTypedRuleContext(vladparser.LexerBlockContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_lexerElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerElement" ):
                listener.enterLexerElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerElement" ):
                listener.exitLexerElement(self)




    def lexerElement(self):

        localctx = vladparser.LexerElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lexerElement)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.lexerAtom()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 184549376) != 0):
                    self.state = 93
                    self.ebnfSuffix()


                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.lexerBlock()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 184549376) != 0):
                    self.state = 97
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
            return self.getToken(vladparser.LPAREN, 0)

        def lexerAltList(self):
            return self.getTypedRuleContext(vladparser.LexerAltListContext,0)


        def RPAREN(self):
            return self.getToken(vladparser.RPAREN, 0)

        def getRuleIndex(self):
            return vladparser.RULE_lexerBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerBlock" ):
                listener.enterLexerBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerBlock" ):
                listener.exitLexerBlock(self)




    def lexerBlock(self):

        localctx = vladparser.LexerBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lexerBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(vladparser.LPAREN)
            self.state = 103
            self.lexerAltList()
            self.state = 104
            self.match(vladparser.RPAREN)
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
                return self.getTypedRuleContexts(vladparser.AlternativeContext)
            else:
                return self.getTypedRuleContext(vladparser.AlternativeContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(vladparser.OR)
            else:
                return self.getToken(vladparser.OR, i)

        def getRuleIndex(self):
            return vladparser.RULE_altList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAltList" ):
                listener.enterAltList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAltList" ):
                listener.exitAltList(self)




    def altList(self):

        localctx = vladparser.AltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.alternative()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 107
                self.match(vladparser.OR)
                self.state = 108
                self.alternative()
                self.state = 113
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
                return self.getTypedRuleContexts(vladparser.ElementContext)
            else:
                return self.getTypedRuleContext(vladparser.ElementContext,i)


        def getRuleIndex(self):
            return vladparser.RULE_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternative" ):
                listener.enterAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternative" ):
                listener.exitAlternative(self)




    def alternative(self):

        localctx = vladparser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 8, 16, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.element()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17179934982) != 0)):
                        break

                pass
            elif token in [15, 17, 28]:
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
            return self.getTypedRuleContext(vladparser.AtomContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(vladparser.EbnfSuffixContext,0)


        def block(self):
            return self.getTypedRuleContext(vladparser.BlockContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = vladparser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 8, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.atom()
                self.state = 125
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [24, 25, 27]:
                    self.state = 123
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 8, 15, 16, 17, 28, 34]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.block()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 184549376) != 0):
                    self.state = 128
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
            return self.getToken(vladparser.QUESTION, 0)

        def STAR(self):
            return self.getToken(vladparser.STAR, 0)

        def PLUS(self):
            return self.getToken(vladparser.PLUS, 0)

        def getRuleIndex(self):
            return vladparser.RULE_ebnfSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEbnfSuffix" ):
                listener.enterEbnfSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEbnfSuffix" ):
                listener.exitEbnfSuffix(self)




    def ebnfSuffix(self):

        localctx = vladparser.EbnfSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 184549376) != 0)):
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

        def characterRange(self):
            return self.getTypedRuleContext(vladparser.CharacterRangeContext,0)


        def terminalDef(self):
            return self.getTypedRuleContext(vladparser.TerminalDefContext,0)


        def notSet(self):
            return self.getTypedRuleContext(vladparser.NotSetContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_lexerAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerAtom" ):
                listener.enterLexerAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerAtom" ):
                listener.exitLexerAtom(self)




    def lexerAtom(self):

        localctx = vladparser.LexerAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lexerAtom)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.characterRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.terminalDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
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

        def terminalDef(self):
            return self.getTypedRuleContext(vladparser.TerminalDefContext,0)


        def ruleref(self):
            return self.getTypedRuleContext(vladparser.RulerefContext,0)


        def notSet(self):
            return self.getTypedRuleContext(vladparser.NotSetContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = vladparser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.terminalDef()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.ruleref()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.notSet()
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


    class NotSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(vladparser.NOT, 0)

        def setElement(self):
            return self.getTypedRuleContext(vladparser.SetElementContext,0)


        def blockSet(self):
            return self.getTypedRuleContext(vladparser.BlockSetContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_notSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotSet" ):
                listener.enterNotSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotSet" ):
                listener.exitNotSet(self)




    def notSet(self):

        localctx = vladparser.NotSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_notSet)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(vladparser.NOT)
                self.state = 146
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(vladparser.NOT)
                self.state = 148
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
            return self.getToken(vladparser.LPAREN, 0)

        def setElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vladparser.SetElementContext)
            else:
                return self.getTypedRuleContext(vladparser.SetElementContext,i)


        def RPAREN(self):
            return self.getToken(vladparser.RPAREN, 0)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(vladparser.OR)
            else:
                return self.getToken(vladparser.OR, i)

        def getRuleIndex(self):
            return vladparser.RULE_blockSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockSet" ):
                listener.enterBlockSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockSet" ):
                listener.exitBlockSet(self)




    def blockSet(self):

        localctx = vladparser.BlockSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_blockSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(vladparser.LPAREN)
            self.state = 152
            self.setElement()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 153
                self.match(vladparser.OR)
                self.state = 154
                self.setElement()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(vladparser.RPAREN)
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

        def FRAGMENT_REF(self):
            return self.getToken(vladparser.FRAGMENT_REF, 0)

        def STRING_LITERAL(self):
            return self.getToken(vladparser.STRING_LITERAL, 0)

        def characterRange(self):
            return self.getTypedRuleContext(vladparser.CharacterRangeContext,0)


        def getRuleIndex(self):
            return vladparser.RULE_setElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetElement" ):
                listener.enterSetElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetElement" ):
                listener.exitSetElement(self)




    def setElement(self):

        localctx = vladparser.SetElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_setElement)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(vladparser.FRAGMENT_REF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(vladparser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
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

        def RULE_REF(self):
            return self.getToken(vladparser.RULE_REF, 0)

        def getRuleIndex(self):
            return vladparser.RULE_ruleref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleref" ):
                listener.enterRuleref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleref" ):
                listener.exitRuleref(self)




    def ruleref(self):

        localctx = vladparser.RulerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ruleref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(vladparser.RULE_REF)
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
            return self.getToken(vladparser.LPAREN, 0)

        def altList(self):
            return self.getTypedRuleContext(vladparser.AltListContext,0)


        def RPAREN(self):
            return self.getToken(vladparser.RPAREN, 0)

        def getRuleIndex(self):
            return vladparser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = vladparser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(vladparser.LPAREN)
            self.state = 170
            self.altList()
            self.state = 171
            self.match(vladparser.RPAREN)
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
                return self.getTokens(vladparser.STRING_LITERAL)
            else:
                return self.getToken(vladparser.STRING_LITERAL, i)

        def RANGE(self):
            return self.getToken(vladparser.RANGE, 0)

        def getRuleIndex(self):
            return vladparser.RULE_characterRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterRange" ):
                listener.enterCharacterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterRange" ):
                listener.exitCharacterRange(self)




    def characterRange(self):

        localctx = vladparser.CharacterRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(vladparser.STRING_LITERAL)
            self.state = 174
            self.match(vladparser.RANGE)
            self.state = 175
            self.match(vladparser.STRING_LITERAL)
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

        def FRAGMENT_REF(self):
            return self.getToken(vladparser.FRAGMENT_REF, 0)

        def STRING_LITERAL(self):
            return self.getToken(vladparser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return vladparser.RULE_terminalDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminalDef" ):
                listener.enterTerminalDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminalDef" ):
                listener.exitTerminalDef(self)




    def terminalDef(self):

        localctx = vladparser.TerminalDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_terminalDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not(_la==1 or _la==8):
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





