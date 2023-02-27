from tkinter import Tk, Button, Frame, messagebox

#funciones
def mostrarMensajes(): #<las funciones en python van con def
    messagebox.showinfo("Hola gei","Presionaste el boton azul", icon = "error")

#1.- Instanciamos el objeto ventana
ventana =  Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2.- agregamos los Frames
seccion1 = Frame(ventana, bg = "red")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(ventana, bg = "gray")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg = "pink")
seccion3.pack(expand=True, fill='both')

#3.- Agregamos botones
botonAzul = Button(seccion1, text="Boton Azul", fg = "black", bg="blue", command=mostrarMensajes)
botonAzul.place(x = 60, y = 60)

botonNegro = Button(seccion2, text="Boton Negro", fg = "white", bg="black")
botonNegro.grid(row = 0, column = 0)

botonAmarillo = Button(seccion2, text="Boton Amarillo", fg = "black", bg="#ffff4d")
botonAmarillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text="Boton Verde", fg = "black", bg = "#99e699")
botonVerde.configure(height=2, width=10)
botonVerde.pack()

#llamamos al main
ventana.mainloop()