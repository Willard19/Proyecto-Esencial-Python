from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from crud import agregar, modificar, delete
from mysql.connector import connect




#funcion guardar
def guardar(idtxt, nombretxt, apellidotxt, telefonotxt, edadtxt, salariotxt, egenero, cargotxt,ecivil, estado):
   iden=idtxt.get()
   nom=nombretxt.get()
   ape=apellidotxt.get()
   tel=telefonotxt.get()
   age=edadtxt.get()
   sal=salariotxt.get()
   gene=egenero
   car=cargotxt.get()
   eci=ecivil
   est=estado.get()
   print(f"{iden, nom, ape, tel, age, sal, gene, car,eci, est}")
   datos = (iden, nom, ape, tel, age, sal, gene, car,eci, est)
   agregar(datos)


def ingresar():
   jwi=Tk()

   jwi.geometry("700x500")
   jwi.title("Formulario de Ingreso")

   titulolabel=Label(jwi,text="INGRESE EMPLEADO")
   titulolabel.place(x=250,y=20)
   estado = IntVar()
   estado2 = IntVar()
#id
   idtxt=StringVar()
   idtxt = Entry(jwi,textvariable=idtxt)
   idtxt.place(x=100, y=60)
   idLabel = Label(jwi, text="Identidad:")
   idLabel.place(x=30, y=60)
#nombre
   nombretxt=StringVar()
   nombretxt=Entry(jwi,textvariable=nombretxt)
   nombretxt.place(x=100, y=100)
   nombreLabel=Label(jwi,text="Nombre:")
   nombreLabel.place(x=50, y=100)

#apellid
   apellidotxt=StringVar()
   apellidotxt = Entry(jwi,textvariable=apellidotxt)
   apellidotxt.place(x=100, y=150)
   apellidoLabel = Label(jwi, text="Apellido:")
   apellidoLabel.place(x=50, y=150)

#edad
   edadtxt=StringVar()
   edadtxt = Entry(jwi,textvariable=edadtxt)
   edadtxt.place(x=450, y=60)
   edadLabel = Label(jwi, text="Edad:")
   edadLabel.place(x=400, y=60)

#telefono
   telefonotxt=StringVar()
   telefonotxt = Entry(jwi,textvariable=telefonotxt)
   telefonotxt.place(x=450, y=100)
   telefonoLabel = Label(jwi, text="Telefono:")
   telefonoLabel.place(x=390, y=100)

#salario
   salariotxt=StringVar()
   salariotxt = Entry(jwi,textvariable=salariotxt)
   salariotxt.place(x=450, y=150)
   salarioLabel = Label(jwi, text="Salario: L.")
   salarioLabel.place(x=390, y=150)

   def marcar_seleccion():
      if estado2.get()==0:
         print(f"{estado2.get()}")
      elif estado2.get()==1:
         print(f"{estado2.get()+1}")



# Estado
   estadolabel=Label(jwi,text="Estado de Empleado").place(x=80,y=200)
   Radiobutton(jwi,text="Activo", variable=estado, value=0, command=marcar_seleccion).place(x=50,y=220)
   Radiobutton(jwi,text="Inactivo", variable=estado, value=1, command=marcar_seleccion).place(x=160, y=220)
# Civil
   CS=StringVar()
   CC=StringVar()
   CV=StringVar()
   CD=StringVar()

   civillabel = Label(jwi, text="Estado de Civil").place(x=80, y=300)
   chkS=Checkbutton(jwi,text="Soltero",variable=CS,onvalue=1, offvalue=0).place(x=50,y=320)
   chkC= Checkbutton(jwi, text="Casado",variable=CC, onvalue=1, offvalue=0).place(x=160, y=320)
   chkV = Checkbutton(jwi, text="Viudo",variable=CV, onvalue=1, offvalue=0).place(x=50, y=340)
   chkD = Checkbutton(jwi, text="Divorciado",variable=CD, onvalue=1, offvalue=0).place(x=160, y=340)
   ecivil="Casado"

 #Genero
   Cm=StringVar()
   Cf=StringVar()
   generolabel = Label(jwi, text="Genero del Empleado").place(x=420, y=200)
   chkF = Checkbutton(jwi, text="Femenino",variable=Cf, onvalue="1",offvalue=0).place(x=400, y=220)
   chkM = Checkbutton(jwi, text="Masculino",variable=Cm, onvalue="1",offvalue=0).place(x=500, y=220)
   egenero="Masculino"
