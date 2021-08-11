from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import csv
import re
from tkcalendar import Calendar,DateEntry
from tkinter import filedialog

#ROOT 
root=Tk()
root.title("Centro de gravedad")
root.geometry("800x450")
root.resizable(1,1)

#Set the initial theme
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")

#FUNCIONES ROOT
def boton_registro():
    pagina_1.lift()
def boton_calculo():
    pagina_2.lift()

#VARIABLES DE CONTROL
operarios_lista1=["Operario 1","David Ramírez","Sebastián Pérez","Fernando Casanova","Jorge Lopera","Cristian Muñoz","Pablo Torres","Jhon Pazos"]
operarios_lista2=["Operario 2","David Ramírez","Sebastián Pérez","Fernando Casanova","Jorge Lopera","Cristian Muñoz","Pablo Torres","Jhon Pazos"]
a=StringVar(value=operarios_lista1[0])
b=StringVar(value=operarios_lista1[0])
c=BooleanVar()

#PAGINAS
pagina_1=Frame(root)
pagina_1.config(background="#FFFFFF")
pagina_1.place(relx=0.2,relheight=1,relwidth=0.8)
pagina_1.columnconfigure((0,1),weight=1,uniform="column")
pagina_1.rowconfigure((0,1,2,3),weight=1,uniform="row")


pagina_2=Frame(root)
pagina_2.config(background="#FFFFFF")
pagina_2.place(relx=0.2,relheight=1,relwidth=0.8)
pagina_2.columnconfigure((0,1,2),weight=1,uniform="column")
pagina_2.rowconfigure((0,1,2),weight=1,uniform="column")

#PESTAÑAS
pestañas=Frame(root)
pestañas.config(bg="#F5F5F5")
pestañas.place(relheight=1,relwidth=0.2)
pestañas.columnconfigure(index=0,weight=1)

home=PhotoImage(file="home.png")
pestaña_registro=ttk.Button(pestañas,text=" | Registro",image=home,compound="left",command=boton_registro)
pestaña_registro.grid(column=0,row=1,sticky="nsew",padx=5,pady=5)

measure=PhotoImage(file="info.png")
pestaña_calculo=ttk.Button(pestañas,text=" | Calculo",image=measure,compound="left",command=boton_calculo)
pestaña_calculo.grid(column=0,row=2,sticky="nsew",padx=5,pady=5)

#PAGINA 1

####FUNCIONES PAGINA 2
def seleccionar_operario_1(selection):
    operarios_optionmenu_2.config(state="normal")
    for i in range(len(operarios_lista1)):
        operarios_optionmenu_2["menu"].entryconfig(i,state="normal")
    operarios_optionmenu_2["menu"].entryconfig(selection,state="disabled")

def seleccionar_operario_2(selection):
    for i in range(len(operarios_lista2)):
        operarios_optionmenu_1["menu"].entryconfig(i,state="normal")
    operarios_optionmenu_1["menu"].entryconfig(selection,state="disabled")

def placa_check():
    if c.get() == 0:
        placa_entry1.config(state="disabled")
    else:
        placa_entry1.config(state="normal")

def guardar_1():
    for child in columna_operarios.winfo_children():
        child.configure(state="disable")

def editar_1():
    for child in columna_operarios.winfo_children():
        child.configure(state="normal")
    if b.get()=="Operario 2" and a.get()=="Operario 1":
        operarios_optionmenu_2.configure(state="disable")

def guardar_2():
    for child in columna_registro.winfo_children():
        child.configure(state="disable")

def editar_2():
    for child in columna_registro.winfo_children():
        child.configure(state="normal")
    if c.get()==0:
        placa_entry1.configure(state="disabled")

def validate_kilometraje(*_):
        if kilometraje_entry.get() == "":
            kilometraje_entry.state(["!invalid"])
        else:
            try:
                int(kilometraje_entry.get())
                kilometraje_entry.state(["!invalid"])
            except ValueError:
                kilometraje_entry.state(["invalid"])

def validate_combustible(*_):
        if combustible_entry.get() == "":
            combustible_entry.state(["!invalid"])
        else:
            try:
                int(combustible_entry.get())
                combustible_entry.state(["!invalid"])
            except ValueError:
                combustible_entry.state(["invalid"])


def validate_placa1(*_):
        if re.match(r"^[A-Z]{3}\d{3}$",placa_entry1.get()):
            placa_entry1.state(["!invalid"])
        else:
            try:
                int(placa_entry1.get())
                placa_entry1.state(["!invalid"])
            except ValueError:
                placa_entry1.state(["invalid"])

def open_imagen():
    f=filedialog.askopenfile(filetypes=[("Image files",".png .jpg .jpeg .ico")])

####FRAMES
columna_registro=ttk.Labelframe(pagina_1,text="")
columna_registro.grid(column=1,row=0,sticky="nsew",rowspan=3,pady=1,padx=5)
columna_registro.columnconfigure((0,1),weight=1)
columna_registro.rowconfigure((0,1,2,3,4,5,6,7),weight=1,uniform="row")

columna_operarios=ttk.Labelframe(pagina_1,text="")
columna_operarios.grid(column=0,row=0,sticky="nsew",rowspan=3,pady=1,padx=5)
columna_operarios.columnconfigure((0),weight=1)
columna_operarios.rowconfigure((0,1,2,3),weight=1)

