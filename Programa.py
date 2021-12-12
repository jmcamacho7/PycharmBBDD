import mysql.connector
from mysql.connector import Error
from bs4 import BeautifulSoup
import requests


tabla = {
    "equipos": "",
    "puntos": ""
}

listdicc = []

equipos = list ()
puntos = list()


def peticion():
    url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    eq = soup.find_all ("span", class_="nombre-equipo")

    count=0
    for i in eq:
        if count < 20:
            equipos.append(i.text)
        else:
            break
        count += 1

    pts = soup.find_all ("td", class_="destacado")

    count=0
    for i in pts:
        if count < 20:
            puntos.append(i.text)
        else:
            break
        count += 1

def lista():
    for x in range(len(equipos)):
        copia = tabla.copy()
        copia["equipos"] = equipos[x]
        copia["puntos"] = puntos[x]
        listdicc.append(copia)
    print(listdicc)

peticion()
lista()

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="patata123",
        database="furbo"
    )
    return conexion

def cursorBBDD(conexion):
    cursor = conexion.cursor()
    return cursor

def tablaactual():
    conexion = conectar()
    cursor = cursorBBDD(conexion)
    for x in listdicc:
        sentencia = "INSERT INTO equipo (nombre, puntos) VALUES ('{0}','{1}')".format(x["equipos"], x["puntos"])
        cursor.execute(sentencia)
        conexion.commit()
        print("Registro insertado con éxito")


def visualizar():
    conexion = conectar()
    cursor = cursorBBDD(conexion)
    cursor.execute("SELECT * FROM equipo")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[0], fila[1], fila[2])
    return resultados

def ingresar():
    conexion = conectar()
    cursor = cursorBBDD(conexion)
    nombre = input("Ingresa el nombre del equipo: ")
    punto = input("Ingresa los puntos del equipo: ")
    sentencia = "INSERT INTO equipo (nombre, puntos) VALUES ('{0}','{1}')".format(nombre, punto)
    cursor.execute(sentencia)
    conexion.commit()
    print("Registro insertado con éxito")

def eliminar():
    conexion = conectar()
    cursor = cursorBBDD(conexion)
    numerito= str(input("Introduce el número del ID:"))
    sentencia= "DELETE FROM equipo WHERE id_equipo = {};".format(numerito)
    cursor.execute(sentencia)
    conexion.commit()
    print("Eliminación realizada con éxito")

def eliminartodo():
    conexion = conectar()
    cursor = cursorBBDD(conexion)
    sentencia= "DELETE FROM equipo;"
    cursor.execute(sentencia)
    conexion.commit()



