class Personaje:
    # definimos el constructor del personaje y los encapsulamos
    def __init__(self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt

    # Métodos Personaje
    def correr(self, status):
        if status:
            print("El personaje " + self.__nombre + " está corriendo")
        else:
            print("El personaje " + self.__nombre + " se detuvo")

    def lanzarGranadas(self):
        print("El personaje " + self.__nombre + " lanzó una granada")

    def recargarArma(self, municiones):
        cargador = 10
        cargador += municiones
        print("El arma tiene " + str(cargador) + " balas")

    def __pensar(self):
        print("El personaje " + self.__nombre + " está pensando")
        
    # getters y setters de atributos encapsulados
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nom):
        self.__nombre = nom
    
    def getEspecie(self):
        return self.__especie

    def setEspecie(self, esp):
        self.__especie = esp
    
    def getAltura(self):
        return self.__altura

    def setAltura(self, alt):
        self.__altura = alt
        