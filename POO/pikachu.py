class Pikachu:
    tipo = "Eléctrico"

    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud


pikachu_1 = Pikachu("Pepe", 750, 500)
pikachu_2 = Pikachu("Rocko", 1200, 1000)
print(pikachu_1.nombre, pikachu_1.nivel, pikachu_1.salud, pikachu_1.tipo)
print(pikachu_2.nombre, pikachu_2.nivel, pikachu_2.salud, pikachu_2.tipo)
