#A continuación te presento un ejemplo básico de un juego de BlackJack (también conocido como 21) en Python. En este juego, el jugador juega contra la computadora, tratando de obtener una mano de cartas cuyo valor total sea lo más cercano posible a 21 sin pasarse.

import random

baraja = [
    'As', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Jota', 'Reina', 'Rey'
]

def obtener_carta():
    return random.choice(baraja)

def obtener_valor_mano(mano):
    valor_mano = 0
    tiene_as = False
    for carta in mano:
        if carta == 'As':
            tiene_as = True
        valor_carta = min(baraja.index(carta) + 1, 10)
        valor_mano += valor_carta

    if tiene_as and valor_mano <= 11:
        valor_mano += 10

    return valor_mano

def jugar_blackjack():
    print("¡Bienvenido al juego de Blackjack!")
    
    mano_jugador = [obtener_carta(), obtener_carta()]
    mano_computadora = [obtener_carta(), obtener_carta()]
    
    while True:
        print(f"Tu mano: {mano_jugador}, Valor total: {obtener_valor_mano(mano_jugador)}")
        print(f"Carta visible del crupier: {mano_computadora[0]}")
        
        if obtener_valor_mano(mano_jugador) == 21:
            print("¡Blackjack! ¡Ganaste!")
            break
        
        accion = input("¿Quieres otra carta(Si/No)?").lower()
        if accion == 'si':
            nueva_carta = obtener_carta()
            mano_jugador.append(nueva_carta)
            print(f"Obtuviste un {nueva_carta}.")
            
            if obtener_valor_mano(mano_jugador) > 21:
                print("Te pasaste de 21. ¡Perdiste!")
                break
        else:
            # Si el jugador responde con cualquier otra cosa que no sea "si", se detiene el juego.
            break

    while obtener_valor_mano(mano_computadora) < 17:
        nueva_carta = obtener_carta()
        mano_computadora.append(nueva_carta)
        print(f"El crupier obtuvo un {nueva_carta}")
    
    print(f"Tu mano: {mano_jugador}, Valor total: {obtener_valor_mano(mano_jugador)}")
    print(f"Mano del crupier: {mano_computadora}, Valor total: {obtener_valor_mano(mano_computadora)}")
    
    if obtener_valor_mano(mano_computadora) > 21:
        print("El crupier se pasó de 21. ¡Ganaste!")
    elif obtener_valor_mano(mano_jugador) > obtener_valor_mano(mano_computadora):
        print("¡Ganaste!")
    elif obtener_valor_mano(mano_jugador) == obtener_valor_mano(mano_computadora):
        print("Empate")
    else:
        print("Perdiste :(")
            
if __name__ == "__main__":
    jugar_blackjack()
