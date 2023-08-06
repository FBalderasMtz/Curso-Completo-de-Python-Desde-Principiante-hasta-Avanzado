#Diccionarios

'''Los diccionarios en Python son una estructura de datos que almacenan pares de ---->clave:valor <---- basicamente esta es la estructura de los datos que maneja un diccionario, cada elemento del diccionario consiste en una clave unica y su correspondeinte valor asociado. La valve es una etiqueta que se utiliza para acceder y buscar el valor correspondiente'''

#Para crear un diccionario en Python, se utilizan "{}" y separamos cada par clave:valor con los : <---Dos puntos... Por ejemplo:

mi_diccionario = {"nombre": "Juan", "edad":30, "Ciudad": "Madrid"} #Este ejemplo, el diccionario --> mi_diccionario tiene tres pares clave valor

#Para acceder a un valor en el diccionario, utilizamos la clave correspondeinte, es decir:
print(mi_diccionario["nombre"]) #Imprimirá "Juan"
print(mi_diccionario["edad"]) #Imprimirá 30
print(mi_diccionario["Ciudad"]) #Imprimirá "Madrid"

'''PRECAUCION Ó NOTA IMPORTANTE ---> Si intentamos acceder a una clave que NO EXISTE en el diccionario, Python lanzará un error 'KeyError' '''

#Se pueden modificar valores asociados a las claves, es decir agregar pares al diccionario:

mi_diccionario["edad"] = 31 #Modificamos el valor de la clave "edad" a 31
mi_diccionario["profesion"] = "Ingeniero" #Agregamos una nueva clave de "profesión" con el valor de "Ingeniero"

#Para verificar si esta clave existe correctamente utilizamos el operador 'in'
if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe en el diccionario")
    
#Ademas podemos utilizar metodos como 'keys()', 'values()'y 'items()' para obtener listas con las claves, o los valores pares

#Te muestro

claves = mi_diccionario.keys()
valores = mi_diccionario.values()
pares = mi_diccionario.items()

print(claves)   # Imprime ["nombre", "edad", "ciudad", "profesion"]
print(valores)  # Imprime ["Juan", 31, "Madrid", "Ingeniero"]
print(pares)    # Imprime [("nombre", "Juan"), ("edad", 31), ("ciudad", "Madrid"), ("profesion", "Ingeniero")]


#Probamos todos los resultados que sean correctos

#Nos vemos en el proximo video, Saludos!