# Ejemplo de argumentos opcionales -> son los argumentos que tienen un valor por defecto y si no se le pasa un valor se tomara el valor por defecto
def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
   precio_final = (cantidad * precio_u) * (1 - descuento)
   
   print(f"El precio final para {nombre_producto} es: {precio_final}")
   
calcular_precio("Camisas", 3, 20, 0.20)