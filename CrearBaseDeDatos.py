#Trabajaremos con una Base de Datos SQLite en Python, para estp es necesario importar el módulo 'sqlite3' y no es necesario instalar una Base de Datos, por ejemplo, SQL Server, Mongo, DB Browser for SQLite.

#Veamos un ejemplo de cómo crear una Base de Datos SQLite, crear una tabla y realizar operaciones básicas como insertar, actualizar, eliminar registros utilizando el módulo 'sqlite3' en Python:

import sqlite3

#Conectar a la BD(Base de Datos) o crear una nueva si no existe
conexion = sqlite3.connect("mi_base_de_datos.db")

#Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

#Crear una tabla (si no existe) para almacenar la información de las Personas
cursor.execute('''CREATE TABLE IF NOT EXISTS personas(
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER)''')

#Insertar datos en la tabla
cursor.execute("INSERT INTO personas(nombre,edad)VALUES('JUAN',30)")
cursor.execute("INSERT INTO personas(nombre,edad)VALUES ('María',25)")

#Actualizar un registro
cursor.execute("UPDATE personas SET edad = 26 WHERE nombre = 'María'")

#Eliminar un registro
cursor.execute("DELETE FROM personas WHERE nombre = 'Juan'")

#Guardar los cambios y cerrar la conexión

conexion.commit()
conexion.close()

#EXPLICACIÓN

'''
En este ejemplo, se crea una base de datos llamada "mi_base_de_datos.db" (o se conecta a ella si ya existe). Luego, se crea una tabla llamada "personas" con tes columnas: "id"(clave primaria), "nombre" y "edad". Se insertan dos registros en la tabla, uno para Juan y otro para María.Después, se actualiza el valor de la edad de María y se elimina el registro de Juan.Finalmente, se guardan los cambios y se cierra la conexión a la base de datos.

Browser es una herramienta para visualizar la base de datos SQLite pero en este caso, no es esencial, primero por que ya podemos trabajar desde Python,Poremos realizar operaciones CRUD(Crear,Leer,Actualizar,Eliminar) directamente desde Python utilizando el módulo 'sqlite3'

Como podrás ver en la barra izquierda existen las extensiones, en videos anteriores te mostré alguna de ellas, entonces en este caso, para eviar descargar y ver las previsualizaciones, descargué esas extensiones que te mostré para evitar tanto manejo de otras aplicaciones.
'''

#Saluds ;)