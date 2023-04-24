import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, simpledialog
import string

class Cuenta:
    def __init__(self, num_cuenta, titular, edad, saldo):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
    
    def consultar_saldo(self):
        return self.saldo
    
    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad
    
    def retirar_efectivo(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en la cuenta.")
        self.saldo -= cantidad
    
    def depositar_a_otra_cuenta(self, otra_cuenta, cantidad):
        self.retirar_efectivo(cantidad)
        otra_cuenta.ingresar_efectivo(cantidad)


class CajaPopularApp:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        
        self.root = tk.Tk()
        self.root.title("Caja Popular App")
        self.root.geometry('500x400')
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="white", foreground="black")
        style.configure("TButton", background="#e0e0e0", foreground="black", font=("Arial", 10))
        style.map("TButton", background=[('active', '#d9d9d9')])
        
        self.label_num_cuenta = ttk.Label(self.root, text="Selecciona una cuenta:")
        self.label_num_cuenta.pack(pady=10)
        self.cuenta_var = tk.StringVar(value="")

        self.cuentas_combo = ttk.Combobox(self.root, values=[cuenta.num_cuenta for cuenta in cuentas], textvariable=self.cuenta_var, state="readonly", width=20)
        self.cuentas_combo.pack(pady=10)

        self.btn_agregar_cuenta = ttk.Button(self.root, text="Agregar cuenta", command=self.agregar_cuenta)
        self.btn_agregar_cuenta.pack(pady=10)

        self.btn_eliminar_cuenta = ttk.Button(self.root, text="Eliminar cuenta", command=self.eliminar_cuenta)
        self.btn_eliminar_cuenta.pack(pady=10)

        self.btn_consultar_saldo = ttk.Button(self.root, text="Consultar saldo", command=self.consultar_saldo)
        self.btn_consultar_saldo.pack(pady=10)
        
        self.btn_ingresar_efectivo = tk.Button(self.root, text="Ingresar efectivo", command=self.ingresar_efectivo)
        self.btn_ingresar_efectivo.pack()
        
        self.btn_retirar_efectivo = tk.Button(self.root, text="Retirar efectivo", command=self.retirar_efectivo)
        self.btn_retirar_efectivo.pack()
        
        self.btn_depositar_otra_cuenta = tk.Button(self.root, text="Depositar a otra cuenta", command=self.depositar_a_otra_cuenta)
        self.btn_depositar_otra_cuenta.pack()
        
    def run(self):
        self.root.mainloop()
        
    def get_selected_cuenta(self):
        num_cuenta = self.cuenta_var.get()
        for cuenta in self.cuentas:
            if cuenta.num_cuenta == num_cuenta:
                return cuenta
        raise ValueError("No se encontró una cuenta con el número especificado.")
        
        
    def agregar_cuenta(self):
        try:
            num_cuenta = simpledialog.askstring("Agregar cuenta", "Ingrese el número de cuenta:")
            if not num_cuenta:
                return
            titular = simpledialog.askstring("Agregar cuenta", "Ingrese el titular de la cuenta:")
            if not titular:
                return
            edad = simpledialog.askinteger("Agregar cuenta", "Ingrese la edad del titular:")
            if not edad:
                return
            saldo = simpledialog.askfloat("Agregar cuenta", "Ingrese el saldo inicial:")
            if not saldo:
                return
            cuenta = Cuenta(num_cuenta, titular, edad, saldo)
            self.cuentas.append(cuenta)
            messagebox.showinfo("Cuenta agregada", f"Se agregó la cuenta con número {num_cuenta}.")
            self.cuentas_combo.configure(values=[cuenta.num_cuenta for cuenta in self.cuentas])
        except ValueError as e:
             messagebox.showerror("Error", str(e))
    
    def eliminar_cuenta(self):
        try:
            cuenta = self.get_selected_cuenta()
            self.cuentas.remove(cuenta)
            messagebox.showinfo("Cuenta eliminada", f"Se eliminó la cuenta con número {cuenta.num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def consultar_saldo(self):
        try:
            cuenta = self.get_selected_cuenta()
            saldo = cuenta.consultar_saldo()
            messagebox.showinfo("Saldo", f"El saldo de la cuenta {cuenta.num_cuenta} es {saldo}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def ingresar_efectivo(self):
        try:
            cuenta = self.get_selected_cuenta()
            cantidad = simpledialog.askfloat("Ingresar efectivo", "Ingrese la cantidad de efectivo:")
            cuenta.ingresar_efectivo(cantidad)
            messagebox.showinfo("Operación exitosa", f"Se ingresó {cantidad} de efectivo a la cuenta {cuenta.num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def retirar_efectivo(self):
        try:
            cuenta = self.get_selected_cuenta()
            cantidad = simpledialog.askfloat("Retirar efectivo", "Ingrese la cantidad de efectivo:")
            cuenta.retirar_efectivo(cantidad)
            messagebox.showinfo("Operación exitosa", f"Se retiró {cantidad} de efectivo de la cuenta {cuenta.num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def depositar_a_otra_cuenta(self):
        try:
            cuenta_origen = self.get_selected_cuenta()
            num_cuenta_destino = simpledialog.askstring("Depositar a otra cuenta", "Ingrese el número de cuenta de destino:")
            cuenta_destino = None
            for cuenta in self.cuentas:
                if cuenta.num_cuenta == num_cuenta_destino:
                    cuenta_destino = cuenta
                    break
            if cuenta_destino is None:
                raise ValueError("No se encontró una cuenta con el número especificado.")
            cantidad = simpledialog.askfloat("Depositar a otra cuenta", "Ingrese la cantidad de efectivo a depositar:")
            cuenta_origen.depositar_a_otra_cuenta(cuenta_destino, cantidad)
            messagebox.showinfo("Éxito", "Efectivo depositado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except TypeError:
            pass

app = CajaPopularApp([])
app.run()

