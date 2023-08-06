#Ejercicio 26
#A partir de una lista de números del 1 al 10, obtener una nueva lista con todos los elementos incrementados en 10 unidades

#Solución

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
def incrementar(numero):
    resultado = numero + 10
    return resultado
    #return numero + 10

resultado = map(incrementar,numeros)
numeros2 = list(resultado)
print(numeros2)

print("**************")
#Solución 2
#Lista con números del 1 al 10
numeros = [1,2,3,4,5,6,7,8,9,10]
#Funcion para incrementar un número en 10 unidades
def incrementar_en_10(numero):
    return numero + 10
#Usamos map para aplicar la funcion a cada elemento de la lista
nueva_lista = list(map(incrementar_en_10,numeros))

#Mostramos la nueva lista con los elementos incrementados en 10 unidades
print (nueva_lista)
#Saluds :)