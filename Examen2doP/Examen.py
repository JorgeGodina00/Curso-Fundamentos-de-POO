import tkinter as tk
from tkinter import messagebox
from ventana import Matricula

class InterfazMatricula:
    def __init__(self, master):
        self.master = master
        master.title("Generador de Matrícula")      

        
        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()
        
        self.label_apellido_paterno = tk.Label(master, text="Apellido Paterno:")
        self.label_apellido_paterno.pack()
        self.entry_apellido_paterno = tk.Entry(master)
        self.entry_apellido_paterno.pack()
        
        self.label_apellido_materno = tk.Label(master, text="Apellido Materno:")
        self.label_apellido_materno.pack()
        self.entry_apellido_materno = tk.Entry(master)
        self.entry_apellido_materno.pack()
        
        
        
        self.label_anio_nacimiento = tk.Label(master, text="Año de Nacimiento:")
        self.label_anio_nacimiento.pack()
        self.entry_anio_nacimiento = tk.Entry(master)
        self.entry_anio_nacimiento.pack()
        
        self.label_carrera = tk.Label(master, text="Carrera:")
        self.label_carrera.pack()
        self.entry_carrera = tk.Entry(master)
        self.entry_carrera.pack()
        
        self.button_generar = tk.Button(master, text="Generar Matrícula", command=self.generar_matricula)
        self.button_generar.pack()
        
    def generar_matricula(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        anio_nacimiento = self.entry_anio_nacimiento.get()
        carrera = self.entry_carrera.get()
            
        matricula = Matricula(nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera)
            
        messagebox.showinfo("Matrícula Generada", f"La matrícula generada es: {matricula.generar_matricula()}")
        
if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazMatricula(root)
    root.mainloop()
    
