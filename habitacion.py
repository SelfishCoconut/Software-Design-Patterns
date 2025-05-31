from contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.entidades=[]

    def entrar(self, alguien):
        print(f"Entrando en la habitación {self.num}")
        if alguien.posicion is not None: 
            alguien.posicion.salir(alguien)
        alguien.posicion=self
        self.entidades.append(alguien)

    
    def salir(self, alguien):
        self.entidades.remove(alguien)
        alguien.posicion=None

    def buscarEnemigo(self, alguien):
        for entidad in self.entidades:
            if entidad is not alguien:
                return entidad
        return None


    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)

    def calcularPosicion(self):
        self.forma.calcularPosicion()
        
    def __str__(self):
        return "Soy una habitacion"
