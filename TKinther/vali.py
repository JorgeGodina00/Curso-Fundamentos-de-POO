class Validador:
    def __init__(self, correo, contrasenia):
        self.correo = correo
        self.contrasenia = contrasenia
    
    def validar_campos_vacios(self):
        if not self.correo or not self.contrasenia:
            return False
        else:
            return True
        
    def validar_credenciales(self):
        if self.correo == "121041136@upq.edu.mx" and self.contrasenia == "12345":
            return True
        else:
            return False
