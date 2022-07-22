from pattern_matching_app import match_func
from data_class_app import new_person
from enum_app import hello_city
from fstring_app import hi_fstring


if __name__ == '__main__':
    print(f"Hello {__file__} :0")
    match_func(1)
    new_person()
    hello_city()
    hi_fstring()
