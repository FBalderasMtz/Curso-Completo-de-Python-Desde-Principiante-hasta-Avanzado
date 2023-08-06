'''
FUNCIONES --> En python, una funcion es un bloque de código reutilizable que realiza una tarea especifica. Se define utilizando la palabra clave "def", seguida del nombre de la función y los parámetros entre paréntesis. Dentro del bloque de la función, se coloca el código que realiza la tarea deseada.
'''

#Ejemplo de función

def saludar (nombre):
    print(f"Hola, {nombre}!")
    
#Llamar a la función
saludar("Juan") #Imprime "Hola Juan!"
saludar("Maria") #Imprime "Hola, Maria!"

#Funciones con retorno(return)

'''Ademas de imprimir resutlados, las funciones pueden devolver valores utilizando la palabra clave "return". Esto te permite que el valor calculado dentro de la función se pueda utilizar en otras parte del programa.'''

#Ejemplo de funcion con return

def suma (a, b):
    resultado = a + b
    return resultado

#Llamar a la función y guardar el resultado en una variable
resultado_suma =suma(3, 5)
print(resultado_suma)  #Imprime 8 

#Paso de valor por referencia:

#En python, los argumentos de una función se pasan por referencia, lo que significa que si se modifica un objeto mutable dentro de la función, los cambios también, se reflejarán fuera de la función.

#Ejemplo de paso de valor por referencia:

def modificar_lista(lista):
    lista.append(4)
    #Agrega un elemento al final de la lista
    
mi_lista = [1,2,3]
modificar_lista(mi_lista)
print(mi_lista) #Imprime [1,2,3,4]

'''
Este ejemplo, la función "modificar_lista" recibe una lista como argumento y agrega el número 4 a esa lista. Como las listas son objetos mutables, lso cambios se reflejan en la lista original "mi_lista"
'''

#Funciones Lambda:
'''Las funciones lambda, tambien conocidas como funciones anonimas, son funciones pequeñas y de una sola línea que no tienen un nombre asociado. Se definen utilizando la palabra clave, "lambda" seguida de los parámetros y la expresión que representa el resultado.'''

#Ejemplo de función lambda:

#Funcion lambda para sumar dos números:

sumar = lambda a, b: a+b
resultado = sumar(5,3)
print(resultado) #Imprime 8

'''
En este ejemplo, se define una función lambda que toma dos parámetros "a" y "b" y devuelve la suma de ambos. Luego, se llama a la función lambda y se almacena el resultado en la variable "resultado".
'''

#Saludos :)