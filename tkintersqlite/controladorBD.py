from tkinter import messagebox
import sqlite3
import bcrypt 

class controladorBD:
    
    def __init__(self):
        pass
        
    #1. preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/reach/OneDrive/Documentos/POO184/tkinterSqlite/DBUsuarios.db")
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
        