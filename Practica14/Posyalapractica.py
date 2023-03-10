from tkinter import *
import tkinter.messagebox

class CajaPopular:
    def __init__(self, master):
        self.master = master
        self.master.title("Caja Popular")
        self.master.geometry("400x300")
        self.master.config(bg="white")
        
        self.label_title = Label(self.master, text="Caja Popular", font=("Arial", 20), bg="white")
        self.label_title.pack(pady=10)

        self.label_cuenta = Label(self.master, text="No. Cuenta:", font=("Arial", 12), bg="white")
        self.label_cuenta.pack(pady=5)

        self.label_titular = Label(self.master, text="Titular:", font=("Arial", 12), bg="white")
        self.label_titular.pack(pady=5)

        self.label_edad = Label(self.master, text="Edad:", font=("Arial", 12), bg="white")
        self.label_edad.pack(pady=5)

        self.label_saldo = Label(self.master, text="Saldo:", font=("Arial", 12), bg="white")
        self.label_saldo.pack(pady=5)

        # Cuadros de texto
        self.entry_cuenta = Entry(self.master, font=("Arial", 12))
        self.entry_cuenta.pack()

        self.entry_titular = Entry(self.master, font=("Arial", 12))
        self.entry_titular.pack()

        self.entry_edad = Entry(self.master, font=("Arial", 12))
        self.entry_edad.pack()

        self.entry_saldo = Entry(self.master, font=("Arial", 12))
        self.entry_saldo.pack()

        # Botones
        self.button_consultar = Button(self.master, text="Consultar saldo", font=("Arial", 12), bg="lightgray", command=self.consultar_saldo)
        self.button_consultar.pack(pady=10)

        self.button_ingresar = Button(self.master, text="Ingresar efectivo", font=("Arial", 12), bg="lightgray", command=self.ingresar_efectivo)
        self.button_ingresar.pack(pady=10)

        self.button_retirar = Button(self.master, text="Retirar efectivo", font=("Arial", 12), bg="lightgray", command=self.retirar_efectivo)
        self.button_retirar.pack(pady=10)

        self.button_depositar = Button(self.master, text="Depositar a otra cuenta", font=("Arial", 12), bg="lightgray", command=self.depositar_otra_cuenta)
        self.button_depositar.pack(pady=10)

        self.button_salir = Button(self.master, text="Salir", font=("Arial", 12), bg="red", command=self.master.quit)
        self.button_salir.pack(pady=10)
        
    def consultar_saldo(self):
        cuenta = self.entry_cuenta.get()
        titular = self.entry_titular.get()
        edad = self.entry_edad.get()

        if cuenta == "" or titular == "" or edad == "":
            tkinter.messagebox.showerror("Error", "Todos los campos son requeridos.")
        else:
            saldo = self.entry_saldo.get()
            tkinter.messagebox.showinfo("Saldo", f"El saldo en la cuenta {cuenta} es de ${saldo}.")
            
    def ingresar_efectivo(self):
        cuenta = self.entry_cuenta.get()
        titular = self.entry_titular.get()
        edad = self.entry_edad.get()

        if cuenta == "" or titular == "" or edad == "":
            tkinter.messagebox.showerror("Error", "Todos los campos son requeridos.")
        else:
            saldo = float(self.entry_saldo.get())
            cantidad = float(tkinter.simpledialog.askstring("Ingresar efectivo", "Ingrese la cantidad a ingresar:"))
            if cantidad is not None:
                saldo += cantidad
                self.entry_saldo.delete(0, END)
                self.entry_saldo.insert(0, saldo)

    def retirar_efectivo(self):
        cuenta = self.entry_cuenta.get()
        titular = self.entry_titular.get()
        edad = self.entry_edad.get()

        if cuenta == "" or titular == "" or edad == "":
            tkinter.messagebox.showerror("Error", "Todos los campos son requeridos.")
        else:
            saldo = float(self.entry_saldo.get())
            cantidad = float(tkinter.simpledialog.askstring("Retirar efectivo", "Ingrese la cantidad a retirar:"))
            if cantidad is not None:
                if cantidad > saldo:
                    tkinter.messagebox.showerror("Error", "No hay suficiente saldo en la cuenta.")
                else:
                    saldo -= cantidad
                    self.entry_saldo.delete(0, END)
                    self.entry_saldo.insert(0, saldo)
                    
    def depositar_otra_cuenta(self):
        cuenta = self.entry_cuenta.get()
        titular = self.entry_titular.get()
        edad = self.entry_edad.get()

        if cuenta == "" or titular == "" or edad == "":
            tkinter.messagebox.showerror("Error", "Todos los campos son requeridos.")
        else:
            saldo = float(self.entry_saldo.get())
            cuenta_destino = tkinter.simpledialog.askstring("Depositar a otra cuenta", "Ingrese el número de cuenta de destino:")
            if cuenta_destino is not None:
                cantidad = float(tkinter.simpledialog.askstring("Depositar a otra cuenta", "Ingrese la cantidad a depositar:"))
                if cantidad is not None:
                    if cantidad > saldo:
                        tkinter.messagebox.showerror("Error", "No hay suficiente saldo en la cuenta.")
                    else:
                        saldo -= cantidad
                        self.entry_saldo.delete(0, END)
                        self.entry_saldo.insert(0, saldo)
                        tkinter.messagebox.showinfo("Depositar a otra cuenta", f"Se han depositado ${cantidad} a la cuenta {cuenta_destino}.") 
                                              
root = Tk()
caja_popular = CajaPopular(root)
root.mainloop()                        