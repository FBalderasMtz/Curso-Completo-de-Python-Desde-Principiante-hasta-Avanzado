#Tratamiento de errores en Python, se realiza utilizando las estrucutras de control --> try,except,else,finally. Estas estructuras permiten manejar situaciones excepcionales que pueden ocurrir durante la ejecución del código, como errores o excepciones, y brindan la oportunidad de tomar acciones adecuadas en caso de que ocurran.

''' La sintaxis básica del tratamiento de rrores en Python es la siguiente:
-try:
    Código que puede generar una Excepción
except TipoDeExcepción:
    Acción a tomar cuando se produce dicha excepción.
else:
    Acciones a realizar si no ocurre ninguna excepcion en el bloque try
finally:
    Acciones a realizar siempre, independientemente de si ocurrió una excepción o no
'''
'''
try: Contiene en código que puede generar una excepción
except: Define el tipo de excepcion que se quiere capturar las acciones a realizar en el caso de que ocurra dicha excepción
else: Opcional.Define las acciones a realizar si no ocurre ninguna excepción en el bloque 'try'
finally: Opcional. Define las acciones que se realizarán siempre, independientemente de si ocurrió una excepción o no
'''

#Ejemplo de tratamiento de errores:

try:
    numero1 = int(input("Ingrese un número: "))
    numero2 = int(input("Ingrese otro número: "))
    resultado = numero1 / numero2
except ValueError:
    print("Error: Ingrese solo números enteros.")
except ZeroDivisionError:
    print("Error:No se puede dividir entre cero")
else:
    print("El resultado es:",resultado)
finally:
    print("Fin del programa.")
    
'''
Este ejemplo, el código dentro del bloque try, intenta leer dos números enteros del usuario y realizar una división entre ellos. Si el usuario ingresa un valor no válido (como una letra en lugar de un número) se capturará en una excepción del tipo 'ValueError' y se capturará una excepción del tipo 'ZeroDivisionError' y se imprimirá otro mensaje de error. Si no ocurre ninugna excepción se mostrará el resultado de la división.Finalmente se imprimirá "Fin del programa" independientemente de si ocurrió o no la excepcion.

El tratamiento de errores es una técnica importante para garantizar que los programas se ejecuten de manera robusta y controlada, evitando que se detengan inesperadamente por excepciones no manejadas. Es especialmente útil cuando se interactúa con usuarios o se accede a recursos externos que pueden no ser confiables o tener comportamientos impredecibles.
'''

#Ejemplo 2

def dividir_numeros():
    try:
        num1 = int(input("Ingresa un número")) #--->Como viste en el ejemplo anterior puedes mencionarle al usuario especificamente que datos quieres obtener es decir
        num2 = int(input("Ingresa un número entero: "))
        resultado = num1/num2
    except ValueError:
        print("Error:Ingrese solo números enteros.")
    except ZeroDivisionError:
        print("Error: No puedes dividir por cero!")
    else:
        print("El resultado es:",resultado)
    finally:
        print("Operación completada")
        
dividir_numeros()

'''
En este ejemplo, hemos definido una función dividir_numeros() que intentará dividir dos números enteros ingresados por el usuario. Si el usuario ingresa un valor no válido (por ejemplo, una letra en lugar de un número), se capturará una excepción del tipo ValueError y se imprimirá un mensaje de error. Si el usuario ingresa cero como el segundo número, se capturará una excepción del tipo ZeroDivisionError y se imprimirá otro mensaje de error. Si no ocurre ninguna excepción, se mostrará el resultado de la división. Finalmente, se imprimirá "Operación completada." independientemente de si ocurrió una excepción o no.

Aquí hay algunas situaciones de entrada y los resultados que podrían generarse:

Si se ingresa 8 y 2, se mostrará: "El resultado es: 4.0" y "Operación completada."
Si se ingresa 10 y 0, se mostrará: "Error: No se puede dividir entre cero." y "Operación completada."
Si se ingresa 5 y abc, se mostrará: "Error: Ingrese solo números enteros." y "Operación completada."
El bloque finally asegura que el mensaje "Operación completada." siempre se imprimirá, independientemente de si ocurrió una excepción o no, lo que brinda una forma de asegurar que ciertas acciones se realicen después de que se ejecuten las operaciones dentro del bloque try.
'''

#La documentación te la dejo en la descripción
#Saluds :)