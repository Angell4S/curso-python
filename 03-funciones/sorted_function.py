estudiante = [
   ('Juana', 22, 95, '555-1234'),
   ('Pedro', 23, 75, '555-1235'),
   ('Alicia', 18, 68, '555-1236'),
   ('Fernando', 23, 88, '555-1237'),
   ('María', 35, 100, '555-1238'),
   ('Luis', 24, 90, '555-1239')
]

lista_estudiantes_edad = list(sorted(estudiante, key=lambda x: x[1], reverse=True))
print(lista_estudiantes_edad)