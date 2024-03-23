# funciones lambda: son funciones anonimas que se pueden usar en una sola linea de codigo y no se pueden reutilizar

# sin usar funciones lambda
#funcion para que retorne la nota de un estudiante
# def retornar_nota(estudiante):
#    return estudiante[1]

lista_estudiantes = [('Angel', 4.2),
                     ('Juan', 4.5),
                     ('Pedro', 4.7),
                     ('Maria', 4.8),
                     ('Jose', 4.9)]

# sin usar funciones lambda
# sorted es una funcion que ordena una lista  de menor a mayor, primero se pasa la lista,
# luego la funcion que se va a usar para ordenar, en este caso retornar_nota
# reverse=True es para que ordene de mayor a menor
# lista_ordenada = sorted(lista_estudiantes, key=retornar_nota, reverse=True)

# ahora usando funciones lambda
# lambda x:x[1] -> x es el parametro que recibe la funcion lambda, x[1] es el indice de la lista que se va a ordenar
lista_ordenada = sorted(lista_estudiantes, key= lambda x:x[1], reverse=True)
print(lista_ordenada)

