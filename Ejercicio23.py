'''EJERCICIO 23
Crear una base de datos "basededatos.db"
Crear una tabla de "productos" con 3 campos
    id : Identificador del producto de tipo numérico
    nombre: Nombre del producto de tipo texto
    precio: Precio del producto de tipo numérico

Insertar 3 productos en la tabla "productos"
    1,"Impresora",300
    2,"Ratón",20
    3,"Ordenador",600
    
Consultar los productos de la tabla "productos"
Cerrar la Base de datos "base de datos.db"
'''

#Solución
'''
import sqlite3

conexion = sqlite3.connect("Ejercicio23.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PRODUCTOS(ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")
conexion.commit()
cursor.execute("INSERT INTO PRODUCTOS VALUES (1,'IMPRESORA',300)")
conexion.commit()
cursor.execute("INSERT INTO PRODUCTOS VALUES(2,'RATON',20)")
conexion.commit()
cursor.execute("INSERT INTO PRODUCTOS VALUES(3,'ORDENADOR',600)")
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
    
#El error era en la creacion del archivo, te muestro el segúndo ejemplo o forma de resolverlo
'''

import sqlite3

conexion = sqlite3.connect("basededatos.db")
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    precio REAL)''')

productos_a_insertar = [
    (1,"Impresora",300),
    (2,"Ratón",20),
    (3,"Ordenador",600)
]

cursor.executemany("INSERT INTO productos (id,nombre,precio) VALUES (?,?,?)", productos_a_insertar)
conexion.commit()

#Consultar los productos de la tabla "productos"
cursor.execute("SELECT * FROM productos")
productos_consultados = cursor.fetchall()
print("Productos en la tabla 'productos: '")
for producto in productos_consultados:
    print("ID:", producto[0])
    print("Nombre: ", producto[1])
    print("Precio: ", producto[2])
    print()
conexion.close()

#Mejor no crees

'''
Este código creará la base de datos "basededatos.db", la tabla "productos" y realizará las inserciones correspondientes. Luego, consultará los productos y los imprimirá en la consola. Finalmente, cerrará la conexión con la base de datos.
'''

#Nos vemos en el proximo video Saluds