# lista = [1,2,3]

# lambda x:x[1] -> x es el parametro que recibe la funcion lambda, x[1] es el indice de la lista que se va a tomar
# retorno = lambda x:x[1]

# print(retorno(lista))

## Practica -> crear una funcion lambda que reciba 2 numeros por argumento y retorne la suma de los dos elementos

sumar = lambda x, y: x + y
restar = lambda x, y: x - y
multi = lambda x, y: x * y
dividir = lambda x, y: x / y

print(sumar(10,11))
print(restar(10,11))
print(multi(10,11))
print(dividir(10,11))

# lambda x: x > 2 -> x es el parametro que recibe la funcion lambda, x > 2 es la condicion que se va a evaluar, (3) es el valor que se le pasa a la funcion lambda
mayor_menor = (lambda x: x > 2)(3)
print(mayor_menor) # => True

# lambda x, y: x ** 2 + y ** 2 -> x, y son los parametros que recibe la funcion lambda, x ** 2 + y ** 2 es la operacion que se va a realizar, (2, 1) son los valores que se le pasan a la funcion lambda
potencia = (lambda x, y: x ** 2 + y ** 2)(2, 1)
print(potencia) # => 5