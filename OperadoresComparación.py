#Operadores de Comparación (==,!=,<,>,>=,<=)

#Empezamos con el "==" es decir igual igual

'''Te explico, el comparador == consta de hacer una comparación de igualdad entre dos variables es decir ---> dar a notar si los valores o variables a comparar son iguales, el mecanismo que maneja este metodo consta de solo denotar True ó False, es decir, Son valores iguales --> True, Son valores desiguales ---> False, no hay más'''
num1 = 6 #Declaramos variables de tipo int
num2 = 5
variable1 = num1 == num2 #---> Almacenamos el valor de lso valores comparados en la variable que nosotros dispongamos es decir, la variable1 ---> comparará oh realizará el metodo de comparar los dos terminos mencionados es decir
print(variable1)

print("****************") #Separador
#En todo caso que querramos obtener un true podemos comparar con una cadena tambien, es decir:

cadena1 = "Hola"
cadena2 = "Hola"
resultado = cadena1 == cadena2
print(resultado)

#Un metodo más eficaz sería 

cadena3 = "Hola Mundo"
if(cadena3 =="Hola Mundo"):
    print("Escribió Hola Mundo")

print("--------------")
# (!=) --> Distinto de ---> Es decir va a comparar si una variable es distinta a otra es decir:

num3 = 96 
num4 = 15
#Almacenamos en otra variable
variable2 = num3 != num4
print(variable2) #Por lo tanto seguimos manejando el mismo mecanismo de True o False

print("--------------")

# Simbolos de Mayor y menor que es decir ---> "<,>"
num5 = 5
num6 = 14
variable3 = num5 < num6
print(variable3)
print("..................")
num7 = 25
num8 = 13
variable4 = num7 > num8
print(variable4)

print("__________________")
#Comparador Menor o Mayor igual que ----> "<=,>=" <--- Estos simbolos hacen ser iguales oh llegar a un tope de un contador, mas adelante lo verémos con diferentes procesos es decir, con ciclos for etc, mostramos lo siguiente

num9 = 14
num10 = 25
variable5 = num9 >= num10
print("Simbolo >= ")
print(variable5)
print("Simbolo <=")
#Mismos datos diferentes valores
num9 = 14
num10 = 25
variable5 = num9 <= num10
print(variable5)

#Nos vemos en el siguiente video Saludos!