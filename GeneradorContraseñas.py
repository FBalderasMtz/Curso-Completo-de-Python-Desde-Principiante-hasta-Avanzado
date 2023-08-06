#Generador de contraseñas simple en Python que te permite crear contraseñas aleatorias de una longitud específica

import random 
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
def main():
    print("Generador de Contraseñas")
    longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
    
    if longitud < 8:
        print ("La longitud debe ser mayor o igual a 8 caracteres.")
    else:
        contraseña_generada = generar_contraseña(longitud)
        print(f"Contraseña generada: {contraseña_generada}")
        
if __name__ == "__main__":
    main()

#Saluds :)