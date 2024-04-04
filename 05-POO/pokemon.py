# Abstracción - En este caso estamos aplicando abstracción
# ya que estamos creando una clase Pokemon con atributos y métodos
# que nos permiten crear objetos de tipo Pokemon.

class Pokemon:

    def __init__(self, nombre, nivel, salud, color):
        self.nombre = nombre  # Atributo público
        self.__nivel = None  # Atributo privado
        self.__salud = None  # Atributo privado
        self.color = color  # Atributo privado

        self.salud = salud
        self.nivel = nivel

    # Manera de declarar getters y setters con decoradores (property)
    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, salud):
        if salud > 0 and salud < 100:
            self.__salud = salud
        else:
            print(
                "La salud no puede ser negativa.", "La salud no puede ser mayor a 100."
            )

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        if nivel > 0 and nivel < 100:
            self.__nivel = nivel
        else:
            print(
                "El nivel no puede ser negativo.", "El nivel no puede ser mayor a 100."
            )
