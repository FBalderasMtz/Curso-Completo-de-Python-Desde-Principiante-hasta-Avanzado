#Bienvenido a un nuevo video esta ocasión veremos lo que viene siendo "Tuplas"

'''Las Tuplas en Python son una estructura de datos que se utilizan para almacenar una colección de elementos, son similares a las listas, la diferiencia clave entre listas y tuplas:
Las listas ---> Son mutables ---> Es decir que sus elementos o contenido puede a llegar a tener modificaciones digace tanto agregar como eliminar
Las tuplas ---> Son inmutables ---> Es decir que una vez creada no tiene modificacion alguna
'''
 #Para crear una tupla en Python simplemente separamos los elementos con comas y los encerramos entre parentesis, Por ejemplo:
 
mi_tupla = (1,2,3,4,5)

#Normalmente se ocupan cuando coleccionas datos que no cambiarás durante la ejecución del programa

#Otro ejemplo sería la ejecucion de coordenadas de un punto plano

punto = (3,5)

#Para acceder a los elementos de nuestra tupla, podemos ocupar una indexación es decir, imprimir los valores que queremos mostrar, como lo hicimos con las listas

print("Posición [0] de mi tupla: ",mi_tupla[0]) #Imprimirá 1
print("Posición [1] de mi tupla 2: " , punto[1]) #Imprimirá 5

#Tambien es posible utilizar para acceder desde el final es decir <--- de derecha a izquierda por ejemplo:

print("Posición de mi tupla1 pero ahora con: [-1]",mi_tupla[-1]) #Imprimirá 5

#Recuerda para saber la longitud de la tupla obtendremos con la funcion 'len()'
print("Longitud de mi tupla1: ",len(mi_tupla)) #Imprimirá 5 ---> Es el valor que tenemos de caracteres, recuerda que se cuenta desde 0

#EJEMPLO 2
'''Aunque las tuplas son inmutables, aun se pueden realizar operaciones con ellas es decir, concatenar distintas tuplas por ejemplo:'''

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla_concatenada = tupla1 + tupla2
print("Ejemplo de mi tupla Concatenada: ", tupla_concatenada) #Veamos que es lo que imprime hasta ahora

#Tambien es posible multiplicar una tupla por un número entero para repetir sus elementos:

tupla_repetida = (1,2) * 3
print("Ejemplo de tupla repetida: (1,2)*3",tupla_repetida) #Obtendremos (1,2,1,2,1,2)
