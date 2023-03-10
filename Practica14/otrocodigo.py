import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Caja Popular")
        self.master.geometry("400x300")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Titular
        self.titular_label = tk.Label(self, text="Titular:")
        self.titular_label.pack()
        self.titular_entry = tk.Entry(self)
        self.titular_entry.pack()

        # No. Cuenta
        self.cuenta_label = tk.Label(self, text="No. Cuenta:")
        self.cuenta_label.pack()
        self.cuenta_entry = tk.Entry(self)
        self.cuenta_entry.pack()

        # Edad
        self.edad_label = tk.Label(self, text="Edad:")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(self)
        self.edad_entry.pack()

        # Saldo
        self.saldo_label = tk.Label(self, text="Saldo:")
        self.saldo_label.pack()
        self.saldo_entry = tk.Entry(self)
        self.saldo_entry.pack()

        # Consultar saldo
        self.consultar_saldo_button = tk.Button(self, text="Consultar Saldo", command=self.consultar_saldo)
        self.consultar_saldo_button.pack()

        # Ingresar efectivo
        self.ingresar_efectivo_button = tk.Button(self, text="Ingresar Efectivo", command=self.ingresar_efectivo)
        self.ingresar_efectivo_button.pack()

        # Retirar efectivo
        self.retirar_efectivo_button = tk.Button(self, text="Retirar Efectivo", command=self.retirar_efectivo)
        self.retirar_efectivo_button.pack()

        # Depositar a otra cuenta
        self.depositar_button = tk.Button(self, text="Depositar a otra cuenta", command=self.depositar)
        self.depositar_button.pack()

        # Salir
        self.quit_button = tk.Button(self, text="Salir", fg="red", command=self.master.destroy)
        self.quit_button.pack()

    def consultar_saldo(self):
        titular = self.titular_entry.get()
        cuenta = self.cuenta_entry.get()
        edad = self.edad_entry.get()
        saldo = self.saldo_entry.get()

        # Validar que se hayan ingresado los datos necesarios
        if not titular or not cuenta or not edad or not saldo:
            messagebox.showerror("Error", "Por favor ingrese todos los datos")
            return

        # Mostrar saldo
        messagebox.showinfo("Saldo", f"El saldo de la cuenta {cuenta} es de {saldo}")

    def ingresar_efectivo(self):
        titular = self.titular_entry.get()
        cuenta = self.cuenta_entry.get()
        edad = self.edad_entry.get()
        saldo = self.saldo_entry.get()

        # Validar que se hayan ingresado los datos necesarios
        if not titular or not cuenta or not edad or not saldo:
            messagebox.showerror("Error", "Por favor ingrese todos los datos")
            return

        # Solicitar monto a ingresar
        monto = tk.simpledialog.askfloat("Ingresar Efectivo", "Ingrese el monto a ingresar")

        # Validar que se haya ingresado un monto válido
        if not monto:
            return
