from laberinto25.elemento_mapa import ElementoMapa

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self,alguien):
        pass
    
    def __str__(self):
        return "Pared"
