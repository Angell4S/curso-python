# Declarar un diccionario
mi_diccionario = {
   'edward' : [1.4, 4.5, 5.0],
   'carla' : [4.4, 5.0, 5.0],
   'jonas' : [0.0, 3.4, 3.0]
}
print(mi_diccionario)

# declarando diccionario con dict()
mi_diccionario_2 = dict( edward = [1.4, 4.5, 5.0],
                        carla = [4.4, 5.0, 5.0],
                        jonas = [0.0, 3.4, 3.0] )
print(mi_diccionario_2)

# declarando diccionario dict_vacio
mi_diccionario_3 = dict()
mi_diccionario_3['edward'] = [1.4, 4.5, 5.0]
mi_diccionario_3['carla'] = [4.4, 5.0, 5.0]
mi_diccionario_3['jonas'] = [0.0, 3.4, 3.0]
print(mi_diccionario_3)





# Los diccionarios son mutables es decir se pueden modificar

mi_diccionario['Maria'] = [1.4, 4.5, 5.0]

print(mi_diccionario)

# Extrayendo valores
print(mi_diccionario['jonas'])

# Eliminando valores de un diccionario

del mi_diccionario['jonas']
print(mi_diccionario)

#keys
print(mi_diccionario.keys())
#values
print(mi_diccionario.values())
#both
print(mi_diccionario.items())