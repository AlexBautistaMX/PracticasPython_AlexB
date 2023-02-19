def make_division_by(x):
    def division(n):
        div = x % n
        return div
    return division

def run():
    div = make_division_by(50)
    print(div(13))


if __name__ == '__main__':
    run()

