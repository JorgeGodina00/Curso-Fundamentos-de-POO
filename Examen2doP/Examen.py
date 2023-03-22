from tkinter import *
import tkinter as tk
from generador import *
class Menu:
    def __init__(self, Principal):
        self.Principal = Principal
        self.Principal.title("Menu")
        
        self.nombre = tk.StringVar
        self.ape = tk.StringVar
        self.ancur = tk.StringVar #año curso
        self.annam = tk.StringVar #año nacimiento
        self.car = tk.StringVar #carrera
        
        tk.Frame(self.Principal, g = "white").pack(expand=True, fill='both')
        tk.Label(self.Principal, text="MatriRandom").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.Principal, text="Ingresa tu nombre: ").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.Principal, textvariable=self.nombre, width=5).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.Principal, text="Ingresa tu apellido: ").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.Principal, textvariable=self.ape, width=5).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.Principal, text="Ingresa tu carrera: ").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.Principal, textvariable=self.car, width=5).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.Principal, text="Ingresa el año de tu carrera: ").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.Principal, textvariable=self.ancur, width=5).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.Principal, text="Ingresa el año de nacimiento: ").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.Principal, textvariable=self.annam, width=5).grid(row=0, column=1, padx=10, pady=10)  
        


Principal = tk.Tk()
menu = Menu(Principal)
Principal.mainloop()

        