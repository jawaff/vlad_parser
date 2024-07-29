rm -rf ./grammar/*.interp
rm -rf ./grammar/*.py
rm -rf ./grammar/*.tokens

antlr4 -Dlanguage=Python3 ./grammar/VLADLexer.g4
antlr4 -Dlanguage=Python3 -visitor ./grammar/VLADParser.g4

ls -l ./grammar/

mv ./grammar/*.py ../libs/vlad-parser/src/vlad/parser/grammar/
rm -rf ./grammar/*.interp
rm -rf ./grammar/*.tokens
rm -rf ./grammar/.antlr/