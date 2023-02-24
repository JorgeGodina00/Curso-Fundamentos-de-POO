class Personaje:
    
    #Definimos el constructor de personaje y los encapsulamos
    def __init__(self, esp,nom,alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    #Metodos
    def correr(self, status):
        if(status):
            print("El personaje "+self.__nombre +" esta corriendo")
        else:
            print("El persoanje "+self.__nombre +" se detuvo")
    
    def LanzarGranadas(self):
        print("El persoanje "+self.__nombre +" lanzo granadas a ")
    
    def RecargarArmas(self, municiones):
        cargador = 10
        cargador = cargador + municiones
        print("El arama tiene: "+ str(cargador) + "balas")
    
    def __pensar(self):
        print("A veces pienso....")
    
    def get_Nombre(self):
        return self.__nombre
    
    def set_Nombre(self, nom):
        self.__nombre = nom  
        
    def get_Especie(self):
        return self.__especie
    
    def set_Especie(self, especie):
        self.__especie = especie
    
    def get_Altura(self):
        return self.__altura
    
    def set_Altura(self, altura):
        self.__altura = altura      
        
