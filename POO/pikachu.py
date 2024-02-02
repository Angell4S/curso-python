from pokemon import Pokemon

class Pikachu(Pokemon):
   
# _ significa que es privado, pero se puede acceder y modificar, __ significa que es privado y no se puede acceder ni modificar
   __tipo = "Eléctrico"

   def __init__(self, nombre, nivel, salud, voltaje_maximo, amperaje_max, color):
      super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color) # super -> llama al constructor de la clase padre (Pokemon)
      self.__voltaje_maximo = voltaje_maximo
      self.__amperaje_max = amperaje_max

# Manera convencional de declarar getters y setters
# Getters y Setters son métodos que permiten obtener y modificar los atributos de una clase desde fuera de la misma clase
   # def get_salud(self):
   #    return self.__salud
   
   # def set_salud(self, salud):
   #    if salud > 0 and salud < 5000:
   #       self.__salud = salud
   #    else:
   #       print("La salud no puede ser negativa.",
   #             "La salud no puede ser mayor a 5000.")


   
   @property
   def voltaje_maximo(self):
      return self._Pokemon__voltaje_maximo

   @voltaje_maximo.setter
   def voltaje_maximo(self, voltaje_maximo):
      self._Pokemon__voltaje_maximo = voltaje_maximo
   
   @property
   def amperaje_max(self):
      return self._Pokemon__amperaje_max
   
   @amperaje_max.setter
   def amperaje_max(self, amperaje_max):
      self._Pokemon__amperaje_max = amperaje_max


   def atacar(self):
      print(f"¡Pikachu ataca y genera {self._Pokemon__nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 70, 100, 6, 2, "amarillo")

pikachu_1.nivel = 90
pikachu_1.salud = 500
pikachu_1.voltaje_maximo = 50
pikachu_1.amperaje_max = 10


print(f"El pikachu llamado {pikachu_1.nombre} tiene una salud de {pikachu_1.salud}",
      f"un nivel de {pikachu_1.nivel}, un voltaje de {pikachu_1.voltaje_maximo}, y un amperaje de {pikachu_1.amperaje_max}.")