#Excelente, ahora crearemos una API simple para manejar una lista de tareas por hacer (To-Do List) utilizando Django Rest Framework(DRF). DRF es una potente biblioteca que facilita la creación de API REST en Django.

#Asegurate de tener Django y Django Rest Framework instalados en tu entorno de desarrollo. podemos instalar DRF ejecutando el siguente comando ---> "pip install djangorestframework"

#En este caso yo ya lo tengo instalado, sería cuestión de que tu lo instales y verás como se instala
#Una vez que tengamos todo listo, sigamos con:
#"django-admin startproject todo_api"

#INGRESAMOS AL DIRECTORIO DEL PROYECTO
'''cd todo_api'''

#CREAREMOS UNA NUEVA APLICACIÓN DENTRO DEL PROYECTO. LA LLAMAREMOS --->"tasks":
#'python manage.py startapp tasks'

#AHORA EN EL ARCHIVO 'models.py' dentro de la aplicación tasks, definamos el modelo de las tareas:

