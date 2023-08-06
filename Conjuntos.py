#Conjuntos en Python

'''
Son estructuras de datos que almacenan una colección de datos, ya sea listas y/o tuplas, pero tienen una gran diferiencia, este elemento de "conjuntos" NO PERMITE DATOS DUPLICADOS, es decir que tanto no tienen un orden en especifico, como por ejemplo una númeración, 1,3,5,7 etc, lo que significa que los elementos no se almacenan en una secuencia específica.
'''

'''Para crear un conjunto utilizamos lo que viene siendo "{}" o la función de set()Por ejemplo:'''

mi_conjunto ={1,2,3,4,5}
otro_conjunto = set([3,4,5,6,7])
#Como se menciona al inicio, NO PERMITE DUPLICADOS es decir que si intentas agregar algun dato del "otro_conjunto", no te lo agregará el dato duplicado nuevamente

mi_conjunto = {1,2,3}
print("Mi_Conjunto original: ", mi_conjunto)
mi_conjunto.add(3) #---> El 3 ya está presente, no se agregará nuevamente
mi_conjunto.add(4) # Se agregará el número 4
#Comprobamos
print("Mi conjunto modificado: ",mi_conjunto)

#Los beneficios de los conjuntos es cuando necesitamos eliminar duplicados en una colección de elementos los cuales queremos remplazar, es decir en terminos matematicos es como union, intersección, diferencia, etc.

'''Por decirlo así, podemos realizar una unón entre dos conjuntos utilizado el operador | ó en su defecto el metodo union().
Te muestro'''

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
union = conjunto1 | conjunto2
print("Este es un conjunto de dos uniones con el simbolo '|'", union) #Imprime {1,2,3,4,5}
#Podemos encontrar intersección de dos conjuntos utilizando el operador '&' o el metodo 'intersection()'

interseccion = conjunto1 & conjunto2
print('Esta es una intersección entre los conjuntos', interseccion)#Imprime {3}

#Podemos encontrar la diferiencia entre dos conjuntos utilizando el operador '-' ó el método "difference()"

diferencia = conjunto1 - conjunto2
print(diferencia) #Imprime {1,2}
