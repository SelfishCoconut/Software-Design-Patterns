import time
from laberinto25.modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        time.sleep(1)

    def __str__(self):
        return "-agresivo"
