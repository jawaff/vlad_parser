# VLAD

This project is for a general purpose LL(1) parser that is designed for parsing a stream of token ids that are produced from an LLM model. The ultimate goal is to validate the output of structured text, such as SQL, within a constrained decoder for an LLM so that the output of the model is always syntactically and semantically correct.

The base parser is language agnostic and provides context for the parsed token ids.

The language specific parsers provide a grammar for the specific structured language that the parser is being used for and may provide tools for using the context of the parsed token ids to do further semantic validation for the target environment. One semantic validation example could be checking that a particular table is valid in the target database schema.

## Base Parser
see documentation [here](libs/vlad-parser/README.md)


## SQLITE Parser
see documentation [here](libs/vlad-sqlite/README.md)