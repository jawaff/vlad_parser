from typing import List, Dict
from tokenizers import Tokenizer # type: ignore

class TokenTranslator:
    def __init__(self, tokenizer_json_path: str, custom_tokens: List[str]):
        self._tokenizer = Tokenizer.from_file(tokenizer_json_path)

        # Adds the new vocab
        self._custom_tokens = custom_tokens
        new_tokens = set(custom_tokens) - set(self._tokenizer.get_vocab(False).keys())
        self._tokenizer.add_tokens(list(new_tokens))

        # The target model must be resized after adding to the vocab!
        # model.resize_token_embeddings(len(self._tokenizer))

    def __len__(self) -> int:
        return len(self._tokenizer)

    def get_vocab(self) -> Dict[str, int]:
        return self._tokenizer.get_vocab(False) # type: ignore

    def decode(self, token_list: List[int]) -> str:
        return self._tokenizer.decode(token_list)

    def translate(self, text: str) -> List[int]:
        return self._tokenizer.encode(text).ids # type: ignore

    def translate_list(self, text_list: List[str]) -> List[List[int]]:
        return list(map(self.translate, text_list))