class Pikachu:
   
# _ significa que es privado, pero se puede acceder y modificar, __ significa que es privado y no se puede acceder ni modificar
   __tipo = "Eléctrico"

   def __init__(self, nombre, nivel, salud, voltaje_maximo, amperaje_max, color):
      self.nombre = nombre
      self.__nivel = nivel
      self.__salud = salud
      self.__voltaje_maximo = voltaje_maximo
      self.__amperaje_max = amperaje_max
      self.color = color

   def atacar(self):
      print(f"¡Pikachu ataca y genera {self.__nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 750, 500, 6, 2, "amarillo")
print(f"El pikachu llamado {pikachu_1.nombre} tiene un nivel {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}.")

pikachu_1.__nivel = -900
pikachu_1.__tipo = "Agua" 

print(f"El pikachu llamado {pikachu_1.nombre} tiene un nivel {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}, su voltaje maximo es {pikachu_1.__voltaje_maximo}.")