# Cargo
   cargotxt=StringVar()
   cargotxt = Entry(jwi,textvariable=cargotxt)
   cargotxt.place(x=450, y=280)
   cargoLabel = Label(jwi, text="Cargo [Administrador|Empleado]")
   cargoLabel.place(x=390, y=250)
   #botton
   #(codempleado,nombres_empleado,apellidos_empleado,telefono_empleado,edad_empleado,salario_empleado,genero,cargo,civil,estado)

   btnGuardar=Button(jwi, text="Guardar",command=lambda:guardar(idtxt, nombretxt, apellidotxt, telefonotxt, edadtxt, salariotxt, egenero, cargotxt,ecivil, estado)).place(x= 200, y= 450)
   btnSalir = Button(jwi, text="Salir",command=jwi.destroy).place(x=350, y=450)
   jwi.mainloop()


def actualizar2(nombretxt,apellidotxt,telefonotxt,edadtxt,salariotxt,estado,idtxt):
   iden = idtxt.get()
   nom = nombretxt.get()
   ape = apellidotxt.get()
   tel = telefonotxt.get()
   age = edadtxt.get()
   sal = salariotxt.get()
   est = estado.get()
   print(f"{iden, nom, ape, tel, age, sal,est}")
   datos2 = ( nom, ape, tel, age, sal, est, iden)
   modificar(datos2)


#-----funcion actualizar----#
def actualizar():
   jw2 = Tk()
   jw2.geometry("700x300")
   jw2.title("Formulario de Actualizar")
   estado=IntVar()
   titulolabel = Label(jw2, text="ACTUALIZE EMPLEADO")
   titulolabel.place(x=250, y=20)
   # id
   idtxt = StringVar()
   idtxt = Entry(jw2, textvariable=idtxt)
   idtxt.place(x=100, y=60)
   idLabel = Label(jw2, text="Identidad:")
   idLabel.place(x=30, y=60)
   # nombre
   nombretxt = StringVar()
   nombretxt = Entry(jw2, textvariable=nombretxt)
   nombretxt.place(x=100, y=100)
   nombreLabel = Label(jw2, text="Nombre:")
   nombreLabel.place(x=50, y=100)

   # apellid
   apellidotxt = StringVar()
   apellidotxt = Entry(jw2, textvariable=apellidotxt)
   apellidotxt.place(x=100, y=150)
   apellidoLabel = Label(jw2, text="Apellido:")
   apellidoLabel.place(x=50, y=150)

   # edad
   edadtxt = StringVar()
   edadtxt = Entry(jw2, textvariable=edadtxt)
   edadtxt.place(x=450, y=60)
   edadLabel = Label(jw2, text="Edad:")
   edadLabel.place(x=400, y=60)

   # telefono
   telefonotxt = StringVar()
   telefonotxt = Entry(jw2, textvariable=telefonotxt)
   telefonotxt.place(x=450, y=100)
   telefonoLabel = Label(jw2, text="Telefono:")
   telefonoLabel.place(x=390, y=100)

   # salario
   salariotxt = StringVar()
   salariotxt = Entry(jw2, textvariable=salariotxt)
   salariotxt.place(x=450, y=150)
   salarioLabel = Label(jw2, text="Salario: L.")
   salarioLabel.place(x=390, y=150)

   def marcar_seleccion():
      if estado.get() == 0:
         print(f"{estado.get()}")
      elif estado.get() == 1:
         print(f"{estado.get()}")

   # Estado
   estadolabel = Label(jw2, text="Estado de Empleado").place(x=80, y=200)
   Radiobutton(jw2, text="Activo", variable=estado, value=0, command=marcar_seleccion).place(x=50, y=220)
   Radiobutton(jw2, text="Inactivo", variable=estado, value=1, command=marcar_seleccion).place(x=160, y=220)

   # botton

   #nombres_empleado = %s, apellidos_empleados = %s, telefono_empleado=%s, edad_empleado=%s,salario_empleado=$s,estado =%s WHERE codempleado = %s"
   # botton
   btnActualizar = Button(jw2, text="Actualizar",command=lambda:actualizar2(nombretxt,apellidotxt,telefonotxt,edadtxt,salariotxt,estado,idtxt)).place(x=200, y=270)
   btnSalir = Button(jw2, text="Salir",command=jw2.destroy).place(x=350, y=270)
   jw2.mainloop()

