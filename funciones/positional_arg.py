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
