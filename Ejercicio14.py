'''Ejercicio 14
Crea un diccionario con los siguientes pares de valores
    manzana, apple
    naranja, orange
    platano, banana
    limon, lemon
Muestra la traducción para la palabra "Naranja"
Añade un elemento nuevo con "piña" y "pineapple"
Haz un bucle para mostrar todos los elementos de diccionario    
'''

#Solución

frutas = {"manzana":"apple","naranja":"orange","platano": "banana","limon":"lemon"}
print(frutas)

print(frutas ["naranja"])

frutas ["piña"] = "pineapple"
print(frutas)

for clave,valor  in frutas.items():
    print("{} en ingles es {}".format(clave,valor))