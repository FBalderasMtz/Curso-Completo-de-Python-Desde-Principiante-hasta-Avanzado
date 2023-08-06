'''Ejericio 20
Crea el diccionario "frutas"
frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

Grabar esta estructura de datos "frutas" en un fichero binario "fichero.pckl"
Ya que en un fichero de texto, solo se guardan caracteres, pero no se pueden guardar estas estructuras.

Recuperar esta estructura de datos del fichero "fichero.pckl"
Verificar que sigue siendo un diccionario, ejecutando el método .values() 
'''

#Solucion

frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}
print(frutas.values())

fichero = open("fichero.pckl",'wb')
import pickle
pickle.dump(frutas,fichero)
fichero.close()

fichero2 = open("fichero.pckl","rb")
datos = pickle.load(fichero2)
print(datos)
print(datos.values())