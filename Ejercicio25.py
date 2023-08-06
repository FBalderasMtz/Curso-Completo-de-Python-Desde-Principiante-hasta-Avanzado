'''Ejercicio 25
A partir de la lista "numeros" que contiene números del 1 al 10,
Obten mediante "filter" una lista denominada "pares" con los números pares de la lista "números"
'''
#Solucion 1 

numeros = [1,2,3,4,5,6,7,8,9,10]
#Lista original
def par(numero):
    if(numero % 2) ==0:
        return True
    else:
        return False

resultado = filter(par,numeros)
pares = list(resultado)
print(pares)

#Solución 2

#Lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]

#Función para determinar si un número es par
def es_par(numero):
    return numero % 2 == 0

#Filtrar los números pares utilizando la función es_par y filter
pares = list(filter(es_par,numeros))
#Mostramos la lista números pares
print(pares)

#Saluds :)