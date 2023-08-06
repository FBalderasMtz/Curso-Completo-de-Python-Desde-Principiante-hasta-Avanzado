#Bienvenido al ejercicio 2

'''
Crear la variable "numero1" con el valor 5
Crear la variable "numero2" con el valor 3
Crear la variable "suma" con el valor de suma de los numeros numero1 y numero2
Convertir esta variable "suma" en una cadena de caracteres y llamarla "strSuma"
Crear una variable resultado que concatene el texto "El resultado es " y la variable "strSuma"
'''
numero1 = 5
numero2 = 3
suma = numero1 + numero2
strSuma = str(suma)# convertimos a string para concatenarlo mas tarde
resultado= 'El resultado es '+ strSuma
print(resultado)

#OPCION 2
suma = str(int(numero1) + int(numero2)) #convertimos de manera directa
print("\nEl resultado es",suma)

#Como podrás notar el resultado el mismo y aveces puedes reducir varias lineas de código, Nos vemos en la siguiente Leccion! Saludos! 