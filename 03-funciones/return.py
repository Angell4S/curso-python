# return -> retorna un valor de la función y se puede almacenar en una variable o imprimir directamente
def sumar(numero1, numero2):
   resultado = numero1 + numero2
   return resultado

resultado = sumar(10, 20)
resultado_final = resultado * 2
print(f"El resultado de la suma es: {resultado_final}")