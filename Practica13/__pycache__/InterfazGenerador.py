from tkinter import *



Interfaz = Tk()
Interfaz.title("Generador de Contraseñas Perron")
Interfaz.geometry("450x450")

Frame1 = Frame(Interfaz)
Frame1.pack(expand = True, fill = "both")
Titulo = Label(Frame1, text = "Generador de Contraseñas Perronas", bg= "white", fg = "black", font=("Helevetica", 18)).pack()

lblContraseña = Label(Frame1, text = "Contraseña Generada: ", bg= "white", fg = "black", font=("Helevetica", 18)).pack()






Interfaz.mainloop()