# Python - Object-relational mapping

Last project of the ALU higher-level programming Python track. The first
part talks to MySQL with the `MySQLdb` module and raw SQL, the second part
uses the SQLAlchemy ORM with the `State` and `City` models.

## Files

| File | Description |
| ---- | ----------- |
| `0-select_states.py` | Lists all states |
| `1-filter_states.py` | States starting with `N` |
| `2-my_filter_states.py` | States matching an argument, query built with `format` |
| `3-my_safe_filter_states.py` | Same, safe from SQL injection |
| `4-cities_by_state.py` | All cities with their state, one `execute()` |
| `5-filter_cities.py` | Cities of the state given as argument |
| `model_state.py` | `Base` and the `State` model |
| `model_city.py` | The `City` model |
| `7-model_state_fetch_all.py` | All `State` objects |
| `8-model_state_fetch_first.py` | First `State` object or `Nothing` |
| `9-model_state_filter_a.py` | States containing the letter `a` |
| `10-model_state_my_get.py` | Id of the state named as argument or `Not found` |
| `11-model_state_insert.py` | Adds Louisiana and prints its id |
| `12-model_state_update_id_2.py` | Renames state 2 to New Mexico |
| `13-model_state_delete_a.py` | Deletes states containing the letter `a` |
| `14-model_city_fetch_by_state.py` | All cities as `<state>: (<id>) <city>` |

Every script takes the MySQL username, password and database name as
arguments and connects to localhost on port 3306.
