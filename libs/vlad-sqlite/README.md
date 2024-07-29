# VLAD SQLite Parser

## Overview

The VLAD parser is a generic parser built specifically for use in a constrained decoder for a transformer. This repository contains a grammar for SQLite along with supporting
code specifically for the purpose of adding runtime validation constraints to supplement the parser for constraining the search space of the transformer.

## References

### SELECT Structure

Due to the fact that our dataset supports sqlite we will be doing the same, but PostgreSQL would be a lot better to actually support in the end. I'm keeping both in mind.

(SQLite)[https://www.sqlite.org/lang_select.html]

### SpiderSQL Dataset Queries

Use these queries as a baseline for what will be supported by our model.

(Gold Queries)[https://github.com/taoyds/spider/blob/master/evaluation_examples/gold_example.txt]

## Supported SQL Grammar

The below grammar will be written specifically for whatever is supported in the Spider v1 dataset, which will be a subset of the SQLite dialect.
Our model will only be trained to do what is in the dataset, so supporting anything else is unnecessary for the scope of this project.
If a need arises, the grammar can be expanded/adapted to support new features and different SQL dialects.
This grammar loosely follows regex and includes tokens to make it more readable.

```
table_alias := \w+
table_name := \w+
column_name := \w+
output_name := \w+

table_column := <table_alias>\.<column_name>
column := (<table_alias>\.)?<column_name>

agg_func := (
        (min|max|sum|avg)\(<column>\)
        |
        count\((\*|DISTINCT <column>)\)
    )

positive_integer := \d+

number := (-)?\d+(\.\d*)?

string := (
        '[^']+'
        |
        "[^"]+"
    )

bool := true|false

literal := <number>|<string>|<bool>


output := (
        <agg_func>
        |
        <column>
    )

output_list := <output>(, <output>)*

operator := (
        >(=)?
        |
        <(=)?
        |
        (!)?=
        |
        // Will not be supported by <agg_condition> in runtime constraints, but technically supported in the grammar.
        (NOT )?IN
    )

between := BETWEEN <number> AND <number>

expression := (
        <literal>
        |
        <column>
        |
        <agg_func>
        |
        \(<select>\)
    )

condition := <expression> (<operator> <expression>|<between>)

agg_condition := <agg_func> (<operator> <literal>|<between>)

select := SELECT 
    (
        *
        |
        (DISTINCT <column>(, <output_list>)?)
        |
        <output_list>
    )
    (
        FROM (<table_name>|\(<select>\)) (<table_alias>)?
        ((LEFT )? JOIN ON <column> = <column>)
    )
    (WHERE <condition>( (AND|OR) <condition>)*)?
    (GROUP BY <column>( HAVING <agg_condition>)?)?
    (ORDER BY ((<agg_func>|<column>) ASC| DESC)?( NULLS (FIRST|LAST)))?
    (LIMIT <positive_integer>)?
    (OFFSET <positive_integer>)?
    ((UNION |INTERSECT |EXCEPT )<select>)?
```
