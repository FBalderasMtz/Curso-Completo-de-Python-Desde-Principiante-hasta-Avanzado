#Gestionar una subasta implica crear un sistema donde los participantes puedan ofertar por un producto o servicio, y el ganador sea aquel que realice la oferta más alta. 

import time

#Funcion para gestionar una subasta
def gestionar_subasta(producto, precio_inicial):
    print(f"¡Bienvenido a la subasta del {producto}!")
    print(f"El precio inicial es {precio_inicial}")
    
    oferta_actual = precio_inicial
    ganador = None
    
    while True:
        #Pedimos al participante que ingrese su nombre
        nombre_participante = input("Ingresa tu nombre (o 'salir' para terminar la subasta): ")
        
        if nombre_participante.lower() == 'salir':
            break
        
        #Pedimos al participante que ingrese su oferta
        oferta = float(input(f"Ingresa tu oferta para el {producto}:"))
        
        if oferta > oferta_actual:
            #Si la oferta es mayor a la oferta actual, actualizamos el valor de la subasta
            oferta_actual = oferta
            ganador = nombre_participante
            print(f"¡{nombre_participante} ha realizado una oferta de  {oferta_actual}!")
        else:
            #Si la oferta es menor o igual que la oferta actual, le informamos al participante que la oferta debe ser mayor
            print("La oferta debe ser mayor a la oferta actual.")
            
    if ganador:
        #Si hay un ganador, mostramos el mensaje de ganador con su nombre y la oferta ganadora
        print(f"\n¡La subasta ha terminado! \n El ganador de la subasta del {producto} es {ganador} con una oferta de {oferta_actual}.")
    else:
        #Si no hay ganador,mostramos el mensaje que la subasta ha terminado sin ganador
       print("\nLa subasta ha terminado sin ganador") 
       
#Ejemplo de uso
gestionar_subasta("Reloj", 1000)

#Saluds :)