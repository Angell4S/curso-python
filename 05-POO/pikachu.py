
from tipoelectrico import TipoElectrico

class Pikachu(TipoElectrico):

   def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
      super().__init__(nombre=nombre,
                       nivel=nivel,
                       salud=salud,
                       color=color,
                       voltaje_max=voltaje_max,
                       amperaje_max=amperaje_max) # super -> llama al constructor de la clase padre (Pokemon)


   def atacar(self):
      print(f"¡Pikachu ataca y genera {self.nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 90, 98, -9000, 2, "amarillo")

pikachu_1.salud = 50


print(f"El pikachu llamado {pikachu_1.nombre} tiene un voltaje maximo de {pikachu_1.voltaje_maximo}")