# Las listas son mutables, es decir, se pueden modificar
# lista_numeros = [1, 2, 3, 4, 5]
# lista_nombres = ['Edwuard', 'Juan', 'Pedro', 'Luis']
# lista_bool = [True, False, True, False]

# lista_numeros[2] = 100

# lista_numeros = list((1,2,3))
# print(type(lista_numeros))

# print(lista_numeros)

# Metodos de las listas

lista_numeros = [1, 2, 3]

#Append, agrega un elemento al final de la lista
lista_numeros.append(4)
lista_numeros.append(5)
lista_numeros.append(5)
print(lista_numeros)

#count, cuenta cuantas veces se repite un elemento en la lista
print(lista_numeros.count(5))

#extend, agrega una lista a otra lista
lista_extendida = [100,101]
lista_numeros.extend(lista_extendida)
print(lista_numeros)

#index, devuelve el indice de un elemento en la lista
print(lista_numeros.index(100))

#insert, inserta un elemento en un indice especifico
lista_numeros.insert(2, 5000)
print(lista_numeros)

#pop, extrae y quita el elemento de la lista de un indice especifico
print(lista_numeros.pop(2))
print(lista_numeros)

#remove, remueve el primer elemento que coincida con el parametro
lista_numeros.remove(100)
print(lista_numeros)

#reverse, invierte el orden de la lista
lista_numeros.reverse()
print(lista_numeros)

#clear, elimina todos los elementos de la lista
lista_numeros.clear()
print(lista_numeros)

#sort, ordena la lista
lista_numeros = [5,2,65,3,1,7]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)