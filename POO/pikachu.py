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

   def atacar(self):
      print(f"¡Pikachu ataca y genera {self.__nivel/4} de daño!")




pikachu_1 = Pikachu("Pepe", 750, 100, 6, 2, "amarillo")

pikachu_1.salud = 500

print(f"El pikachu llamado {pikachu_1.nombre} tiene una salud de {pikachu_1.salud}.")