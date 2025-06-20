from laberinto25.contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.entidades=[]
        self.visitado = False

    def entrar(self, alguien):
        if alguien.posicion is not None: 
            alguien.posicion.salir(alguien)
        alguien.posicion=self
        self.entidades.append(alguien)
        if alguien.esPersonaje() == True:
            self.visitado = True

    def aceptar(self, unVisitor):
        if not self.visitado:
            return
        self.visitarContenedor(unVisitor)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)

        if self.visitado:
            for entidad in self.entidades:
                entidad.aceptar(unVisitor)

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
