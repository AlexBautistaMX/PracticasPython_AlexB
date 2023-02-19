pesos = input("¿Cuantos pesos tienes?: ")
#Input: Pide al usuario ingresar un valor.
pesos = float(pesos)
#Float: Transforma un valor o variable a
#un numero decimal.
valor_dolar = 20
dolares = pesos / valor_dolar
#Dolares es igual a la cantidad ingresada entre
#20.
dolares = round(dolares, 2)
#Usando round, estamos redondeando el contenido
#de la variable dolares en la cantidad de 
#decimales designada (en este caso 2).
dolares = str(dolares)
#str traduce la variable numerica
#dolares en texto.
print("Tienes $" + dolares + " dolares")
#print hace que el mensaje se reprodusca
#al usuario.