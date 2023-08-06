#Hola Nuevamente ocupare asistente de voz, y al final te explicaré a detalle, ¡Vamos!

#Funciones de cadenas

cadena ="Hola Mundo"
print("Te muestro la longitud de la cadena:",len(cadena), "\n") #Ocupamos "len" ---> Para medir la longitud de la cadena es decir, cuantos caracteres contiene nuestra cadena por ejemplo

texto = "¡No se por que aun no me sigues si estas aprendiendo!"  #-----> Verás como todo caracter esta contando
print("Este texto contiene:",len((texto)),"caracteres\n") #-----> Es importante poner las comas para separar variables recuerda eso

#Convertir cadena a Mayusculas
cadena = cadena.upper() #Convierte en mayusculas aqui lo que estas haciendo es asignar una nueva funcion a la variable cadena es decir -----> cadena ----> va a pasar a todas las letras o caracteres de lo que contenga cadena lo pondrás en MAYUSCULAS
print("Este es un ejemplo de conversion de Hola mundo a ----->",cadena , "\n") #Aqui comprobamos que haya hecho los cambios correspondientes, la diferiencia es que a la hora de mandar llamar la variable, mandas llamar lo que viene siendo la estructura de tu código, es decir llamas a la ultima modificación de tu codigo, es decir, toma el original, perooooo ----> Realiza esa modificación

cadena = cadena.lower() #Las pone todas las letras en Minuscula
print("Esta cadena mostrará un HOLA MUNDO en ----->", cadena, "<----- minusculas \n") #Mandas llamar la funcion el cambio recien creado

cadena= cadena.split() #Separa la cantidad de palabras concretas que contiene la variable original de "cadena"
print("Este ejemplo es de separar por palabras la cadena --->",cadena, "\n") #En este caso debe mostrar ['hola','mundo']

cadena2 = "uva, pera, manzana, naranja" #Aqui le estamos asignando una nueva lista, en este caso frutas
cadena2= cadena2.split(",") #Damos la instruccion de que cada palabra separada o almacenada que es separada por una "," la separe por posiciones concretas es decir, las almacene por diferentes tipos y las muestre o separe cada una de ellas en posiciones netas en un par de '  ',  '  '
print("Este ejemplo muestra la separación de cada fruta dentro de la lista -----> ",cadena2)

#Una vez elaborado esto, explicamos todo -----> Demos estetica para cada una de las variables que trabajamos

#NOS VEMOS EN EL SIGUIENTE VIDEOS, SALUDOS!