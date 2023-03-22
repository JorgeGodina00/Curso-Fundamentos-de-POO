from tkinter import *
import tkinter as tk

def __init__(self, n,s,t):
    self.num = N
    self.sal = S
    self.tit = t
    
cuenta1 = CuentaCliente(1,200,"Luis")

Ventana = Tk()
Ventana.title("Caja Popular")
Ventana.geometry("600x400")
    
SeccionPrincipal = Frame(Ventana, bg = "white")
SeccionPrincipal.pack(expand = True, fill = "both")
    
Titulo = Label(SeccionPrincipal, text="CAJA POPULAR", bg = "white", fg = "black", font = ("Helvetica",18)).pack()
    
Saldo = Label(SeccionPrincipal, text="SALDO ACTUAL: $0", bg = "white", fg = "black", font = ("Helvetica",18)).pack()
    
ingres = Label(SeccionPrincipal, text="INGRESAR EFECTIVO", bg = "white", fg = "black", font = ("Helvetica",18)).pack()
ingres2 = Entry(SeccionPrincipal)


    
    
    
Ventana.mainloop()