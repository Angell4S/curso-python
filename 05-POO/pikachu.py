
from tipoelectrico import TipoElectrico

class Pikachu(TipoElectrico):

   def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color, longitud_cola):
      super().__init__(nombre=nombre,
                       nivel=nivel,
                       salud=salud,
                       color=color,
                       voltaje_max=voltaje_max,
                       amperaje_max=amperaje_max) # super -> llama al constructor de la clase padre (Pokemon)
      self.__longitud_cola = None
      self.longitud_cola = longitud_cola
   
   @property
   def longitud_cola(self):
      return self.__longitud_cola
   
   @longitud_cola.setter
   def longitud_cola(self, longitud_cola):
      if longitud_cola > 0:
         self.__longitud_cola = longitud_cola
      else:
         print("La longitud no puede ser negativa.")

   def atacar_cola_hierro(self):
      print(f"Pikachu ataca y genera {self.longitud_cola/0.5}")




pikachu_1 = Pikachu("Pepe", 90, 98, 120, 2, "amarillo", 1)

pikachu_1.salud = 50


pikachu_1.atacar()
pikachu_1.atacar_cola_hierro()