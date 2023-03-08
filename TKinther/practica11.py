from tkinter import Tk, Button, Frame, messagebox
from playsound import playsound
import threading

pista = "russia-national-anthem-russian-english-lyrics.mp3"
def play_30():
    thread = threading.Thread(target=playsound, args=("pista"))
    thread.start()


#funciones
def mostrarMensajes(): #<las funciones en python van con def
    messagebox.showinfo("Hola gei","Presionaste el boton azul", icon = "error")
    messagebox.showerror("Error: ", "Todo fallo con exito")
    print(messagebox.askokcancel("Pregunta:","¿Ella estuvo jugando con tu corazon?"))
     
#6.- Funcion agregar botones

def agregar_boton():
     botonVerde.config(text = "+", bg = "green", fg = "white")   
     botonNuevo = Button(seccion3, text = "Nuevo")
     botonNuevo.pack()

#1.- Instanciamos el objeto ventana
ventana =  Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2.- agregamos los Frames
seccion1 = Frame(ventana, bg = "white")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(ventana, bg = "blue")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg = "red")
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