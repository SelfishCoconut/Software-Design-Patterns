class EstadoEnte:
    def __init__(self):
        pass

    def vivir(self, ente):
        pass

    def morir(self, ente):
        pass

class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print("El ente ya está vivo")

    def morir(self, ente):
        print("El ente muere")
        ente.event_manager.notify({'type': 'bicho_muere', 'data': hash(ente)})
        ente.estadoEnte = Muerto()
        ente.juego.terminarBicho(ente)

class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print("El ente revive")
        ente.estadoEnte = Vivo()

    def morir(self, ente):
        print("El ente ya está muerto")
        ente.juego.terminarJuego()
