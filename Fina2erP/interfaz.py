from tkinter import *
from tkinter import ttk
from logica import RomanArabicConverter
from tkinter import messagebox


convertir = RomanArabicConverter()


class ConvertirGUI:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de números romanos y arábigos")
        master.geometry("400x300")

        
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)

        
        self.panel1 = ttk.Frame(self.notebook)
        self.notebook.add(self.panel1, text="Romano a arábigo")

        self.panel2 = ttk.Frame(self.notebook)
        self.notebook.add(self.panel2, text="Arábigo a romano")

      
        self.labelTitulo = Label(self.panel1, text="Convertir de romano a arábigo", fg="green")
        self.labelTitulo.pack(pady=10)

        self.labelIngresar = Label(self.panel1, text="Insertar número romano", fg="green")
        self.labelIngresar.pack(pady=10)

        self.romano_ingresar = StringVar()
        self.entryRomano = Entry(self.panel1, textvariable=self.romano_ingresar)
        self.entryRomano.pack(pady=5)

        self.botonIngresar = Button(self.panel1, text="Convertir", command=self.romano_arabigo, bg="green", fg="white")
        self.botonIngresar.pack(pady=10)

        
        self.labelTitulo = Label(self.panel2, text="Convertir de arábigo a romano", fg="red")
        self.labelTitulo.pack(pady=10)

        self.labelIngresar = Label(self.panel2, text="Insertar número arábigo", fg="red")
        self.labelIngresar.pack(pady=10)

        self.arabigo_ingresar = StringVar()
        self.entryArabigo = Entry(self.panel2, textvariable=self.arabigo_ingresar)
        self.entryArabigo.pack(pady=5)

        self.botonIngresar = Button(self.panel2, text="Convertir", command=self.arabigo_romano, bg="red", fg="white")
        self.botonIngresar.pack(pady=10)


    def romano_arabigo(self):
        numero_romano = self.romano_ingresar.get()
     
        try:
            numero_romano = int(numero_romano)
            messagebox.showerror("Error", "El campo no es un número romano")
            return
        except:
            pass
        convertir.roman_to_arabic(numero_romano)

    def arabigo_romano(self):
        numero_arabigo = self.arabigo_ingresar.get()
       
        if numero_arabigo == "":
            messagebox.showerror("Error", "El campo esta vacio")
            return
        
        try:
            numero_arabigo = int(numero_arabigo)
        except:
            messagebox.showerror("Error", "El campo no es un número arábigo")
            return

        convertir.arabic_to_roman(numero_arabigo)


if __name__ == '__main__':
    root = Tk()
    my_menu = ConvertirGUI(root)
    root.mainloop()
