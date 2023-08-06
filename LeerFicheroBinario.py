#Para leer un fichero Binario --->Usaremos pickle podemos utilizar el metodo "pickle.load()" junto con la función 'open()' en modo lectura binaria ('rb').

#Ejemplo
import pickle

#Abrir el fichero en modo lectura binaria ('rb') utilizando pickle.load()
with open('lista_binaria.pkl','rb')as archivo:
    lista_datos_cargada = pickle.load(archivo)
print("Lista cargada desde el fichero binario",lista_datos_cargada)

'''
En este ejemplo, hemos abierto el fichero 'lista_binaria.pkl' en modo lectura binaria ('rb') utilizando open() y luego hemos utilizado pickle.load() para cargar el contenido del fichero en la variable 'lista_datos_cargada
Finalmente, imprimimos el contenido de la lista cargada desde el fichero.

Recuerda que pickle.load() carga el contenido del fichero en la misma estructura de datos que se grabó previamente, en este caso, la lista lista_datos. Si el fichero contiene otro tipo de objeto, asegúrate de utilizar el tipo de objeto correcto al cargar el contenido.

También, ten en cuenta que cuando utilizas pickle para grabar y leer ficheros binarios, es importante tener cuidado con la seguridad, ya que pickle puede ejecutar código malicioso si se carga un fichero de origen no confiable. Por lo tanto, solo debes cargar ficheros binarios que provengan de fuentes seguras y confiables.
'''

#Toda esta documentación que te muesto de copiar y pegar, hace enfasis a lo que viene siendo documentación directa de python

#Saluds :)