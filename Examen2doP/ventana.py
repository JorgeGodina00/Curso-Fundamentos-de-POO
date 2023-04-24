import random
import datetime

class Matricula:
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
       
        self.anio_nacimiento = anio_nacimiento
        self.carrera = carrera
        
    def generar_matricula(self):
        anio_actual= datetime.datetime.now().year % 100
        anio_nacimiento = str(self.anio_nacimiento)[2:]
        letra_nombre = self.nombre[0].upper()
        letras_apellido_paterno = self.apellido_paterno[:3].upper()
        letras_apellido_materno = self.apellido_materno[:3].upper()
        numeros_aleatorios = str(random.randint(100, 999))
        letras_carrera = self.carrera[:3].upper()
        
        return f"{letras_carrera}{anio_actual}{anio_nacimiento}{letra_nombre}{letras_apellido_paterno}{letras_apellido_materno}{numeros_aleatorios}"
