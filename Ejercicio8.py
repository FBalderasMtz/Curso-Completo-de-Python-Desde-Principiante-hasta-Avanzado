'''
1.Crea una variable "minimo" con el valor 20
2.Crea una variable "maximo" con el valor 500
3.Recoge un valor del teclado y almacenalo en la variable "dato"
4.Convierte la variable "dato" en un número y almacénalo en la variable "número"
5.Si el "número" es menor que el valor "minimo", mostrar el texto "Valor bajo"
6.Si el "número" es mayor que el valor "maximo", mostrar el texto "Valor alto"
7.Si el "número" esta entre el valor "minimo" y "maximo", mostrar el texto "Valor medio"
'''

minimo = 20
maximo = 500

dato = input("Ingresa un dato: ")
numero = int(dato)
if(numero < minimo):
    print("Valor Bajo")

if(numero > maximo):
    print("Valor Alto")
    
if(numero > minimo) and ( numero < maximo):
    print("Valor Medio")