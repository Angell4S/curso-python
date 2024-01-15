# condicionales una forma de controlar el flujo de un programa

# edad = 17

# if edad >= 18:
#    print("Es mayor de edad")
# else:
#    print("Es menor de edad")


# if else encadenado
# edad = 60

# if edad >= 0 and edad <= 12:
#    print("Usted es un niño")
# elif edad >= 13 and edad <= 17:
#    print("Usted es un adolescente")
# elif edad >= 18 and edad <= 59:
#    print("Usted es un adulto")
# else:
#    print("Usted es un adulto mayor")

# if anidados
# casteo de datos -> convertir un tipo de dato a otro
edad = int(input("Ingrese su edad: "))
altura = int(input("Ingrese tu altura: "))

if edad >= 18:
   if (altura >= 170) or (edad >= 25 and altura >= 165):
      print("Puedes participar en el equipo de baloncesto")
   else:
      print("No cumples con los requisitos para el equipo de baloncesto")
else:
   print("Debes ser mayor de edad para participar en el equipo de baloncesto")
