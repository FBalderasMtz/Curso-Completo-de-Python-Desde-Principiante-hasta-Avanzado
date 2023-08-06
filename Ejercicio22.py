'''Ejercicio 22
Crear una funcion "buscar" que mediante una expresion regular indique si una palabra está en una frase

Probar la funcion "buscar" con estas frases
    texto ="Esto es una frase de pruebas para hacer busquedas
    palabra_a_buscar = 'frase'
En caso de encontrar la palabra en la frase, indicar en que posición empieza y en cual finaliza   
'''
#Solución

import re

def buscar(palabra,texto):
    resultado = re.search(palabra,texto)
    return resultado

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra = "una"

resultado = buscar(palabra,texto)
if(resultado):
    print("Palabra '{}' encontrada".format(palabra))
    incial = resultado.start()
    final = resultado.end()
    print("Empieza en la posición {} y finaliza en la posición {}".format(incial,final))
else:
    print("Palabra {} no encontrada".format(palabra))
    
#SOLUCION 2
print("-----------------")

import re
def buscar(palabra_a_buscar,frase):
    #Crear el patrón de busqueda con la palabra a buscar
    patron = re.compile(r'\b'+re.escape(palabra_a_buscar)+r'\b',re.IGNORECASE)
    
    #Buscar la palabra en la frase utilizando el patrón
    resultado = patron.search(frase)
    
    if resultado:
        inicio = resultado.start()
        fin = resultado.end()
        print(f"La palabra '{palabra_a_buscar}' esta presente en la frase.")
        print(f"Posición de incio: {inicio},Posicion de fin:{fin-1}")
    else: 
        print(f"La palabra '{palabra_a_buscar} no se encontró en la frase.'")
        
#Prueba de la función con las frases dadas
texto = "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = 'frase'
buscar(palabra_a_buscar,texto)

'''
La función buscar utiliza re.compile para crear un patrón de búsqueda que buscará la palabra exacta (ignorando mayúsculas y minúsculas) y que esté delimitada por caracteres no alfabéticos (como espacios, comas, puntos, etc.). Luego, utiliza patron.search(frase) para buscar la palabra en la frase. Si la encuentra, muestra la posición de inicio y fin de la palabra en la frase. Si no la encuentra, indica que la palabra no se encontró en la frase.

Espero que esto te sea útil. ¡Si tienes más preguntas o necesitas más ayuda, no dudes en preguntar!
'''
#Saluds :)