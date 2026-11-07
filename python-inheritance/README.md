# Python - Inheritance

Tenth Python project of the ALU higher-level programming curriculum.
It covers superclasses and subclasses, `isinstance`, `issubclass`, `type`
and `super`, overriding methods, and documenting code with doctests.

## Files

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | `lookup(obj)`: returns the attributes and methods of an object |
| `1-my_list.py` | `MyList(list)` with `print_sorted()` |
| `2-is_same_class.py` | `is_same_class(obj, a_class)`: exact class match |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)`: instance or subclass |
| `4-inherits_from.py` | `inherits_from(obj, a_class)`: strict subclass only |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an unimplemented `area()` |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator()` |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` with private validated sides |
| `9-rectangle.py` | `Rectangle` with `area()` and `__str__` |
| `10-square.py` | `Square(Rectangle)` with `area()` |
| `11-square.py` | `Square` with its own `__str__` |
| `tests/` | Doctest files run with `python3 -m doctest ./tests/*` |
