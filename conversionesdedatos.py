'''#Bienvenido a un nuevo video, este video tratará de conversiónes de tipos de datos, pero que es esto

#De un valor entero a str o de str a flotante o de str a entero ¿Quieres saber como? Hagamoslo

num1 = 12
print(num1)
print(type(num1)) #Aqui mostrará que sigue siendo de la categoria int 
#A la hora de imprimir una variable puedes darle Diseño a tu código o resultado es decir:
print("****************") #Basicamente es una división de espacios en tu salida de código
cadena = str(num1)#Esta variable almacenará el nuevo cambio que estamos haciendo es decir, aqui mostrará que ya es string es decir un texto ya no un número -----> Para que tu texto se ajuste al tamaño de tu pantalla pon las teclas Alt+Z y se ajustará para que no estes desplazandote toda la pantalla, continuamos
print(cadena)
print(type(cadena))
#Para separar a la hora de imprimir
print("-----------------")
#Float a String
num2 = 163.56
print(num2)
print(type(num2))
cadena=str(num2)
print(cadena)
print(type(cadena))

print("-----------------------")
#String a int
numero3 = "5" #Recuerda que todo "string" -----> Debe llevar comillas de lo contrario se tomará como entero o flotante
print(numero3)
print(type(numero3))
int = int(numero3)
print(int)
print(type(int))

print("*********************")

#String a float
numero4 = "369.14"
print(numero4) #Imprime Número en String
print(type(numero4))
float = float(numero4) #Convierte a Flotante
print(float)
print(type(float))'''


#Flotante a int se podra? Claro que si

f1 = 16.5
entero1 = int(f1)
print("Antes: ", f1)
print("Despues: ", entero1)

#Y al reves? es decir, de entero a flotante, Claro que siiii

print("++++++++++++++++++++") #Recuerda, decoración :)

i1 = 16
f2 = float(i1)
print("Antes: ",i1)
print("Despues: ",f2)

#Como podrás ver a uno se le quita el decimal y al otro continua el decimal

#Dato añadido quiere evitar estar escribiendo "#" esta almoadilla para comentarios la otra alternativa es -----> '''   ''' <----- 3 acentos te harán un multiple comentario de varios textos es decir

'''Texto
Muestra
Aqui podrás seguir escribiendo

Hasta más abajo y no se mostrará nada en el código

Sigueme! Nos vemos en el siguiente video, saludos!'''