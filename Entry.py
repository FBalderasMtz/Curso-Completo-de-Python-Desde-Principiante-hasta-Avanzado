#El componenten "Entry" O "Entrada" en tkinter es utilizado para obtener datos de entrada del usuario através del teclado, Es basicamente un campo de texto en el que el usuario puede escribir información
#Para crear una entrada en tkinter, se utiliza la clase 'Entry'. A continuación, te mostraré un ejemplo de cómo crear una entrada y agregarla a una nueva ventana:

import tkinter as tk

def obtener_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text="Texto ingresado: "+texto)
    
#Creamos la ventana principal (componente raiz)
ventana_principal = tk.Tk()
ventana_principal.title("Ejemplo de Entry")

entrada = tk.Entry(ventana_principal,width=30,font=("Arial,12"))
entrada.pack(pady = 20)

boton_obtener = tk.Button(ventana_principal, text="Obtener Texto", command=obtener_texto)
boton_obtener.pack()

etiqueta_resultado = tk.Label(ventana_principal, text="", font=("Arial",14))
etiqueta_resultado.pack(pady=10)

ventana_principal.mainloop()

'''
En este ejemplo, creamos una entrada llamada entrada con un ancho de 30 caracteres y una fuente de tamaño 12. Luego, creamos un botón llamado boton_obtener que ejecuta la función obtener_texto() cuando se hace clic en él. La función obtener_texto() obtiene el texto ingresado en la entrada y lo muestra en la etiqueta etiqueta_resultado.

Cuando el usuario ingrese datos en la entrada y haga clic en el botón "Obtener texto", el texto ingresado se mostrará en la etiqueta como resultado.

Las entradas son especialmente útiles cuando necesitas que el usuario proporcione información en un formulario o cuando necesitas obtener datos de entrada para realizar alguna operación en la interfaz gráfica.
'''

#Saluds