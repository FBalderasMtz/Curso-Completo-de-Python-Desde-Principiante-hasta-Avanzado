#Ejercicio de análisis de datos utilizando SQLite en Python. En este ejercicio, crearemos una base de datos SQLite que contendrá información sobre empleados, y realizaremos algunas consultas para analizar los datos. Supongamos que tenemos la siguiente información sobre los empleados:
'''
Nombre
Edad
Puesto
Salario
Puedes utilizar la siguiente base de datos SQLite para realizar el análisis'''

import sqlite3

# Conectamos a la BD o creamos si no existe
conn = sqlite3.connect("Empleados.db")

# Creamos una tabla para almacenar la información de los empleados
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Empleados(
                id INTEGER PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Edad INTEGER,
                Puesto TEXT,
                Salario REAL)''')

# Insertamos datos de ejemplo en la tabla
empleados = [
    ('Juan Perez', 30, 'Analista', 45000.0),
    ('María López', 28, 'Desarrollador', 55000.0),
    ('Carlos Gómez', 35, 'Gerente', 75000.0),
    ('Ana Torres', 25, 'Asistente', 35000.0)
]

cursor.executemany('INSERT INTO Empleados(nombre, edad, puesto, salario) VALUES (?,?,?,?)', empleados)

# Obtener la cantidad total de empleados
cursor.execute('SELECT COUNT(*) FROM Empleados')
total_empleados = cursor.fetchone()[0]
print(f"Cantidad total de empleados: {total_empleados}")

# Obtener el salario promedio de los empleados
cursor.execute('SELECT AVG(salario) FROM Empleados')
promedio_salario = cursor.fetchone()[0]
print(f"Salario promedio de los empleados: {promedio_salario}")

# Obtener el empleado con el salario más alto
cursor.execute('SELECT nombre, salario FROM Empleados ORDER BY salario DESC LIMIT 1')
empleado_salario_mas_alto = cursor.fetchone()
print(f"Empleado con el salario más alto: {empleado_salario_mas_alto[0]}, Salario: {empleado_salario_mas_alto[1]}")

# Obtener todos los empleados con un salario mayor a 50000
cursor.execute('SELECT nombre, salario FROM Empleados WHERE salario > 50000')
empleados_salario_mayor_50000 = cursor.fetchall()
print("Empleados con salario mayor a 50000:")
for empleado in empleados_salario_mayor_50000:
    print(f"{empleado[0]}, Salario: {empleado[1]}")

# Cerrar la conexión a la BD
conn.close()
