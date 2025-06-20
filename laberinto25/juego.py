import copy
from laberinto25.laberinto import Laberinto
from laberinto25.bicho import Bicho
from laberinto25.habitacion import Habitacion
from laberinto25.puerta import Puerta
from laberinto25.norte import Norte
from laberinto25.sur import Sur
from laberinto25.este import Este
from laberinto25.oeste import Oeste
from laberinto25.orientacion import Orientacion
from laberinto25.agresivo import Agresivo
from laberinto25.perezoso import Perezoso
from laberinto25.pared import Pared
from laberinto25.bomba import Bomba
from laberinto25.pared_bomba import ParedBomba
from laberinto25.ente import Personaje
from laberinto25.faseJuego import *
import threading

class Juego:
    def __init__(self):
        self.habitaciones = {}
        self.bichos = []
        self.prototipo = None
        self.personaje=None
        self.bicho_threads = {}
        self.fase: FaseJuego = FaseInicial()
    
    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)

    

    def agregar_bicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)

    def lanzarBicho(self, bicho):
        thread = threading.Thread(target=bicho.actua)
        if hash(bicho) not in self.bicho_threads:
            self.bicho_threads[hash(bicho)] = thread
            thread.start()

    def lanzarPersonaje(self):
        thread = threading.Thread(target=self.personaje.actua)
        self.personaje.thread = thread
        thread.start()

    def terminarBicho(self, bicho):
        if hash(bicho) in self.bicho_threads:
            self.eliminarBicho(bicho)
            

    def eliminarBicho(self, bicho):
        if bicho in self.bichos:
             self.bichos.remove(bicho)
        for hab in self.laberinto.hijos:
            if bicho in hab.entidades:
                hab.salir(bicho)

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregar_personaje(self, nombre):
        self.personaje = Personaje(10, 1, self, nombre)
        self.laberinto.entrar(self.personaje)

    def buscarPersonaje(self,bicho):
        if bicho.posicion == self.personaje.posicion:
            self.personaje.esAtacadoPor(bicho)

    def buscarBicho(self, bicho):
        pass
                
    def abrir_puertas(self):
        def abrirPuertas(obj):
            if obj.esPuerta():
                obj.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrar_puertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto
    
    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())

        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.ponerElementoEnOrientacion(bomba1, Este())

        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.ponerElementoEnOrientacion(bomba2, Oeste())

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crearLaberinto4Hab(self, creator):
        laberinto = creator.crear_laberinto()

        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        habitacion3 = creator.crear_habitacion(3)
        habitacion4 = creator.crear_habitacion(4)

        puerta12 = creator.crear_puerta(habitacion1, habitacion2)
        puerta13 = creator.crear_puerta(habitacion1, habitacion3)
        puerta24 = creator.crear_puerta(habitacion2, habitacion4)
        puerta34 = creator.crear_puerta(habitacion3, habitacion4)

        habitacion1.ponerElementoEnOrientacion(puerta12, Sur())
        habitacion1.ponerElementoEnOrientacion(puerta13, Este())
        habitacion3.ponerElementoEnOrientacion(puerta13, Oeste())
        habitacion3.ponerElementoEnOrientacion(puerta34, Sur())
        habitacion2.ponerElementoEnOrientacion(puerta12, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta24, Este())
        habitacion4.ponerElementoEnOrientacion(puerta34, Norte())
        habitacion4.ponerElementoEnOrientacion(puerta24, Oeste())

        bicho1 = creator.crear_bicho(5, 10, habitacion1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, habitacion3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, habitacion2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, habitacion4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        habitacion1.bicho = bicho1
        habitacion2.bicho = bicho2
        habitacion3.bicho = bicho3
        habitacion4.bicho = bicho4

        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        laberinto.agregarHabitacion(habitacion3)
        laberinto.agregarHabitacion(habitacion4)

        return laberinto

    def terminarJuego(self, ui):
        self.fase.finalizar(self, ui)
