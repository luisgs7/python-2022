from enum import Enum


class City(Enum):
    GOIANIA = 1
    SALVADOR = 2
    BELEM = 3


def hello_city():
    for city in City:
        cidade = city.name
        print(cidade)