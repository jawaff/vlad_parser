lexer grammar VLADLexer;

options {
    superClass = LexerAdaptor;
}

import VLADLexBasic;

// Standard set of fragments
tokens {
    FRAGMENT_REF,
    RULE_REF
}

channels {
    COMMENT
}

// -------------------------
// Comments
DOC_COMMENT
    : DocComment -> channel (COMMENT)
    ;

BLOCK_COMMENT
    : BlockComment -> channel (COMMENT)
    ;

LINE_COMMENT
    : LineComment -> channel (COMMENT)
    ;

// -------------------------
// Integer

INT
    : DecimalNumeral
    ;

// -------------------------
// Literal string
//
// ANTLR makes no distinction between a single character literal and a
// multi-character string. All literals are single quote delimited and
// may contain unicode escape sequences of the form \uxxxx, where x
// is a valid hexadecimal number (per Unicode standard).
REGEX_LITERAL
    : 'r' SQuoteLiteral
    ;

STRING_LITERAL
    : SQuoteLiteral
    ;

UNTERMINATED_STRING_LITERAL
    : USQuoteLiteral
    ;

// -------------------------
// Keywords

FRAGMENT
    : 'fragment'
    ;

SPECIAL
    : 'special'
    ;

// -------------------------
// Punctuation

COLON
    : Colon
    ;

COLONCOLON
    : DColon
    ;

COMMA
    : Comma
    ;

SEMI
    : Semi
    ;

LPAREN
    : LParen
    ;

RPAREN
    : RParen
    ;

LBRACE
    : LBrace
    ;

RBRACE
    : RBrace
    ;

RARROW
    : RArrow
    ;

LT
    : Lt
    ;

GT
    : Gt
    ;

ASSIGN
    : Equal
    ;

QUESTION
    : Question
    ;

STAR
    : Star
    ;

PLUS_ASSIGN
    : PlusAssign
    ;

PLUS
    : Plus
    ;

OR
    : Pipe
    ;

DOLLAR
    : Dollar
    ;

RANGE
    : Range
    ;

DOT
    : Dot
    ;

AT
    : At
    ;

POUND
    : Pound
    ;

NOT
    : Tilde
    ;

// -------------------------
// Identifiers - allows unicode rule/token names

ID
    : NameStartChar NameChar*
    ;

// -------------------------
// Whitespace
WS : [ \t\r\n\u000C]+ -> skip;

// -------------------------
// Illegal Characters
//
// This is an illegal character trap which is always the last rule in the
// lexer specification. It matches a single character of any value and being
// the last rule in the file will match when no other rule knows what to do
// about the character. It is reported as an error but is not passed on to the
// parser. This means that the parser to deal with the gramamr file anyway
// but we will not try to analyse or code generate from a file with lexical
// errors.

// Comment this rule out to allow the error to be propagated to the parser
ERRCHAR : . -> channel (HIDDEN);
