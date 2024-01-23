import random # Importamos el módulo random
import turtle


ventana = turtle.Screen()
ventana.title("Carrera de caracoles")
ventana.bgcolor("lightblue")
ventana.setup(width=800, height=600)

caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("red")
caracol1.penup()
caracol1.goto(-300, 100)

caracol2 = turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("blue")
caracol2.penup()
caracol2.goto(-300, 0)

meta = 300

# Dibujar linea de meta
meta_linea = turtle.Turtle()
meta_linea.penup()
meta_linea.goto(meta, 150)
meta_linea.pendown()
meta_linea.goto(meta, -150)
meta_linea.hideturtle()

#Carrera
while True:
   avance_caracol_1 = random.randint(1, 20)
   avance_caracol_2 = random.randint(1, 20)
   
   if avance_caracol_1 % 2 == 0 or avance_caracol_2 % 2 == 0: 
      continue
   
   caracol1.forward(avance_caracol_1)
   caracol2.forward(avance_caracol_2)
   
   print(f"El caracol 1 avanza {avance_caracol_1}")
   print(f"El caracol 2 avanza {avance_caracol_2}")
   print(f"------------------------------")
   
   if caracol1.xcor() >= meta or caracol2.xcor() >= meta:
      break

if caracol1.xcor() > caracol2.xcor():
   print("El caracol 1 ha ganado")
elif caracol2.xcor() > caracol1.xcor():
   print("El caracol 2 ha ganado")
else:
   print("Esto es un Empate")

ventana.exitonclick()