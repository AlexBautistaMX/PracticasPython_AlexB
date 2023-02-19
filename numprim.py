from typing import Union

def es_primo(x:int) -> bool:
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def run() -> None:
    x = int(input('Ingrese un número: '))
    if es_primo(x):
        print(f'{x} es primo')
    else:
        print(f'{x} no es primo')

if __name__ == '__main__':
    run()

