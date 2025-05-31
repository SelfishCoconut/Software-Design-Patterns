class ElementoMapa:
    _id_counter = 0
    def __init__(self):
        self.padre = None
        self.id = ElementoMapa._id_counter
        ElementoMapa._id_counter += 1
    def recorrer(self, func):
        func(self)

    def entrar(self, alguien):
        pass

    def esPuerta(self):
        return False

    def aceptar(self, unVisitor):
        pass

    def calcularPosicionDesde(self,forma):
        pass
    def calcularPosicion(self):
        pass
    def calcularPosicionDesdeEn(self,forma, punto):
        pass
    def __str__(self):
        return "Soy un ElementoMapa"

    def __hash__(self):
        return hash((self.__class__, self.id))
