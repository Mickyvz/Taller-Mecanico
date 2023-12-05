import pymysql.cursors
def get_conexion():
  try:
    return pymysql.connect(host = "localhost",
                           port=3306,
                           user="root",
                           passwd="Micky!0501",
                           db="mydb",
                           cursorclass=pymysql.cursors.DictCursor)
  except pymysql.Error as error:
    print("Error al conectar a la base de datos" + error)
    return None


