#En este video me apoyaré de un asistente de audio, conforme el audio me guiaré para que comprendas la teoria

cadena = "HOLA MUNDO" #----> Una cadena como verás puede ser desde una palabra que contiene lo que viene siendo "CARACTERES" es decir, la cantidad de letras que ocupa la palabra incluyendo espacios, es decir, "HOLA MUNDO" puedes contar las letras son9 peroooo, ¿Estas contando el espacio? ¡Claro el espacio tambien se cuenta! y tambien debes empezar a contar en este caso desde 0
print(cadena)

#H O L A   M U N D O ----> Lo que te muestra aqui es las posiciones que ocupan cada caracter(Cada letra) comienza desde el cero hasta el final
#0 1 2 3 4 5 6 7 8 9 ----> Asi para que puedas mirar mejor

print(cadena[5]) #--->¿Esto para que me sirve? ---> Realizas una busqueda especifica es decir en vez de ir contando caracter por caracter tu buscas que caracter ocupa la posición 5 en este caso.
print(cadena[-1]) #Quieres empezar a contar de Derecha a izquierda ¡Claro que se puede! ---> Empezamos lo que viene siendo del -1 dado que lógicamente no existe el -0 no mostraria nada, entonces podemos poner [-7] prueba y verás que letra te muestra

print(cadena[2:7]) #----> Quiero que solo me muestres desde una letra o una palabra despues del inicio, para esto existe este es decir [Inicio:Final] ----> Es decir pides que te muestre caracteres especificos de cierta distancia
print(cadena[2:]) #------> Quiero que me muestres de la posición hasta el final! ---> Claro! para eso existe esto [Inicio: ->>>>>] Hasta donde llegue aun así sean miles de palabras o caracteres

#ERROR
'''cadena[5]= 'p'
print(cadena[5])------> Lo que comentamos aqui fue lo siguiente no puedes modificar la cadena! es decir si quiero que mi "Hola" sea todo en mayusculas, Este no es el metodo correcto para cambiarlo, pero no te preocupes que más adelante lo veremos :)''' 

cadena1 ="Hola"
cadena2 = "Mundo"
cadena3 = " "
cadena= cadena1 + cadena3 + cadena2 
print(cadena) #Esto ya lo sabes ---> Concatenacion, ¿Te suena? Claro que si

#¿Entendiste? Bueno ahora te explico con comentarios

#Ahora si quedó claro? --->Te leeo en los comentarios, cuidate! Saludos