rm -rf ./grammar/*.interp
rm -rf ./grammar/*.py
rm -rf ./grammar/*.tokens

antlr4 -Dlanguage=Python3 ./grammar/vladlexer.g4
antlr4 -Dlanguage=Python3 ./grammar/vladparser.g4

mv ./grammar/*.py ./src/vlad/parser/grammar/
rm -rf ./grammar/*.interp
rm -rf ./grammar/*.tokens
rm -rf ./grammar/.antlr/