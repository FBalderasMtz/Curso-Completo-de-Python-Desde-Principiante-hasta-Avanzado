#Para leer ficheros en Python, puedes utilizar la funcion "open()" junto con el método read(). Ejemplo de ello

#Paso 1.Creamos un archivo llamado "ejemplo.txt" <---- Contendrá el siguiente contenido "Hola, este es un ejemplo del archivo de texto.
# Esta es otra linea del archivo."
#Guardamos cambios

#Ahora para leer el contenido de archivo en Python, podemos hacer lo siguiente:

#Abrimos el archivo en modo lectura ('r') <--- Read
with open ('ejemplo.txt','r') as archivo:
    #Leemos todo el contenido del archivo y guardamos la variable 'contenido' <--Read
    contenido =  archivo.read()
    
#Imprimimos el contenido del archivo
print(contenido)

#Obtenemos de resultado
'''"Hola, este es un ejemplo del archivo de texto.
Esta es otra linea del archivo.'''

#El bloque with open(...) as archivo: se asegura de que el archivo se cierre automáticamente cada vez que hayas terminado de leerlo, De esta manera no tienes que preocuparte por cerrar explicitamente el archivo después de usarlo.

#También puedes leer el archivo línea por linea utilizando el método readline()

with open('ejemplo.txt','r') as archivo:
    linea =  archivo.readline()
    while linea:
        print(linea,end='')
        linea = archivo.readline()
        
'''
Esto imprimirá el contenido del archivo línea por línea.

Recuerda que cuando abras un archivo en modo de lectura ('r'), asegúrate de que el archivo exista en la ubicación especificada. Si el archivo no existe, Python generará un error. Además, ten en cuenta que la lectura de archivos puede generar errores si el archivo es muy grande y no tienes suficiente memoria disponible. En ese caso, puedes considerar leer el archivo en bloques o utilizar técnicas de lectura más avanzadas.
'''

#Saluds :)