#----Funcion eliminar---#
def eliminar2(idtxt):
   iden=idtxt.get()
   print(f"{iden}")
   delete(iden)


def eliminar():
   jw3 = Tk()
   jw3.geometry("400x180")
   jw3.title("Eliminar")
   titulolabel = Label(jw3, text="ELIMINE EMPLEADO")
   titulolabel.place(x=120, y=20)
   # id
   idtxt = StringVar()
   idtxt = Entry(jw3, textvariable=idtxt)
   idtxt.place(x=100, y=60)
   idLabel = Label(jw3, text="Identidad:")
   idLabel.place(x=30, y=60)


   btneliminar = Button(jw3, text="Eliminar", command=lambda:eliminar2(idtxt)).place(x=150, y=130)
   btnSalir = Button(jw3, text="Salir", command=jw3.destroy).place(x=250, y=130)
   jw3.mainloop()


#--Funcion de mostrar-#
def mostrar():
    # -Funcion jalar -#
    connection = connect(host='localhost', database='jw', user='root', password='123456',
                         auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    sqlstm = "SELECT * FROM empleado"
    cursor.execute(sqlstm)
    rows = cursor.fetchall()
    total = cursor.rowcount
    print("Total entradas" + str(total))
    #_--Termina de jalar--#
    jw4=Tk()
    jw4.geometry("900x600")
    jw4.title("Listado")

    tb=tkrttk.Treeview(jw4, columns=(1,2,3,4,5,6,7,8,9,10),show="headings",height="20")
    tb.pack()
    tb.heading(1, text="Identidad")
    tb.heading(2, text="Nombre")
    tb.heading(3, text="Apellido")
    tb.heading(4, text="Telefono")
    tb.heading(5, text="Edad")
    tb.heading(6, text="Salario")
    tb.heading(7, text="Genero")
    tb.heading(8, text="Cargo")
    tb.heading(9, text="Civil")
    tb.heading(10, text="Estado")


    for i in rows:
        tb.insert('','end',values=i)

    #vBar = tkr.Scrollbar(jw4, orient=tkr.VERTICAL, command=tb.yview)
    #vBar.pack(side=tkr.RIGHT, fill="y")

    hBar=tkr.Scrollbar(jw4,orient=tkr.HORIZONTAL, command=tb.xview)
    hBar.pack(side=tkr.BOTTOM,fill="x")

    tb.configure(xscrollcommand=hBar.set)
    jw4.mainloop()




#----MENU PRINCIPAL---#
jw = Tk()
jw.geometry("400x300")
jw.title("Menu Principal")
#Botones
#Crear barra de menus
barraMenu=Menu(jw)
#Crear los menus
mnuIngresar=Menu(barraMenu)
mnuEliminar=Menu(barraMenu)
mnuActualizar=Menu(barraMenu)
mnuMostrar=Menu(barraMenu)
mnuSalir=Menu(barraMenu)
#Comandos
mnuIngresar.add_command(label="Nuevo Empleado",command=ingresar)
mnuActualizar.add_command(label="Actualizar Empleado",command=actualizar)
mnuEliminar.add_command(label="Eliminar Empleado",command=eliminar)
mnuMostrar.add_command(label="Mostrar",command=mostrar)

mnuSalir.add_command(label="SALIR",command=jw.destroy)
#Agregar los menus a la barra de menus
barraMenu.add_cascade(label="Ingresar",menu=mnuIngresar)
barraMenu.add_cascade(label="Eliminar",menu=mnuEliminar)
barraMenu.add_cascade(label="Actualizar",menu=mnuActualizar)
barraMenu.add_cascade(label="Mostrar",menu=mnuMostrar)
barraMenu.add_cascade(label="SALIR",menu=mnuSalir)
#asignamos la barra a la ventana

jw.config(menu=barraMenu)

jw.mainloop()


