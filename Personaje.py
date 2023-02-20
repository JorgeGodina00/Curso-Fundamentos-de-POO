class Personaje:
    #atributos Persoanje
    especie = "Humano"
    nombre = "Master Chief"
    altura = "2.70"

#Metodos del Personaje

def correr(self, status):
    if(status):
        print("El persoanje " +self.nombre + " esta corriendo")
    else:
        print("El personaje "+self.nombre +" se detuvo")    

def lanzarGranadas(self,  municiones):
    print("El personaje "+self.nombre +" lanzo una granada")

def recargarArma(self, municiones):
    cargador = 10
    cargador = cargador+municiones
    print("El arma tiene: "+cargador+" balas")
        