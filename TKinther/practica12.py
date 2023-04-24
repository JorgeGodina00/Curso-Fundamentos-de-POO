from tkinter import *
from tkinter import messagebox
from vali import Validador

class Ventana:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")
        self.master.resizable(0, 0)
        
        self.lbl_email = Label(self.master, text="Correo electrónico:")
        self.lbl_email.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        self.entry_email = Entry(self.master)
        self.entry_email.grid(row=0, column=1, padx=5, pady=5)
        
        self.lbl_password = Label(self.master, text="Contraseña:")
        self.lbl_password.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.entry_password = Entry(self.master, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_login = Button(self.master, text="Iniciar sesión", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=10)
        
    def login(self):
        correo = self.entry_email.get()
        contrasenia = self.entry_password.get()
        
        validador = Validador(correo, contrasenia)
        
        if not validador.validar_campos_vacios():
            messagebox.showerror("Error", "Debe ingresar correo y contraseña")
        elif not validador.validar_credenciales():
            messagebox.showerror("Error", "Correo o contraseña incorrectos")
        else:
            messagebox.showinfo("Bienvenido", "Bienvenido al sistema!")
root = Tk()
ventana = Ventana(root)
root.mainloop()