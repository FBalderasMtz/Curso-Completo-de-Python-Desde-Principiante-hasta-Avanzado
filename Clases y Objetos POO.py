'''
Clases y Objetos (Programación Orientada a Objetos- POO):

La programación Orientada a Objetos (POO) es un paradigma de programación que se basa en el concepto de "objetos". Un objeto es una instancia de una clase, y una clase es una plantilla o modelo para crear objetos. la POO se enfoca en organizar el código en objetos que interactuan entre sí para realizar tareas especificas.

Clase: Una calse es una estructura que define un conjunto de atributos y métodos que representan las caraterísticas y comportamientos de un tipo de objeto. Es como un plano o una plantilla para crear objetos. Los atributos son variables que almacenan datos y los métodos son funciones que definen las acciones que puede realizar el objeto.

Por ejemplo, una clase "Persona" puede tener atributos como "nombre", "edad", y "género" y métodos como "saludar" o "cumplir años"

Objeto: Un objeto es una instancia de una clase, es una varible que se crea utilizando una plantilla de la clase. Cada objeto tiene sus propios valores, para los atributos y puede invocar los métodos definidos en la clase.

Por ejemplo, si creamos un objeto llamado "persona1" apartir de la clase "Persona", podríamos acceder a sus atrubutos como "persona1.nombre" o invocar sus metodos como "persona1.saludar()"

'''

#Ejemplo de Clase y Objeto:

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
#Crear objetos apartir de la clase persona

persona1 =  Persona("Juan",20)
persona2 = Persona("Maria",35)

#Acceder a los atributos y métodos de los objetos

print(persona1.nombre) #Imprimirá "Juan"
print(persona2.edad) #Imprimirá 20

persona1.saludar() #Imprime "Hola mi nombre es Juan y tengo 20 años"
persona2.saludar() #Imprimirá "Hola mi nombre es Maria y tengo 25 años"

'''
Te explico, Este ejemplo, define la clase "Persona" con los atributos "nombre" y "edad" y asi como el metodo "saludar". Luego se crean dos objetos "persona1" y "persona2" a partir de la calse "persona". Cada objeto tiene sus propios valores para los atributos, y pueden invocar el método "saludar" para imprimir un mensaje personalizado
'''

#Saludos :)