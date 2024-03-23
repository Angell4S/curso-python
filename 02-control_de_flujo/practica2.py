import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.speed(1)

#dibujar una estrella
for _ in range(5):
   tortuga.forward(250) # avanzar 250 pasos hacia adelante
   tortuga.right(144) # giro hacia la derecha 144 grados, 180 - 36 = 144 grados es el giro que debe hacer para dibujar una estrella de 5 puntas
   
ventana.exitonclick()