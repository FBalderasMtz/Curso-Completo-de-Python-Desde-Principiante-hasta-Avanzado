#Los Operadores Logicos constan de (and, or, not)

#Son de igual comparadores de distintos aspectos estos nos ayudan a hacer comparaciones de conjuntos más amplios es decir

num1 = 15
num2 = 19
num3 = 84
num4 = 14

variable1 = num1 > num2
print("Variable 1:", variable1)
#Esto ya lo vimos, ahora continuamos más o menos con el mismo procedimiento
variable2 = num3 < num4
print("Variable 2 :" , variable2)

#Operador AND ---> compara en grupos en este caso el valor de 2 variables por cada lado es decir lado derecho y lado izquiero, te explico: 

resultado = (num1 > num2) and (num3 < num4) #-----> Si ambos valores internos arrojan como resultados igual es decir (False) and (False) ==> Como resultado obtendremos True, en este ejemplo es claro que alguno de los dos valores no es igual es decir, tenemos un True and False ---> Por lo tanto es False
print(resultado)

num5 = 10
num6 = 5
num7 = 7
num8 = 8

#Hacemos segunda prueba
resultado2 = (num5 > num6) and (num7 < num8) 
print(resultado2) #Cumple los terminos que solicita el operador AND

#Operador OR ---> Funciona de un modo similar el cual la diferiencia en AND es que cualquier valor de los campos sea True por automatico la variable de resultado será True es decir:

num5 = 10
num6 = 5
num7 = 7
num8 = 8
#Ocupamos los mismos datos

print(num6 < num7) #Una vez que obtenemos un true podemos hacer el proceso el cual nos va permitir hacer lo siguiente

resultado3 = (num5 > num6) or (num7 > num8) #Cualquiera de los dos valores que se muestre aqui será True 
print(resultado3)

#Operador not, más simple aún

print("-------------------") #Para diferenciar
print(not(num7 > num8))

#Nos vemos en el siguiente video, Saludos!