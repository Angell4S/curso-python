# Argumentos posicionales -> son los argumentos que se pasan en el orden en el que se declaran en la función

def imprimir_nombre(primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
   
   print(f"Hola {primer_nombre} {segundo_nombre} "\
      f"{primer_apellido} {segundo_apellido} "\
      "bienvenido al curso de python")   

# positional arguments
imprimir_nombre("Angel", "Julian", "Asencios", "Mory")

# Keyword arguments -> son los argumentos que se pasan con el nombre de la variable y su valor pero el orden no importa ya que se ordenara de acuerdo a la función
imprimir_nombre(segundo_apellido="Mory", primer_nombre="Angel", primer_apellido="Asencios", segundo_nombre="Julian")

imprimir_nombre("Angel", "Julian", segundo_apellido="Mory", primer_apellido="Asencios")

# Iterable unpacking -> es cuando se pasa una lista o tupla como argumento y se desempaqueta en la función
estudiante = ("Angel", "Julian", "Asencios", "Mory")
# para decirle a python que "estudiantes" es un iterable que debe ser desempaquetado se coloca un "*" antes del nombre de la variable
imprimir_nombre(*estudiante)

# Dictionary unpacking -> es cuando se pasa un diccionario como argumento y se desempaqueta en la función
estudiante_dict = {"primer_apellido": "Asencios",
                  "primer_nombre": "Angel",
                  "segundo_nombre": "Julian",
                  "segundo_apellido": "Mory"}
# para decirle a python que "estudiantes" es un diccionario que debe ser desempaquetado se coloca un "**" antes del nombre de la variable
imprimir_nombre(**estudiante_dict)