class Pikachu:
   
   tipo = "Eléctrico"

   def __init__(self, nombre, nivel, salud, voltaje_maximo, amperaje_max, color):
      self.nombre = nombre
      self.nivel = nivel
      self.salud = salud
      self.voltaje_maximo = voltaje_maximo
      self.amperaje_max = amperaje_max
      self.color = color

   def atacar(self):
      print(f"¡Pikachu ataca y genera {self.nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 750, 500, 6, 2, "amarillo")
print(f"El pikachu llamado {pikachu_1.nombre} tiene un nivel {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}.")

pikachu_1.nivel = -900
pikachu_1.tipo = "Agua"

print(f"El pikachu llamado {pikachu_1.nombre} tiene un nivel {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}.")