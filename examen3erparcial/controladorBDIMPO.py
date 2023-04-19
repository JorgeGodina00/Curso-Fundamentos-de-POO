from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

class controladorBDIMPO:
    
    def __init__(self):
        pass
        
    #Conexion con BD
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/JABOW/Documents/GitHub/Curso-Fundamentos-de-POO/examen3erparcial/BDImportaciones.db")
            print("conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
      
    #Metodo para Insertar      
    def guardarImportacion(self, merc, pais):
        
        conx = self.conexionBD()
        
        #Revisar parametros vacios
        if(merc == "" or pais == ""):
            messagebox.showwarning("Los campos se encuentran vacios", "Vuelve a insertar los datos correctamente")
            conx.close()
        else:
           
            cursor = conx.cursor()
                                                                      
            datos = (merc, pais)
            qrInsert = "insert into TB_Europa(Mercancia, Pais) values(?,?)"
            
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Registro", "El Registro se ha realizado de forma exitosa")
            
   
    
    #Consultar x Pais   
    def consultarPais(self, pais):
        #1. preparar la conexion
        conx= self.conexionBD()
            
        #2. verificar el ID no este vacio
        if pais =="":
            messagebox.showwarning("Cuidado", "Campo Vacio, Inserte un Dato")
         
            return
        else:
            try:
                #4. Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from TB_Europa where Pais=?"
                    
                #5. Ejecutar la consulta y recuperar los datos
                cursor.execute(sqlSelect, (pais,))
                rsMateriales = cursor.fetchall()
                
                #6. cerrar conexion y devolver los datos
                print(rsMateriales)
                conx.close()
                return rsMateriales
            except Exception as ex:
                messagebox.showwarning("Error", str(ex))
                conx.close()
                return None
    
    #Consultar Todos los Materiales        
    def consultarMateriales(self):
       
        conx= self.conexionBD()
        
     
        cursor= conx.cursor()
        sqlSelect="select * from TB_Europa"
                
             
        cursor.execute(sqlSelect)
        rsUsuarios = cursor.fetchall()
                
        
        conx.close()
        return rsUsuarios

    

    def eliminarMaterial(self, id):
        #1. preparar la conexion
        conx= self.conexionBD()
            
        #2. Revisar parametros vacios
        if(id == ""):
            messagebox.showwarning("CUIDADO", "Llena bien el campo")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            datos = (id,)
            qrDelete = "delete from TB_Europa where IDMAT=?"
            
            #4.confirmacion de eliminar usuario
            confirmacion = messagebox.askquestion("ELIMINAR", "¿Estas seguro de eliminar el Registro?")
            if confirmacion == "no":
                return  
            
            #5. verificamos si el usuario aun existe en nuestra base de datos
            sqlSelect = "select * from TB_Europa where IDMAT=?"
            cursor.execute(sqlSelect, (id,))
            rsUsuario = cursor.fetchall()

            if len(rsUsuario) == 0:
                messagebox.showerror("Error", "El Registro no existe")
                return

            #6. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrDelete, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Eliminado", "Se ha eliminiado el Registro de forma exitosa")
            
            return None

