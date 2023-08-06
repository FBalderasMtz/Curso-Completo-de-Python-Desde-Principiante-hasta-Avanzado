'''Ejercicio 17
Crear una clase "Coche" que tenga estos atributos:
Marca,Color,Combustible, y cilindrada
Crear la funcion "__init__" que asigna los parametros de la clase a los atributos de la clase
Crear otra función "mostrar_caracteristicas" que mediante print muestre por pantalla las caraterísticas (o atributos) que tiene el coche
Crear un objeto "coche1" de la clase "Coche" con los atributos "Opel","rojo","gasolina","1.6"
Ejecutar la función "mostrar_caracteristicas" del objeto "coche1"
'''

#Solución

class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print("Características del coche:")
        print("Marca:", self.marca)
        print("Color:", self.color)
        print("Combustible:", self.combustible)
        print("Cilindrada:", self.cilindrada)

coche1 = Coche("Opel", "rojo", "gasolina", "1.6")
coche1.mostrar_caracteristicas()


#SE REALIZARÁN MODIFICACIONES DADO QUE NO ESTA ARROJANDO EL RESULTADO CORRECTO