from typing import List
import re
from transformer_parser.parser import Grammar
from transformer_parser.token_matchers import LiteralTokenMatcher
from transformer_parser.token_translator import TokenTranslator

INTEGER_PATTERN = r"\d+"
NUMBER_PATTERN = r"\d+\.?\d*"
WORD_PATTERN = r"\w+"
OPERATOR_PATTERN = r""





def create_grammar(translator: TokenTranslator, special_token_ids: List[int]):
    int_regex = re.compile(INTEGER_PATTERN)
    int_token_ids = []
    number_regex = re.compile(NUMBER_PATTERN)
    number_token_ids = []
    word_regex = re.compile(WORD_PATTERN)
    word_token_ids = []
    
    for token, id in translator.get_vocab().items():
        if int_regex.match(token):
            int_token_ids.append(id)
        if number_regex.match(token):
            number_token_ids.append(id)
        if word_regex.match(token):
            word_token_ids.append(id)

    # TODO Use the token id lists above to construct token matchers.
    #rm1 = LiteralTokenMatcher(token_ids={1: None}, is_optional=False, matches_multiple=False)
    #root_matchers = [rm1]
    #m1 = LiteralTokenMatcher(token_ids={2: None}, is_optional=False, matches_multiple=False)
    #m2 = LiteralTokenMatcher(token_ids={3: None}, is_optional=False, matches_multiple=False)
    #m3 = LiteralTokenMatcher(token_ids={4: None}, is_optional=False, matches_multiple=False)
    #m4 = LiteralTokenMatcher(token_ids={5: None}, is_optional=False, matches_multiple=False)
    #m5 = LiteralTokenMatcher(token_ids={6: None}, is_optional=False, matches_multiple=False)
    #m6 = LiteralTokenMatcher(token_ids={7: None}, is_optional=False, matches_multiple=False)
    #grammar = Grammar(root_rule=root_matchers, rules={1: [m1, m4], 2: [m2, m3], 5: [m5, m6]})