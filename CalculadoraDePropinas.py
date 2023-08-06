#Precio de la factura
#Porcentaje de la propina 
#Personas a repartir

#Solucion 1

'''print("Bienvenido a la calculadora propinas")
factura=float(input("¿Cual es el importe de tu factura?"))
propina = int(input("¿Cúal es el porcentaje de propina que quieres dejar?"))
personas = int(input("¿Cuantas personas hay que repartir la factura?"))

importe_propina = (factura * propina)/100
factura_total = factura + importe_propina

importe_por_persona = factura_total / personas
importe_redondeado = round(importe_por_persona,2)
print("El importe a pagar por persona es de "+ str(importe_por_persona))'''

#SOLUCION 2

#Definimos una función llamada 'calcular_propina' que recibirá el monto total de la cuenta y el porcentaje de la propina.
#Esta función calculará el monto de la propina y el total a pagar con la propina incluida

def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina/100) #Calculamos el monto de la propina
    total_a_pagar = total_cuenta + propina #Calculamos el total a pagar sumando el monto de la cuenta y la propina.
    return total_a_pagar

try:
#Pedimos al usuario que ingrese el monto total de la cuenta y lo guardamos en la variable 'total_cuenta'
    total_cuenta = float(input("Ingrese el monto total de la cuenta: "))
#Solicitamos al usuario que ingrese el porcentaje de propina que desea  
    porcentaje_propina= float(input("Ingrese el porcentaje de propia que desea dejar: "))
#Llamamos a la función 'calcular_propina' pasando argumentos el monto total
#El resultado lo guardamos en la variable 'total_a_pagar'
    total_a_pagar = calcular_propina(total_cuenta, porcentaje_propina)
    
#Mostramos los resultados al usuario con los mensajes descriptivos
    print(f"\n Monto de la cuenta: $ {total_cuenta:.2f}")
    print(f"Porcentaje de propina: {porcentaje_propina}%")
    print(f"Propina a dejar:${total_a_pagar - total_cuenta:.2f}")
    print(f"Total a pagar (con propina): ${total_a_pagar:.2f}")
    
#Capturamos la excepción ValueError en caso de que el usuario ingrese valores no númericos
except ValueError:
    print("Error: Ingrese valores numéricos válidos para el monto de la cuenta y el porcentaje de la propina")
    
#Saluds :)