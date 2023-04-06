from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import *

# Creamos una instancia de tipo controlador
controlador = controladorBD()

# Procedemos a Guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())
    varNom.set("")
    varCor.set("")
    varCon.set("")
    
    
#Funcion para buscar un Usuario
def ejecutaSelectU():
    rsUsuario = controlador.consultarUsuario(varBus.get())

    if rsUsuario:
        textBus.delete("1.0","end")
        # usuario_data = str(rsUsuario[0])
        # Extraemos solamente nombre y correo
        usuario_data = f"Nombre: {rsUsuario[0][1]}\nCorreo: {rsUsuario[0][2]}"
        textBus.insert(tk.INSERT, usuario_data) 
    
    else:
        messagebox.showinfo("Ojito", "Usuario no registrado en la BD")
        textBus.delete("1.0","end")
        return
    
# Definimos una función para consultar todos los usuarios en la base de datos
def ejecutaSelectA():
    rsUsuarios = controlador.consultarUsuarios()
    # Limpiamos el treeview
    tree.delete(*tree.get_children())
    # Insertamos los datos en el treeview
    for usuario in rsUsuarios:
        tree.insert("", tk.END, values=usuario)
    return

# Funcion para actualizar un usuario    
def ejecutaUpdate():
    controlador.actualizarUsuario(varid2.get(), varNom2.get(), varCor2.get(), varCon2.get())
    textBus.delete("1.0","end")
    varid2.set("")
    varNom2.set("")
    varCor2.set("")
    varCon2.set("")
    return
 
# Funcion para eliminar un usuario
def ejecutaDelete():
    controlador.eliminarUsuario(varBuseliminar.get())  
    textBus.delete("1.0","end")
    varBuseliminar.set("")
    return


            
# Funcion para limpiar los campos   
def limpiarCampos():
    txtNom.delete(0, END)
    txtCor.delete(0, END)
    txtCon.delete(0, END)
    textBus.delete("1.0","end")
    return
 

# Creamos la ventana principal
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("650x400")

# Creamos el Notebook
panel = ttk.Notebook(ventana, style='TNotebook')
panel.pack(fill="both", expand="yes")

# Creamos un estilo para el Notebook
estilo = ttk.Style()
estilo.configure('TNotebook', tabposition='n')

# Creamos las pestañas
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)


# Agregamos las pestañas al Notebook
panel.add(pestana1, text="Formulario de usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuario")
panel.add(pestana5, text= "Eliminar Usuario")


# Pestaña1: Formulario de Usuario
titulo1 = Label(pestana1, text="Formulario de usuario", font=("Arial", 20, "bold"), bg = '#535e57')
titulo1.pack(pady=10)

varNom = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ")
lblNom.pack(pady=5)
txtNom = Entry(pestana1, textvariable=varNom, width=30)
txtNom.pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ")
lblCor.pack(padx=5)
txtCor = Entry(pestana1, textvariable=varCor, width=30)
txtCor.pack()

lblCon = Label(pestana1, text="Contraseña:")
lblCon.pack(pady=5)
varCon = tk.StringVar()
txtCon = Entry(pestana1, textvariable=varCon, width=30, show="*")
txtCon.pack()

btnGuardar = Button(pestana1, text="Guardar usuario", command=ejecutaInsert, bg="#008CBA", fg="white")
btnGuardar.pack(pady=10)

btnLimpiar = Button(pestana1, text="Limpiar campos", command=limpiarCampos, bg="#008CBA", fg="white")
btnLimpiar.pack(pady=10)


# Creamos los elementos para la pestaña 2 (Buscar usuario)
titulo2= Label(pestana2, text="Buscar usuario", font=("Arial", 20, "bold"), bg = '#d2f5e0')
titulo2.pack(pady=10)

varBus = tk.StringVar()
lblid = Label(pestana2, text="Identificador de Usuario: ")
lblid.pack(pady=5)

txtid = Entry(pestana2, textvariable=varBus, width=30)
txtid.pack()

btnBusqueda = Button(pestana2, text="Buscar usuario", command=ejecutaSelectU, bg="#008CBA", fg="white")
btnBusqueda.pack(pady=10)


subBus= Label(pestana2, text="Usuario: ", font=("Arial", 10, "bold"), bg = '#0c0261')   
subBus.pack()

textBus = Text(pestana2, width=40, height=5)
textBus.pack(pady=10)


# Creamos los elementos para la pestaña 3 (Consultar usuarios)
titulo3 = Label(pestana3, text="Consultar usuarios", font=("Arial", 20, "bold"), bg= '#c6c6c5')
titulo3.pack(pady=10)

# Creamos un Treeview
tree = ttk.Treeview(pestana3, columns=(1,2,3), show="headings", height="5")
tree.pack()

# Creamos las columnas del Treeview
tree.heading(1, text="ID")
tree.heading(2, text="Nombre")
tree.heading(3, text="Correo")

# Creamos un botón para consultar todos los usuarios
btnConsulta = Button(pestana3, text="Consultar usuarios", command=ejecutaSelectA, bg="#008CBA", fg="white")
btnConsulta.pack(pady=10)

# Creamos los elementos para la pestaña 4 (Actualizar usuario)
titulo4 = Label(pestana4, text="Actualizar usuario", font=("Arial", 20, "bold"))
titulo4.pack(pady=10)

varid2 = tk.StringVar()
lblid = Label(pestana4, text="Identificador de Usuario: ")
lblid.pack(pady=5)

txtid = Entry(pestana4, textvariable=varid2, width=30)
txtid.pack()

varNom2 = tk.StringVar()
lblNom = Label(pestana4, text="Nombre: ")
lblNom.pack(pady=5)
txtNom = Entry(pestana4, textvariable=varNom2, width=30)
txtNom.pack()


varCor2 = tk.StringVar()
lblCor = Label(pestana4, text="Correo: ")
lblCor.pack(padx=5)
txtCor = Entry(pestana4, textvariable=varCor2, width=30)
txtCor.pack()

lblCon = Label(pestana4, text="Contraseña:")
lblCon.pack(pady=5)
varCon2 = tk.StringVar()
txtCon = Entry(pestana4, textvariable=varCon2, width=30, show="*")
txtCon.pack()

btnActualizar = Button(pestana4, text="Actualizar usuario", command=ejecutaUpdate, bg="#008CBA", fg="white")
btnActualizar.pack(pady=10)

btnLimpiar = Button(pestana4, text="Limpiar campos", command=limpiarCampos, bg="#008CBA", fg="white")
btnLimpiar.pack(pady=10)

# Creamos los elementos para la pestaña 5 (Eliminar usuario)
titulo5 = Label(pestana5, text="Eliminar usuario", font=("Arial", 20, "bold"))
titulo5.pack(pady=10)

varBuseliminar = tk.StringVar()
lblid = Label(pestana5, text="Identificador de Usuario: ")
lblid.pack(pady=5)
    
txtid = Entry(pestana5, textvariable=varBuseliminar, width=30)
txtid.pack()

# Creamos un botón para eliminar un usuario
btnEliminar = Button(pestana5, text="Eliminar usuario", command=ejecutaDelete, bg="#008CBA", fg="white")
btnEliminar.pack(pady=10)



ventana.mainloop()