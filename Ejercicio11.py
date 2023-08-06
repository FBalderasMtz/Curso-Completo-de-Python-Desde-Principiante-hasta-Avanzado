'''
1.Crear una variable 'tupla' que sea una tupla de los siguientes nombres: Antonio, Pedro y Maria
2.Mostrar el valor de la variable "tupla"
3.Recoger un dato por teclado y almacenarlo en la variable "dato"
4.Si el valor de "dato" está dentro de los valores de la variable "tupla" mostrar "si"
5.Si el valor de "dato" no está dentro de los valores de la variable "tupla, mostrar "No"
'''

#Solución

tupla = ('Antonio', 'Pedro', 'Maria')
print(tupla)
dato = input("Ingresa un Nombre: ")

if ( dato in tupla):
    print('Si')  # si es uno de los elementos del tuple imprime este mensaje
    
if (dato not in tupla):
    print("No")
    