import pygame
from .director import Director
from .point import Point
import laberinto25.estado_puerta as estado_puerta
import laberinto25.maze_gui_visitor as vs
import laberinto25.event_manager as em
import threading

class MazeGUI:
    def __init__(self, laberinto_file):
        self.laberinto_file = laberinto_file
        self.juego = None
        self.screen = None
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
        self.event_manager = em.EventManager()
        self.event_listener = em.EventListener(self)
        self.event_manager.add_listener(self.event_listener)
        [bicho.agregarEvent_manager(self.event_manager) for bicho in self.juego.bichos]
        self.juego.lanzarBichos()
    
    def init_ui(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1150, 900))
        pygame.display.set_caption("Maze Game")
        self.calcularLaberinto()
        for habitacion in self.juego.laberinto.hijos:
            print("num-punto", habitacion.num, habitacion.forma.punto.x, habitacion.forma.punto.y)
        self.dibujarLaberinto()
        self.draw_person()
        self.draw_bichos()

    def calcularLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularTamContenedor()
        self.asignarPuntosReales()

    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self)
    
    def render_habitacion(self, hab):
        pass        

    def dibujarRectangulo(self, forma):
        pygame.draw.rect(self.screen, (200, 200, 200), (forma.punto.x, forma.punto.y, forma.extent.x, forma.extent.y))
        pygame.display.flip()

    def draw_person(self):
        self.juego.personaje.aceptar(self)
    def draw_bicho_muere(self, data):
        self.visuales.pop(hash(data))
        pygame.display.flip()
    
    def draw_caminar(self, ente):
        self._draw_caminar(ente)

    def _draw_caminar(self, ente):
        if self.visuales.get(hash(ente)):
            self.visuales.pop(hash(ente))
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
        self.render_habitacion(hab)
        #self.dibujarRectangulo(hab.forma)

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

        color = (0, 255, 0) if isinstance(puerta.estadoPuerta, estado_puerta.Abierta) else (255, 0, 0)
        self.visuales[hash(puerta)] = pygame.draw.rect(self.screen, color, (x_medio - width / 2, y_medio - height / 2, width, height))

    def dibujarPuerta(self, puerta, x_medio, y_medio, width, height, color):
        self.visuales[hash(puerta)] = pygame.draw.rect(self.screen, color, (x_medio - width / 2, y_medio - height / 2, width, height))

    def visitarBomba(self, bomba):
        pass

    def visitarTunel(self, tunel):        
        pass

    def visitarPersonaje(self, personaje):
        personaje.agregarEvent_manager(self.event_manager)
        habitacion = personaje.posicion
        x = habitacion.forma.punto.x + habitacion.forma.extent.x / 2 - 30
        y = habitacion.forma.punto.y + habitacion.forma.extent.y / 2
        self.visuales[hash(personaje)] = pygame.draw.ellipse(self.screen, (0, 0, 255), (x - 10, y - 10, 20, 20))

    def visitarBicho(self, bicho):
        habitacion = bicho.posicion
        x = habitacion.forma.punto.x + habitacion.forma.extent.x / 2
        y = habitacion.forma.punto.y + habitacion.forma.extent.y / 2

        offset = bicho.posicion.entidades.index(bicho) * 25
        color = (255, 0, 0)
        self.visuales[hash(bicho)] = pygame.draw.ellipse(self.screen, color, (x + offset - 10, y - 10, 20, 20))

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

if __name__ == '__main__':
    pygame.init()
    gui = MazeGUI("./laberintos/lab4HabIzd4Bichos.json")
    pygame.display.set_mode((1150, 900))
    pygame.display.set_caption("Maze Game")
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

