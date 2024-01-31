class Pikachu:
   tipo = "Eléctrico"

   def __init__(self, nombre, nivel, salud):
      self.nombre = nombre
      self.nivel = nivel
      self.salud = salud

   def atacar(self):
      print(f"¡Pikachu ataca y genera {self.nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 750, 500)
pikachu_2 = Pikachu("Rocko", 1200, 1000)

print(pikachu_1.nombre, pikachu_1.nivel, pikachu_1.salud, pikachu_1.tipo)
print(f"El pikachu llamado {pikachu_1.nombre} ataca.")
pikachu_1.atacar()

print(f"El pikachu llamado {pikachu_2.nombre} ataca.")
pikachu_2.atacar()