def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dist = {'firstname': 'Facundo', 'lastname': 'Garcia'}

    super_list = [
        {'firstname': 'Facundo01', 'lastname': 'Garcia01'},
        {'firstname': 'Facundo02', 'lastname': 'Garcia02'},
        {'firstname': 'Facundo03', 'lastname': 'Garcia03'},
        {'firstname': 'Facundo04', 'lastname': 'Garcia04'},
        {'firstname': 'Facundo05', 'lastname': 'Garcia01'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)


if __name__ == '__main__':
    main()