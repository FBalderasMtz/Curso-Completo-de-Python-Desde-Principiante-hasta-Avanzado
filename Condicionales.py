#Los condicinales "if", "elif", "else" ---> Son estructuras de control en Python
'''Nos permiten tomar desiciones basadas en el valor de una o varias codiciones.Estas condiciones pueden ser expresionles lógicas que evalúan a "true" o "False" y en funcion de su resultado, se ejecutará un bloque de código u otro:

-if ---> Se ultiliza para ejecutar un bloque de código si la condicion especificada es verdadera (True). La sintaxis se maneja asi

if condicion:
#Codigo que se ejecuta si la condición es verdadera 
'''
#Ejemplo:
edad = 20
if edad >= 18:
    print("Eres Mayor de edad")
    
#elif ---> es la abreviatura de "else if"---> Se utiliza para evaluar múltiples condiciones despúes de un if, Se verifica si la condición especificada es verdadera (True)y, en caso afirmativo, se ejecutará el bloque de código correspondiente. Si la codición del "if" es falsa(False), se evaluará la siguiente condición en "elif".La sintaxis es la siguiente:
'''
if condicion1 :
    #codigo a realizar cuando la primera condición sea cierta
elif condicion2 :
    #codigo a realizar cuando las dos primeras condiciones no son ciertas 
'''

#Ejemplo:
edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <65:
    print("Eres adulto")
else: 
    print("Eres mayor de edad")
    
#else -->
'''
La estructura "else" se utiliza cuando queremos ejecutar un bloque de código en caso de que ninguna de las condiciones anteriores sea verdadera (False). Solo puede haber un bloque de código "else" en la estructura "if - elif - else" La sintaxis es asi:

if condicion1:
 #Bloque de código si la condicion1 es True
elif condicion2:
 #Bloque de código si la condición2 es True
else:
 #Bloque de código si ninguna de las condiciones anteriores es True
'''

#Ejemplo

edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
else:
    print("Eres Jubilado")


#En resumen "if","elif","else" nos permiten controlar el flujo de ejecución de nuestro código según el cumplimiento de ciertas condiciones, es una herramienta para tomar desiciones y ejecutar diferentes acciones en función de las circunstancias.

#Nos vemos en el proximo video, Saludos!