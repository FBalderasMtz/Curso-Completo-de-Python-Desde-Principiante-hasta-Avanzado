#Te explico, todo lenguaje de programación tienen a usar variables de diferentes tipos aqui te muestro en breve cuales son y para que se usan :)

#Primero tendremos los valores Enteros es decir, cualquier numero que no tenga punto decimal
#Para declarar una variable en Python solo se pone ----> NombreDeLaVariable = Valor de la Variable 
#Por ejemplo

num = 1 #-----> Esto es una variable de tipo ENTERO 
#Para saber el valor de cada variable tenemos la opcion de "type()" ----> Te muestro como se usa
print(num) #-----> Imprimimos el valor que se almacenó en la variable nombrada "num" como resultado debemos obtener el valor asignado en este caso 1
#Ocupemos el type()
print(type(num)) #-----> Si notas la estructura denota que es primero imprimir(type(nombre de la variable))

cadena = "Esto es de valor String" #Esto es un valor String es decir para todo tipo de palabras o textos -----> En python lo denotará como str
#Mandas a imprimir o mandas a llamar a la variable para que te muestre el resultado, hazlo conmigo
print(cadena)
#De paso imprimimos el type para ver que nos arroja
print(type(cadena))

#IMPORTANTE -----> PRESIONA CTRL+S PARA GUARDAR CAMBIOS Y SE EJECUTE EN CONSOLA DE LO CONTRARIO TE SEGUIRÁ MOSTRANDO LO MISMO QUE HICISTE AL COMIENZO Y ASI SE VAYA ACTUALIZANDO CONSTANTEMENTE DE IGUAL PUEDES PONER EL AUTOSAVE PARA AUTOGUARDAR LO QUE VIENE SIENDO TODO LO QUE VAS REGISTRANDO EN TU CÓDIGO

#ERRORES EN PYTHON
#PARA DECLARAR UNA VARIABLE YA SEA ENTERO, STRING, FLOAT, BOOLEAN, ETC DEBES TENER EN CUENTA LA SIGUIENTE ESTRUCTURA ----> VARIABLE COMIENZA CON MINUSCULA, NO DEBE EMPEZAR CON ALGUN NUMERO O CARACTERER ESPECIAL ES DECIR 

num = 6 #Nisiquiera deja imprimir o ejecutar por que es un error de sintaxis dado que es invalido a la hora de programar "5num ---> Error 1, Error 2 ----> @drian = 6" de igual no puedes usar espacios en la declaración de variables es decir 
nombre_completo = "José" #Si te das cuenta muestra un error el cual no te permite nisiquiera corregir dado que muestra un error, para corregir este error debes tener en cuenta que si vas a ocupar un nombre largo de declaración de variable será con un "_" guión bajo;

#Por ultimo -----> Existe algo que se le llama "Concatenación es decir juntar 2 variables o el resultado de dos variables es decir"

var1 = "Hola"
var2 = " Mundo" #Dejamos un espacio para que a la hora de imprimir no se junten las palabras es decir
resultado = var1 + var2
print(resultado)#Esta es una forma
print(var1 ,var2) #Para separar variables se usa la "," ya sea para numeros o palabras o cualquier dato 

#NOS VEMOS EN EL SUGUIENTE VIDEO, SALUDOS