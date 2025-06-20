import time
from laberinto25.modo import Modo

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        time.sleep(3)

    def __str__(self):
        return "-perezoso"
