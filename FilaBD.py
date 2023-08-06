#Para insertar una fila en una tabal de SQLite utilizando Python, debemos seguir la siguiente estructura
'''
1.Conectamos a la BD o Creamos una si no existe
2.Creamos un cursor para interactuar con la BD
3.Utilizamos la sentencia SQL 'INSERT INTO' para agregar una nueva fila a la tabla.
4.Utilizar el método 'execute()' para ejecutar la sentencia SQL y pasar los valores que deseas insertar en la fila.
5.Utilizar el métood 'commit()' para guardar los cambios en la BD
6.Cerrar la conexión con el método 'close()'
'''

#Ejemplo de como hacerlo
import sqlite3

#Conectar a la BD o Creamos
conexion = sqlite3.connect("mi_base_de_datos.db")

#Creamos un cursor para interactuar con la BD
cursor = conexion.cursor()

#Sentencia SQL para insertar una nueva fila en la tabla "productos"
sentencia_insertar = "INSERT INTO productos(nombre,precio) VALUES (?,?)"

#Valores de la nueva fila que deseas insertar
nombre_producto = "Camiseta"
precio_producto = 25.99

#Ejecutar la sentencia SQL con los valores proporcionados
cursor.execute(sentencia_insertar,(nombre_producto,precio_producto))

#Guardamos los cambios y cerramos la conexión
conexion.commit()
conexion.close

#EXPLICACIÓN

'''
En este ejemplo, estamos insertando una nueva fila en la tabla "productos" con el nombre "Camiseta" y el precio de "25.99". Nota que utilizamos el simbolo de '?', en la sentencia SQL para indicar que los valores serán pasados como parámetros en forma de tupla al método execute(). Esto se hace para evitar posibles ataque de inyección de SQL y mantener la seguridad de la BD.
'''

#Saluds :)