import moduloficheros

nombre_fichero = 'fichero1.txt'
fichero = moduloficheros.Fichero(nombre_fichero)

texto = 'Esta es la primera fila del fichero.\n Esta será la segunda fila.'
fichero.grabar_fichero(texto)

texto = '\n Este es un texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)

#Saluds