from pattern_matching_app import match_func
from data_class_app import new_person
from enum_app import hello_city
from fstring_app import hi_fstring
from typing_app import type_app


if __name__ == '__main__':
    print(f"Hello {__file__} :0")
    match_func(1)
    new_person()
    hello_city()
    hi_fstring()
    type_app([1, 2, 3], (4.1, 5.2, 6.3))
