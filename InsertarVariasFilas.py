#Para insertar varias filas a la vez en una tabla de SQLite utilizando Python, puedes utilizar el nétodo executemany() junto con una lista de tuplas que contengan los valores de cada fila que deseas insertar.

import sqlite3

# Conectar a la base de datos o crear una nueva si no existe
conexion = sqlite3.connect("mi_base_de_datos.db")

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Sentencia SQL para insertar varias filas en la tabla "productos"
sentencia_insertar = "INSERT INTO productos (nombre, precio) VALUES (?, ?)"

# Lista de tuplas con los valores de las filas que deseas insertar
productos_a_insertar = [
    ("Camiseta", 25.99),
    ("Pantalón", 39.99),
    ("Zapatos", 49.99),
]

# Ejecutar la sentencia SQL con la lista de tuplas de valores
cursor.executemany(sentencia_insertar, productos_a_insertar)

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

#EXPLICACIÓN.

#HICE ESO PARA QUE REVISES DENUEVO EL ERROR EN CASO DE QUE TE MARQUE

'''
En este ejemplo, estamos insertando tres filas en la tabla "productos" de una sola vez utilizando el método 'executemany()' Cada fila está representada por una tupla en la lista 'productos_a_insertar' y cada tupla contiene el nombre y el precio de un producto.

Al utilizar 'executemany()' la operación de inserción es más eficiente y rápida que hacer varias inserciones individuales, ya que se realiza en una sola trasacción.
'''

#Nos vemos en el siguiente video Saluds :)