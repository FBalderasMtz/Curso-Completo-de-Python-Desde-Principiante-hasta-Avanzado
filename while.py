#El bucle "while" ---> se utiliza para repetir un bloque de código mientras una condicion sea verdadera la estructura básica es:

'''
while condicion:
    #Bloque de código se ejecutará mientras la condición sea verdadera
'''

contador = 0
while contador < 5:
    print(contador)
    contador += 1 #Cuenta desde 0 hasta que sea menor a 5, por eso mismo no toca el 5 por que como no pusimos la declaración <= 5 solo cumple antes del 5
    
#While con if:

#El bucle while puede confibarse con la instrucción "if" para controlar el flujo del programa dentro del bucle. Podemos utilizar el "if" dentro del bloque de código del "while" para realizar una acción condicional en cada iteración.

contador = 0 
while contador < 5:
    if contador == 2:
        print("El contador es igual a 2")
    else:
        print(contador)
    contador += 1
'''
Este ejempli, se inicia una variable contador, con valor 0 y se ejecuta un valor meintras contador sea menor a 5, cuando llega a ser == 2 imprime el texto que pusimos, posteriormente a eso incrementa su valor a 1 es decir suma despues del proceso que ya pasó hasta llegar antes de 5
'''  

#while con If y continue:

#La instrucción "continue" se utiliza dentro del bucle while para la siguiente iteración sin ejecutar el resto del codigo

contador = 0
while contador <5:
    if contador ==2:
        contador += 1
        continue
    print(contador)
    contador +=1

#En este ejemplo, se inicializa una variable "contador" con valor 0 y se ejecuta un bucle "while" mientras "contador" sea menor que 5. Dentro del bucle, se utiliza la instrucción "if" para comprobar si "contador" es igual a 2. Si es así, se incrementa el contador en 1 y se utiliza la instrucción "continue" para pasar a la siguiente iteración. Esto evita que se imprima el valor 2 en el bucle. Luego, se continúa con las iteraciones restantes.

#Saludos :)