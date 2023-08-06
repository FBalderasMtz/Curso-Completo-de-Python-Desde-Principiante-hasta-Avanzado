#Trabajaremos ahora con fecha y hora en Python, puedes utilizar "datatime".Para ello, primero debemos importar la clase date y datetime del módulo.

#Aqui esta un ejemplo de cómo obtener la fecha y hora actual utilizando datetime.now()

from datetime import datetime

#Obtenemos la fecha y hora actual

fecha_hora_actual = datetime.now()
print("Fecha y hora Actual: ",fecha_hora_actual)

#datetime.now() devuelve un objeto 'datetime' que contiene la fecha y hora actual.La precisión de los milisengundos dependerá del sistema y la configuración del reloj.

#Tambien puedes obtener por separado la fecha y la hora utilizando los atributos del objeto datetime: Por ejemplo:

fecha_actual = fecha_hora_actual.date()
print("Fecha actual:",fecha_actual)

#Obtener la hora actual
hora_actual = fecha_hora_actual.time()
print("Hola actual: ",hora_actual)

#Ademas, si necesitamos trabajar con fechas y horas específicas, puedes crear objetos 'datatime' personalizados utilizando el constructor 'datatime'. Por ejemplo:

from datetime import datetime

#Crear un objeto datetime personalizado

mi_fecha_hora = datetime(2023,7,19,12,0)
print("Mi fecha y hora personalizada: ",mi_fecha_hora)

'''
El constructor datetime toma los argumentos en el siguiente orden: año, mes, día, hora, minuto y segundo. También puedes proporcionar argumentos adicionales como microsegundos, zona horaria, etc., si es necesario.

Recuerda que trabajar con fechas y horas puede ser complicado debido a las diferencias en formatos y zonas horarias. Siempre es recomendable asegurarse de que los datos sean consistentes y utilizar funciones y métodos proporcionados por el módulo datetime para realizar operaciones y cálculos con fechas y horas de manera correcta.
'''
#Saluds :)