#El componente "RadioButton" es un botón de opción que permite al usuario seleccionar una opción de un conjunto predefinido de opciones.Solo una opcion puede ser seleccionada a la vez en un grupo de botones de opción, lo que significa que si se selecciona una opción, las demás opciones se deseleccionarán automaticamente.

#Deberemos utilizar la clase "RadioButton", cada botón de opcioón se crea como ina instancia y se asocia a una variable de control que almacenará el valor seleccionado.

#Hagamos un ejemplo de crear un grupo de botones de opción con tres opciones "Opcion 1", "Opcion 2" "Opcion3"

import tkinter  as tk

def mostrar_seleccion():
    etiqueta_resultado.config(text="Opción seleccionada: "+ opcion.get())
    
ventana_principal = tk.Tk()
ventana_principal.title("Ejemplo de Radiobutton")

opcion = tk.StringVar()

#Creamos los botones de opción
opcion1 = tk.Radiobutton(ventana_principal, text="Opción 1", variable=opcion, value="Opción 1", command=mostrar_seleccion)
opcion2 = tk.Radiobutton(ventana_principal, text="Opción 2", variable=opcion, value="Opción 2", command=mostrar_seleccion)
opcion3 = tk.Radiobutton(ventana_principal, text="Opción 3", variable=opcion, value="Opción 3", command=mostrar_seleccion)

opcion1.pack()
opcion2.pack()
opcion3.pack()

etiqueta_resultado = tk.Label(ventana_principal, text="", font=("Arial",14))
etiqueta_resultado.pack(pady=10)

ventana_principal.mainloop()

'''
En este ejemplo, creamos tres botones de opción con las etiquetas "Opción 1", "Opción 2" y "Opción 3". Cada botón de opción está asociado a la variable opcion y tiene un valor diferente (en este caso, el texto de la opción).

Cuando el usuario selecciona una opción, se llama a la función mostrar_seleccion() que actualiza el texto de la etiqueta etiqueta_resultado con la opción seleccionada.

Recuerda que solo una opción puede estar seleccionada a la vez en un grupo de botones de opción. Si seleccionas una opción diferente, la selección anterior se deseleccionará automáticamente.
'''

#Saluds :)