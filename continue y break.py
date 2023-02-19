# def run():
#     for contador in range(10):
#         if contador % 2 != 0:
#             continue
#         print(contador)


# def run():
#     for i in range(99):
#         print
#         if i == 58:
#             break


def run():
    texto = input('Ingresa un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()


