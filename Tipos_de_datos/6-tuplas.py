mi_tupla = (1, False, 'Edwuard', 0.145)

# La tupla es inmutable, no se puede modificar
#mi_tupla[3] = True

print(type(mi_tupla))

#tupla en función
def retornar_estudiante():
    return 'Edwuard', 21, 1.75

#tupla en variable
tupla_estudiante = retornar_estudiante()
#Imprimiendo toda la tupla
print(tupla_estudiante)

# Desempaquetando la tupla, es decir, asignando cada valor de la tupla a una variable
nombre_estudiante, edadm_estudiante, estatura_estudiante = retornar_estudiante()
print(nombre_estudiante)
print(edadm_estudiante)
print(estatura_estudiante)

#one-line swapping
# intercambiando valores de variables con tuplas
variable1 = 1.0
variable2 = 2.0

# haciendo el intercambio de valores en la tupla
variable1, variable2 = variable2, variable1
print(variable1, variable2)
