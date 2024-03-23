# kwargs: keyword arguments -> son argumentos que se pasan como clave=valor
def conectar_bd(**kwargs):
   # si no se pasa un valor, por defecto se tomara el valor por defecto o none si esta vacio el argumento
   nombre = kwargs.get('nombre_bd', 'default')
   # si no se pasa un valor marcara error ya que no tiene un valor por defecto y solo extrae el valor que se le pasa
   user = kwargs['usuario']
   passwd = kwargs['password']
   port = kwargs['port']
   dir_db = kwargs['dir_db']
   print(f"Conectando con la base de datos: {nombre}")
   print(f"login with: {user} - {passwd}")

conectar_bd(
            nombre_bd='produccion',
            usuario='admin',
            password='1234',
            port=5002,
            dir_db='10.25.47.3',
            query = 'SELECT * FROM tabla'
            )