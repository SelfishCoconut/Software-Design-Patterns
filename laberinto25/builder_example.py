from laberinto25.director import Director
from laberinto25.laberinto_builder import LaberintoBuilder
from laberinto25.laberinto import Laberinto
from laberinto25.habitacion import Habitacion
from laberinto25.puerta import Puerta
import time

director = Director()

filename = "./laberintos/lab2HabTunel.json"

data = director.leerArchivo(filename)
if data:
    print("Data from JSON file:")
    print(data)
else:
    print("Failed to read data from JSON file.")

juego = director.procesar(filename)
juego = director.obtenerJuego()
juego.agregar_personaje("Pepe")

# Ejemplo de uso de recorrer con print
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

#mostrar los bichos del juego
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")

juego.abrir_puertas()
juego.lanzarBichos()
time.sleep(15)
juego.terminarBichos()