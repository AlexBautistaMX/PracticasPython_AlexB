


import random



def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Adivina el numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Es mayor.')
        else:
            print('Es menor.')
        numero_elegido = int(input('Intena de nuevo: '))
    print('Correcto!.')


if __name__ == '__main__':
    run()