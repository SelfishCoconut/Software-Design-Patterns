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
        pass

    def morir(self, ente):
        ente.estadoEnte = Muerto()
        ente.juego.terminarBicho(ente)
        ente.event_manager.notify({'type': 'bicho_muere', 'data': ente})

class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        ente.estadoEnte = Vivo()

    def morir(self, ente):
        pass