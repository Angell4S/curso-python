# scopes -> son los alcances de las variables

# scope global -> variables que se pueden usar en cualquier parte del programa
#nombre = "Angel"

# def imprimir_nombre():
#    global nombre # con esto podemos acceder a la variable global y modificarla por el scope local

#    nombre = "Juan"
#    print(f"Hola como estas {nombre}")

#imprimir_nombre()
#print(f"El valor de mi variable global es {nombre}")


# Scope local -> variables que solo se pueden usar dentro de una función
# def imprimir_nombre():
#    local = "Juan"
#    print(f"Hola {local} como estas?")

# imprimir_nombre()
# print(f"Hola {local} como estas?")

# Scope enclosing -> variables que se pueden usar en funciones anidadas (funciones dentro de funciones)
def imprimir_nombre():
   nombre_local = "Juan"
   edad_local = 30
   print(f"Hola {nombre_local} como estas?")
   def imprimir_edad():
      # nonlocal -> permite acceder a una variable que esta en el scope superior y modificarla por el scope local
      nonlocal edad_local
      edad_local = 40
      print(f"Su edad es {edad_local}")
   imprimir_edad()
   print(f"Edad es igual a {edad_local}")
   
imprimir_nombre()