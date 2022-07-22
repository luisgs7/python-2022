from typing import List


def walrus_operator(index: List[int]) -> None:
    if(a := len(index)) > 2:
        print(f"Esta lista contém:{a} números")
    elif(a := len(index)) < 2:
        print(f"Esta lista possui:{a} números")
    else:
        print(f"Esta lista tem: {len(index)} números")