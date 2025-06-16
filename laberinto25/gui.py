import tkinter as tk
from .director import Director
from .point import Point
import laberinto25.estado_puerta as estado_puerta
import laberinto25.maze_gui_visitor as vs
import laberinto25.event_manager as em
import threading

class MazeGUI:
    def __init__(self, master, laberinto_file):
        self.master = master
        self.laberinto_file = laberinto_file
        self.juego = None
        self.canvas = None
        self.ancho = 0
        self.alto = 0
        self.visuales = {}
        self.event_manager = None
        self.event_listener = None        
        self.load_laberinto()
        self.init_ui()

    def load_laberinto(self):
        director = Director()
        director.procesar(self.laberinto_file)
        self.juego = director.obtenerJuego()
        self.juego.agregar_personaje("Pepe")
        self.juego.abrir_puertas()
        self.master.after(0, self.juego.lanzarPersonaje)
        self.master.after(0, self.juego.lanzarBichos)
    
    def init_ui(self):
        self.master.title("Maze Game")
        self.canvas = tk.Canvas(self.master, width=1150, height=900, bg="white")
        self.canvas.pack()

        self.event_manager = em.EventManager()
        self.event_listener = em.EventListener(self)
        self.event_manager.add_listener(self.event_listener)
        [bicho.agregarEvent_manager(self.event_manager) for bicho in self.juego.bichos]
        self.calcularLaberinto()
        for habitacion in self.juego.laberinto.hijos:
            print("num-punto", habitacion.num, habitacion.forma.punto.x, habitacion.forma.punto.y)
        self.dibujarLaberinto()
        #self.draw_person()
        #self.draw_bichos()

    def calcularLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularTamContenedor()
        self.asignarPuntosReales()

    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self)

    def dibujarRectangulo(self, forma):

        self.master.after(0, lambda: self.visuales.update({
            hash(forma): self.canvas.create_rectangle(
                forma.punto.x, forma.punto.y, 
                forma.punto.x + forma.extent.x, forma.punto.y + forma.extent.y, 
                fill="lightgray"
            )
        }))
        self.master.after(0, lambda: self.canvas.tag_lower(self.visuales[hash(forma)]))

    def draw_person(self):
        
        self.master.after(0, self.juego.personaje.aceptar, self)
    def draw_bicho_muere(self, data):
        if data in self.visuales:
            self.master.after(0, lambda: self.canvas.delete(self.visuales[data]))
    
    def draw_caminar(self, ente):
        self.master.after(0, self._draw_caminar, ente)

    def _draw_caminar(self, ente):
        if self.visuales.get(hash(ente)):
            self.canvas.delete(self.visuales[hash(ente)])
        if ente.posicion.visitado == True: 
            ente.aceptar(self)

    def draw_bichos(self):
        for bicho in self.juego.bichos:
            if bicho.posicion.visitado == True:
                bicho.aceptar(self)

    def calcularPosicion(self):
        habitacion1 = self.juego.obtenerHabitacion(1)
        habitacion1.forma.punto = Point(0, 0)
        for habitacion in self.juego.laberinto.hijos:
            habitacion.calcularPosicion()

    def visitarHabitacion(self, hab):
        if hash(hab.forma) in self.visuales:
            return
        self.dibujarRectangulo(hab.forma)

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        hab1 = puerta.lado1
        hab2 = puerta.lado2

        x1 = hab1.forma.punto.x + hab1.forma.extent.x / 2
        y1 = hab1.forma.punto.y + hab1.forma.extent.y / 2
        x2 = hab2.forma.punto.x + hab2.forma.extent.x / 2
        y2 = hab2.forma.punto.y + hab2.forma.extent.y / 2

        x_medio = (x1 + x2) / 2
        y_medio = (y1 + y2) / 2

        if hab1.forma.punto.x != hab2.forma.punto.x:
            width = 10
            height = 40
        else:
            width = 40
            height = 10

        color = "green" if isinstance(puerta.estadoPuerta, estado_puerta.Abierta) else "red"
        self.canvas.after(0, self.dibujarPuerta, puerta, x_medio, y_medio, width, height, color)

    def dibujarPuerta(self, puerta, x_medio, y_medio, width, height, color):
        self.visuales[hash(puerta)] = self.canvas.create_rectangle(
            x_medio - width / 2, y_medio - height / 2, 
            x_medio + width / 2, y_medio + height / 2, 
            fill=color
        )

    def visitarBomba(self, bomba):
        pass

    def visitarTunel(self, tunel):        
        pass

    def visitarPersonaje(self, personaje):
        if hash(personaje) in self.visuales:
            self.master.after(0, lambda: self.canvas.delete(self.visuales[hash(personaje)]))
        personaje.agregarEvent_manager(self.event_manager)
        habitacion = personaje.posicion
        x = habitacion.forma.punto.x + habitacion.forma.extent.x / 2 - 30
        y = habitacion.forma.punto.y + habitacion.forma.extent.y / 2
        self.visuales[hash(personaje)] = self.canvas.create_oval(
            x - 10, y - 10, x + 10, y + 10, fill="blue"
        )

    def visitarBicho(self, bicho):
        if hash(bicho) in self.visuales:
            self.master.after(0, lambda: self.canvas.delete(self.visuales[hash(bicho)]))
        habitacion = bicho.posicion
        x = habitacion.forma.punto.x + habitacion.forma.extent.x / 2
        y = habitacion.forma.punto.y + habitacion.forma.extent.y / 2

        offset = bicho.posicion.entidades.index(bicho) * 25
        color = "red"
        self.canvas.after(0, lambda: self.visuales.update({
            hash(bicho): self.canvas.create_oval(
                x + offset - 10, y - 10, x + offset + 10, y + 10, fill=color
            )
        }))

    def normalizar(self):
        min_x = min(hab.forma.punto.x for hab in self.juego.laberinto.hijos)
        min_y = min(hab.forma.punto.y for hab in self.juego.laberinto.hijos)

        for hab in self.juego.laberinto.hijos:
            hab.forma.punto.x += abs(min_x)
            hab.forma.punto.y += abs(min_y)

    def calcularTamContenedor(self):
        max_x = max(hab.forma.punto.x for hab in self.juego.laberinto.hijos)
        max_y = max(hab.forma.punto.y for hab in self.juego.laberinto.hijos)

        self.ancho = round(1050 / (max_x + 1))
        self.alto = round(600 / (max_y + 1))

    def asignarPuntosReales(self):
        origen_x, origen_y = 70, 10

        for hab in self.juego.laberinto.hijos:
            hab.forma.punto.x = origen_x + (hab.forma.punto.x * self.ancho)
            hab.forma.punto.y = origen_y + (hab.forma.punto.y * self.alto)
            hab.forma.extent = Point(self.ancho, self.alto)







