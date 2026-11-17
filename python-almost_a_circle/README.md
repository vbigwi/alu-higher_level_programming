# Python - Almost a circle

Fifteenth project of the ALU higher-level programming curriculum and a
rehearsal for the AirBnB clone: classes, inheritance, properties with
validation, `*args` and `**kwargs`, JSON serialization to files, and a
full unittest suite.

## Layout

| Path | Description |
| ---- | ----------- |
| `models/base.py` | `Base`: id management, JSON helpers, save/load to `<Class>.json` |
| `models/rectangle.py` | `Rectangle(Base)`: width, height, x, y with validation, area, display, update, to_dictionary |
| `models/square.py` | `Square(Rectangle)`: size property, update, to_dictionary |
| `tests/test_models/` | Unit tests for the three classes |

## Running the tests

```
python3 -m unittest discover tests
python3 -m unittest tests/test_models/test_base.py
```
