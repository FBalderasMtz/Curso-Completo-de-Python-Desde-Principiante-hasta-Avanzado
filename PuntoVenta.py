import tkinter as tk
import sqlite3

# Crear una conexión con la base de datos
conexion = sqlite3.connect('punto_venta.db')
cursor = conexion.cursor()

# Crear tabla de productos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio REAL,
        stock INTEGER
    )
''')
conexion.commit()

# Función para agregar un producto a la base de datos
def agregar_producto():
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())
    stock = int(entry_stock.get())

    # Verificar si el producto ya está en la base de datos
    cursor.execute('SELECT * FROM productos WHERE nombre = ?', (nombre,))
    producto_existente = cursor.fetchone()

    if producto_existente:
        mensaje_aviso.config(text=f"El producto '{nombre}' ya se encuentra en la base de datos.")
    else:
        # Agregar el producto a la base de datos
        cursor.execute('INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)', (nombre, precio, stock))
        conexion.commit()
        mostrar_productos()
        mensaje_aviso.config(text="Producto agregado correctamente.")

# Función para mostrar todos los productos en la lista
def mostrar_productos():
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    for producto in productos:
        lista_productos.insert(tk.END, f"{producto[1]} - Precio: {producto[2]} - Stock: {producto[3]}")

# Función para eliminar un producto de la base de datos
def eliminar_producto():
    seleccionado = lista_productos.curselection()
    if seleccionado:
        indice = seleccionado[0]
        producto = lista_productos.get(indice)
        nombre = producto.split(" - ")[0]
        cursor.execute('DELETE FROM productos WHERE nombre = ?', (nombre,))
        conexion.commit()
        mostrar_productos()
        mensaje_aviso.config(text="Producto eliminado correctamente.")
    else:
        mensaje_aviso.config(text="Selecciona un producto para eliminar.")

# Función para buscar productos por nombre
def buscar_producto():
    nombre_buscar = entry_buscar.get()
    cursor.execute('SELECT * FROM productos WHERE nombre LIKE ?', (f"%{nombre_buscar}%",))
    productos_encontrados = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    if productos_encontrados:
        for producto in productos_encontrados:
            lista_productos.insert(tk.END, f"{producto[1]} - Precio: {producto[2]} - Stock: {producto[3]}")
    else:
        mensaje_aviso.config(text="No se encontraron productos.")

# Función para actualizar la tabla de productos
def actualizar_tabla():
    mostrar_productos()
    mensaje_aviso.config(text="Tabla actualizada.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Punto de Venta")

# Campos de entrada para agregar productos
label_nombre = tk.Label(ventana, text="Nombre del producto:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_precio = tk.Label(ventana, text="Precio:")
label_precio.pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

label_stock = tk.Label(ventana, text="Stock:")
label_stock.pack()
entry_stock = tk.Entry(ventana)
entry_stock.pack()

# Botón para agregar producto
boton_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
boton_agregar.pack()

# Lista de productos
lista_productos = tk.Listbox(ventana, width=50)
lista_productos.pack()

# Botón para eliminar producto
boton_eliminar = tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto)
boton_eliminar.pack()

# Campos de entrada y botón para buscar productos
label_buscar = tk.Label(ventana, text="Buscar producto:")
label_buscar.pack()
entry_buscar = tk.Entry(ventana)
entry_buscar.pack()
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_producto)
boton_buscar.pack()

# Botón para actualizar la tabla de productos
boton_actualizar = tk.Button(ventana, text="Actualizar Tabla", command=actualizar_tabla)
boton_actualizar.pack()

# Mensaje de aviso
mensaje_aviso = tk.Label(ventana, text="", fg="red")
mensaje_aviso.pack()

# Mostrar productos al inicio
mostrar_productos()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

# Cerrar la conexión con la base de datos al cerrar la aplicación
conexion.close()
