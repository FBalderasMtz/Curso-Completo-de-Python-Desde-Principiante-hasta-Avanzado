# Importamos el ModuMódulo

import pywhatkit 

# Usamos Un try-except
try: 

  # Enviamos el mensaje

  pywhatkit.sendwhatmsg("+525539317854",  
                        "Mensaje De Prueba",
                        15,34) 

  print("Mensaje Enviado") 

  

except: 

  print("Ocurrio Un Error")