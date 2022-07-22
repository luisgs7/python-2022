def match_func(var: int):
    match var:
        case 1:
            print(f"{var}--One")
        case 2:
            print(f"{var}--Two")
        case 3:
            print(f"{var}--three")
        case _:
            print("Outro número.")

