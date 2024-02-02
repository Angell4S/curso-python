class Pokemon:
   
   def __init__(self, nombre, nivel, salud, color):
      self.nombre = nombre # Atributo público
      self.__nivel = nivel # Atributo privado
      self.__salud = salud # Atributo privado
      self.__color = color # Atributo privado
      