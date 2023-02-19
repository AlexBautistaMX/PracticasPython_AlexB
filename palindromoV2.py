# def palindrome(palabra):
#     palabra = palabra.replace(' ', '')
#     palabra = palabra.lower()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('ERROR: Cadena vacia.')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    palindrome('')
except TypeError:
    print('ERROR: ingresa un string.')
    

def run():
    string = input('Escribe una palabra: ')
    es_palindromo = palindrome(string)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()

