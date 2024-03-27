
from tipofuego import TipoFuego

class Charmander(TipoFuego):
   def __init__(self, nombre, nivel, salud, color, temperatura_max):
      super().__init__(nombre, nivel, salud, color, temperatura_max)
   

charmander_1 = Charmander("chori",99,99,"rojo", 1200)


print(f"El charmander llamado {charmander_1.nombre} tiene una salud de {charmander_1.salud}")