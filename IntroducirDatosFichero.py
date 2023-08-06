#Para Incluir datos (agregar contenido) al final de un fichero existente sin eliminar su contenido actual, puedes abrir el archivo en modo de escritura al final ('a'). Te muestro un ejemplo:

#Abrir el archivo en modo escritura al final ('a')
with open('datos.txt','a')as archivo:
    #Escribir datos dentro del archivo con un salto de linea (\n)
    archivo.write('Este es un nuevo dato que se agrega.\n')
    archivo.write('Otro dato que se incluye en el archivo.\n')
    
'''
Este ejemplo el archivo "datos.txt" se abrirá en modo escritura al final ('a')lo que significa que el contenido previo del archivo se mantendrá y los nuevos datos se agregarán al final del archivo.

En esta caso como el archivo no existe, se crea uno nuevo y se agregan los datos al final del archivo
'''

