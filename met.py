from db import get_conexion
import pymysql

def buscarIdUsuarios(id):
  try:
    conexion = get_conexion()
    with conexion.cursor() as cursor:
      if id == "*":
        print(id)
        cursor.execute("SELECT * FROM usuarios")
      else:
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id))
      info = cursor.fetchall()
      conexion.close()
    return info
  except pymysql.Error as error:
    print("Error al conectar a la base de datos" + error )
    return None
  
def buscarUsuario(email):
  try:
    conexion = get_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (email))
        info = cursor.fetchall()
        conexion.close()
        return info
  except pymysql.Error as error:
    print("Error al conectar a la base de datos" + error)
    return None
  
def registrar_usuario(nombre, telefono, correo, contraseña):
  try:
    conexion = get_conexion()
    with conexion.cursor() as cursor:
      sql = "INSERT INTO usuario (nombre, telefono, correo, contraseña) VALUES (%s, %s, %s)"
      cursor.execute(sql(nombre, telefono, correo, contraseña))
      conexion.commit()
      conexion.close()
      return['1']
  except:
    return[]
  
