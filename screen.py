import tkinter
from tkinter import *
from tkinter import ttk
from Programa import *


def pantalla2():

    clasificacion = visualizar()

    pantalla = Tk()
    pantalla.title("Clasificación")
    pantalla.config(height=500, width=900)
    pantalla.resizable(True, True)

    datos = ttk.Treeview(pantalla, columns = ("id_equipo","nombre","puntos"), show="headings")
    datos.column("id_equipo", anchor=CENTER, width= 80)
    datos.column("nombre", anchor=CENTER, width=500)
    datos.column("puntos", anchor=CENTER, width=80)

    datos.heading("id_equipo", text="Posición")
    datos.heading("nombre", text="Equipo")
    datos.heading("puntos", text="Puntos")

    for x in clasificacion:
        datos.insert("", tkinter.END, values=x)

    datos.pack()
    pantalla.mainloop()

def pantalla3():

    pantalla = Tk()
    pantalla.title("Ingresar")
    pantalla.config(height=500, width=900)
    pantalla.resizable(True, True)

    frame = tkinter.Frame(pantalla)
    datoarriba=Label(frame, text="Agregar equipo")
    datoarriba.grid(column=1, row=0)
    dato = Label(frame, text="Introduzca el nombre del equipo")
    dato.grid(column=0, row=1)
    escribir = Entry(frame)
    escribir.grid(column=0, row=2)
    dato = Label(frame, text="Introduzca los puntos")
    dato.grid(column=0, row=3)
    escribir2 = Entry(frame)
    escribir2.grid(column=0, row=4)

    frame.pack
    pantalla.mainloop()




def pantalla():
    pantalla = Tk()
    pantalla.title("LaLiga")
    pantalla.config(height= 500, width= 900)
    pantalla.resizable (True,True)
    barramenu = Menu(pantalla)
    pantalla.config(menu=barramenu)
    # Botón Cargar
    menu1 = Menu(barramenu, tearoff=0)
    barramenu.add_cascade(label="Cargar", menu=menu1)
    menu1.add_command(label="Datos", command=lambda: tablaactual())
    # Botón visualizar
    menu2 = Menu(barramenu, tearoff=0)
    barramenu.add_cascade(label="Mostrar", menu=menu2)
    menu2.add_command(label="Clasificación", command=lambda: pantalla2())
    # Botón eliminar
    menu3 = Menu(barramenu, tearoff=0)
    barramenu.add_cascade(label="Eliminar", menu=menu3)
    menu3.add_command(label="Todo", command=lambda: eliminartodo())
    # Botón insertar
    menu4 = Menu(barramenu, tearoff=0)
    barramenu.add_cascade(label="Insertar", menu=menu4)
    menu4.add_command(label="Dato", command=lambda: pantalla3())
    pantalla.mainloop()

pantalla()

