#El componente "text" se utiliza para crear campos de entrada de texto de varias líneas en los que el usuario puede escribir y editar información. A diferiencia de Entry permite solo una linea de entreda de texto, el componente "Text" permite múltiples lineas de Texto, lo que hace ideal para capturar texto más largo o para crear un área de texto más grande donde el usuario pueda escribir libremente.

#El componente "Text" es similar a un editor de texto en el que el usuario puede ingresar y editar texto con facilidad. Puedes definir el número de filas y columnas para determinar el tamaño del área de texto que se mostrará. Además, puedes agregar barras de desplazamiento (scrollbars) para facilitar la navegación en el texto si el contenido es más grande que el área visible.

#Ejemplo de Text:

import tkinter as tk
def obtener_texto():
    texto = texto_entrada.get("1.0", tk.END)
    etiqueta_resultado.config("Texto ingresado:\n"+texto)
    
#Creamos la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ejemplo de Text")

#Creamos el componente Text con scrollbars
scrollbar_vertical = tk.Scrollbar(ventana_principal)
scrollbar_horizontal = tk.Scrollbar(ventana_principal,orient=tk.HORIZONTAL)
texto_entrada = tk.Text(ventana_principal, wrap= tk.NONE,
                        yscrollcommand= scrollbar_vertical.set , 
                        xscrollcommand= scrollbar_horizontal.set,
                        width=30, height=10, font=("Arial",12))

#Configuramos los scrollbars para que estén vinculadas al componente Text
scrollbar_vertical.config(command=texto_entrada.yview)
scrollbar_horizontal.config(command=texto_entrada.xview)

#Agregamos los scrollbars y el componente y el componente Text a la ventana principal
texto_entrada.grid(row = 0, column=0)
scrollbar_vertical.grid(row=0 ,column=1,sticky=tk.NS)
scrollbar_horizontal.grid(row=1,column=0,sticky=tk.EW)

#Creamos un botón para obtener el texto ingresado
boton_obtener = tk.Button(ventana_principal, text = "Obtener Texto", command=obtener_texto)
boton_obtener.grid(row = 2,column = 0, pady=10)

#Creamos una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana_principal, text="", font=("Arial",14))
etiqueta_resultado.grid(row=3,column=0,pady=10)

ventana_principal.mainloop()

'''
En este ejemplo, creamos una ventana principal llamada "ventana_principal" utilizando "tkinter.Tk()". Luego, creamos un componente "Text" llamado "texto_entrada" con scrollbars tanto vertical como horizontal para permitir el desplazamiento del contenido del área de texto.

El componente "Text" se configura con un ancho de 30 caracteres y una altura de 10 líneas. También se establece una fuente de tamaño 12 para el texto.

El texto ingresado en el componente "Text" se obtiene mediante el método "get()" con los argumentos "1.0" (que significa línea 1, carácter 0) y "tk.END" (que representa el final del texto). Esto permite obtener todo el texto ingresado en el componente "Text".

Cuando el usuario hace clic en el botón "Obtener Texto", el texto ingresado se muestra en la etiqueta "etiqueta_resultado" como resultado.

El componente "Text" es especialmente útil cuando se requiere una entrada de texto más extensa o cuando se necesita que el usuario proporcione comentarios, descripciones largas o cualquier texto más extenso que no se ajuste en un solo campo de entrada.

Espero que este ejemplo te sea útil para comprender cómo utilizar el componente "Text" en tkinter para obtener y mostrar datos de entrada de varias líneas del usuario. Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar. ¡Saludos! :)
'''