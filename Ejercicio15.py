'''Ejercicio 15
Creamos una variable "nota" que tenga el valor 4.5
Creamos una variable "trabajo_realizado" que tenga el valor "si"
Calcular  el valor de la variable "nota_final", teniendo en cuenta que, si la nota_final es mayor o igual a 4, y el valor de la variable "trabajo_realizado" es igual a "si", entonces "nota_final" será igual a "aprobado", en caso contrario será igual a "suspenso"
'''

#Solucion

nota = 6
trabajo_realizado = "si"
if (nota >= 4) and (trabajo_realizado == "si"):
    nota_final = "aprobado" 
else:
    nota_final = "suspenso"
    
print(nota_final)