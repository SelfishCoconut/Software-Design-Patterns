class EstadoPuerta:
    def __init__(self):
        pass

    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        pass

    def entrar(self, puerta, alguien):
        pass

    def esAbierta(self):
        pass

class Abierta(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        pass
    def cerrar(self, puerta):
        puerta.estadoPuerta = Cerrada()

    def entrar(self, puerta, alguien):
        puerta.puedeEntrar(alguien)

    def esAbierta(self):
        return True

class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        puerta.estadoPuerta = Abierta()

    def cerrar(self, puerta):
        pass
    def entrar(self, puerta, alguien):
        pass

    def esAbierta(self):
        return False
