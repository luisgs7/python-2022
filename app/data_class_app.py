from dataclasses import dataclass


@dataclass()
class Person:
    name: str
    age: int = 1


def new_person():
    person = Person("Pedro", 22)
    print(person.__repr__())