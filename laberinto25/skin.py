class Skin:
    def __init__(self, ente, sprite):
        self.sprite= sprite
        self.ente = ente
    
    def getTUISprite(self):
        health_percent = self.ente.vidas / self.ente.vidasTotales
        if self.ente.esPersonaje():
            green = int(health_percent * 255)
            return f"\033[38;2;0;{green};0m{self.sprite}\033[0m"
        else:
            red = int(health_percent * 255)
            return f"\033[38;2;{red};0;0m{self.sprite}\033[0m"
    def getGUISprite(self):
        health_percent = self.ente.vidas / self.ente.vidasTotales
        if self.ente.esPersonaje():
            blue = int(health_percent * 255)
            return f"#{0:02x}{0:02x}{blue:02x}"
        elif self.sprite == '.':
            red = int(health_percent * 255)
            return f"#{red:02x}{red:02x}{0:02x}"
        elif self.sprite == 'A':
            red = int(health_percent * 255)
            return f"#{red:02x}{0:02x}{0:02x}"
        else:
            red = int(health_percent * 255)
            return f"#{0:02x}{red:02x}{red:02x}"
            
