from typing import List


def walrus_operator(index: List[int]) -> None:
    if(a := len(index)) > 2:
        print(f"Esta lista é maior que 2, ela tem:{a} números inteiros")
    elif(a := len(index)) < 2:
        print(f"Esta lista é menor que 2, ela eh:{a} números inteiros")
    else:
        print(f"Esta lista tem: {len(index)} números inteiros")