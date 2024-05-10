from typing import List
import re
from vlad_parser import Grammar
from vlad_parser.matchers import LiteralTokenMatcher
from vlad_parser.translator import TokenTranslator

INTEGER_PATTERN = r"\d+"
NUMBER_PATTERN = r"\d+\.?\d*"
WORD_PATTERN = r"\w+"
OPERATOR_PATTERN = r"" # TODO
NAME_PATTERN = r"[a-zA-Z0-9\-_]+"
SPACE_PATTERN = r" "
PERIOD_PATTERN = r"\."
COMMA_PATTERN = r"\."
CONDITION_DELIMITER_PATTERN = r"(and|AND|or|OR)"

def create_grammar(translator: TokenTranslator, special_token_ids: List[int]) -> Grammar:
    int_regex = re.compile(INTEGER_PATTERN)
    int_token_ids = {}
    number_regex = re.compile(NUMBER_PATTERN)
    number_token_ids = {}
    word_regex = re.compile(WORD_PATTERN)
    word_token_ids = {}
    operator_regex = re.compile(OPERATOR_PATTERN)
    operator_token_ids = {}
    name_regex = re.compile(NAME_PATTERN)
    name_token_ids = {}
    space_regex = re.compile(SPACE_PATTERN)
    space_token_ids = {}
    period_regex = re.compile(PERIOD_PATTERN)
    period_token_ids = {}
    comma_regex = re.compile(COMMA_PATTERN)
    comma_token_ids = {}
    condition_delimiter_regex = re.compile(CONDITION_DELIMITER_PATTERN)
    condition_delimiter_token_ids = {}
    
    for token, id in translator.get_vocab().items():
        if int_regex.match(token):
            int_token_ids[id] = None
        if number_regex.match(token):
            number_token_ids[id] = None
        if word_regex.match(token):
            word_token_ids[id] = None
        if operator_regex.match(token):
            operator_token_ids[id] = None
        if name_regex.match(token):
            name_token_ids[id] = None
        if space_regex.match(token):
            space_token_ids[id] = None
        if period_regex.match(token):
            period_token_ids[id] = None
        if comma_regex.match(token):
            comma_token_ids[id] = None
        if condition_delimiter_regex.match(token):
            condition_delimiter_token_ids[id] = None

    select_token_id = special_token_ids.pop(0)
    star_token_id = special_token_ids.pop(0)
    outputs_token_id = special_token_ids.pop(0)
    column_token_id = special_token_ids.pop(0)
    next_column_token_id = special_token_ids.pop(0)
    table_alias_token_id = special_token_ids.pop(0)
    alias_token_id = special_token_ids.pop(0)

    from_token_id = special_token_ids.pop(0)
    table_token_id = special_token_ids.pop(0)
    next_table_token_id = special_token_ids.pop(0)
    where_token_id = special_token_ids.pop(0)
    condition_token_id = special_token_ids.pop(0)
    next_condition_token_id = special_token_ids.pop(0)

    select_matcher = LiteralTokenMatcher(token_ids={select_token_id: None}, is_optional=False, matches_multiple=False)
    root_matchers = [select_matcher]

    # Leaf Matchers:
    name_matcher = LiteralTokenMatcher(token_ids=name_token_ids, is_optional=False, matches_multiple=True)
    period_matcher = LiteralTokenMatcher(token_ids=period_token_ids, is_optional=False, matches_multiple=False)
    comma_matcher = LiteralTokenMatcher(token_ids=comma_token_ids, is_optional=False, matches_multiple=False)

    star_or_outputs_matcher = LiteralTokenMatcher(token_ids={star_token_id: None, outputs_token_id: None}, is_optional=False, matches_multiple=False)
    column_matcher = LiteralTokenMatcher(token_ids={column_token_id: None}, is_optional=False, matches_multiple=False)
    next_column_matcher = LiteralTokenMatcher(token_ids={next_column_token_id: None}, is_optional=False, matches_multiple=True)
    table_alias_opt_matcher = LiteralTokenMatcher(token_ids={table_alias_token_id: None}, is_optional=True, matches_multiple=False)
    alias_opt_matcher = LiteralTokenMatcher(token_ids={alias_token_id: None}, is_optional=True, matches_multiple=False)

    from_matcher = LiteralTokenMatcher(token_ids={from_token_id: None}, is_optional=False, matches_multiple=False)
    table_matcher = LiteralTokenMatcher(token_ids={table_token_id: None}, is_optional=False, matches_multiple=False)
    next_table_matcher = LiteralTokenMatcher(token_ids={next_table_token_id: None}, is_optional=False, matches_multiple=True)
    where_matcher = LiteralTokenMatcher(token_ids={where_token_id: None}, is_optional=False, matches_multiple=False)
    condition_matcher = LiteralTokenMatcher(token_ids={condition_token_id: None}, is_optional=False, matches_multiple=False)
    next_condition_matcher = LiteralTokenMatcher(token_ids={next_condition_token_id: None}, is_optional=False, matches_multiple=True)
    condition_delimiter_matcher = LiteralTokenMatcher(token_ids=condition_delimiter_token_ids, is_optional=False, matches_multiple=False)

    rules = {
        select_token_id: [star_or_outputs_matcher, from_matcher, where_matcher],
        outputs_token_id: [column_matcher, next_column_matcher],
        column_token_id: [table_alias_opt_matcher, name_matcher, alias_opt_matcher],
        table_alias_token_id: [name_matcher, period_matcher],
        next_column_token_id: [comma_matcher, column_matcher],
        alias_token_id: [name_matcher],
        from_token_id: [table_matcher, next_table_matcher],
        table_token_id: [name_matcher, alias_opt_matcher],
        next_table_token_id: [comma_matcher, table_matcher],
        where_token_id: [condition_matcher, next_condition_matcher],
        condition_token_id: [],
        next_condition_token_id: [condition_delimiter_matcher, condition_matcher]
    }
    #m1 = LiteralTokenMatcher(token_ids={2: None}, is_optional=False, matches_multiple=False)
    #m2 = LiteralTokenMatcher(token_ids={3: None}, is_optional=False, matches_multiple=False)
    #m3 = LiteralTokenMatcher(token_ids={4: None}, is_optional=False, matches_multiple=False)
    #m4 = LiteralTokenMatcher(token_ids={5: None}, is_optional=False, matches_multiple=False)
    #m5 = LiteralTokenMatcher(token_ids={6: None}, is_optional=False, matches_multiple=False)
    #m6 = LiteralTokenMatcher(token_ids={7: None}, is_optional=False, matches_multiple=False)
    #rules = {1: [m1, m4], 2: [m2, m3], 5: [m5, m6]}
    return Grammar(root_rule=root_matchers, rules=rules)