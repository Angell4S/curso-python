nombre = ""
correo = ""
mensaje = ""

condicion_salida = "CONTINUE"

# Mientras la condicion sea verdadera se ejecutara el codigo
while condicion_salida == "CONTINUE":
   nombre = input("Ingrese su nombre: ")
   correo = input("Ingrese su correo: ")
   mensaje = input("Ingrese su mensaje a enviar: ")
   
   print(f"""
      Mensaje a enviado a {nombre}.
      
      destinatario: {correo}
      
      mensaje a enviar: {mensaje}
   """)
   
   condicion_salida = input("En caso de querer continuar con el programa escriba CONTINUE: ")