'''Ejercicio 24
Crear la función "primos" que será una función generadora de números primos entre 0 y el 100
Esta es la lista de números primos entre 1 y 100
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
Utilizar la función generadora para mostrar por pantalla los números primos menores a 50
'''

#Solucion 1
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def primos(maximo):
    for numero in range(maximo):
        if(numero in numeros_primos):
            yield numero
        if (numero > 100):
            break
        
maximo = 50
for numero in primos(maximo):
    print(numero)

print("*************************")
#Solución 2

def es_primo(numero):
    #Los números primos son mayores que 1
    if numero <=1:
        return False
    #Verificamos si el número es divisible por algún número entre 2 y su raíz cuadrada
    for i in range(2,int(numero**0.5)+1):
        if numero %i == 0 :
            return False
    return True
    
def primos(maximo):
    #Generador de números primos hasta el valor máximo
    for num in range(maximo):
        if es_primo(num):
            yield num
            
#Mostramos los números primos menores a 50
for primo in primos(50):
    print(primo)
    
#Depende de ti que solución quieras darle, Saluds :)