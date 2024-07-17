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
fragmentRule: FRAGMENT ID COLON lexerRuleBlock SEMI;

ruleBlock
    : STRING_LITERAL ruleAltList
    ;

ruleAltList
    : alternative (OR alternative)*
    ;

lexerRuleBlock
    : lexerAltList
    ;

lexerAltList
    : lexerAlt (OR lexerAlt)*
    ;

lexerAlt
    : lexerElement+
    |
    // explicitly allow empty alts
    ;

lexerElement
    : lexerAtom ebnfSuffix?
    | lexerBlock ebnfSuffix?
    ;

lexerBlock
    : LPAREN lexerAltList RPAREN
    ;

// --------------------
// Rule Alts

altList
    : alternative (OR alternative)*
    ;

alternative
    : element+
    |
    // explicitly allow empty alts
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

lexerAtom
    : setElement
    | terminalDef
    | notSet
    ;

atom
    : setElement
    | terminalDef
    | ruleref
    | notSet
    ;

// --------------------
// Inverted element set
notSet
    : NOT setElement
    | NOT blockSet
    ;

blockSet
    : LPAREN setElement (OR setElement)* RPAREN
    ;

setElement
    : ID
    | STRING_LITERAL
    | characterRange
    ;

// ----------------
// Parser rule ref
ruleref
    : ID
    ;

// -------------
// Grammar Block
block
    : LPAREN altList RPAREN
    ;

// ---------------
// Character Range
characterRange
    : STRING_LITERAL RANGE STRING_LITERAL
    ;

terminalDef
    : ID
    | STRING_LITERAL
    ;
