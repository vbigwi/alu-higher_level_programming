# SQL - More queries

Second SQL project of the ALU higher-level programming curriculum.
It covers MySQL users and privileges, NOT NULL, UNIQUE, PRIMARY KEY and
FOREIGN KEY constraints, subqueries, and INNER and LEFT joins.

| Script | What it does |
| ------ | ------------ |
| `0-privileges.sql` | Lists the privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and a SELECT-only `user_0d_2` |
| `3-force_name.sql` | Table `force_name` with a NOT NULL name |
| `4-never_empty.sql` | Table `id_not_null` with id defaulting to 1 |
| `5-unique_id.sql` | Table `unique_id` with a unique id defaulting to 1 |
| `6-states.sql` | Database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California using a subquery |
| `9-cities_by_state_join.sql` | Cities with their state name using JOIN |
| `10-genre_id_by_show.sql` | Shows with at least one genre |
| `11-genre_id_all_shows.sql` | All shows with their genre id or NULL |
| `12-no_genre.sql` | Shows without any genre |
| `13-count_shows_by_genre.sql` | Number of shows per genre |
| `14-my_genres.sql` | Genres of the show Dexter |
| `15-comedy_only.sql` | Comedy shows |
| `16-shows_by_genre.sql` | All shows with all their genres |
