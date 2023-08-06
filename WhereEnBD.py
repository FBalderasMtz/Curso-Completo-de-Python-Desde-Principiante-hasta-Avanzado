#Para realizar una consulta con la cláusula WHERE en una BD SQLite usando Python, necesitamos seguis los mimos pasos, agregando la condición WHERE a la consulta SQL.

'''
La clausula WHERE se utiliza para filtrar los resultados de la consulta según ciertos criterios. Por ejemplo, si deseamos trabajar o obtener solo los registros que cumplan con una determinada condición, como aquellos que tengan un precio mayor a cierto valor, puedes usar WHERE para lograrlo

Veamos en este ejemplo una consulta de WHERE para obtener los productos que tengan un precio mayor a $30
'''

import sqlite3

#Conectamos la BD
conexion = sqlite3.connect("mi_base_de_datos.db")

#Creamos un cursor par ainteractuar con la BD
cursor = conexion.cursor()

#Ejecutamos la consulta SQL con WHERE para obtener los productos mayores a $30
cursor.execute("SELECT * FROM productos WHERE precio > ?",(30,))

#Recuperamos los datos mediante fetchall()
datos = cursor.fetchall()

#Usamos un bucle for para recorrer los resultados
for fila in datos:
    id_producto, nombre_producto, precio_producto = fila
    print(f"ID: {id_producto}, Nombre: {nombre_producto}, Precio: {precio_producto}")
    
#Cerrar la conexión
conexion.close()

'''
En este ejemplo, usamos el símbolo de interrogación (?) en la consulta para indicar el valor del precio será como un parametro en forma de tupla al método 'execute()'. Esto es una medida de seguridad para eviar ataque de inyección SQL y asegurarnos de que la consulta sea correcta.

La consulta buscará en la tabla "productos" aquellos registros cuyo precio sea mayor a $30 y luego imprimirá la información de cada fila que cumpla con la condición.

Puedes utilizar diferentes operadores (>, <, >=, <=, =, etc.) en la cláusula WHERE para realizar consultas más complejas según tus necesidades.

Espero que esta explicación te haya sido útil. Si tienes más preguntas o necesitas más ayuda, no dudes en preguntar. ¡Saludos!
'''

