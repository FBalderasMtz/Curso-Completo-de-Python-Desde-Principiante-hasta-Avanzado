#Te presento un juego simple de Piedra, Papel o Tijera en Python, donde el usuario juega contra la computadora

import random
def obtener_opcion_usuario():
    opcion_valida = False
    while not opcion_valida:
        opcion_usuario = input("Elige una opción (piedra, papel o tijera): ").lower()
        if opcion_usuario in ["piedra","papel", "tijera"]:
            opcion_valida= True
        else:
            print("Opción Invalida, Favor de elegir entre 'piedra,papel o tijera'")
    return opcion_usuario

def obtener_opcion_computadora():
    opciones = ["piedra","papel","tijera"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "empate"
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
        (opcion_usuario == "tijera" and opcion_computadora == "papel"):
        return "usuario"
    else:
        return "computadora" 
    
def jugar():
    print("Bienvenido al juego de Piedra, Papel ó Tijera. ¡Vamos a jugar!")
    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()
        
        print(f"Tú elegiste: {opcion_usuario}")
        print(f"La computadora eligió:{opcion_computadora}")
        
        ganador  = determinar_ganador(opcion_usuario, opcion_computadora)
        if ganador == "empate":
            print("Es un empate.¡Vuelve a intetarlo!")
        elif ganador == "usuario":
            print("¡Felicidades! Ganaste")
        else:
            print("La computadora ganó. ¡Intentalo denuevo!")
            
            
        jugar_nuevamente = input("¿Quieres jugar denuevo? (Si/No): ").lower()
        if jugar_nuevamente != "si":
            break

if __name__ == "__main__":
    jugar()
    
#Saluds :)