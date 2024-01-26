# sin paramentros variables posicionales 
# def suma(numero1, numero2):
#    return numero1 + numero2

# def suma_tres(numero1, numero2, numero3):
#    return numero1 + numero2 + numero3

# resultado = suma_tres(10, 20, 10)
# print(f"El resultado es {resultado}")

# Con parametros variables posicionales
def suma(*args):
   resultado = 0
   for element in args:
      resultado += element
   return resultado


resultado = suma(10, 20, 10, 30, 10)
print(f"El resultado es {resultado}")