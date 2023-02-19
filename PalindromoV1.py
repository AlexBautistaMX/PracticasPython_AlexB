def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    #return sustituye el valor de una variable por otra cosa.

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
#Recibimos una palabra, le quitamos los espacios, la pasamos a minusculas, la ponemos al revez
#y asignamos este valor a una nueva variable, luego comparamos ambas variables con True y
#False. La palabra es igual al revez si o no? eso hace el programa.

