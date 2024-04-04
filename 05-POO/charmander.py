
from tipofuego import TipoFuego

class Charmander(TipoFuego):
   def __init__(self, nombre, nivel, salud, color, temperatura_max):
      super().__init__(nombre, nivel, salud, color, temperatura_max)
   
if __name__ == "__main__":
   charmander_1 = Charmander("chori",94,91,"rojo", 1200)
   print(charmander_1.nivel)

