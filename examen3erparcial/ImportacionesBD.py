from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBDIMPO import *

controlador = controladorBDIMPO()

#InsertarRegistro
def ejecutaInsert():
    controlador.guardarImportacion(varMat.get(), varPais.get())
    varMat.set("")
    varPais.set("")
    
    
#Consultar x Pais
def ejecutaSelectU():
    rsMateriales = controlador.consultarPais(varPais.get())

    if rsMateriales:
        textBus.delete("1.0","end")
       
        Material_data = f"IDMAT: {rsMateriales[0][1]}"
        textBus.insert(tk.INSERT, Material_data) 
    
    else:
        messagebox.showinfo("CUIDADO", "Registro no hallado en la BD")
        textBus.delete("1.0","end")
        return
    
#ConsultarTodos
def ejecutaSelectA():
    rsMateriales = controlador.consultarMateriales()
   
    tree.delete(*tree.get_children())
    # Insertamos los datos en el treeview
    for usuario in rsMateriales:
        tree.insert("", tk.END, values=usuario)
    return


 
#Eliminar Registro
def ejecutaDelete():
    controlador.eliminarMaterial(varBuseliminar.get())  
    textBus.delete("1.0","end")
    varBuseliminar.set("")
    return


            

def limpiarCampos():
  
    txtCor.delete(0, END)
    txtCon.delete(0, END)
    textBus.delete("1.0","end")
    return
 


ventana = Tk()
ventana.title("CRUD de Materiales Chiquito")
ventana.geometry("650x400")


panel = ttk.Notebook(ventana, style='TNotebook')
panel.pack(fill="both", expand="yes")


estilo = ttk.Style()
estilo.configure('TNotebook', tabposition='n')


pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)



panel.add(pestana1, text="Insertar Registro")
panel.add(pestana2, text="Buscar x Pais")
panel.add(pestana3, text="Consultar Registros")
panel.add(pestana5, text="Eliminar Registro")



titulo1 = Label(pestana1, text="Insertar registro", font=("Arial", 20, "bold"))
titulo1.pack(pady=10)


varMat = tk.StringVar()
lblCor = Label(pestana1, text="Material: ")
lblCor.pack(padx=5)
txtCor = Entry(pestana1, textvariable=varMat, width=30)
txtCor.pack()

lblCon = Label(pestana1, text="Pais: ")
lblCon.pack(pady=5)
varPais = tk.StringVar()
txtCon = Entry(pestana1, textvariable=varPais, width=30)
txtCon.pack()

btnGuardar = Button(pestana1, text="Guardar Registro", command=ejecutaInsert, bg="#008CBA", fg="white")
btnGuardar.pack(pady=10)

btnLimpiar = Button(pestana1, text="Limpiar Campos", command=limpiarCampos, bg="#008CBA", fg="white")
btnLimpiar.pack(pady=10)


# Creamos los elementos para la pestaña 2 (Buscar usuario)
titulo2= Label(pestana2, text="Buscar x Pais", font=("Arial", 20, "bold"))
titulo2.pack(pady=10)

varBus = tk.StringVar()
lblid = Label(pestana2, text="Pais: ")
lblid.pack(pady=5)

txtid = Entry(pestana2, textvariable=varBus, width=30)
txtid.pack()

btnBusqueda = Button(pestana2, text="Buscar Pais", command=ejecutaSelectU, bg="#008CBA", fg="white")
btnBusqueda.pack(pady=10)


subBus= Label(pestana2, text="IDMaterial: ", font=("Arial", 10, "bold"))   
subBus.pack()

textBus = Text(pestana2, width=40, height=5)
textBus.pack(pady=10)



titulo3 = Label(pestana3, text="Consultar Registros", font=("Arial", 20, "bold"))
titulo3.pack(pady=10)

#Treeview
tree = ttk.Treeview(pestana3, columns=(1,2,3), show="headings", height="5")
tree.pack()

#Treeview
tree.heading(1, text="IDMAT")
tree.heading(2, text="Mercancia")
tree.heading(3, text="Pais")


btnConsulta = Button(pestana3, text="Consultar Registros", command=ejecutaSelectA, bg="#008CBA", fg="white")
btnConsulta.pack(pady=10)



titulo5 = Label(pestana5, text="Eliminar Registro", font=("Arial", 20, "bold"))
titulo5.pack(pady=10)

varBuseliminar = tk.StringVar()
lblid = Label(pestana5, text="Identificador de Mercancia:")
lblid.pack(pady=5)
    
txtid = Entry(pestana5, textvariable=varBuseliminar, width=30)
txtid.pack()

# Creamos un botón para eliminar un usuario
btnEliminar = Button(pestana5, text="Eliminar Registro:", command=ejecutaDelete, bg="#008CBA", fg="white")
btnEliminar.pack(pady=10)



ventana.mainloop()