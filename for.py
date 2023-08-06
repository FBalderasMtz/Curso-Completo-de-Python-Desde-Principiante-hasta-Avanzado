#Bucle For ---> Es una estructura de control que nos permite iterar (recorrer) sobre una secuencia de elementos, como listas, tuplas, diccionarios, conjuntos y otras estructuras de datos. Con "for" ---> Podemos ejecutar un bloque de código para cada elemento de la secuencia de manera ordenada, realizando alguna operación o acción con cada elemento.

'''
La sintaxis básica del bucle "for" es la siguiente:

for elemento in secuencia:
    #Bloque de código a ejecutar para cada elemento
    
ELEMENTO: es una variable que toma como valor en la "secuencia" en cada iteación del bucle
SECUENCIA: Es un objeto iterable, por ejemplo, una lista o tupla. El puede ser una lista, tupla diccionario etc.
'''

#Ejemplo con una Lista:

frutas = ["manzana", "naranja", "plátano", "uva"]
for fruta in frutas:
    print(fruta) #Por cada fruta, que contenga la lista fruta, imprime fruta, es decir, el for se dará a la tarea de ir analizando parte por parte, o en este caso fruta por fruta que contenga la lista dado que esta separada por "" se denota cuantas deberá imprimir, veamos:
    
#Rango númerico:
for numero in range(1,6):
    print(numero)
    
#Diccionario

paises = {"España": "Madrid", "Francia": "Paris", "Italia":"Roma"}
for pais in paises:
    print(f"La capital de {pais} es {paises[pais]}")
    
#La funcion range() ---> Se ocupa para generar una secuencia númerica en un bucle "for" --> Puede tomar uno, dos, tres argumentos

'''
-range(stop) --> Genera una secuencia desde 0 hasta (stop-1)
-range(start,stop): Genera una secuencia desde "start" hasta (stop-1)
-range(start,stop,step): Genera una secuencia desde "start" hasta (stop-1) con un incremento "step"
'''

for i in range(1,10,2):
    print(i) #Crea un rango del número del 1 al 10, pero que la secuencia tenga de números de 2 en 2 es decir, 1,3,5,7,9 todo esto al final de 10, pero dado que no es número impar no toma en cuenta el 10, solo es su limite.
    
#El bucle "for" es una herramienta esencial para iterar sobre colecciones de datos y realizar operaciones repetitivas en Python. Es una forma eficiente y sencilla de procesar datos y realizar tareas repetitivas en nuestros programas.

#Parte 2

'''Como se explicó anteriormente, el bucle for ---> se utiliza para iterar una secuencia de elementos y ejecutar un bloque de código para cada elemento de la secuencia

Break ---> se utiliza dentro del un bucle (for,while) para detener la ejecución del bucle de manera prematura, sin completar todas las iteraciones. Cuando se encuentra la instrucción Break, el programa inmediatamente sale del bucle es decir rompe con el proceso y continua con la ejecución del código que sigue después del bucle

'''

#Ejemplo con Break:

for i in range(1,6):
    if i == 3:
        break
    print(i)
    
#Continue ---> La instrucción continue se utiliza de igual manera en el bucle (for,while) para pasar a la siguiente iteración sin ejecutar el resto del bloque del código, cuadno se encuenta la instrucción "continue", el bucle salta la siguiente iteración sin ejecutar el código que sigue despues del continue

#Ejemplo con continue:

for i in range(1,6):
    if i ==3:
        continue #Es importante las posiciones de las declaraciones dado que por ese hecho puede que no te compile tu código
    print(i) #Imprime del 1 al 6 pero si tienes un dato = 3, no lo toques y saltalo
    #Resultado = 1,2,4,5
    
#For Doble

#Un for doble o un bucle anidado es cuando se coloca un bucle dentro de otro bucle, esto se utiliza para iterar sobre elementos en múltiples dimensiones, como matrices, bidimensionales(listas de listas) o para realizar combinaciones de elementos en dos o más secuencias

#Ejemplo de for doble:

nombres = ["Ana","Juan","María"]
apellidos = ["Pérez", "Gomez", "Lopez"]

for nombre in nombres:
    for apellido in apellidos:
        print(nombre,apellido)
        
#Los conceptos de "for", "break", "range", "continue" y "for doble" son fundamentales para el control de flujo en Python, ya que nos permiten realizar tareas repetitivas y trabajar con diferentes tipos de datos de manera eficiente.

#Saludos :)