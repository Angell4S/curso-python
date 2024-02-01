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

# Manera de declarar getters y setters con decoradores (property)
   @property
   def salud(self):
      return self.__salud
   
   @salud.setter
   def salud(self, salud):
      if salud > 0 and salud < 5000:
         self.__salud = salud
      else:
         print("La salud no puede ser negativa.",
               "La salud no puede ser mayor a 5000.")

   @property
   def nivel(self):
      return self.__nivel
   
   @nivel.setter
   def nivel(self, nivel):
      if nivel > 0 and nivel < 100:
         self.__nivel = nivel
      else:
         print("El nivel no puede ser negativo.",
               "El nivel no puede ser mayor a 100.")
   
   @property
   def voltaje_maximo(self):
      return self.__voltaje_maximo

   @voltaje_maximo.setter
   def voltaje_maximo(self, voltaje_maximo):
      self.__voltaje_maximo = voltaje_maximo
   
   @property
   def amperaje_max(self):
      return self.__amperaje_max
   
   @amperaje_max.setter
   def amperaje_max(self, amperaje_max):
      self.__amperaje_max = amperaje_max


   def atacar(self):
      print(f"¡Pikachu ataca y genera {self.__nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 70, 100, 6, 2, "amarillo")

pikachu_1.nivel = 90
pikachu_1.salud = 500
pikachu_1.voltaje_maximo = 50
pikachu_1.amperaje_max = 10


print(f"El pikachu llamado {pikachu_1.nombre} tiene una salud de {pikachu_1.salud}",
      f"un nivel de {pikachu_1.nivel}, un voltaje de {pikachu_1.voltaje_maximo}, y un amperaje de {pikachu_1.amperaje_max}.")