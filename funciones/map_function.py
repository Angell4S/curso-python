lista_nombre = ['maria','carlos','pepe']

# convirtiendo en mayuscula los elementos de la lista_nombre
lista_nombres_mayus = list(map(str.upper, lista_nombre))
print(lista_nombres_mayus)

lista_frutas = ['banana','pera','manzana', 'uva']
sufix = '_fruta'

lista_frutas_sufix = list(map(lambda x: x + sufix, lista_frutas))
print(lista_frutas_sufix)