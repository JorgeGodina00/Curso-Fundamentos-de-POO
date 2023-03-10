import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de contraseñas")

        self.password_length = tk.IntVar()
        self.password_length.set(8)
        self.include_uppercase = tk.BooleanVar()
        self.include_special_characters = tk.BooleanVar()
        self.password_strength = tk.StringVar()
        self.password_strength.set("Débil")

        tk.Label(self.root, text="Longitud de contraseña:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.password_length, width=5).grid(row=0, column=1, padx=10, pady=10)

        tk.Checkbutton(self.root, text="Incluir mayúsculas", variable=self.include_uppercase).grid(row=1, column=0, padx=10, pady=10)
        tk.Checkbutton(self.root, text="Incluir caracteres especiales", variable=self.include_special_characters).grid(row=2, column=0, padx=10, pady=10)

        tk.Button(self.root, text="Generar contraseña", command=self.generate_password).grid(row=3, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Fortaleza de la contraseña:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.root, textvariable=self.password_strength).grid(row=4, column=1, padx=10, pady=10)
        
        
    def generate_password(self):
        length = self.password_length.get()
        include_uppercase = self.include_uppercase.get()
        include_special_characters = self.include_special_characters.get()

        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_special_characters:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))
        self.check_password_strength(password)
        messagebox.showinfo("Contraseña generada", f"La contraseña generada es: {password}")
        

    def check_password_strength(self, password):
        if len(password) < 8:
            self.password_strength.set("Débil")
        elif len(password) < 12:
            self.password_strength.set("Media")
        else:
            self.password_strength.set("Fuerte")

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()