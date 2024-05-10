parser grammar VLADParser;

options {
    tokenVocab = VLADLexer;
}

// --------------------
// Main Rule Defs

tokenRule: RULE_REF COLON ruleBlock SEMI;
specialRule: SPECIAL RULE_REF COLON ruleBlock SEMI;
fragmentRule: FRAGMENT FRAGMENT_REF COLON lexerRuleBlock SEMI;

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
    : characterRange
    | terminalDef
    | notSet
    ;

atom
    : terminalDef
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
    : FRAGMENT_REF
    | STRING_LITERAL
    | characterRange
    ;

// ----------------
// Parser rule ref
ruleref
    : RULE_REF
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
    : FRAGMENT_REF
    | STRING_LITERAL
    ;
