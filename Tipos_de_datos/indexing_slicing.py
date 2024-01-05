#### Indexing-> Extraer un caracter de una cadena a travez de un indice ####
cadena = "Hola, mundo!"
print(cadena[0])
print(cadena[1])
print(cadena[2])
#Accediendo al ultimo caracter de la cadena
print(cadena[-1])


#### Slicing-> Extraer un subconjunto de caracteres de una cadena a travez de un indice ####
cadena = "Hola, mundo!"
# Toma desde el indice 0 hasta el 4 sin incluir el 4 es decir toma hasta el 3 y solo saldra Hola
print(cadena[0:4])
# Toma desde el indice 6 hasta el 11 sin incluir el 11 es decir toma hasta el 10 y solo saldra mundo
print(cadena[6:11])

# Si no se especifica el primer indice se toma desde el inicio de la cadena
print(cadena[:4])

# Si no se especifica el segundo indice se toma hasta el final de la cadena
print(cadena[6:])

# Extrayendo caracteres haciendo saltos de 2 en 2, al inicio no especificamos el primer indice por lo que se toma desde el inicio de la cadena,
# al final no especificamos el segundo indice por lo que se toma hasta el final de la cadena,
# y al final especificamos el salto de 2 en 2
print(cadena[::2])

telefono = "4-5-6-3-2-4-7-9"
# Extrayendo solo numeros
print(telefono[::2])

telefono = "-4-5-6-3-2-4-7-9"
# Extrayendo solo numeros, empezando desde el indice 1 que es el primer numero
print(telefono[1::2])


cadena = "Hola, mundo!"
# Extrayendo con slicing negativo, se empieza desde el final de la cadena y se va hacia el inicio
print(cadena[-6:-1])

cadena = "Hola, mundo!"
# Extrayendo con slicing negativo, haciendo saltos negativos de 1 en 1, se empieza desde el final de la cadena y se va hacia el inicio y cambia el orden de los caracteres
print(cadena[::-1])