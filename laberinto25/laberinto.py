from laberinto25.contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()        

    def entrar(self,alguien):
        hab1=self.obtenerHabitacion(1)
        hab1.entrar(alguien)

    def __str__(self):
        return "Soy un laberinto"

    def agregarHabitacion(self, habitacion):
        self.hijos.append(habitacion)

    def obtenerHabitacion(self, num):
        for habitacion in self.hijos:
            if habitacion.num == num:
                return habitacion
        return None
    
    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)

    def entrar(self, alguien):        
        hab1=self.obtenerHabitacion(1)
        hab1.entrar(alguien)
        print(f"{alguien} entra en el laberinto")
    
    def aceptar(self, unVisitor):
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
