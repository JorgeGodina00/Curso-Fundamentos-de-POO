from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana = Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pest1 = ttk.Frame(panel)
pest2 = ttk.Frame(panel)
pest3 = ttk.Frame(panel)
pest4 = ttk.Frame(panel)

panel.add(pest1, text = "Formulario de Usuarios")
panel.add(pest2, text = "Buscar Usuario")
panel.add(pest3, text = "Consultar Usuarios")
panel.add(pest4, text = "Actualizar Usuario")

#Pest1: Formulario de Usuarios
titulo = Label(pest1, text = "Registro de Usuarios", fg = "Blue", font = ("Modern", 18)).pack()

varNom = tk.StringVar()
lblNom = Label(pest1, text="Nombre: ").pack()
txtNom = Entry(pest1, textvariable=varNom).pack()

varCor = tk.StringVar()
lblNom = Label(pest1, text="Correo: ").pack()
txtNom = Entry(pest1, textvariable=varCor).pack()

varCon = tk.StringVar()
lblNom = Label(pest1, text="Contrase;a: ").pack()
txtNom = Entry(pest1, textvariable=varCon).pack()

btnGuardar = Button(pest1, text="Guardar Usuario").pack()

Ventana.mainloop()