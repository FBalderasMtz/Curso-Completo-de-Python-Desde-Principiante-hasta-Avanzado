#Las expresiones regulares (o regex) son secuencias de caracteres que forman un patrón donde búsqueda. En python, podemos utilizar el módulo 're' para trabajar con expresiones regulares.A continuación, te mostraré algunos ejemplos de como utilizar las funciones
'''search,findall,slipt, y sub del modulo "re" '''

import re

#Ejemplo de la funcion search

texto = "Hola, mi número de télefono es 123-456-7890"
patron = r'\d{3}-\d{3}-\d{4}' #Patrón para buscar un número de telefono en formato XXX-XXX-XXXX
resultado = re.search(patron,texto)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())
else:
    print("Número de teléfono no encontrado.")
    
#Ejemplo de la función findall
texto = "La lista de números es: 123,456,789 y 987"
patron = r'\d+' #Patrón para buscar números enteros

numeros_encontrados = re.findall(patron,texto)
print("Números encontrados:", numeros_encontrados)

#Ejemplo de la funcion split
texto = "Python-es-un-lenguaje-de-programación."
patron = r'-' #Patron para dividir el texto en guiones

palabras = re.split(patron,texto)
print("Palabras:",palabras)

#Ejemplo de la función sub
texto ="Hoy es un hermoso día"
patron =r'hermoso'#Patron para remplazar

nuevo_texto = re.sub(patron,'maravilloso', texto)
print("Texto modificado:",nuevo_texto)

#Explicación de cada función

'''
-search: Busca el patron en el texto y devuelve el primer resultado que encuentre.Si encuentra una coincidencia, se puede obtener utilizando 'resultado.group()'
-findall: Busca todas las coincidencias del patrón en el texto y las devuelve en una lista.
-slipt:Divide el texto en función del patrón y devuelve una lista con las partes resultantes.
-sub:Remplaza todas las coincidencias del patrón de un nuevo texto

En todos los ejemplos, utilizamos el patrón r'', que indica una cadena de caracteres "raw" (cruda), lo que significa que los caracteres escapados como \d o \ se interpretan literalmente como están escritos.

Recuerda que las expresiones regulares pueden ser bastante poderosas y útiles para trabajar con cadenas de texto más complejas y realizar tareas de búsqueda y manipulación de texto de manera más eficiente.
'''

#Siguemeeeee! Saluds :)