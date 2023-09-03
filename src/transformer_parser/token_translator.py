from typing import List, Dict
from tokenizers import Tokenizer

class TokenTranslator:
    def __init__(self, tokenizer_json_path: str):
        self._tokenizer = Tokenizer.from_file(tokenizer_json_path)

    def get_vocab(self) -> Dict[str, int]:
        return self._tokenizer.get_vocab(False)

    def translate(self, text: str) -> List[int]:
        return self._tokenizer.encode(text).ids

    def translate(self, text_list: List[str]) -> List[List[int]]:
        return list(map(self.translate, text_list))