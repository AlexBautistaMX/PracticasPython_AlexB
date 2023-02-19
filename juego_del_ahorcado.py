import random, os


lista_de_palabras = ['Uno', 'Dos', 'Tres']
palabra = random.choice(lista_de_palabras)
palabra = palabra.lower()
guiones = '_' * len(palabra)
intentos = 6
os.system('cls')

# Ciclo que cumple una funcion mientras en la variable 'guiones' haya un caracter "_"
while '_' in guiones:
    # Si se acaban los intentos, se imprime un mensaje y se cierra el programa
    if intentos == 0:
          print('Perdiste :(')
          exit()
    # Esta variable guarda la letra que ingrese el usuario
    letra = input('Adivina una letra: ')
    # Condicion que se cumple mientras la letra ingresada se encuantre en la variable 'palabra'
    if letra in palabra:
        # Esta variable almacenara los caracteres adivinados
        y = ''
        # Se itera en la variable 'palabra', en 'i' se guarda el indice y en 'x' se guarda el caracter
        for i, x in enumerate(palabra):
            # Si el caracter(x) es igual a la letra ingresada...
            if x == letra:
                        # La letra ingresada se añade en la variable 'y', en el indice actual de 'i'
                        y += letra
            # Si 'x' no es igual a 'letra'...
            else:
                # El caracter actual (en i) se añade a la variable 'y', manteniendo asi los guiones
                # de las letras que todavia no se han adivinado
                y += guiones[i]
        # Se actualiza la variable 'guiones' con las nuevas letras adivinadas
        guiones = y
        print(guiones)
    # Si no se adivina una letra, solo se imprime un mensaje y se repite el ciclo
    else:
         intentos -= 1
         print("Letra no encontrada.")
# Al adivinar todo, termina el ciclo y se imprime un mensaje
print('Adivinaste!')