#Contenido del archivo "main.py"

import mi_modulo #Este es el nombre del otro archivo donde dejamos instrucciones

#Utilizamos la funcion de saludo del módulo
nombre = "Juan"
saludo = mi_modulo.saludar(nombre)
print(saludo) #Imprimirá "Hola,Juan!"

#Utilizamos la función para calcular el área de un círculo
radio = 5
area = mi_modulo.calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area}")

#Guardamos cambios
