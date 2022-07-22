from pattern_matching import match_func
from data_class import Person


if __name__ == '__main__':
    print(f"Hello {__file__} :0")
    match_func(1)
    person = Person("Pedro", 22)
    print(person.__repr__())
