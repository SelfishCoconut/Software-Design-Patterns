from laberinto25.lock_singleton import get_global_lock
class Modo:
    def __init__(self):
        self.lock = get_global_lock()

    def actuar(self, bicho):
        self.dormir(bicho)
        with get_global_lock():
            if bicho.estaVivo() and bicho.juego.fase.running:  
                self.caminar(bicho)
        with get_global_lock():
            if bicho.estaVivo() and bicho.juego.fase.running:
                self.atacar(bicho)

    def dormir(self, bicho):
        pass

    def caminar(self, bicho):
        bicho.caminar()

    def atacar(self, bicho):
        bicho.atacar()

    def __str__(self):
        return "Soy un modo"
