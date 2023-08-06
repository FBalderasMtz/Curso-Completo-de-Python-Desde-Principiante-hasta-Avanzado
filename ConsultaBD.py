#Continuamos con la Consulta de Datos en una Base de Datos SQLite utilizando Python es una operación fundamental para obtener información almacenada previamente.SQLite es una base de datos incorporada en Python, lo que significa que podemos interactuar con ella sin necesidad de instalar un servidor de Base de Datos adicional.

import sqlite3

#Conectar a la base de datos o crear una nueva si no existe
conexion = sqlite3.connect("mi_base_de_datos.db")

#Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

#Ejecutar una consulta SQL para obtener todos los datos de la tabla "productos"
cursor.execute("SELECT * FROM productos")

#Recuperar los datos mediante fetchall()
datos = cursor.fetchall()

#Utilizamos un bucle for para recorrer los resultados
for fila in datos:
    id_producto, nombre_producto, precio_producto = fila
    print(f"ID: {id_producto}, Nombre: {nombre_producto}, Precio:{precio_producto}")
    
#Cerramos la conexión
conexion.close()

'''
En este ejemplo, se realiza una consulta SELECT para obtener todos los datos de la tabla "productos". Luego, se recorren los resultados utilizando un bucle 'for' para imprimir la información de cada fila.

Recuerda que las consultas SQL pueden variar según tus necesidades y requerimientos específicos. Puedes utilizar cláusulas WHERE, ORDER BY, LIMIT y otras para filtrar, ordenar y limitar los resultados según tus criterios.

'''

#Saluds