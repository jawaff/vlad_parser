from typing import List
from .parser import Grammar, TokenMatcher

# TODO This needs a lot of work too convert from the rule text to the token matchers.

def is_root_rule(rule_line: str) -> bool:
    return rule_line.startswith('ROOT = ')

def is_other_rule(rule_line: str) -> bool:
    return not is_root_rule(rule_line)

def build_matchers(rule: str) -> List[TokenMatcher]:
    return []

def load_grammar(filename: str) -> Grammar:
    with open(filename) as file:
        # Collects the nonempty rule lines
        rule_lines = [line.strip() for line in file if not line.strip()]

    root_rule_line = next(filter(is_root_rule, rule_lines), None)
    assert root_rule_line is not None
    root_rule = build_matchers(root_rule_line)

    other_rule_lines = filter(is_other_rule, rule_lines)
    # TODO Figure out what the maximum number of special token ids we can use and subtract the offset for the first token.
    # TODO Figure out what the offset for the first special token should be.
    assert len(other_rule_lines) < 99

    # There needs to be a certain offset that we use for the first rule's token id.
    other_rules = {i+2: build_matchers(other_rule_lines[i]) for i in range(0, len(other_rule_lines))}

    return Grammar(root_rule, other_rules)

    