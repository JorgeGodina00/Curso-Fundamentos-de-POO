import tkinter as tk
from tkinter import messagebox
from GeneradorPasswords import PasswordGenerator
from application_window import ApplicationWindow

class ApplicationWindow:
    def _init_(self):
        # Creamos la ventana principal
        self.window = tk.Tk()
        self.window.title("Generador de Contraseñas Seguras")
        self.window.geometry("350x250")

        # Creamos los widgets
        self.create_widgets()

    def create_widgets(self):
        # Creamos el título
        self.title_label = tk.Label(
            self.window,
            text="Generador de Contraseñas",
            font=("Arial", 18, "bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Creamos el campo para la longitud de la contraseña
        self.length_label = tk.Label(
            self.window,
            text="Longitud:",
            font=("Arial", 12)
        )
        self.length_label.grid(row=1, column=0)
        self.length_entry = tk.Entry(
            self.window,
            font=("Arial", 12)
        )
        self.length_entry.insert(0, "8")
        self.length_entry.grid(row=1, column=1)

        # Creamos el checkbox para incluir mayúsculas
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(
            self.window,
            text="Incluir Mayúsculas",
            variable=self.uppercase_var,
            font=("Arial", 12)
        )
        self.uppercase_check.grid(row=2, column=0, columnspan=2)

        # Creamos el checkbox para incluir caracteres especiales
        self.special_var = tk.BooleanVar()
        self.special_check = tk.Checkbutton(
            self.window,
            text="Incluir Caracteres Especiales",
            variable=self.special_var,
            font=("Arial", 12)
        )
        self.special_check.grid(row=3, column=0, columnspan=2)

        # Creamos el botón para generar la contraseña
        self.generate_button = tk.Button(
            self.window,
            text="Generar Contraseña",
            command=self.generate_password,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white"
        )
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Creamos el campo de texto para mostrar la contraseña generada
        self.password_label = tk.Label(
            self.window,
            text="Contraseña Generada:",
            font=("Arial", 12)
        )
        self.password_label.grid(row=5, column=0)
        self.password_entry = tk.Entry(
            self.window,
            font=("Arial", 12)
        )
        self.password_entry.grid(row=5, column=1)
        
    def generate_password(self):
        length = int(self.length_entry.get())
        include_uppercase = self.uppercase_var.get()
        include_special = self.special_var.get()
        generator = PasswordGenerator(length, include_uppercase, include_special)
        password = generator.generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        messagebox.showinfo("Generated Password", f"Password: {password}")

    def run(self):
        # ejecutamos con main loop
        self.window.mainloop()
        



