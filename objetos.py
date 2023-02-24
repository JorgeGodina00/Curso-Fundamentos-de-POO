
from Personaje import *
#1.-Solicitar Datos
print("")
print("- Datos Heroe -")
especieH = input("Escribe el espacie del heroe: ")
nombreH = input("Escribe el nombre del heroe: ")
alturaH = float(input("Escribe la altura del heroe: "))
recargaH = int(input("Cuantas balas recargas al heroe: "))

print("")
print("- Datos Villano -")
especieV = input("Escribe la especie del villano: ")
nombreV = input("Escribe la especie del villano: ")
AlturaV = float(input("Ecribe la altura del villano: "))
recargaV = int(input("Cuantas balas recargas al VILLANO: "))

#2.- Crear objeto de clase Persoanje
heroe = Personaje(especieH, nombreH, alturaH)
villano = Personaje(especieV, nombreV, AlturaV)

#3. Usar atributos
#Ejemplo de metodo con set
#heroe.set()
print("")
print("- Objeto Heroe -")
print("El personaje se llama: "+ heroe.get_Nombre())
print("Pertenece a la especie: "+ heroe.get_Especie())
print("Y tiene una altura de: "+ str(heroe.get_Altura() ))
heroe.correr(True)
heroe.LanzarGranadas()
heroe.RecargarArmas(recargaH)

print("")
print("- Objeto Villano -")
print("El personaje se llama: "+ villano.get_Nombre())
print("Pertenece a la especie: "+ villano.get_Especie())
print("Y tiene una altura de: "+ str(villano.get_Altura() ))



