def run():
    pass
    
    # filter:
    # my_list = [1,4,5,6,9,13,19,21]
    # reto = list(filter(lambda x: x % 2 != 0, my_list))
    # print(reto)

    #///
    # CON COMPREHENSION:
    # reto = [i**3 for i in range(1, 6)]
    # print(reto)
    
    # CON CICLO FOR:
    # list = [1,2,3,4,5]
    # for i in range(1, 6):
    #     print(i**3)

    # CON MAP:
    # my_list = [1,2,3,4,5]
    # squares = list(map(lambda x: x**2, my_list))
    # print(squares)

    #///
    # reduce:
    # from functools import reduce
    # my_list = [2,2,2,2,2]
    # multi_2 = reduce(lambda a, b: a*b, my_list)
    # print(multi_2)




if __name__ == '__main__':
    run()


