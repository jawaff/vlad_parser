# TODO (Started in Lansing, Michigan)

1. Our grammar needs to match the Spider SQL dataset (e.g. Keywords are in all caps, functions are lowercase, table aliases are T1-T?). All of our custom
tokens and grammar rules should follow the dataset expectations.

2. We can easily make our grammar unambiguous by making rule branch ids unique (i.e. making them new tokens). The problem is that some of the SQL keywords might already be taken up by existing tokens and we thus need to share some of them with string literals, thereby making them not unique. We do support contextual ambiguity with rule ids, because we only check if an id is for a rule if it doesn't match the current rules on the stack. We should however ensure no ambiguity by checking the parse table when the grammar is loaded (https://cs.stackexchange.com/a/111778). The parse table check should exist within the grammar factory!!! The parser itself doesn't know what the matchers actually are looking for because they're kind of abstract. The grammar factory being the place that will create the matchers will have a better idea of what the parse table
actually looks like.

3. We need to finish the parser. The "get_next_possible_tokens()" function is just not implemented at all. Do we really need this though? It might be too inefficient
since it could possibly return a list of 31k tokens. As an alternative we can just find the top 10 or 20 tokens that are valid in the transformer and mark all other tokens with a 0% probability.

4. Grammar factory needs to be finished so that we can make grammar files easier. There's going to be several types of grammar files for the projcet and they need to be readable so that other people can reuse this parser for their own purposes.