from typing import List, Dict

from .parser import TokenMatcher

class LiteralTokenMatcher(TokenMatcher):
    def __init__(self, token_ids: Dict[int, None], is_optional: bool, matches_multiple: bool):
        self._token_ids = token_ids
        self._is_optional = is_optional
        self._matches_multiple = matches_multiple
    def is_optional(self) -> bool:
        return self._is_optional

    def matches_multiple(self) -> bool:
        return self._matches_multiple

    def test_token(self, token_id: int) -> bool:
        return token_id in self._token_ids
