def divisors(num):
    div1 = [i for i in range(1, num + 1) if num % i == 0]
    return div1


def run():
    num = input('Ingresa un numero: ')
    assert num.isnumeric(), 'Ingresa un NUMERO'
    num = int(num)
    assert num > 0, 'Ingresa un numero POSITIVO'
    print(divisors(num))
    print('Termino mi programa')



if __name__ == '__main__':
    run()

