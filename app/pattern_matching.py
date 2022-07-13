def match_func(var: int):

    match var:
        case 1:
            print(f"{var}--OK")
        case 2:
            print(f"{var}--OK")
        case 3:
            print(f"{var}--OK")
        case _:
            print("Você digitou um número diferente.")