botones_operarios=ttk.Labelframe(pagina_1,text="")
botones_operarios.grid(column=0,row=3,sticky="nsew",pady=1,padx=5)
botones_operarios.columnconfigure((0,1),weight=1,uniform="column")
botones_operarios.rowconfigure((0),weight=1)

botones_registro=ttk.Labelframe(pagina_1,text="")
botones_registro.grid(column=1,row=3,sticky="nsew",pady=1,padx=5)
botones_registro.columnconfigure((0,1),weight=1,uniform="column")
botones_registro.rowconfigure((0),weight=1)

####WIDGETS PAGINA 2
fecha_label=ttk.Label(columna_registro,text="Fecha",font=("",13))
fecha_entry=DateEntry(columna_registro,locale='es_ES', date_pattern='dd/MM/yyyy')
fecha_label.grid(column=0,row=0,padx=10,pady=5,sticky="w")
fecha_entry.grid(column=1,row=0,padx=5,pady=5)

modelo_label=ttk.Label(columna_registro,text="Modelo",font=("",13))
modelo_entry=ttk.Entry(columna_registro)
modelo_label.grid(column=0,row=1,padx=10,pady=5,sticky="w")
modelo_entry.grid(column=1,row=1,padx=5,pady=5)

serie_label=ttk.Label(columna_registro,text="Numero de serie",font=("",13))
serie_entry=ttk.Entry(columna_registro)
serie_label.grid(column=0,row=2,padx=10,pady=5,sticky="w")
serie_entry.grid(column=1,row=2,padx=5,pady=5)

placa_checkbutton=ttk.Checkbutton(columna_registro,text="¿Placa?",variable=c,command=placa_check)
placa_entry1=ttk.Entry(columna_registro,state="disabled")
placa_entry1.grid(column=1,row=3,pady=5,padx=5)
placa_checkbutton.grid(column=0,row=3,padx=5,pady=5,sticky="w")
placa_entry1.bind("<FocusOut>",validate_placa1)
placa_entry1.bind("<FocusIn>",validate_placa1)
placa_entry1.bind("<KeyRelease>",validate_placa1)

kilometraje_label=ttk.Label(columna_registro,text="Kilometraje",font=("",13))
kilometraje_entry=ttk.Entry(columna_registro)
kilometraje_label.grid(column=0,row=4,padx=10,pady=5,sticky="w")
kilometraje_entry.grid(column=1,row=4,padx=5,pady=5)

kilometraje_entry.bind("<FocusOut>",validate_kilometraje)
kilometraje_entry.bind("<FocusIn>",validate_kilometraje)
kilometraje_entry.bind("<KeyRelease>",validate_kilometraje)

combustible_label=ttk.Label(columna_registro,text="Combustible",font=("",13))
combustible_entry=ttk.Entry(columna_registro)
combustible_label.grid(column=0,row=5,padx=10,pady=5,sticky="w")
combustible_entry.grid(column=1,row=5,padx=5,pady=5)

combustible_entry.bind("<FocusOut>",validate_combustible)
combustible_entry.bind("<FocusIn>",validate_combustible)
combustible_entry.bind("<KeyRelease>",validate_combustible)

upload=PhotoImage(file="upload.png")
foto_label=ttk.Label(columna_registro,text="Foto",font=("",13))
foto_boton=ttk.Button(columna_registro,text=" | Adjuntar archivo",image=upload,compound="left",command=open_imagen)
foto_label.grid(column=0,row=6,padx=10,pady=5,sticky="w")
foto_boton.grid(column=1,row=6,padx=5,pady=5)

usuario_1=PhotoImage(file="usuario 1.png")
usuario_2=PhotoImage(file="usuario 2.png")
imagen_1=ttk.Label(columna_operarios,image=usuario_1)
imagen_2=ttk.Label(columna_operarios,image=usuario_2)
imagen_1.grid(column=0,row=0,sticky="ns",padx=5,pady=5)
imagen_2.grid(column=0,row=2,sticky="ns",padx=5,pady=5)

operarios_optionmenu_1=ttk.OptionMenu(columna_operarios,a,*operarios_lista1,command=seleccionar_operario_1)
operarios_optionmenu_2=ttk.OptionMenu(columna_operarios,b,*operarios_lista2,command=seleccionar_operario_2)
operarios_optionmenu_1.grid(column=0,row=1,sticky="new",pady=5,padx=5)
operarios_optionmenu_2.grid(column=0,row=3,sticky="new",pady=5,padx=5)
operarios_optionmenu_2.config(state="disabled")

pencil=PhotoImage(file="pencil.png")
floppy_disk=PhotoImage(file="floppy-disk.png")

boton_guardar1=ttk.Button(botones_operarios,image=floppy_disk,command=guardar_1)
boton_editar1=ttk.Button(botones_operarios,image=pencil,command=editar_1)
boton_guardar1.grid(column=0,row=0,sticky="nsew")
boton_editar1.grid(column=1,row=0,sticky="nsew")

boton_guardar2=ttk.Button(botones_registro,image=floppy_disk,command=guardar_2)
boton_editar2=ttk.Button(botones_registro,image=pencil,command=editar_2)
boton_guardar2.grid(column=0,row=0,sticky="nsew")
boton_editar2.grid(column=1,row=0,sticky="nsew")

pagina_1.lift()

root.mainloop()
    


