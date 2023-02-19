def mi_funcion():
    print("Hola, soy una función.")
# mi_funcion()


def mi_closure(func):
    def wrapper():
        print("Antes de llamar a la función.")
        func()
        print("Después de llamar a la función.")
    return wrapper

funcion_envuelta = mi_closure(mi_funcion)
# funcion_envuelta()


def mi_decorador(func):
    def wrapper():
        print("Antes de llamar a la función.")
        func()
        print("Después de llamar a la función.")
    return wrapper

@mi_decorador
def mi_funcion():
    print("Hola, soy una función.")
# mi_funcion()


