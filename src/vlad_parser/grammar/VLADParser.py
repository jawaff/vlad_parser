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
        4,1,36,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,1,1,1,1,1,1,1,
        3,1,42,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,
        8,1,8,5,8,75,8,8,10,8,12,8,78,9,8,1,9,4,9,81,8,9,11,9,12,9,82,1,
        10,1,10,1,10,3,10,88,8,10,1,10,1,10,3,10,92,8,10,3,10,94,8,10,1,
        11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,3,14,108,
        8,14,1,15,1,15,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,0,1,2,0,23,24,26,26,109,0,33,1,0,0,0,2,41,1,0,0,0,
        4,43,1,0,0,0,6,49,1,0,0,0,8,54,1,0,0,0,10,60,1,0,0,0,12,66,1,0,0,
        0,14,69,1,0,0,0,16,71,1,0,0,0,18,80,1,0,0,0,20,93,1,0,0,0,22,95,
        1,0,0,0,24,97,1,0,0,0,26,101,1,0,0,0,28,107,1,0,0,0,30,109,1,0,0,
        0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,1,1,0,0,0,37,42,3,4,2,0,38,42,3,6,3,0,39,42,3,8,4,0,40,
        42,3,10,5,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,
        0,0,42,3,1,0,0,0,43,44,5,8,0,0,44,45,5,34,0,0,45,46,5,11,0,0,46,
        47,3,12,6,0,47,48,5,14,0,0,48,5,1,0,0,0,49,50,5,34,0,0,50,51,5,11,
        0,0,51,52,3,12,6,0,52,53,5,14,0,0,53,7,1,0,0,0,54,55,5,10,0,0,55,
        56,5,34,0,0,56,57,5,11,0,0,57,58,3,12,6,0,58,59,5,14,0,0,59,9,1,
        0,0,0,60,61,5,9,0,0,61,62,5,34,0,0,62,63,5,11,0,0,63,64,3,14,7,0,
        64,65,5,14,0,0,65,11,1,0,0,0,66,67,5,6,0,0,67,68,3,16,8,0,68,13,
        1,0,0,0,69,70,3,16,8,0,70,15,1,0,0,0,71,76,3,18,9,0,72,73,5,27,0,
        0,73,75,3,18,9,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,
        1,0,0,0,77,17,1,0,0,0,78,76,1,0,0,0,79,81,3,20,10,0,80,79,1,0,0,
        0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,19,1,0,0,0,84,87,
        3,26,13,0,85,88,3,22,11,0,86,88,1,0,0,0,87,85,1,0,0,0,87,86,1,0,
        0,0,88,94,1,0,0,0,89,91,3,24,12,0,90,92,3,22,11,0,91,90,1,0,0,0,
        91,92,1,0,0,0,92,94,1,0,0,0,93,84,1,0,0,0,93,89,1,0,0,0,94,21,1,
        0,0,0,95,96,7,0,0,0,96,23,1,0,0,0,97,98,5,15,0,0,98,99,3,16,8,0,
        99,100,5,16,0,0,100,25,1,0,0,0,101,102,3,28,14,0,102,27,1,0,0,0,
        103,108,5,34,0,0,104,108,5,6,0,0,105,108,3,30,15,0,106,108,5,5,0,
        0,107,103,1,0,0,0,107,104,1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,
        0,108,29,1,0,0,0,109,110,5,6,0,0,110,111,5,29,0,0,111,112,5,6,0,
        0,112,31,1,0,0,0,8,35,41,76,82,87,91,93,107
    ]

