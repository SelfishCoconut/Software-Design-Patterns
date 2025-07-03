class Skin:
    def __init__(self, ente, sprite):
        self.sprite= sprite
        self.ente = ente
    
    def getSprite(self):
        if isinstance(self.sprite, str):
            health_percent = self.ente.vidas / self.ente.vidasTotales
            if self.ente.esPersonaje():
                green = int(health_percent * 255)
                return f"\033[38;2;0;{green};0m{self.sprite}\033[0m"
            else:
                red = int(health_percent * 255)
                return f"\033[38;2;{red};0;0m{self.sprite}\033[0m"
        else:
            return self.sprite