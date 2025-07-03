from laberinto25.modo import Modo
from laberinto25.agresivo import Agresivo
from laberinto25.ente import Ente
from skin import Skin
class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo: Modo = None
        self.running = True
        self.poder = None
        self.vidas = None
        self.posicion = None

    def actua(self):
        while self.estaVivo() and self.juego.fase.running:
            self.modo.actuar(self)
        print(f"--------------{self.id} ha terminado de actuar--------------")
    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5
        self.vidasTotales = 5
        self.skin = Skin(self, 'A')
    def iniPerezoso(self):        
        self.poder = 1
        self.vidas = 5
        self.vidasTotales = 5   
        self.skin = Skin(self, 'P')
    def atacar(self):
        self.juego.buscarPersonaje(self)

    def caminar(self):
        self.posicion.caminarAleatorio(self)
        self.event_manager.notify({'type': 'caminar', 'data': self})

    def estaVivo(self):
        return self.vidas > 0
    
    def aceptar(self, unVisitor):
        unVisitor.visitarBicho(self)

    def __str__(self):
        return "Soy un bicho"+self.modo.__str__()

    def __hash__(self):
        return hash((self.__class__, self.id))

