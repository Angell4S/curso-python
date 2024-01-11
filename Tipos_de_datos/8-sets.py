#los sets son tipo de datos mutables y no ordenada

#declarando un set
mi_set = {1,2,3,4,5}
print(mi_set)

# los sets no pueden tener elementos repetidos
mi_set = set()
mi_set.add(1)
mi_set.add(2)
mi_set.add(2)
mi_set.add(3)
print(mi_set)

#usando set para eliminar elementos repetidos de una lista
lista_numero = [1,1,3,4,6,6,1,7]
mi_set = set(lista_numero)
print(mi_set)

pertenece = 10 in mi_set
print(pertenece)

frutas = {'manzana', 'Banana', 'pera', 'uva'}


# Frozen sets -> son inmutables no se pueden modificar

frutas = {'manzana', 'Banana', 'pera', 'uva'}

mi_frozen_set = frozenset(frutas)
#mi_frozen_set.add('melon') # no se puede agregar elementos
print(mi_frozen_set)