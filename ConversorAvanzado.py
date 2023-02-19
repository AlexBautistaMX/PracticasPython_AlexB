def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos ' + tipo_pesos + 'tienes? ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print('Tienes $' + str(dolares) + ' dolares')

menu = """
Bienvenido al conversor de divisas.

1- Mex
2- Col
3- Arg

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor('MEX ', 20)

elif opcion == 2:
    conversor('COL ', 4060)

elif opcion == 3:
    conversor('ARG ', 147)

else:
    print('Error: ingrese una opcion valida')