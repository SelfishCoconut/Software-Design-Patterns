class FaseJuego:
    def __init__(self):
        pass

    def iniciar(self, juego):
        pass

    def finalizar(self, juego, ui):
        pass

class FaseJugando(FaseJuego):
    def __init__(self):
        super().__init__()
        self.running = True

    def iniciar(self, juego):
        pass

    def finalizar(self, juego, ui):
        juego.fase = FaseFinal()
        juego.fase.finalizar(juego, ui)


class FaseInicial(FaseJuego):
    def __init__(self):
        super().__init__()
        self.running = True

    def iniciar(self, juego):
        juego.agregar_personaje("Pepe")
        juego.abrir_puertas()
        juego.lanzarPersonaje()
        juego.lanzarBichos()
        juego.fase = FaseJugando()

    def finalizar(self, juego, ui):
        pass


class FaseFinal(FaseJuego):
    def __init__(self):
        super().__init__()
        self.running = False

    def iniciar(self, juego):
        pass
    
    def finalizar(self, juego, ui):

        if juego.personaje.vidas > 0:
            ui.victoria()

        else:
            ui.derrota()