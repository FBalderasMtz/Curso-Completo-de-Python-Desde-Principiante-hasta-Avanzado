#Hola denuevo, esta vez aprenderás a imprimir variables de una cadena pero no como normalmente lo hacemos, esta vez tendrá algo especial

#Ejemplo común
nombre ="Eduardo"
print("Buen día "+ nombre) #Esto ya lo sabemos, a esto le llamamo "Concatenación" ----> juntar dos terminos en una impresión

#.format

Nombre = "José" #Aqui la diferiencia de la primer variable a esta es la Mayuscula ten presente eso, recuerda que puedes nombrar a tus variables de modo que tu quieras
edad = 19
print("Hola, mi nombre es {} y tengo {}" .format(nombre ,edad)) #El punto clave de esto es lo siguiente, si te das cuenta lo que sucedió fue que agregamos esos signos que se conocen como "llaves" o al menos yo los conozco asi, si te das cuenta lo dejamos como un espacio de tal modo que, el .format(manda llamar las variables que quieras mostrar en las {} correspondientes que tu pongas en el texto de impresión, esto con el fin de ahorrar espacio)


print("--------------------") #Recuerda, Decoración para separar ejemplos o ejercicios
#En el caso de las Matematicas o operaciones que conllevan mas de 2 decimales puede ocuparse el format para esto

resultado = 10/3
print(resultado)
#De resultado obtenemos #3.333333... etc pero y si te piden que solo ocupes 2 decimales? te muestro
print("El resultado es {r}".format(r=resultado)) #Esto es nuestra primer concatenación ocupando el Format si te das cuenta en vez de poner toda la palabra "resultado" ---> Simplifique a {r} y le dije, r va a ser igual a resultado es decir, es como una declaración de variables dentro de un format, esto con el fin de notar que se pueden ocupar distintas maneras de imprimir los resultados
#Recortar decimales
print("El resultado en 3 decimales es: {r:1.3f}".format(r=resultado)) #Te explico, lo que se llevó acabo aqui fue que a la hora de declarar el r:1.3f ----> r como bien viste es la variable a imprimir, 1.3f ---> 1 entero. 3 decimales que en este caso se representa como la f

#Prosigamos, 
print("--------------------------") #Decoración


#f-strings
nombre = "Ramon"
edad = 29
print(f"Buenos dias {nombre}, felices {edad} años!") #Te explico, las f-strings son una forma más sencilla de comobiar valores de variables y texto en una cadena, Se utilizarán cuando necesites construir cadenas dinámicas con valores variables 

#Nos vemos en el proximo video, Saludos!