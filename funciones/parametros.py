def sumar(numero1, numero2):
   resultado = numero1 + numero2
   print(f"La suma de {numero1} y {numero2} es {resultado}")

def restar(numero1, numero2):
   resultado = numero1 - numero2
   print(f"La resta de {numero1} y {numero2} es {resultado}")

def multiplicar(numero1, numero2):
   resultado = numero1 * numero2
   print(f"La multiplicación de {numero1} y {numero2} es {resultado}")

def dividir(numero1, numero2):
   resultado = numero1 / numero2
   print(f"La división de {numero1} y {numero2} es {resultado}")

operacion = input("Que operación quieres realizar? (sumar, restar, multiplicar, dividir): ")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if operacion == "sumar":
   sumar(num1, num2)
elif operacion == "restar":
   restar(num1, num2)
elif operacion == "multiplicar":
   multiplicar(num1, num2)
elif operacion == "dividir":
   dividir(num1, num2)
else:
   print("Operación no válida, Escriba sumar,"\
      " restar, multiplicar o dividir")