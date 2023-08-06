#Para actualizar datos en una tabal SQLite usaremos UPDATE en una consulta SQL, nos permitirá modificar los valores de uno o varios registros que cumplan con una condición especifica.

#En este ejemplo actualizaremos el precio de un producto en la tabla "productos" donde el nombre del producto sea "Camiseta"

import sqlite3

conexion = sqlite3.connect("mi_base_de_datos.db")
cursor = conexion.cursor()
nuevo_precio = 29.99
cursor.execute("UPDATE productos SET precio = ? WHERE nombre = 'Pantalón'",(nuevo_precio,))
conexion.commit()
conexion.close()

#Cometí un error el cual creo que fue claro, de principio faltaba la "," más aparte, en el video anterior habiamos elimiando el archivo "Camisa" en todo caso, en este caso para darle un nuevo formato a los datos existentes, podemos hacerlo con Pantalón que aqui se muestra claramente.

'''
En este ejemplo, utilizamos la cláusula UPDATE con la condición WHERE para especificar que queremos actualizar el precio del producto con nombre "Camiseta" con el nuevo precio de 29.99. Utilizamos el símbolo "?" para indicar que el valor del nuevo precio se pasará como parámetro en forma de tupla al método execute(). Esto se hace para evitar posibles ataques de inyección de SQL y mantener la seguridad de la base de datos.

Es importante destacar que al utilizar la cláusula UPDATE, los registros existentes se modifican y los datos antiguos serán reemplazados por los nuevos valores.

Recuerda que siempre es recomendable tener cuidado al actualizar datos y asegurarte de que realmente deseas realizar los cambios. Siempre es aconsejable hacer una copia de seguridad de la base de datos antes de realizar operaciones de actualización masiva, para evitar la pérdida de datos importantes.
'''