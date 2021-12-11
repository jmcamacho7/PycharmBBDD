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
        eleccion = input("Selecciona que quieres hacer: a si quieres leer la base de datos, b si quieres introducir datos, c si quieres eliminar datos")

        if eleccion == "a":
            cursor.execute("SELECT * FROM equipo")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila[0], fila[1], fila[2])

        if eleccion == "b":
            nombre = input("Ingresa el nombre del equipo: ")
            puntos = input("Ingresa los puntos del equipo: ")
            sentencia = "INSERT INTO equipo (nombre, puntos) VALUES ('{0}','{1}')".format(nombre, puntos)
            cursor.execute(sentencia)
            conexion.commit()
            print("Registro insertado con éxito")

        if eleccion == "c":
            cursor.execute("DELETE FROM equipo WHERE id_equipo = 1")
            conexion.commit()
            print("Eliminación realizada con éxito")

        nombre = input("Ingresa el nombre del equipo: ")
        puntos = input("Ingresa los puntos del equipo: ")
        sentencia = "INSERT INTO equipo (nombre, puntos) VALUES ('{0}','{1}')".format(nombre, puntos)
        cursor.execute(sentencia)
        conexion.commit()
        print("Registro insertado con éxito")

except Error as ex:
    print("Error durante la conexión :(")
finally:
    if conexion.is_connected():
        conexion.close()
        print("Se cerró la conexión")