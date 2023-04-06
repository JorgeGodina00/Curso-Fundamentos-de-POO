from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3
import bcrypt 
          
class controladorBD:
    
    def __init__(self):
        pass
        
    #1. preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/JABOW/Documents/GitHub/Curso-Fundamentos-de-POO/tkintersqlite/DBUsuarios.db")
            print("conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
      
    #Metodo para Insertar      
    def guardarUsuario(self, nom, cor, con):
        #1. llamar a la conexion
        conx = self.conexionBD()
        
        #2. Revisar parametros vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas!!", "Revisa este show")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            conH= self.encriptarCon(con)
            
            #validad si el correo ya esta registrado
            sqlSelect = "select * from TBRegistrados where Correo=?"
            cursor.execute(sqlSelect, (cor,))
            rsUsuario = cursor.fetchall()
            
            if len(rsUsuario) > 0:
                messagebox.showerror("Error", "El correo ya esta registrado")
                return
            
            datos = (nom, cor, conH)
            qrInsert = "insert into TBRegistrados(Nombre, Correo, Contraseñas) values(?,?,?)"
            
            #4. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Registro", "Registro exitoso")
            
    #Metodo para encryptar
    def encriptarCon(self, con):
        conPlana= con
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt()
        
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa
    
    def consultarUsuario(self, id):
        #1. preparar la conexion
        conx= self.conexionBD()
            
        #2. verificar el ID no este vacio
        if id =="":
            messagebox.showwarning("Cuidado", "Id vacio con escribe un valor")
         
            return
        else:
            try:
                #4. Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from TBRegistrados where id=?"
                    
                #5. Ejecutar la consulta y recuperar los datos
                cursor.execute(sqlSelect, (id,))
                rsUsuario = cursor.fetchall()
                
                #6. cerrar conexion y devolver los datos
                print(rsUsuario)
                conx.close()
                return rsUsuario
            except Exception as ex:
                messagebox.showwarning("Error", str(ex))
                conx.close()
                return None
            
    def consultarUsuarios(self):
        #1. preparar la conexion
        conx= self.conexionBD()
        
        #2. Preparar lo necesario para el select
        cursor= conx.cursor()
        sqlSelect="select * from TBRegistrados"
                
                #3. Ejecutar la consulta y recuperar los datos
        cursor.execute(sqlSelect)
        rsUsuarios = cursor.fetchall()
                
        #4. cerrar conexion y devolver los datos
        #print(rsUsuarios)
        conx.close()
        return rsUsuarios

    def actualizarUsuario(self, id, nom, cor, con):
        #1. preparar la conexion
        conx= self.conexionBD()
        
        #2. Revisar parametros vacios
        if(id == "" or nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas!!", "Revisa este show")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            datos = (nom, cor, con, id)
            qrUpdate = "update TBRegistrados set Nombre=?, Correo=?, Contraseñas=? where id=?"
            
            #4.verificamos que el Usuario exista en la base de datos
            sqlSelect = "select * from TBRegistrados where id=?"
            cursor.execute(sqlSelect, (id,))
            rsUsuario = cursor.fetchall()

            if len(rsUsuario) == 0:
                messagebox.showerror("Error", "Usuario no encontrado en la base de datos")
                return
            
            #5. confirmacion de guardad cambios
            confirmacion = messagebox.askquestion("Actualizar", "¿Estas seguro de guardar los cambios?")
            if confirmacion == "no":
                return    
            
            #6. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrUpdate, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Actualización", "Actualización exitosa")
            
            return None
        

    def eliminarUsuario(self, id):
        #1. preparar la conexion
        conx= self.conexionBD()
            
        #2. Revisar parametros vacios
        if(id == ""):
            messagebox.showwarning("Aguas!!", "Revisa este show")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            datos = (id,)
            qrDelete = "delete from TBRegistrados where id=?"
            
            #4.confirmacion de eliminar usuario
            confirmacion = messagebox.askquestion("Eliminar", "¿Estas seguro de eliminar el usuario?")
            if confirmacion == "no":
                return  
            
            #5. verificamos si el usuario aun existe en nuestra base de datos
            sqlSelect = "select * from TBRegistrados where id=?"
            cursor.execute(sqlSelect, (id,))
            rsUsuario = cursor.fetchall()

            if len(rsUsuario) == 0:
                messagebox.showerror("Error", "El usuario no existe")
                return

            #6. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrDelete, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Eliminación", "Eliminación exitosa")
            
            return None

