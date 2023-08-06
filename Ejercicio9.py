'''
1.Crear una variable "números" con la lista de los números del uno al 10 (ambos incluidos)
2.Mostrar el valor de la variable "numeros"
3.Recoger un dato del teclado y almacenarlo en la variable "dato"
4.Convertir "dato" en númerico y almacenarlo en la variable "número"
5.Si el valor de "número" está en la lista de números, mostrar el mensaje "Si"
6.Si el número introducido no está en la lista de números, mostrar el mensaje "No"
'''

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
print("--------------")
dato = input("Ingresa un dato: ")
numero = int(dato)

if(numero in numeros):
    print("Si se encuentra en la lista")
    
if(numero not in numeros):
    print("No se encuentra en la lista")