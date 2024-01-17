import random # Importamos el módulo random

meta = 20

caracol1 = 0
caracol2 = 0


while True:
   avance_caracol_1 = random.randint(1, 4)
   avance_caracol_2 = random.randint(1, 4)
   
   caracol1 += avance_caracol_1
   caracol2 += avance_caracol_2
   
   print(f"El caracol 1 avanza {avance_caracol_1} para un total de: {caracol1}")
   print(f"El caracol 2 avanza {avance_caracol_2} para un total de: {caracol2}")
   print(f"------------------------------")
   
   if caracol1 >= 20 or caracol2 >= 20:
      break

if caracol1 > caracol2:
   print("El caracol 1 ha ganado")
elif caracol2 > caracol1:
   print("El caracol 2 ha ganado")
else:
   print("Esto es un Empate")
   