class VLADParser ( Parser ):

    grammarFileName = "VLADParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'root'", "'fragment'", "'special'" ]

    symbolicNames = [ "<INVALID>", "DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "INT", "REGEX_LITERAL", "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", 
                      "ROOT", "FRAGMENT", "SPECIAL", "COLON", "COLONCOLON", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "RARROW", "LT", "GT", "ASSIGN", "QUESTION", "STAR", 
                      "PLUS_ASSIGN", "PLUS", "OR", "DOLLAR", "RANGE", "DOT", 
                      "AT", "POUND", "NOT", "ID", "WS", "ERRCHAR" ]

    RULE_rules = 0
    RULE_rule = 1
    RULE_rootTokenRule = 2
    RULE_tokenRule = 3
    RULE_specialRule = 4
    RULE_fragmentRule = 5
    RULE_ruleBlock = 6
    RULE_fragmentRuleBlock = 7
    RULE_altList = 8
    RULE_alternative = 9
    RULE_element = 10
    RULE_ebnfSuffix = 11
    RULE_block = 12
    RULE_atom = 13
    RULE_terminalDef = 14
    RULE_characterRange = 15

    ruleNames =  [ "rules", "rule", "rootTokenRule", "tokenRule", "specialRule", 
                   "fragmentRule", "ruleBlock", "fragmentRuleBlock", "altList", 
                   "alternative", "element", "ebnfSuffix", "block", "atom", 
                   "terminalDef", "characterRange" ]

    EOF = Token.EOF
    DOC_COMMENT=1
    BLOCK_COMMENT=2
    LINE_COMMENT=3
    INT=4
    REGEX_LITERAL=5
    STRING_LITERAL=6
    UNTERMINATED_STRING_LITERAL=7
    ROOT=8
    FRAGMENT=9
    SPECIAL=10
    COLON=11
    COLONCOLON=12
    COMMA=13
    SEMI=14
    LPAREN=15
    RPAREN=16
    LBRACE=17
    RBRACE=18
    RARROW=19
    LT=20
    GT=21
    ASSIGN=22
    QUESTION=23
    STAR=24
    PLUS_ASSIGN=25
    PLUS=26
    OR=27
    DOLLAR=28
    RANGE=29
    DOT=30
    AT=31
    POUND=32
    NOT=33
    ID=34
    WS=35
    ERRCHAR=36

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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.rule_()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17179870976) != 0)):
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

        def rootTokenRule(self):
            return self.getTypedRuleContext(VLADParser.RootTokenRuleContext,0)


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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.rootTokenRule()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.tokenRule()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.specialRule()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
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


    class RootTokenRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT(self):
            return self.getToken(VLADParser.ROOT, 0)

        def ID(self):
            return self.getToken(VLADParser.ID, 0)

        def COLON(self):
            return self.getToken(VLADParser.COLON, 0)

        def ruleBlock(self):
            return self.getTypedRuleContext(VLADParser.RuleBlockContext,0)


        def SEMI(self):
            return self.getToken(VLADParser.SEMI, 0)

        def getRuleIndex(self):
            return VLADParser.RULE_rootTokenRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootTokenRule" ):
                listener.enterRootTokenRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootTokenRule" ):
                listener.exitRootTokenRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRootTokenRule" ):
                return visitor.visitRootTokenRule(self)
            else:
                return visitor.visitChildren(self)




    def rootTokenRule(self):

        localctx = VLADParser.RootTokenRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rootTokenRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(VLADParser.ROOT)
            self.state = 44
            self.match(VLADParser.ID)
            self.state = 45
            self.match(VLADParser.COLON)
            self.state = 46
            self.ruleBlock()
            self.state = 47
            self.match(VLADParser.SEMI)
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
        self.enterRule(localctx, 6, self.RULE_tokenRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(VLADParser.ID)
            self.state = 50
            self.match(VLADParser.COLON)
            self.state = 51
            self.ruleBlock()
            self.state = 52
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
        self.enterRule(localctx, 8, self.RULE_specialRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(VLADParser.SPECIAL)
            self.state = 55
            self.match(VLADParser.ID)
            self.state = 56
            self.match(VLADParser.COLON)
            self.state = 57
            self.ruleBlock()
            self.state = 58
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
        self.enterRule(localctx, 10, self.RULE_fragmentRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(VLADParser.FRAGMENT)
            self.state = 61
            self.match(VLADParser.ID)
            self.state = 62
            self.match(VLADParser.COLON)
            self.state = 63
            self.fragmentRuleBlock()
            self.state = 64
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
        self.enterRule(localctx, 12, self.RULE_ruleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(VLADParser.STRING_LITERAL)
            self.state = 67
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
        self.enterRule(localctx, 14, self.RULE_fragmentRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
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
        self.enterRule(localctx, 16, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.alternative()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 72
                self.match(VLADParser.OR)
                self.state = 73
                self.alternative()
                self.state = 78
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
        self.enterRule(localctx, 18, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.element()
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17179902048) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.atom()
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23, 24, 26]:
                    self.state = 85
                    self.ebnfSuffix()
                    pass
                elif token in [5, 6, 14, 15, 16, 27, 34]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.block()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 92274688) != 0):
                    self.state = 90
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
        self.enterRule(localctx, 22, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 92274688) != 0)):
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
        self.enterRule(localctx, 24, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(VLADParser.LPAREN)
            self.state = 98
            self.altList()
            self.state = 99
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
        self.enterRule(localctx, 26, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
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
        self.enterRule(localctx, 28, self.RULE_terminalDef)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(VLADParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(VLADParser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.characterRange()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
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
        self.enterRule(localctx, 30, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(VLADParser.STRING_LITERAL)
            self.state = 110
            self.match(VLADParser.RANGE)
            self.state = 111
            self.match(VLADParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





