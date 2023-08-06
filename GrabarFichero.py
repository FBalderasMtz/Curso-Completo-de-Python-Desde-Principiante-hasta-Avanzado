#Para grabar (escribir) en un archivo de Python, puedes utilizar la función open() en modo de escritura ('w+'). Hagamos un ejemplo:

#Supongamos que queremos escribir en un archivo llamado "nuevo_archivo.txt" hacemos lo siguiente:

#Abrimos el arhcivo en modo de escritura ('w')
with open('nuevo_archivo.txt','w') as archivo:
    #Escribimos contenido del archivo
    archivo.write('Hola, este es un nuevo archivo.\n') #Alt+92 --> \n
    archivo.write('Esta es otra linea del archivo.\n')
    
'''
En este ejemplo, el archivo "nuevo_archivo.txt" se abrirá en modo escritura ('w'), lo que significa que si el archivo ya existe, su contenido será eliminado y se comenzará a escribir desde el principio.Sel archivo no existe, se creará uno nuevo

Recuerda que el método "write()" escribe una cadena de caracteres en el archivo.Puedes utilizar caracteres de escape como \n para insertar nuevas líneas

Si deseas agregar contenido al final de un archivo existente sin eliminar su contenido actual, puedes abrir el archivo en modo de escritura y lectura ('w+'). Por ejemplo:
'''

#Abrir el archivo en modo escritura y lectura ('w+')
with open('nuevo_archivo.txt','w+')as archivo:
    #Escribimos el contenido del archivo
    archivo.write('Hola, este es un nuevo archivo.\n')
    archivo.write('Esta es otra línea del archivo.\n')
    
    #Posicionar el puntero al inicio del archivo para leer su contenido
    archivo.seek(0)
    
    #Leer y mostrar el contenido del archivo
    contenido =  archivo.read()
    print(contenido)
    
'''
Al utilizar w+, ten en cuenta que el contenido previo del archivo será reemplazado si ya existía. Si solo deseas agregar contenido al final del archivo, puedes abrirlo en modo de escritura al final ('a').
'''

#Saluds :)
    