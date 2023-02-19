menu = """"
Bienvenido al conversor de monedas 💲💲

1- AmloCoins
2- Peronios
3- Colombos

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    AmloCoins = input("¿Cuantas AmloCoins tienes?: ")
    AmloCoins = float(AmloCoins)
    valor_dolar = 20
    dolares = AmloCoins / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == '2':
    Peronios = input("¿Cuantos Peronios tienes?: ")
    Peronios = float(Peronios)
    valor_dolar = 147
    dolares = Peronios / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == '3':
    Colombos = input("¿Cuantos Colombos tienes?: ")
    Colombos = float(Colombos)
    valor_dolar = 4610
    dolares = Colombos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print('Opcion invalida')
