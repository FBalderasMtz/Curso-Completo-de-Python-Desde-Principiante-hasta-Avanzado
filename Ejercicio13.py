'''
1.Crear una variable "diccionario" con los pares de valores siguientes
clave =  uno  valor= one
clave = dos   valor = two
clave = tres    valor = three
2.Mostrar por pantalla el valor de la variable "diccionario"
3.Añadir un nuevo elemento al diccionario
clave = cuatro  valor= four
4.Mostrar ahora el valor del diccionario
5.Recoger un valor introducido por el teclado y almacenarlo en "dato"
6.Utilizar "dato" como clave del diccionario para recuperar su valor
'''

#Solucion

diccionario = {'uno':"one", "dos":"two", 'tres': 'three'}

print(diccionario)
diccionario["cuatro"] = "four" #Se añade el núevo elemento
print(diccionario) #Comprobamos

dato = input("Ingresa un dato: ")
valor = diccionario[dato]
print(valor)