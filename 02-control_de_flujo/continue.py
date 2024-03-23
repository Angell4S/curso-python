lista_numero = [34,10,23,57,19,2,8,3]

#Listando numeros pares utilizando continue, 
# como el residuo es diferente de cero es impar asi que seguimos iterando el siguiente numero hasta encontrar un numero que sea igual a cero e imprimirlo
for numero in lista_numero:
   if numero % 2 != 0:
      continue
   print(numero)