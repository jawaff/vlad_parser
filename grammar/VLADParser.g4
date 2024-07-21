parser grammar VLADParser;

options {
    tokenVocab = VLADLexer;
}

// --------------------
// Root of the parse tree
rules: rule+;
rule: tokenRule | specialRule | fragmentRule;

// --------------------
// Main Rule Defs

tokenRule: ID COLON ruleBlock SEMI;
specialRule: SPECIAL ID COLON ruleBlock SEMI;
fragmentRule: FRAGMENT ID COLON fragmentRuleBlock SEMI;

ruleBlock
    : STRING_LITERAL altList
    ;

fragmentRuleBlock
    : altList
    ;

altList
    : alternative (OR alternative)*
    ;

alternative
    : element+
    ;

element
    : atom (ebnfSuffix |)
    | block ebnfSuffix?
    ;

// --------------------
// EBNF
ebnfSuffix
    : QUESTION
    | STAR
    | PLUS
    ;

// -------------
// Grammar Block
block
    : LPAREN altList RPAREN
    ;

atom
    : terminalDef
    ;

terminalDef
    : ID
    | STRING_LITERAL
    | characterRange
    | REGEX_LITERAL
    ;

// ---------------
// Character Range
characterRange
    : STRING_LITERAL RANGE STRING_LITERAL
    ;

