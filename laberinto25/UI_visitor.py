from visitor import Visitor

class MazeUIVisitor(Visitor):
    def __init__(self, ui):
        self.ui = ui

    def visitarLaberinto(self, laberinto):
        pass

    def visitarHabitacion(self, habitacion):
        self.ui.dibujarHabitacion(habitacion)

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        self.ui.dibujarPuerta(puerta)

    def visitarPersonaje(self, personaje):
        self.ui.dibujarPersonaje(personaje)

    def visitarBicho(self, bicho):
        self.ui.dibujarBicho(bicho)

    def visitarOrientacion(self, orientacion):
        pass
