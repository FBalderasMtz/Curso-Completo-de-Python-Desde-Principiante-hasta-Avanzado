'''
Imprime por pantalla el texto "Introduce el primer número"
Crea la variable "dato1" con el primer valor introducido en el paso anterior
Imprime por pantalla el texto "Introduce el segundo número"
Crea la variable "dato2" con el segundo valor introducido en el paso anterior
Convertir la variable "dato1" en una variable númerica denominada "num1"
Convertir la variable "dato2" en una variable númerica denominada "num2"
Crear la variable "suma" con la suma de "num1" y "num2"
Convertir la variable "suma" en una variable del texto denominada "strSuma"
Crear la variable "resultado" con la concatenación de "La suma es" y "strSuma"
Imprimir el valor de "resultado"
'''

#Solución

print("Introduce el primer número")
dato1 = input()
print("Introduce el segundo número")
dato2 = input()
num1 = int(dato1)
num2 = int(dato2)
suma = num1 + num2
strSuma = str(suma)
resultado = "La suma es " + strSuma

print(resultado)