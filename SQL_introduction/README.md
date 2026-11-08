# SQL - Introduction

First SQL project of the ALU higher-level programming curriculum.
It covers creating and deleting databases and tables, inserting, selecting,
updating and deleting rows, and basic aggregate functions with MySQL 8.0.

| Script | What it does |
| ------ | ------------ |
| `0-list_databases.sql` | Lists all databases |
| `1-create_database_if_missing.sql` | Creates `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Drops `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists the tables of the given database |
| `4-first_table.sql` | Creates `first_table` (id, name) |
| `5-full_table.sql` | Shows the CREATE statement of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts id 89, name Best School |
| `8-count_89.sql` | Counts rows with id 89 |
| `9-full_creation.sql` | Creates `second_table` and inserts four rows |
| `10-top_score.sql` | Lists score and name ordered by score |
| `11-best_score.sql` | Lists rows with score >= 10 |
| `12-no_cheating.sql` | Sets Bob's score to 10 by name |
| `13-change_class.sql` | Deletes rows with score <= 5 |
| `14-average.sql` | Average score as `average` |
| `15-groups.sql` | Number of rows per score |
| `16-no_link.sql` | Score and name of rows with a name |
