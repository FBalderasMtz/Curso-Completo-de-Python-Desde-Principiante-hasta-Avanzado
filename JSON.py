#JSON, es un tema importante en la programación y es ampliamente utilizado para el intercambio de datos entre aplicaciónes.

'''JSON(JavaScript Object Notation) es un formato de texto ligero utilizado para representar datos estructurados.Es fácilmente legible tanto para humanos como para máquinas y se ah convertido en un formato estándar para el intercambio de datos en aplicaciones Web y APIs.

En Python el modulo 'json' proporciona funciones para trabajar con JSON.Puedes usar el módulo 'json' para convertir objetos de Python en cadenas JSON y viceversa.

Por ejemplo, para convertir un objeto de Python en una cadena JSON, Puedes utilizar 'json.dumps()'.
'''

import json

datos = {
    "nombre" : "Juan",
    "edad" : 30,
    "ciudad" : "Madrid"
}

cadena_json = json.dumps(datos)
print(cadena_json) #Obtendremos {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

#Por otro lado, para convertir una cadeja JSON en un objeto de Python, puedes utilizar 'json.loads()'.

cadena_json = '{"nombre":"Juan","edad":30,"ciudad":"Madrid"}'
datos = json.loads(cadena_json)
print(datos) #Obtenemos {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

#JSON es especialmente útil cuando necesitas intercambiar datos entres diferentes plataformas y lenguajes de programación, ya que es un ampliamente compatible y fácil de utilizar.Ademas, muchas APIs devuelven datos en formato JSON, lo que facilita su manipulación y procesamiento en aplicaciones.