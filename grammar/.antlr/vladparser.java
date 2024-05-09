// Generated from /home/jake/Projects/transformer_parser/grammar/vladparser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class vladparser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		FRAGMENT_REF=1, RULE_REF=2, DOC_COMMENT=3, BLOCK_COMMENT=4, LINE_COMMENT=5, 
		INT=6, REGEX_LITERAL=7, STRING_LITERAL=8, UNTERMINATED_STRING_LITERAL=9, 
		FRAGMENT=10, SPECIAL=11, COLON=12, COLONCOLON=13, COMMA=14, SEMI=15, LPAREN=16, 
		RPAREN=17, LBRACE=18, RBRACE=19, RARROW=20, LT=21, GT=22, ASSIGN=23, QUESTION=24, 
		STAR=25, PLUS_ASSIGN=26, PLUS=27, OR=28, DOLLAR=29, RANGE=30, DOT=31, 
		AT=32, POUND=33, NOT=34, ID=35, WS=36, ERRCHAR=37;
	public static final int
		RULE_tokenRule = 0, RULE_specialRule = 1, RULE_fragmentRule = 2, RULE_ruleBlock = 3, 
		RULE_ruleAltList = 4, RULE_lexerRuleBlock = 5, RULE_lexerAltList = 6, 
		RULE_lexerAlt = 7, RULE_lexerElement = 8, RULE_lexerBlock = 9, RULE_altList = 10, 
		RULE_alternative = 11, RULE_element = 12, RULE_ebnfSuffix = 13, RULE_lexerAtom = 14, 
		RULE_atom = 15, RULE_notSet = 16, RULE_blockSet = 17, RULE_setElement = 18, 
		RULE_ruleref = 19, RULE_block = 20, RULE_characterRange = 21, RULE_terminalDef = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"tokenRule", "specialRule", "fragmentRule", "ruleBlock", "ruleAltList", 
			"lexerRuleBlock", "lexerAltList", "lexerAlt", "lexerElement", "lexerBlock", 
			"altList", "alternative", "element", "ebnfSuffix", "lexerAtom", "atom", 
			"notSet", "blockSet", "setElement", "ruleref", "block", "characterRange", 
			"terminalDef"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "'fragment'", 
			"'special'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FRAGMENT_REF", "RULE_REF", "DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", 
			"INT", "REGEX_LITERAL", "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", 
			"FRAGMENT", "SPECIAL", "COLON", "COLONCOLON", "COMMA", "SEMI", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "RARROW", "LT", "GT", "ASSIGN", "QUESTION", 
			"STAR", "PLUS_ASSIGN", "PLUS", "OR", "DOLLAR", "RANGE", "DOT", "AT", 
			"POUND", "NOT", "ID", "WS", "ERRCHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "vladparser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public vladparser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokenRuleContext extends ParserRuleContext {
		public TerminalNode RULE_REF() { return getToken(vladparser.RULE_REF, 0); }
		public TerminalNode COLON() { return getToken(vladparser.COLON, 0); }
		public RuleBlockContext ruleBlock() {
			return getRuleContext(RuleBlockContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vladparser.SEMI, 0); }
		public TokenRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokenRule; }
	}

	public final TokenRuleContext tokenRule() throws RecognitionException {
		TokenRuleContext _localctx = new TokenRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_tokenRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(RULE_REF);
			setState(47);
			match(COLON);
			setState(48);
			ruleBlock();
			setState(49);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SpecialRuleContext extends ParserRuleContext {
		public TerminalNode SPECIAL() { return getToken(vladparser.SPECIAL, 0); }
		public TerminalNode RULE_REF() { return getToken(vladparser.RULE_REF, 0); }
		public TerminalNode COLON() { return getToken(vladparser.COLON, 0); }
		public RuleBlockContext ruleBlock() {
			return getRuleContext(RuleBlockContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vladparser.SEMI, 0); }
		public SpecialRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specialRule; }
	}

	public final SpecialRuleContext specialRule() throws RecognitionException {
		SpecialRuleContext _localctx = new SpecialRuleContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_specialRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(SPECIAL);
			setState(52);
			match(RULE_REF);
			setState(53);
			match(COLON);
			setState(54);
			ruleBlock();
			setState(55);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FragmentRuleContext extends ParserRuleContext {
		public TerminalNode FRAGMENT() { return getToken(vladparser.FRAGMENT, 0); }
		public TerminalNode FRAGMENT_REF() { return getToken(vladparser.FRAGMENT_REF, 0); }
		public TerminalNode COLON() { return getToken(vladparser.COLON, 0); }
		public LexerRuleBlockContext lexerRuleBlock() {
			return getRuleContext(LexerRuleBlockContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vladparser.SEMI, 0); }
		public FragmentRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fragmentRule; }
	}

	public final FragmentRuleContext fragmentRule() throws RecognitionException {
		FragmentRuleContext _localctx = new FragmentRuleContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_fragmentRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(FRAGMENT);
			setState(58);
			match(FRAGMENT_REF);
			setState(59);
			match(COLON);
			setState(60);
			lexerRuleBlock();
			setState(61);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleBlockContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(vladparser.STRING_LITERAL, 0); }
		public RuleAltListContext ruleAltList() {
			return getRuleContext(RuleAltListContext.class,0);
		}
		public RuleBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleBlock; }
	}

	public final RuleBlockContext ruleBlock() throws RecognitionException {
		RuleBlockContext _localctx = new RuleBlockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ruleBlock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(STRING_LITERAL);
			setState(64);
			ruleAltList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleAltListContext extends ParserRuleContext {
		public List<AlternativeContext> alternative() {
			return getRuleContexts(AlternativeContext.class);
		}
		public AlternativeContext alternative(int i) {
			return getRuleContext(AlternativeContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(vladparser.OR); }
		public TerminalNode OR(int i) {
			return getToken(vladparser.OR, i);
		}
		public RuleAltListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleAltList; }
	}

	public final RuleAltListContext ruleAltList() throws RecognitionException {
		RuleAltListContext _localctx = new RuleAltListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ruleAltList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			alternative();
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(67);
				match(OR);
				setState(68);
				alternative();
				}
				}
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LexerRuleBlockContext extends ParserRuleContext {
		public LexerAltListContext lexerAltList() {
			return getRuleContext(LexerAltListContext.class,0);
		}
		public LexerRuleBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexerRuleBlock; }
	}

	public final LexerRuleBlockContext lexerRuleBlock() throws RecognitionException {
		LexerRuleBlockContext _localctx = new LexerRuleBlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_lexerRuleBlock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			lexerAltList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LexerAltListContext extends ParserRuleContext {
		public List<LexerAltContext> lexerAlt() {
			return getRuleContexts(LexerAltContext.class);
		}
		public LexerAltContext lexerAlt(int i) {
			return getRuleContext(LexerAltContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(vladparser.OR); }
		public TerminalNode OR(int i) {
			return getToken(vladparser.OR, i);
		}
		public LexerAltListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexerAltList; }
	}

	public final LexerAltListContext lexerAltList() throws RecognitionException {
		LexerAltListContext _localctx = new LexerAltListContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_lexerAltList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			lexerAlt();
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(77);
				match(OR);
				setState(78);
				lexerAlt();
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LexerAltContext extends ParserRuleContext {
		public List<LexerElementContext> lexerElement() {
			return getRuleContexts(LexerElementContext.class);
		}
		public LexerElementContext lexerElement(int i) {
			return getRuleContext(LexerElementContext.class,i);
		}
		public LexerAltContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexerAlt; }
	}

	public final LexerAltContext lexerAlt() throws RecognitionException {
		LexerAltContext _localctx = new LexerAltContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_lexerAlt);
		int _la;
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FRAGMENT_REF:
			case STRING_LITERAL:
			case LPAREN:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(85); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(84);
					lexerElement();
					}
					}
					setState(87); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 17179934978L) != 0) );
				}
				break;
			case SEMI:
			case RPAREN:
			case OR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LexerElementContext extends ParserRuleContext {
		public LexerAtomContext lexerAtom() {
			return getRuleContext(LexerAtomContext.class,0);
		}
		public EbnfSuffixContext ebnfSuffix() {
			return getRuleContext(EbnfSuffixContext.class,0);
		}
		public LexerBlockContext lexerBlock() {
			return getRuleContext(LexerBlockContext.class,0);
		}
		public LexerElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexerElement; }
	}

	public final LexerElementContext lexerElement() throws RecognitionException {
		LexerElementContext _localctx = new LexerElementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_lexerElement);
		int _la;
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FRAGMENT_REF:
			case STRING_LITERAL:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(92);
				lexerAtom();
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 184549376L) != 0)) {
					{
					setState(93);
					ebnfSuffix();
					}
				}

				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(96);
				lexerBlock();
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 184549376L) != 0)) {
					{
					setState(97);
					ebnfSuffix();
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LexerBlockContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vladparser.LPAREN, 0); }
		public LexerAltListContext lexerAltList() {
			return getRuleContext(LexerAltListContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vladparser.RPAREN, 0); }
		public LexerBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexerBlock; }
	}

	public final LexerBlockContext lexerBlock() throws RecognitionException {
		LexerBlockContext _localctx = new LexerBlockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_lexerBlock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(LPAREN);
			setState(103);
			lexerAltList();
			setState(104);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AltListContext extends ParserRuleContext {
		public List<AlternativeContext> alternative() {
			return getRuleContexts(AlternativeContext.class);
		}
		public AlternativeContext alternative(int i) {
			return getRuleContext(AlternativeContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(vladparser.OR); }
		public TerminalNode OR(int i) {
			return getToken(vladparser.OR, i);
		}
		public AltListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_altList; }
	}

	public final AltListContext altList() throws RecognitionException {
		AltListContext _localctx = new AltListContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_altList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			alternative();
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(107);
				match(OR);
				setState(108);
				alternative();
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AlternativeContext extends ParserRuleContext {
		public List<ElementContext> element() {
			return getRuleContexts(ElementContext.class);
		}
		public ElementContext element(int i) {
			return getRuleContext(ElementContext.class,i);
		}
		public AlternativeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alternative; }
	}

	public final AlternativeContext alternative() throws RecognitionException {
		AlternativeContext _localctx = new AlternativeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_alternative);
		int _la;
		try {
			setState(120);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FRAGMENT_REF:
			case RULE_REF:
			case STRING_LITERAL:
			case LPAREN:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(115); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(114);
					element();
					}
					}
					setState(117); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 17179934982L) != 0) );
				}
				break;
			case SEMI:
			case RPAREN:
			case OR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElementContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public EbnfSuffixContext ebnfSuffix() {
			return getRuleContext(EbnfSuffixContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element; }
	}

	public final ElementContext element() throws RecognitionException {
		ElementContext _localctx = new ElementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_element);
		int _la;
		try {
			setState(131);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FRAGMENT_REF:
			case RULE_REF:
			case STRING_LITERAL:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(122);
				atom();
				setState(125);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case QUESTION:
				case STAR:
				case PLUS:
					{
					setState(123);
					ebnfSuffix();
					}
					break;
				case FRAGMENT_REF:
				case RULE_REF:
				case STRING_LITERAL:
				case SEMI:
				case LPAREN:
				case RPAREN:
				case OR:
				case NOT:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				block();
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 184549376L) != 0)) {
					{
					setState(128);
					ebnfSuffix();
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EbnfSuffixContext extends ParserRuleContext {
		public TerminalNode QUESTION() { return getToken(vladparser.QUESTION, 0); }
		public TerminalNode STAR() { return getToken(vladparser.STAR, 0); }
		public TerminalNode PLUS() { return getToken(vladparser.PLUS, 0); }
		public EbnfSuffixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ebnfSuffix; }
	}

	public final EbnfSuffixContext ebnfSuffix() throws RecognitionException {
		EbnfSuffixContext _localctx = new EbnfSuffixContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ebnfSuffix);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 184549376L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LexerAtomContext extends ParserRuleContext {
		public CharacterRangeContext characterRange() {
			return getRuleContext(CharacterRangeContext.class,0);
		}
		public TerminalDefContext terminalDef() {
			return getRuleContext(TerminalDefContext.class,0);
		}
		public NotSetContext notSet() {
			return getRuleContext(NotSetContext.class,0);
		}
		public LexerAtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexerAtom; }
	}

	public final LexerAtomContext lexerAtom() throws RecognitionException {
		LexerAtomContext _localctx = new LexerAtomContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_lexerAtom);
		try {
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				characterRange();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				terminalDef();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(137);
				notSet();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public TerminalDefContext terminalDef() {
			return getRuleContext(TerminalDefContext.class,0);
		}
		public RulerefContext ruleref() {
			return getRuleContext(RulerefContext.class,0);
		}
		public NotSetContext notSet() {
			return getRuleContext(NotSetContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_atom);
		try {
			setState(143);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FRAGMENT_REF:
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				terminalDef();
				}
				break;
			case RULE_REF:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				ruleref();
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(142);
				notSet();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NotSetContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(vladparser.NOT, 0); }
		public SetElementContext setElement() {
			return getRuleContext(SetElementContext.class,0);
		}
		public BlockSetContext blockSet() {
			return getRuleContext(BlockSetContext.class,0);
		}
		public NotSetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_notSet; }
	}

	public final NotSetContext notSet() throws RecognitionException {
		NotSetContext _localctx = new NotSetContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_notSet);
		try {
			setState(149);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				match(NOT);
				setState(146);
				setElement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				match(NOT);
				setState(148);
				blockSet();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockSetContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vladparser.LPAREN, 0); }
		public List<SetElementContext> setElement() {
			return getRuleContexts(SetElementContext.class);
		}
		public SetElementContext setElement(int i) {
			return getRuleContext(SetElementContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vladparser.RPAREN, 0); }
		public List<TerminalNode> OR() { return getTokens(vladparser.OR); }
		public TerminalNode OR(int i) {
			return getToken(vladparser.OR, i);
		}
		public BlockSetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockSet; }
	}

	public final BlockSetContext blockSet() throws RecognitionException {
		BlockSetContext _localctx = new BlockSetContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_blockSet);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(LPAREN);
			setState(152);
			setElement();
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(153);
				match(OR);
				setState(154);
				setElement();
				}
				}
				setState(159);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(160);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetElementContext extends ParserRuleContext {
		public TerminalNode FRAGMENT_REF() { return getToken(vladparser.FRAGMENT_REF, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(vladparser.STRING_LITERAL, 0); }
		public CharacterRangeContext characterRange() {
			return getRuleContext(CharacterRangeContext.class,0);
		}
		public SetElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setElement; }
	}

	public final SetElementContext setElement() throws RecognitionException {
		SetElementContext _localctx = new SetElementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_setElement);
		try {
			setState(165);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				match(FRAGMENT_REF);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				match(STRING_LITERAL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(164);
				characterRange();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RulerefContext extends ParserRuleContext {
		public TerminalNode RULE_REF() { return getToken(vladparser.RULE_REF, 0); }
		public RulerefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleref; }
	}

	public final RulerefContext ruleref() throws RecognitionException {
		RulerefContext _localctx = new RulerefContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_ruleref);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(RULE_REF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vladparser.LPAREN, 0); }
		public AltListContext altList() {
			return getRuleContext(AltListContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vladparser.RPAREN, 0); }
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(LPAREN);
			setState(170);
			altList();
			setState(171);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CharacterRangeContext extends ParserRuleContext {
		public List<TerminalNode> STRING_LITERAL() { return getTokens(vladparser.STRING_LITERAL); }
		public TerminalNode STRING_LITERAL(int i) {
			return getToken(vladparser.STRING_LITERAL, i);
		}
		public TerminalNode RANGE() { return getToken(vladparser.RANGE, 0); }
		public CharacterRangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_characterRange; }
	}

	public final CharacterRangeContext characterRange() throws RecognitionException {
		CharacterRangeContext _localctx = new CharacterRangeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_characterRange);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(STRING_LITERAL);
			setState(174);
			match(RANGE);
			setState(175);
			match(STRING_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminalDefContext extends ParserRuleContext {
		public TerminalNode FRAGMENT_REF() { return getToken(vladparser.FRAGMENT_REF, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(vladparser.STRING_LITERAL, 0); }
		public TerminalDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminalDef; }
	}

	public final TerminalDefContext terminalDef() throws RecognitionException {
		TerminalDefContext _localctx = new TerminalDefContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_terminalDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			_la = _input.LA(1);
			if ( !(_la==FRAGMENT_REF || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001%\u00b4\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0005\u0004F\b\u0004\n\u0004\f\u0004I\t\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006P\b\u0006"+
		"\n\u0006\f\u0006S\t\u0006\u0001\u0007\u0004\u0007V\b\u0007\u000b\u0007"+
		"\f\u0007W\u0001\u0007\u0003\u0007[\b\u0007\u0001\b\u0001\b\u0003\b_\b"+
		"\b\u0001\b\u0001\b\u0003\bc\b\b\u0003\be\b\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0005\nn\b\n\n\n\f\nq\t\n\u0001\u000b\u0004"+
		"\u000bt\b\u000b\u000b\u000b\f\u000bu\u0001\u000b\u0003\u000by\b\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0003\f~\b\f\u0001\f\u0001\f\u0003\f\u0082\b"+
		"\f\u0003\f\u0084\b\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0003\u000e\u008b\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u0090\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010"+
		"\u0096\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011"+
		"\u009c\b\u0011\n\u0011\f\u0011\u009f\t\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00a6\b\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0000"+
		"\u0000\u0017\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,\u0000\u0002\u0002\u0000\u0018\u0019\u001b"+
		"\u001b\u0002\u0000\u0001\u0001\b\b\u00b1\u0000.\u0001\u0000\u0000\u0000"+
		"\u00023\u0001\u0000\u0000\u0000\u00049\u0001\u0000\u0000\u0000\u0006?"+
		"\u0001\u0000\u0000\u0000\bB\u0001\u0000\u0000\u0000\nJ\u0001\u0000\u0000"+
		"\u0000\fL\u0001\u0000\u0000\u0000\u000eZ\u0001\u0000\u0000\u0000\u0010"+
		"d\u0001\u0000\u0000\u0000\u0012f\u0001\u0000\u0000\u0000\u0014j\u0001"+
		"\u0000\u0000\u0000\u0016x\u0001\u0000\u0000\u0000\u0018\u0083\u0001\u0000"+
		"\u0000\u0000\u001a\u0085\u0001\u0000\u0000\u0000\u001c\u008a\u0001\u0000"+
		"\u0000\u0000\u001e\u008f\u0001\u0000\u0000\u0000 \u0095\u0001\u0000\u0000"+
		"\u0000\"\u0097\u0001\u0000\u0000\u0000$\u00a5\u0001\u0000\u0000\u0000"+
		"&\u00a7\u0001\u0000\u0000\u0000(\u00a9\u0001\u0000\u0000\u0000*\u00ad"+
		"\u0001\u0000\u0000\u0000,\u00b1\u0001\u0000\u0000\u0000./\u0005\u0002"+
		"\u0000\u0000/0\u0005\f\u0000\u000001\u0003\u0006\u0003\u000012\u0005\u000f"+
		"\u0000\u00002\u0001\u0001\u0000\u0000\u000034\u0005\u000b\u0000\u0000"+
		"45\u0005\u0002\u0000\u000056\u0005\f\u0000\u000067\u0003\u0006\u0003\u0000"+
		"78\u0005\u000f\u0000\u00008\u0003\u0001\u0000\u0000\u00009:\u0005\n\u0000"+
		"\u0000:;\u0005\u0001\u0000\u0000;<\u0005\f\u0000\u0000<=\u0003\n\u0005"+
		"\u0000=>\u0005\u000f\u0000\u0000>\u0005\u0001\u0000\u0000\u0000?@\u0005"+
		"\b\u0000\u0000@A\u0003\b\u0004\u0000A\u0007\u0001\u0000\u0000\u0000BG"+
		"\u0003\u0016\u000b\u0000CD\u0005\u001c\u0000\u0000DF\u0003\u0016\u000b"+
		"\u0000EC\u0001\u0000\u0000\u0000FI\u0001\u0000\u0000\u0000GE\u0001\u0000"+
		"\u0000\u0000GH\u0001\u0000\u0000\u0000H\t\u0001\u0000\u0000\u0000IG\u0001"+
		"\u0000\u0000\u0000JK\u0003\f\u0006\u0000K\u000b\u0001\u0000\u0000\u0000"+
		"LQ\u0003\u000e\u0007\u0000MN\u0005\u001c\u0000\u0000NP\u0003\u000e\u0007"+
		"\u0000OM\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000"+
		"\u0000\u0000QR\u0001\u0000\u0000\u0000R\r\u0001\u0000\u0000\u0000SQ\u0001"+
		"\u0000\u0000\u0000TV\u0003\u0010\b\u0000UT\u0001\u0000\u0000\u0000VW\u0001"+
		"\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"X[\u0001\u0000\u0000\u0000Y[\u0001\u0000\u0000\u0000ZU\u0001\u0000\u0000"+
		"\u0000ZY\u0001\u0000\u0000\u0000[\u000f\u0001\u0000\u0000\u0000\\^\u0003"+
		"\u001c\u000e\u0000]_\u0003\u001a\r\u0000^]\u0001\u0000\u0000\u0000^_\u0001"+
		"\u0000\u0000\u0000_e\u0001\u0000\u0000\u0000`b\u0003\u0012\t\u0000ac\u0003"+
		"\u001a\r\u0000ba\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ce\u0001"+
		"\u0000\u0000\u0000d\\\u0001\u0000\u0000\u0000d`\u0001\u0000\u0000\u0000"+
		"e\u0011\u0001\u0000\u0000\u0000fg\u0005\u0010\u0000\u0000gh\u0003\f\u0006"+
		"\u0000hi\u0005\u0011\u0000\u0000i\u0013\u0001\u0000\u0000\u0000jo\u0003"+
		"\u0016\u000b\u0000kl\u0005\u001c\u0000\u0000ln\u0003\u0016\u000b\u0000"+
		"mk\u0001\u0000\u0000\u0000nq\u0001\u0000\u0000\u0000om\u0001\u0000\u0000"+
		"\u0000op\u0001\u0000\u0000\u0000p\u0015\u0001\u0000\u0000\u0000qo\u0001"+
		"\u0000\u0000\u0000rt\u0003\u0018\f\u0000sr\u0001\u0000\u0000\u0000tu\u0001"+
		"\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000"+
		"vy\u0001\u0000\u0000\u0000wy\u0001\u0000\u0000\u0000xs\u0001\u0000\u0000"+
		"\u0000xw\u0001\u0000\u0000\u0000y\u0017\u0001\u0000\u0000\u0000z}\u0003"+
		"\u001e\u000f\u0000{~\u0003\u001a\r\u0000|~\u0001\u0000\u0000\u0000}{\u0001"+
		"\u0000\u0000\u0000}|\u0001\u0000\u0000\u0000~\u0084\u0001\u0000\u0000"+
		"\u0000\u007f\u0081\u0003(\u0014\u0000\u0080\u0082\u0003\u001a\r\u0000"+
		"\u0081\u0080\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000"+
		"\u0082\u0084\u0001\u0000\u0000\u0000\u0083z\u0001\u0000\u0000\u0000\u0083"+
		"\u007f\u0001\u0000\u0000\u0000\u0084\u0019\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0007\u0000\u0000\u0000\u0086\u001b\u0001\u0000\u0000\u0000\u0087"+
		"\u008b\u0003*\u0015\u0000\u0088\u008b\u0003,\u0016\u0000\u0089\u008b\u0003"+
		" \u0010\u0000\u008a\u0087\u0001\u0000\u0000\u0000\u008a\u0088\u0001\u0000"+
		"\u0000\u0000\u008a\u0089\u0001\u0000\u0000\u0000\u008b\u001d\u0001\u0000"+
		"\u0000\u0000\u008c\u0090\u0003,\u0016\u0000\u008d\u0090\u0003&\u0013\u0000"+
		"\u008e\u0090\u0003 \u0010\u0000\u008f\u008c\u0001\u0000\u0000\u0000\u008f"+
		"\u008d\u0001\u0000\u0000\u0000\u008f\u008e\u0001\u0000\u0000\u0000\u0090"+
		"\u001f\u0001\u0000\u0000\u0000\u0091\u0092\u0005\"\u0000\u0000\u0092\u0096"+
		"\u0003$\u0012\u0000\u0093\u0094\u0005\"\u0000\u0000\u0094\u0096\u0003"+
		"\"\u0011\u0000\u0095\u0091\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000"+
		"\u0000\u0000\u0096!\u0001\u0000\u0000\u0000\u0097\u0098\u0005\u0010\u0000"+
		"\u0000\u0098\u009d\u0003$\u0012\u0000\u0099\u009a\u0005\u001c\u0000\u0000"+
		"\u009a\u009c\u0003$\u0012\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009c"+
		"\u009f\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0001\u0000\u0000\u0000\u009e\u00a0\u0001\u0000\u0000\u0000\u009f"+
		"\u009d\u0001\u0000\u0000\u0000\u00a0\u00a1\u0005\u0011\u0000\u0000\u00a1"+
		"#\u0001\u0000\u0000\u0000\u00a2\u00a6\u0005\u0001\u0000\u0000\u00a3\u00a6"+
		"\u0005\b\u0000\u0000\u00a4\u00a6\u0003*\u0015\u0000\u00a5\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a5\u00a4\u0001"+
		"\u0000\u0000\u0000\u00a6%\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005\u0002"+
		"\u0000\u0000\u00a8\'\u0001\u0000\u0000\u0000\u00a9\u00aa\u0005\u0010\u0000"+
		"\u0000\u00aa\u00ab\u0003\u0014\n\u0000\u00ab\u00ac\u0005\u0011\u0000\u0000"+
		"\u00ac)\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005\b\u0000\u0000\u00ae"+
		"\u00af\u0005\u001e\u0000\u0000\u00af\u00b0\u0005\b\u0000\u0000\u00b0+"+
		"\u0001\u0000\u0000\u0000\u00b1\u00b2\u0007\u0001\u0000\u0000\u00b2-\u0001"+
		"\u0000\u0000\u0000\u0012GQWZ^bdoux}\u0081\u0083\u008a\u008f\u0095\u009d"+
		"\u00a5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}