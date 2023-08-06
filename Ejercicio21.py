'''Ejercicio 21
Crear la funcion "operación" que dado 3 números, divida el primer número entre la resta de los otros dos numeros

Utilizar la función creada con los números 5,4,2
Utilizar la función creada con los números 6,3,3

Utilizar el bloque try...except para controlar cualquier posible error
'''

#Solución

def operacion(num1,num2,num3):
    resultado = num1 / (num2-num3)
    return resultado

num1 = 6
num2 = 4
num3 = 3
try:
    resultado = operacion(num1,num2,num3)
    print(resultado)
except:
    print("Error. Los ultimos dos números tienen que ser diferentes")