// Generated from /home/jake/Projects/transformer_parser/grammar/vladlexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class vladlexer extends LexerAdaptor {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DOC_COMMENT=1, BLOCK_COMMENT=2, LINE_COMMENT=3, INT=4, REGEX_LITERAL=5, 
		STRING_LITERAL=6, UNTERMINATED_STRING_LITERAL=7, FRAGMENT=8, SPECIAL=9, 
		COLON=10, COLONCOLON=11, COMMA=12, SEMI=13, LPAREN=14, RPAREN=15, LBRACE=16, 
		RBRACE=17, RARROW=18, LT=19, GT=20, ASSIGN=21, QUESTION=22, STAR=23, PLUS_ASSIGN=24, 
		PLUS=25, OR=26, DOLLAR=27, RANGE=28, DOT=29, AT=30, POUND=31, NOT=32, 
		ID=33, WS=34, ERRCHAR=35;
	public static final int
		COMMENT=2;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN", "COMMENT"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", "INT", "REGEX_LITERAL", 
			"STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", "FRAGMENT", "SPECIAL", 
			"COLON", "COLONCOLON", "COMMA", "SEMI", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "RARROW", "LT", "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", 
			"PLUS", "OR", "DOLLAR", "RANGE", "DOT", "AT", "POUND", "NOT", "ID", "WS", 
			"ERRCHAR", "Ws", "Hws", "Vws", "BlockComment", "DocComment", "LineComment", 
			"EscSeq", "EscAny", "UnicodeEsc", "DecimalNumeral", "HexDigit", "DecDigit", 
			"BoolLiteral", "CharLiteral", "SQuoteLiteral", "DQuoteLiteral", "USQuoteLiteral", 
			"NameChar", "NameStartChar", "Int", "Esc", "Colon", "DColon", "SQuote", 
			"DQuote", "LParen", "RParen", "LBrace", "RBrace", "LBrack", "RBrack", 
			"RArrow", "Lt", "Gt", "Equal", "Question", "Star", "Plus", "PlusAssign", 
			"Underscore", "Pipe", "Dollar", "Comma", "Semi", "Dot", "Range", "At", 
			"Pound", "Tilde"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'fragment'", "'special'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", "INT", "REGEX_LITERAL", 
			"STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", "FRAGMENT", "SPECIAL", 
			"COLON", "COLONCOLON", "COMMA", "SEMI", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "RARROW", "LT", "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", 
			"PLUS", "OR", "DOLLAR", "RANGE", "DOT", "AT", "POUND", "NOT", "ID", "WS", 
			"ERRCHAR"
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


	public vladlexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "vladlexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000#\u01da\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007"+
		":\u0002;\u0007;\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007"+
		"?\u0002@\u0007@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007"+
		"D\u0002E\u0007E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007"+
		"I\u0002J\u0007J\u0002K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007"+
		"N\u0002O\u0007O\u0002P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007"+
		"S\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0001\u001f\u0001 \u0001 \u0005 \u0100\b \n \f \u0103\t \u0001!\u0004"+
		"!\u0106\b!\u000b!\f!\u0107\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0001#\u0001#\u0003#\u0112\b#\u0001$\u0001$\u0001%\u0001%\u0001&\u0001"+
		"&\u0001&\u0001&\u0005&\u011c\b&\n&\f&\u011f\t&\u0001&\u0001&\u0001&\u0003"+
		"&\u0124\b&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0005\'\u012b\b\'\n"+
		"\'\f\'\u012e\t\'\u0001\'\u0001\'\u0001\'\u0003\'\u0133\b\'\u0001(\u0001"+
		"(\u0001(\u0001(\u0005(\u0139\b(\n(\f(\u013c\t(\u0001)\u0001)\u0001)\u0001"+
		")\u0001)\u0003)\u0143\b)\u0001*\u0001*\u0001*\u0001+\u0001+\u0001+\u0001"+
		"+\u0001+\u0003+\u014d\b+\u0003+\u014f\b+\u0003+\u0151\b+\u0003+\u0153"+
		"\b+\u0001,\u0001,\u0001,\u0005,\u0158\b,\n,\f,\u015b\t,\u0003,\u015d\b"+
		",\u0001-\u0001-\u0001.\u0001.\u0001/\u0001/\u0001/\u0001/\u0001/\u0001"+
		"/\u0001/\u0001/\u0001/\u0003/\u016c\b/\u00010\u00010\u00010\u00030\u0171"+
		"\b0\u00010\u00010\u00011\u00011\u00011\u00051\u0178\b1\n1\f1\u017b\t1"+
		"\u00011\u00011\u00012\u00012\u00012\u00052\u0182\b2\n2\f2\u0185\t2\u0001"+
		"2\u00012\u00013\u00013\u00013\u00053\u018c\b3\n3\f3\u018f\t3\u00014\u0001"+
		"4\u00014\u00014\u00034\u0195\b4\u00015\u00015\u00016\u00016\u00016\u0001"+
		"6\u00017\u00017\u00018\u00018\u00019\u00019\u00019\u0001:\u0001:\u0001"+
		";\u0001;\u0001<\u0001<\u0001=\u0001=\u0001>\u0001>\u0001?\u0001?\u0001"+
		"@\u0001@\u0001A\u0001A\u0001B\u0001B\u0001B\u0001C\u0001C\u0001D\u0001"+
		"D\u0001E\u0001E\u0001F\u0001F\u0001G\u0001G\u0001H\u0001H\u0001I\u0001"+
		"I\u0001I\u0001J\u0001J\u0001K\u0001K\u0001L\u0001L\u0001M\u0001M\u0001"+
		"N\u0001N\u0001O\u0001O\u0001P\u0001P\u0001P\u0001Q\u0001Q\u0001R\u0001"+
		"R\u0001S\u0001S\u0002\u011d\u012c\u0000T\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b"+
		"7\u001c9\u001d;\u001e=\u001f? A!C\"E#G\u0000I\u0000K\u0000M\u0000O\u0000"+
		"Q\u0000S\u0000U\u0000W\u0000Y\u0000[\u0000]\u0000_\u0000a\u0000c\u0000"+
		"e\u0000g\u0000i\u0000k\u0000m\u0000o\u0000q\u0000s\u0000u\u0000w\u0000"+
		"y\u0000{\u0000}\u0000\u007f\u0000\u0081\u0000\u0083\u0000\u0085\u0000"+
		"\u0087\u0000\u0089\u0000\u008b\u0000\u008d\u0000\u008f\u0000\u0091\u0000"+
		"\u0093\u0000\u0095\u0000\u0097\u0000\u0099\u0000\u009b\u0000\u009d\u0000"+
		"\u009f\u0000\u00a1\u0000\u00a3\u0000\u00a5\u0000\u00a7\u0000\u0001\u0000"+
		"\f\u0003\u0000\t\n\f\r  \u0002\u0000\t\t  \u0002\u0000\n\n\f\r\u0002\u0000"+
		"\n\n\r\r\b\u0000\"\"\'\'\\\\bbffnnrrtt\u0001\u000019\u0003\u000009AFa"+
		"f\u0001\u000009\u0004\u0000\n\n\r\r\'\'\\\\\u0004\u0000\n\n\r\r\"\"\\"+
		"\\\u0003\u0000\u00b7\u00b7\u0300\u036f\u203f\u2040\r\u0000AZaz\u00c0\u00d6"+
		"\u00d8\u00f6\u00f8\u02ff\u0370\u037d\u037f\u1fff\u200c\u200d\u2070\u218f"+
		"\u2c00\u2fef\u3001\u8000\ud7ff\u8000\uf900\u8000\ufdcf\u8000\ufdf0\u8000"+
		"\ufffd\u01c4\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000"+
		"\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000"+
		"A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001"+
		"\u0000\u0000\u0000\u0001\u00a9\u0001\u0000\u0000\u0000\u0003\u00ad\u0001"+
		"\u0000\u0000\u0000\u0005\u00b1\u0001\u0000\u0000\u0000\u0007\u00b5\u0001"+
		"\u0000\u0000\u0000\t\u00b7\u0001\u0000\u0000\u0000\u000b\u00ba\u0001\u0000"+
		"\u0000\u0000\r\u00bc\u0001\u0000\u0000\u0000\u000f\u00be\u0001\u0000\u0000"+
		"\u0000\u0011\u00c7\u0001\u0000\u0000\u0000\u0013\u00cf\u0001\u0000\u0000"+
		"\u0000\u0015\u00d1\u0001\u0000\u0000\u0000\u0017\u00d3\u0001\u0000\u0000"+
		"\u0000\u0019\u00d5\u0001\u0000\u0000\u0000\u001b\u00d7\u0001\u0000\u0000"+
		"\u0000\u001d\u00d9\u0001\u0000\u0000\u0000\u001f\u00db\u0001\u0000\u0000"+
		"\u0000!\u00dd\u0001\u0000\u0000\u0000#\u00df\u0001\u0000\u0000\u0000%"+
		"\u00e1\u0001\u0000\u0000\u0000\'\u00e3\u0001\u0000\u0000\u0000)\u00e5"+
		"\u0001\u0000\u0000\u0000+\u00e7\u0001\u0000\u0000\u0000-\u00e9\u0001\u0000"+
		"\u0000\u0000/\u00eb\u0001\u0000\u0000\u00001\u00ed\u0001\u0000\u0000\u0000"+
		"3\u00ef\u0001\u0000\u0000\u00005\u00f1\u0001\u0000\u0000\u00007\u00f3"+
		"\u0001\u0000\u0000\u00009\u00f5\u0001\u0000\u0000\u0000;\u00f7\u0001\u0000"+
		"\u0000\u0000=\u00f9\u0001\u0000\u0000\u0000?\u00fb\u0001\u0000\u0000\u0000"+
		"A\u00fd\u0001\u0000\u0000\u0000C\u0105\u0001\u0000\u0000\u0000E\u010b"+
		"\u0001\u0000\u0000\u0000G\u0111\u0001\u0000\u0000\u0000I\u0113\u0001\u0000"+
		"\u0000\u0000K\u0115\u0001\u0000\u0000\u0000M\u0117\u0001\u0000\u0000\u0000"+
		"O\u0125\u0001\u0000\u0000\u0000Q\u0134\u0001\u0000\u0000\u0000S\u013d"+
		"\u0001\u0000\u0000\u0000U\u0144\u0001\u0000\u0000\u0000W\u0147\u0001\u0000"+
		"\u0000\u0000Y\u015c\u0001\u0000\u0000\u0000[\u015e\u0001\u0000\u0000\u0000"+
		"]\u0160\u0001\u0000\u0000\u0000_\u016b\u0001\u0000\u0000\u0000a\u016d"+
		"\u0001\u0000\u0000\u0000c\u0174\u0001\u0000\u0000\u0000e\u017e\u0001\u0000"+
		"\u0000\u0000g\u0188\u0001\u0000\u0000\u0000i\u0194\u0001\u0000\u0000\u0000"+
		"k\u0196\u0001\u0000\u0000\u0000m\u0198\u0001\u0000\u0000\u0000o\u019c"+
		"\u0001\u0000\u0000\u0000q\u019e\u0001\u0000\u0000\u0000s\u01a0\u0001\u0000"+
		"\u0000\u0000u\u01a3\u0001\u0000\u0000\u0000w\u01a5\u0001\u0000\u0000\u0000"+
		"y\u01a7\u0001\u0000\u0000\u0000{\u01a9\u0001\u0000\u0000\u0000}\u01ab"+
		"\u0001\u0000\u0000\u0000\u007f\u01ad\u0001\u0000\u0000\u0000\u0081\u01af"+
		"\u0001\u0000\u0000\u0000\u0083\u01b1\u0001\u0000\u0000\u0000\u0085\u01b3"+
		"\u0001\u0000\u0000\u0000\u0087\u01b6\u0001\u0000\u0000\u0000\u0089\u01b8"+
		"\u0001\u0000\u0000\u0000\u008b\u01ba\u0001\u0000\u0000\u0000\u008d\u01bc"+
		"\u0001\u0000\u0000\u0000\u008f\u01be\u0001\u0000\u0000\u0000\u0091\u01c0"+
		"\u0001\u0000\u0000\u0000\u0093\u01c2\u0001\u0000\u0000\u0000\u0095\u01c5"+
		"\u0001\u0000\u0000\u0000\u0097\u01c7\u0001\u0000\u0000\u0000\u0099\u01c9"+
		"\u0001\u0000\u0000\u0000\u009b\u01cb\u0001\u0000\u0000\u0000\u009d\u01cd"+
		"\u0001\u0000\u0000\u0000\u009f\u01cf\u0001\u0000\u0000\u0000\u00a1\u01d1"+
		"\u0001\u0000\u0000\u0000\u00a3\u01d4\u0001\u0000\u0000\u0000\u00a5\u01d6"+
		"\u0001\u0000\u0000\u0000\u00a7\u01d8\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0003O\'\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac\u0006"+
		"\u0000\u0000\u0000\u00ac\u0002\u0001\u0000\u0000\u0000\u00ad\u00ae\u0003"+
		"M&\u0000\u00ae\u00af\u0001\u0000\u0000\u0000\u00af\u00b0\u0006\u0001\u0000"+
		"\u0000\u00b0\u0004\u0001\u0000\u0000\u0000\u00b1\u00b2\u0003Q(\u0000\u00b2"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b4\u0006\u0002\u0000\u0000\u00b4"+
		"\u0006\u0001\u0000\u0000\u0000\u00b5\u00b6\u0003Y,\u0000\u00b6\b\u0001"+
		"\u0000\u0000\u0000\u00b7\u00b8\u0005r\u0000\u0000\u00b8\u00b9\u0003c1"+
		"\u0000\u00b9\n\u0001\u0000\u0000\u0000\u00ba\u00bb\u0003c1\u0000\u00bb"+
		"\f\u0001\u0000\u0000\u0000\u00bc\u00bd\u0003g3\u0000\u00bd\u000e\u0001"+
		"\u0000\u0000\u0000\u00be\u00bf\u0005f\u0000\u0000\u00bf\u00c0\u0005r\u0000"+
		"\u0000\u00c0\u00c1\u0005a\u0000\u0000\u00c1\u00c2\u0005g\u0000\u0000\u00c2"+
		"\u00c3\u0005m\u0000\u0000\u00c3\u00c4\u0005e\u0000\u0000\u00c4\u00c5\u0005"+
		"n\u0000\u0000\u00c5\u00c6\u0005t\u0000\u0000\u00c6\u0010\u0001\u0000\u0000"+
		"\u0000\u00c7\u00c8\u0005s\u0000\u0000\u00c8\u00c9\u0005p\u0000\u0000\u00c9"+
		"\u00ca\u0005e\u0000\u0000\u00ca\u00cb\u0005c\u0000\u0000\u00cb\u00cc\u0005"+
		"i\u0000\u0000\u00cc\u00cd\u0005a\u0000\u0000\u00cd\u00ce\u0005l\u0000"+
		"\u0000\u00ce\u0012\u0001\u0000\u0000\u0000\u00cf\u00d0\u0003q8\u0000\u00d0"+
		"\u0014\u0001\u0000\u0000\u0000\u00d1\u00d2\u0003s9\u0000\u00d2\u0016\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d4\u0003\u009bM\u0000\u00d4\u0018\u0001\u0000"+
		"\u0000\u0000\u00d5\u00d6\u0003\u009dN\u0000\u00d6\u001a\u0001\u0000\u0000"+
		"\u0000\u00d7\u00d8\u0003y<\u0000\u00d8\u001c\u0001\u0000\u0000\u0000\u00d9"+
		"\u00da\u0003{=\u0000\u00da\u001e\u0001\u0000\u0000\u0000\u00db\u00dc\u0003"+
		"}>\u0000\u00dc \u0001\u0000\u0000\u0000\u00dd\u00de\u0003\u007f?\u0000"+
		"\u00de\"\u0001\u0000\u0000\u0000\u00df\u00e0\u0003\u0085B\u0000\u00e0"+
		"$\u0001\u0000\u0000\u0000\u00e1\u00e2\u0003\u0087C\u0000\u00e2&\u0001"+
		"\u0000\u0000\u0000\u00e3\u00e4\u0003\u0089D\u0000\u00e4(\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e6\u0003\u008bE\u0000\u00e6*\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e8\u0003\u008dF\u0000\u00e8,\u0001\u0000\u0000\u0000\u00e9\u00ea\u0003"+
		"\u008fG\u0000\u00ea.\u0001\u0000\u0000\u0000\u00eb\u00ec\u0003\u0093I"+
		"\u0000\u00ec0\u0001\u0000\u0000\u0000\u00ed\u00ee\u0003\u0091H\u0000\u00ee"+
		"2\u0001\u0000\u0000\u0000\u00ef\u00f0\u0003\u0097K\u0000\u00f04\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0003\u0099L\u0000\u00f26\u0001\u0000\u0000"+
		"\u0000\u00f3\u00f4\u0003\u00a1P\u0000\u00f48\u0001\u0000\u0000\u0000\u00f5"+
		"\u00f6\u0003\u009fO\u0000\u00f6:\u0001\u0000\u0000\u0000\u00f7\u00f8\u0003"+
		"\u00a3Q\u0000\u00f8<\u0001\u0000\u0000\u0000\u00f9\u00fa\u0003\u00a5R"+
		"\u0000\u00fa>\u0001\u0000\u0000\u0000\u00fb\u00fc\u0003\u00a7S\u0000\u00fc"+
		"@\u0001\u0000\u0000\u0000\u00fd\u0101\u0003k5\u0000\u00fe\u0100\u0003"+
		"i4\u0000\u00ff\u00fe\u0001\u0000\u0000\u0000\u0100\u0103\u0001\u0000\u0000"+
		"\u0000\u0101\u00ff\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000"+
		"\u0000\u0102B\u0001\u0000\u0000\u0000\u0103\u0101\u0001\u0000\u0000\u0000"+
		"\u0104\u0106\u0007\u0000\u0000\u0000\u0105\u0104\u0001\u0000\u0000\u0000"+
		"\u0106\u0107\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000"+
		"\u0107\u0108\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000"+
		"\u0109\u010a\u0006!\u0001\u0000\u010aD\u0001\u0000\u0000\u0000\u010b\u010c"+
		"\t\u0000\u0000\u0000\u010c\u010d\u0001\u0000\u0000\u0000\u010d\u010e\u0006"+
		"\"\u0002\u0000\u010eF\u0001\u0000\u0000\u0000\u010f\u0112\u0003I$\u0000"+
		"\u0110\u0112\u0003K%\u0000\u0111\u010f\u0001\u0000\u0000\u0000\u0111\u0110"+
		"\u0001\u0000\u0000\u0000\u0112H\u0001\u0000\u0000\u0000\u0113\u0114\u0007"+
		"\u0001\u0000\u0000\u0114J\u0001\u0000\u0000\u0000\u0115\u0116\u0007\u0002"+
		"\u0000\u0000\u0116L\u0001\u0000\u0000\u0000\u0117\u0118\u0005/\u0000\u0000"+
		"\u0118\u0119\u0005*\u0000\u0000\u0119\u011d\u0001\u0000\u0000\u0000\u011a"+
		"\u011c\t\u0000\u0000\u0000\u011b\u011a\u0001\u0000\u0000\u0000\u011c\u011f"+
		"\u0001\u0000\u0000\u0000\u011d\u011e\u0001\u0000\u0000\u0000\u011d\u011b"+
		"\u0001\u0000\u0000\u0000\u011e\u0123\u0001\u0000\u0000\u0000\u011f\u011d"+
		"\u0001\u0000\u0000\u0000\u0120\u0121\u0005*\u0000\u0000\u0121\u0124\u0005"+
		"/\u0000\u0000\u0122\u0124\u0005\u0000\u0000\u0001\u0123\u0120\u0001\u0000"+
		"\u0000\u0000\u0123\u0122\u0001\u0000\u0000\u0000\u0124N\u0001\u0000\u0000"+
		"\u0000\u0125\u0126\u0005/\u0000\u0000\u0126\u0127\u0005*\u0000\u0000\u0127"+
		"\u0128\u0005*\u0000\u0000\u0128\u012c\u0001\u0000\u0000\u0000\u0129\u012b"+
		"\t\u0000\u0000\u0000\u012a\u0129\u0001\u0000\u0000\u0000\u012b\u012e\u0001"+
		"\u0000\u0000\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012c\u012a\u0001"+
		"\u0000\u0000\u0000\u012d\u0132\u0001\u0000\u0000\u0000\u012e\u012c\u0001"+
		"\u0000\u0000\u0000\u012f\u0130\u0005*\u0000\u0000\u0130\u0133\u0005/\u0000"+
		"\u0000\u0131\u0133\u0005\u0000\u0000\u0001\u0132\u012f\u0001\u0000\u0000"+
		"\u0000\u0132\u0131\u0001\u0000\u0000\u0000\u0133P\u0001\u0000\u0000\u0000"+
		"\u0134\u0135\u0005/\u0000\u0000\u0135\u0136\u0005/\u0000\u0000\u0136\u013a"+
		"\u0001\u0000\u0000\u0000\u0137\u0139\b\u0003\u0000\u0000\u0138\u0137\u0001"+
		"\u0000\u0000\u0000\u0139\u013c\u0001\u0000\u0000\u0000\u013a\u0138\u0001"+
		"\u0000\u0000\u0000\u013a\u013b\u0001\u0000\u0000\u0000\u013bR\u0001\u0000"+
		"\u0000\u0000\u013c\u013a\u0001\u0000\u0000\u0000\u013d\u0142\u0003o7\u0000"+
		"\u013e\u0143\u0007\u0004\u0000\u0000\u013f\u0143\u0003W+\u0000\u0140\u0143"+
		"\t\u0000\u0000\u0000\u0141\u0143\u0005\u0000\u0000\u0001\u0142\u013e\u0001"+
		"\u0000\u0000\u0000\u0142\u013f\u0001\u0000\u0000\u0000\u0142\u0140\u0001"+
		"\u0000\u0000\u0000\u0142\u0141\u0001\u0000\u0000\u0000\u0143T\u0001\u0000"+
		"\u0000\u0000\u0144\u0145\u0003o7\u0000\u0145\u0146\t\u0000\u0000\u0000"+
		"\u0146V\u0001\u0000\u0000\u0000\u0147\u0152\u0005u\u0000\u0000\u0148\u0150"+
		"\u0003[-\u0000\u0149\u014e\u0003[-\u0000\u014a\u014c\u0003[-\u0000\u014b"+
		"\u014d\u0003[-\u0000\u014c\u014b\u0001\u0000\u0000\u0000\u014c\u014d\u0001"+
		"\u0000\u0000\u0000\u014d\u014f\u0001\u0000\u0000\u0000\u014e\u014a\u0001"+
		"\u0000\u0000\u0000\u014e\u014f\u0001\u0000\u0000\u0000\u014f\u0151\u0001"+
		"\u0000\u0000\u0000\u0150\u0149\u0001\u0000\u0000\u0000\u0150\u0151\u0001"+
		"\u0000\u0000\u0000\u0151\u0153\u0001\u0000\u0000\u0000\u0152\u0148\u0001"+
		"\u0000\u0000\u0000\u0152\u0153\u0001\u0000\u0000\u0000\u0153X\u0001\u0000"+
		"\u0000\u0000\u0154\u015d\u00050\u0000\u0000\u0155\u0159\u0007\u0005\u0000"+
		"\u0000\u0156\u0158\u0003].\u0000\u0157\u0156\u0001\u0000\u0000\u0000\u0158"+
		"\u015b\u0001\u0000\u0000\u0000\u0159\u0157\u0001\u0000\u0000\u0000\u0159"+
		"\u015a\u0001\u0000\u0000\u0000\u015a\u015d\u0001\u0000\u0000\u0000\u015b"+
		"\u0159\u0001\u0000\u0000\u0000\u015c\u0154\u0001\u0000\u0000\u0000\u015c"+
		"\u0155\u0001\u0000\u0000\u0000\u015dZ\u0001\u0000\u0000\u0000\u015e\u015f"+
		"\u0007\u0006\u0000\u0000\u015f\\\u0001\u0000\u0000\u0000\u0160\u0161\u0007"+
		"\u0007\u0000\u0000\u0161^\u0001\u0000\u0000\u0000\u0162\u0163\u0005t\u0000"+
		"\u0000\u0163\u0164\u0005r\u0000\u0000\u0164\u0165\u0005u\u0000\u0000\u0165"+
		"\u016c\u0005e\u0000\u0000\u0166\u0167\u0005f\u0000\u0000\u0167\u0168\u0005"+
		"a\u0000\u0000\u0168\u0169\u0005l\u0000\u0000\u0169\u016a\u0005s\u0000"+
		"\u0000\u016a\u016c\u0005e\u0000\u0000\u016b\u0162\u0001\u0000\u0000\u0000"+
		"\u016b\u0166\u0001\u0000\u0000\u0000\u016c`\u0001\u0000\u0000\u0000\u016d"+
		"\u0170\u0003u:\u0000\u016e\u0171\u0003S)\u0000\u016f\u0171\b\b\u0000\u0000"+
		"\u0170\u016e\u0001\u0000\u0000\u0000\u0170\u016f\u0001\u0000\u0000\u0000"+
		"\u0171\u0172\u0001\u0000\u0000\u0000\u0172\u0173\u0003u:\u0000\u0173b"+
		"\u0001\u0000\u0000\u0000\u0174\u0179\u0003u:\u0000\u0175\u0178\u0003S"+
		")\u0000\u0176\u0178\b\b\u0000\u0000\u0177\u0175\u0001\u0000\u0000\u0000"+
		"\u0177\u0176\u0001\u0000\u0000\u0000\u0178\u017b\u0001\u0000\u0000\u0000"+
		"\u0179\u0177\u0001\u0000\u0000\u0000\u0179\u017a\u0001\u0000\u0000\u0000"+
		"\u017a\u017c\u0001\u0000\u0000\u0000\u017b\u0179\u0001\u0000\u0000\u0000"+
		"\u017c\u017d\u0003u:\u0000\u017dd\u0001\u0000\u0000\u0000\u017e\u0183"+
		"\u0003w;\u0000\u017f\u0182\u0003S)\u0000\u0180\u0182\b\t\u0000\u0000\u0181"+
		"\u017f\u0001\u0000\u0000\u0000\u0181\u0180\u0001\u0000\u0000\u0000\u0182"+
		"\u0185\u0001\u0000\u0000\u0000\u0183\u0181\u0001\u0000\u0000\u0000\u0183"+
		"\u0184\u0001\u0000\u0000\u0000\u0184\u0186\u0001\u0000\u0000\u0000\u0185"+
		"\u0183\u0001\u0000\u0000\u0000\u0186\u0187\u0003w;\u0000\u0187f\u0001"+
		"\u0000\u0000\u0000\u0188\u018d\u0003u:\u0000\u0189\u018c\u0003S)\u0000"+
		"\u018a\u018c\b\b\u0000\u0000\u018b\u0189\u0001\u0000\u0000\u0000\u018b"+
		"\u018a\u0001\u0000\u0000\u0000\u018c\u018f\u0001\u0000\u0000\u0000\u018d"+
		"\u018b\u0001\u0000\u0000\u0000\u018d\u018e\u0001\u0000\u0000\u0000\u018e"+
		"h\u0001\u0000\u0000\u0000\u018f\u018d\u0001\u0000\u0000\u0000\u0190\u0195"+
		"\u0003k5\u0000\u0191\u0195\u000209\u0000\u0192\u0195\u0003\u0095J\u0000"+
		"\u0193\u0195\u0007\n\u0000\u0000\u0194\u0190\u0001\u0000\u0000\u0000\u0194"+
		"\u0191\u0001\u0000\u0000\u0000\u0194\u0192\u0001\u0000\u0000\u0000\u0194"+
		"\u0193\u0001\u0000\u0000\u0000\u0195j\u0001\u0000\u0000\u0000\u0196\u0197"+
		"\u0007\u000b\u0000\u0000\u0197l\u0001\u0000\u0000\u0000\u0198\u0199\u0005"+
		"i\u0000\u0000\u0199\u019a\u0005n\u0000\u0000\u019a\u019b\u0005t\u0000"+
		"\u0000\u019bn\u0001\u0000\u0000\u0000\u019c\u019d\u0005\\\u0000\u0000"+
		"\u019dp\u0001\u0000\u0000\u0000\u019e\u019f\u0005:\u0000\u0000\u019fr"+
		"\u0001\u0000\u0000\u0000\u01a0\u01a1\u0005:\u0000\u0000\u01a1\u01a2\u0005"+
		":\u0000\u0000\u01a2t\u0001\u0000\u0000\u0000\u01a3\u01a4\u0005\'\u0000"+
		"\u0000\u01a4v\u0001\u0000\u0000\u0000\u01a5\u01a6\u0005\"\u0000\u0000"+
		"\u01a6x\u0001\u0000\u0000\u0000\u01a7\u01a8\u0005(\u0000\u0000\u01a8z"+
		"\u0001\u0000\u0000\u0000\u01a9\u01aa\u0005)\u0000\u0000\u01aa|\u0001\u0000"+
		"\u0000\u0000\u01ab\u01ac\u0005{\u0000\u0000\u01ac~\u0001\u0000\u0000\u0000"+
		"\u01ad\u01ae\u0005}\u0000\u0000\u01ae\u0080\u0001\u0000\u0000\u0000\u01af"+
		"\u01b0\u0005[\u0000\u0000\u01b0\u0082\u0001\u0000\u0000\u0000\u01b1\u01b2"+
		"\u0005]\u0000\u0000\u01b2\u0084\u0001\u0000\u0000\u0000\u01b3\u01b4\u0005"+
		"-\u0000\u0000\u01b4\u01b5\u0005>\u0000\u0000\u01b5\u0086\u0001\u0000\u0000"+
		"\u0000\u01b6\u01b7\u0005<\u0000\u0000\u01b7\u0088\u0001\u0000\u0000\u0000"+
		"\u01b8\u01b9\u0005>\u0000\u0000\u01b9\u008a\u0001\u0000\u0000\u0000\u01ba"+
		"\u01bb\u0005=\u0000\u0000\u01bb\u008c\u0001\u0000\u0000\u0000\u01bc\u01bd"+
		"\u0005?\u0000\u0000\u01bd\u008e\u0001\u0000\u0000\u0000\u01be\u01bf\u0005"+
		"*\u0000\u0000\u01bf\u0090\u0001\u0000\u0000\u0000\u01c0\u01c1\u0005+\u0000"+
		"\u0000\u01c1\u0092\u0001\u0000\u0000\u0000\u01c2\u01c3\u0005+\u0000\u0000"+
		"\u01c3\u01c4\u0005=\u0000\u0000\u01c4\u0094\u0001\u0000\u0000\u0000\u01c5"+
		"\u01c6\u0005_\u0000\u0000\u01c6\u0096\u0001\u0000\u0000\u0000\u01c7\u01c8"+
		"\u0005|\u0000\u0000\u01c8\u0098\u0001\u0000\u0000\u0000\u01c9\u01ca\u0005"+
		"$\u0000\u0000\u01ca\u009a\u0001\u0000\u0000\u0000\u01cb\u01cc\u0005,\u0000"+
		"\u0000\u01cc\u009c\u0001\u0000\u0000\u0000\u01cd\u01ce\u0005;\u0000\u0000"+
		"\u01ce\u009e\u0001\u0000\u0000\u0000\u01cf\u01d0\u0005.\u0000\u0000\u01d0"+
		"\u00a0\u0001\u0000\u0000\u0000\u01d1\u01d2\u0005.\u0000\u0000\u01d2\u01d3"+
		"\u0005.\u0000\u0000\u01d3\u00a2\u0001\u0000\u0000\u0000\u01d4\u01d5\u0005"+
		"@\u0000\u0000\u01d5\u00a4\u0001\u0000\u0000\u0000\u01d6\u01d7\u0005#\u0000"+
		"\u0000\u01d7\u00a6\u0001\u0000\u0000\u0000\u01d8\u01d9\u0005~\u0000\u0000"+
		"\u01d9\u00a8\u0001\u0000\u0000\u0000\u0019\u0000\u0101\u0107\u0111\u011d"+
		"\u0123\u012c\u0132\u013a\u0142\u014c\u014e\u0150\u0152\u0159\u015c\u016b"+
		"\u0170\u0177\u0179\u0181\u0183\u018b\u018d\u0194\u0003\u0000\u0002\u0000"+
		"\u0006\u0000\u0000\u0000\u0001\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}