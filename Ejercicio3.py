'''
Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
Según la posición de cada letra en la cadena, Calcular los valores (x,y) hay que poner para seleccionar solo la palabra "texto"
cadena [x:y] = "texto"
'''

cadena = "Esto es un texto de ejemplo" #Declaramos nuestra cadena hasta ahi todo bien
print(cadena) #Hacemos una impresión simple
#Contamos los caracteres es decir de "Esto es un texto de ejemplo" ----> El ejercicio nos pide que imprimamos solo "texto" entonces "x" ---> Viene siendo el inicio de izquierda a derecha y "y" ----> Viene siendo de continuando de izquierda, contamos los carateres RECUERDA QUE SE CUENTA DESDE 0 EN ADELANTE, por eso pusimos el 11 y llegamos al 16 por que se cuenta el espacio adicional es decir se contó hasta donde terminó la letra

print("Resultado: ")
print(cadena[11:16])#Mandamos imprimir especificaciones ----> 

#¿Dudas? JAJA si, ok te explico, Si aun tienes dudas dejamelos en los comentarios y con gusto te apoyo, SALUDOS!