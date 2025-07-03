import tkinter as tk
from laberinto25.director import Director
from laberinto25.point import Point
from laberinto25.visitor import Visitor
import laberinto25.estado_puerta as estado_puerta
import laberinto25.UI_visitor as vs
import laberinto25.event_manager as em
import threading
import tkinter as tk

class UserInterface:
    def __init__(self, laberinto_file):
        self.laberinto_file = laberinto_file
        self.juego = None
        self.event_manager = None
        self.event_listener = None        
        self.visitor = vs.MazeUIVisitor(self)
        self.load_laberinto()
        self.setup_event_manager()

    def load_laberinto(self):
        director = Director()
        director.procesar(self.laberinto_file)
        self.juego = director.obtenerJuego()
        self.juego.fase.iniciar(self.juego)
    
    def setup_event_manager(self):
        self.event_manager = em.EventManager()
        self.event_listener = em.EventListener(self)
        self.event_manager.add_listener(self.event_listener)
        [bicho.agregarEvent_manager(self.event_manager) for bicho in self.juego.bichos]
        self.juego.personaje.agregarEvent_manager(self.event_manager)

    def dibujarHabitacion(self, hab):
        pass

    def init_ui(self):
        pass
    def dibujarPuerta(self, puerta):
        pass

    def dibujarPersonaje(self, personaje):
        pass

    def dibujarBicho(self, bicho):
        pass

    def dibujarLaberinto(self, laberinto):
        pass

    def dibujarRectangulo(self, forma):
        pass

    def dibujarOrientacion(self, orientacion):
        pass

    def dibujarPared(self, pared):
        pass

    def dibujarCaminar(self, ente):
        pass

    def dibujarBichoMuere(self, data):
        pass

    def derrota(self):
        pass

    def victoria(self):
        pass

    def draw_atacado(self, ente):
        pass