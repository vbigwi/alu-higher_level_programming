# Python - Test-driven development

Fourteenth project of the ALU higher-level programming curriculum.
Every function is documented and tested first: interactive doctests live in
`tests/*.txt` and a unittest suite in `tests/6-max_integer_test.py`.

## Files

| File | Description |
| ---- | ----------- |
| `0-add_integer.py` | `add_integer(a, b=98)`: adds two numbers cast to integers |
| `2-matrix_divided.py` | `matrix_divided(matrix, div)`: divides every element of a matrix |
| `3-say_my_name.py` | `say_my_name(first_name, last_name="")`: prints a greeting |
| `4-print_square.py` | `print_square(size)`: prints a square of `#` |
| `5-text_indentation.py` | `text_indentation(text)`: two new lines after `.`, `?` and `:` |
| `6-max_integer.py` | `max_integer(list=[])`: provided function tested with unittest |
| `tests/` | Doctest files and the unittest module |

## Running the tests

```
python3 -m doctest ./tests/*
python3 -m unittest tests.6-max_integer_test
```
