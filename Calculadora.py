#Crearemos una calculadora gráfica con Tkinter te permitirá tener una interfaz visual más amigable para el usuario. A continuación te mostraré como hacerla:

#Proyecto 1 :) Que emocion!

import tkinter as tk

#Funcion para agregar el número o operador al campo de entrada
def agregar_numero(numero):
    entrada.insert(tk.END,numero)
    
#Funciones para realizar las operaciones aritmeticas basicas (+,-,* y /
def realizar_operacion():
    try:
        resultado = eval(entrada.get()) #Evalúa la expresión matemática ingresada
        entrada.delete(0,tk.END) #Borra el contenido actual del campo de entrada
        entrada.insert(tk.END,str(resultado))#Muestra el resultado en el campo de entrada
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END,"Error")
        
#Funcion para limpiar el campo de entrada
def limpiar():
    entrada.delete(0,tk.END)
    
#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

#Creamos el campo de entrada 
entrada = tk.Entry(ventana, font=("Arial",20), justify="right")
entrada.grid(row=0,column=0, columnspan=4, padx=10, pady=10)

#Lista de botones con sus respectivos valores y la ubicación en la cuadrícula
botones = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3)    
]

#Creamos los botones y ubicamos en la cuadrícula
for valor, fila , columna in botones:
    boton = tk.Button(ventana,text=valor,font=("Arial",20),command=lambda v=valor: agregar_numero(v))
    boton.grid(row=fila,column=columna,padx=5,pady=6,sticky="nsew")
    
#Creamos el botón para limpiar el campo de entrada
limpiar_boton = tk.Button(ventana,text="C", font=("Arial",20),command=limpiar)
limpiar_boton.grid(row=5,column=0,padx=5,pady=5,columnspan=2,sticky="nsew")

#Crear el botón de igual para obtener el resultado
calcular_boton = tk.Button(ventana,text="=", font=("Arial",20), command=realizar_operacion)
calcular_boton.grid(row=5,column=2,padx=5,pady=5, columnspan=2, sticky="nsew")

#Iniciamos el bucle principal de la aplicación
ventana.mainloop()

'''
Este código crea una interfaz gráfica para una calculadora simple utilizando la biblioteca Tkinter. La calculadora tiene botones numéricos del 0 al 9, botones para las operaciones básicas (+, -, *, /), un botón de punto decimal y un botón de igual para obtener el resultado.

Cuando el usuario hace clic en los botones numéricos y operadores, los números y operadores se muestran en el campo de entrada. Al hacer clic en el botón "=", la calculadora evalúa la expresión matemática ingresada y muestra el resultado en la entrada.

Este es solo un ejemplo básico de una calculadora gráfica con Tkinter. Puedes personalizarla o agregar más funcionalidades según tus necesidades y conocimientos de programación.

Espero que este ejemplo te sea útil y te inspire a seguir explorando y aprendiendo sobre la creación de interfaces gráficas en Python con Tkinter. Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar. ¡Buena suerte con tu proyecto!
'''