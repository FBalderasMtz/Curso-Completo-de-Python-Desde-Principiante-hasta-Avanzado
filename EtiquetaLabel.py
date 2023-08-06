#El componente "Etiqueta" o "Label" es uno de los más comunes en las interfaces graficas con tkinter

#Ejemplo más simple de su creación

import tkinter as tk

ventana_principal = tk.Tk()
ventana_principal.title("Ejemplo de Etiqueta")

etiqueta_texto = tk.Label(ventana_principal, text="¡Hola desde la etiqueta!")
etiqueta_texto.pack(pady=20)

ventana_principal.mainloop()

'''
En este ejemplo, creamos una etiqueta llamada etiqueta_texto y le asignamos el texto "¡Hola desde la etiqueta!" con una fuente de tamaño 16. Luego, utilizamos el método pack() para agregar la etiqueta a la ventana principal (ventana_principal). La propiedad pady se utiliza para agregar un espacio entre la etiqueta y los bordes de la ventana.

Puedes personalizar la apariencia de la etiqueta utilizando diferentes opciones, como el tamaño de la fuente, el color del texto, el color de fondo, entre otros. Además, las etiquetas también pueden contener imágenes en lugar de texto.

Las etiquetas son especialmente útiles para mostrar información al usuario o como elementos descriptivos en la interfaz gráfica.
'''

#Saluds