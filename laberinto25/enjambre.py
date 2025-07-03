import time
from laberinto25.modo import Modo

class Enjambre(Modo):
    def __init__(self):
        super().__init__()
        
    def dormir(self, bicho):
        time.sleep(0.5)

    def __str__(self):
        return "-Enjambre"
