'''
1-Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
2-Crear una variable "longitud" que contiene la longitud de la variable "cadena"
3-Crear una variable "strlongitud" que tenga el valor de "longitud" pero convertida a cadena de caracteres o string
4-Crear una variable "Mayusculas" que contiene la variable "cadena" en Mayusculas
5-Crear una variable "resultado" que concatene "mayusculas" con el texto "tiene longitud de" y "strlongitud"
'''

#Solución

cadena= "Esto es un texto de ejemplo"
longitud = len(cadena)
print(longitud)

strlongitud = str(longitud)
print(strlongitud)

mayusculas = cadena.upper()
print(mayusculas)

resultado = mayusculas + " tiene longitud de " + strlongitud
print(resultado)