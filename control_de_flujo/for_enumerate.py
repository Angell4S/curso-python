lista_nombres = ['Edward', 'David', 'Jimena']

# sin usar la funcion enumerate
# for indice in range(3):
#    print(indice, lista_nombres[indice])
   
# usando la funcion enumerate
for indice, valor in enumerate(lista_nombres):
   print(indice, valor)