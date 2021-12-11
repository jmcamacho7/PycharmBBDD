import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="patata123",
        database="furbo"
    )

    if conexion.is_connected():
        print("Conexión correcta :D")
        inforserver = conexion.get_server_info()
        print("Info del servidor:", inforserver)
        cursor = conexion.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone()
        print("Conectado a la BD:", registro)
        cursor.execute("SELECT * FROM equipo")
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila[0], fila[1], fila[2])

except Error as ex:
    print("Error durante la conexión :(")
finally:
    if conexion.is_connected():
        conexion.close()
        print("Se cerró la conexión")