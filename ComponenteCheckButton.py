#El componente Checkbutton es un boton de verificación que permite al usuario seleccionar una o varias opciones, de un conjunto predefinido de opciones. A diferiencia de los botones de opción (Radiobutton), los botones de verificación pueden tener múltiples selecciones al mismo tiempo.

import tkinter as tk

def mostrar_seleccion():
    seleccion=[]
    if opcion1_var.get():
        seleccion.append("Opción 1")
    if opcion2_var.get():
        seleccion.append("Opción 2")
    if opcion3_var.get():
        seleccion.append("Opción 3")

    etiqueta_resultado.config(text="Opciones seleccionadas: "+", ".join(seleccion))

ventana_principal = tk.Tk()
ventana_principal.title("Ejemplo de Checkbutton")

opcion1_var = tk.BooleanVar()
opcion2_var = tk.BooleanVar()
opcion3_var = tk.BooleanVar()

opcion1 = tk.Checkbutton(ventana_principal, text="Opción 1", variable =opcion1_var, command= mostrar_seleccion)
opcion2 = tk.Checkbutton(ventana_principal, text="Opción 2", variable =opcion2_var, command= mostrar_seleccion)
opcion3 = tk.Checkbutton(ventana_principal, text="Opción 3", variable =opcion3_var, command= mostrar_seleccion)

opcion1.pack()
opcion2.pack()
opcion3.pack()

etiqueta_resultado = tk.Label(ventana_principal, text="",font=("Arial",14))
etiqueta_resultado.pack(pady=10)

ventana_principal.mainloop()

'''
En este ejemplo, creamos tres botones de verificación con las etiquetas "Opción 1", "Opción 2" y "Opción 3". Cada botón de verificación está asociado a una variable de control (opcion1_var, opcion2_var, opcion3_var) que almacena un valor booleano (True si está seleccionado y False si no lo está).

Cuando el usuario selecciona una opción, se llama a la función mostrar_seleccion() que verifica qué botones de verificación están seleccionados y actualiza el texto de la etiqueta etiqueta_resultado con las opciones seleccionadas.

Recuerda que los botones de verificación pueden tener múltiples selecciones al mismo tiempo, a diferencia de los botones de opción que solo permiten una selección.
'''

#Saluds :)