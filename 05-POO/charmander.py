from pokemon import Pokemon

class Charmander(Pokemon):
   def __init__(self, nombre, nivel, salud, color):
      super().__init__(nombre, nivel, salud, color)
   

charmander_1 = Charmander("chori",99,99,"rojo")


print(f"El charmander llamado {charmander_1.nombre} tiene una salud de {charmander_1.salud}")