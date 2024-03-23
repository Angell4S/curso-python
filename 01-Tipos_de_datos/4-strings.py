
# string con una comilla
nombre = '  '
# string con dos comillas
nombre1 = "Edward"
# string con tres comillas (multilinea) sirve para documentar
texto = """Este es un texto
me llamo edward y quiero enseñarte
"""
producto1 = "0001 - Manzana"
producto2 = "Manzana - 0001"

# Eliminando prefijo del string producto1
print(producto1.removeprefix("0001 - "))

# Eliminando sufijo del string producto2
print(producto2.removesuffix(" - 0001"))