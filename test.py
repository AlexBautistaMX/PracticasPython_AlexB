# list = []
# for i in range(1, 11):
#     list.append(i)
# for i in list:
#     print(i)
# for i in list:
#     if i % 2 == 0:
#         print(i)


# dic_nombre = {
#     'Ana': 20,
#     'Amy': 21,
#     'Aly': 22,
#     'Sam': 23,
#     'Nat': 24
# }
# for name, age in dic_nombre.items():
#     print(name, age)
# for name, age in dic_nombre.items():
#     if age > 18:
#         print(name, age)


# x = 1
# y = 2
# z1 = x + y
# z2 = x - y
# z3 = x * y
# z4 = x / y
# print(z1)
# print(z2)
# print(z3)
# print(z4)


# listnum = [1, 2, 3]
# listmul= []
# for i in listnum:
#     if i > 0:
#         listmul.append(i * 2)
# print(listmul)

# frutas = ['manzana', 'uva', 'naranja', 'sandia', 'melon', 'platano', 'kiwi', 'anana']
# frutas_a = []
# for i in frutas:
#     if i[0] == 'a':
#         frutas_a.append(i)
# print(frutas_a)

# s1 = 'texto'
# if s1[0] == s1[0-1]:
#     print(True)
# else:
#     print(False)


# num = 0
# while num < 10:
#     num += 1
#     print(num)

# num1 = input('numero: ')
# num2 = 0
# while int(num1) != 0:
#     num2 += int(num1)
#     num1 = input('numero: ')
#     if int(num1) == 0:
#         print(num2)
#         break


# dic = {
#     'pro1': 'cat1',
#     'pro2': 'cat2'
# }
# def calc():
#     cant = len(dic)
#     print(cant)

# dic2 = {
#     {'Nombre': 'Glen Halsey', 'edad': 21, 'ciudad': 'NY'}
# }
# def nom():
#     n = input('Ingrese nombre: ')
#     if n == len(dic2):
#         print(n)

# dict3 = {
#     'pro1': 20,
#     'pro2': 10
# }
# sum1 = sum([dict3 for dict3 in dict3.values()])
# print('Precio: ', sum1)


# list1 = [x for x in range(1, 21) if x % 2 == 0]
# print (list1)

# phrases = ['El sol brilla en el cielo', 'La nieve cae en invierno', 'Los pájaros vuelan en el aire', 'El río fluye hacia el mar', 'Los niños juegan en el parque']
# list3 = [phrases for phrases in phrases if len(phrases) % 2 == 0]
# print(list3)

# dict0 = {}
# dict1 = {dict0:value for value in range(1, 21) if value % 2 != 0}
# print(dict1)
# dict_comp = {val:val**2 for val in range(1,21) if val % 2 != 0}
# print(dict_comp)

# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# dict1 = {list1:i for i in list2 }
# print(dict1)

# x = int(input('num: '))
# lam1 = lambda x: x ** 2
# print(lam1(x))

# def lam2():
#     x = 1
#     y = 2
#     lam3 = lambda x, y: x * y
#     print(lam3(x, y))
# lam2()


# list1 = [-1, -2, -3, 1, 2, 3]
# list2 = list(filter(lambda x: x > 0, list1))
# print(list2)

# list3 = [1, 2, 3]
# list3 = list(map(lambda x: x * 3, list3))
# print(list3)


word = "azul"
guess = "____"

while guess != word:
    letter = input("Ingrese una letra: ")
    if letter in word:
        new_guess = ""
        for i, char in enumerate(word):
            if char == letter:
                new_guess += letter
            else:
                new_guess += guess[i]
        guess = new_guess
        print(guess)
    else:
        print("Letra no encontrada.")

print("Adivinaste la palabra!")