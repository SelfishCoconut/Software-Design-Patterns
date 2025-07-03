from laberinto25.userInterface import UserInterface
from laberinto25.puerta import Puerta
from random import randint
from ente import Personaje
from lock_singleton import get_global_lock
from bicho import Bicho
class TUI(UserInterface):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.init_ui()
        self.visuals = []
        
    def init_ui(self):
        self.dibujarLaberinto()
    
    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self.visitor)

    def dibujarHabitacion(self, hab):
        with get_global_lock():
            pass
        self._dibujarHabitacion(hab)
    def _dibujarHabitacion(self, hab):
        alto = 10
        ancho = 20
        map = "\n"
        print("\033[2J\033[1;1H")
        def add_door(puerta, open_symbol, closed_symbol):
            return open_symbol if puerta.esAbierta else closed_symbol if isinstance(puerta, Puerta) else '════'
        bcount = len(hab.entidades) -1
        for i in range(alto):
            for j in range(ancho):
                if i == 0 or i == alto-1 or j == 0 or j == ancho-1:
                    # Corners
                    if (i, j) == (0, 0): map += '╔'
                    elif (i, j) == (0, ancho-1): map += '╗'
                    elif (i, j) == (alto-1, 0): map += '╚'
                    elif (i, j) == (alto-1, ancho-1): map += '╝'
                    
                    # North and South walls
                    elif i == 0 and j == ancho//2-1:
                        if isinstance(hab.forma.norte, Puerta):
                            map += add_door(hab.forma.norte, '╣  ╠', '╣──╠')
                        else:
                            map += '════'
                    elif i == alto-1 and j == ancho//2-1:
                        if isinstance(hab.forma.sur, Puerta):
                            map += add_door(hab.forma.sur, '╣  ╠', '╣──╠')
                        else: 
                            map+="════"
                    elif i in (0, alto-1):
                        map += '═'
                        
                    # West and East walls
                    elif j in (0, ancho-1):
                        if i == alto//2-2 and j==0:
                            if isinstance(hab.forma.oeste, Puerta):
                                map += '╩   '
                            else:
                                map += '║   '
                        elif i== alto//2-1 and j==0:
                            if isinstance(hab.forma.oeste, Puerta):
                                map += '    ' if hab.forma.oeste.esAbierta else '|   '
                            else:
                                map += '║   '
                        elif i == alto//2 and j==0:
                            if isinstance(hab.forma.oeste, Puerta):
                                map += '╦   '
                            else:
                                map += '║   '
                        elif i == alto//2-2 and j==ancho-1:
                            if isinstance(hab.forma.este, Puerta):
                                map += '╩   '
                            else:
                                map += '║   '
                        elif i== alto//2-1 and j==ancho-1:
                            if isinstance(hab.forma.este, Puerta):
                                map += '    ' if hab.forma.este .esAbierta else '|   '
                            else: 
                                map += '║   '  
                        elif i == alto//2 and j==ancho-1:
                            if isinstance(hab.forma.este, Puerta):
                                map += '╦   '
                            else:
                                map += '║   '
                        else:
                            map += '║   '
                else:         
                    if 0 <= bcount:
                        x = randint(j, ancho-2)
                        while x == ancho//2-1:
                            x = randint(j, ancho-2)
                        y = randint(i, alto-2)
                        while y == alto//2-1:
                            y = randint(i, alto-2)
                        if i == y and j == x:
                            map += hab.entidades[bcount].skin.getTUISprite()
                            bcount -= 1
                        else:
                            map += ' '
                    else:
                        map += ' '
           
            map += '\n'
        
        print(map)
        print(f"\t**Entidades**")
        for ente in hab.entidades:
            print(f"\t\tEnte: {ente}")
    
    def draw_atacado(self, ente):
        if ente.posicion == ente.juego.personaje.posicion:
            self.dibujarHabitacion(ente.posicion)
    
    def draw_caminar(self, ente):
        if ente.posicion == ente.juego.personaje.posicion:
            self.visuals.append(hash(ente))
        if hash(ente) in self.visuals:
            self.visuals.remove(hash(ente))
            self.dibujarHabitacion(self.juego.personaje.posicion)
  
    def draw_bicho_muere(self, ente):
        self.dibujarHabitacion(ente.juego.personaje.posicion)
        print(f"El bicho {ente} ha muerto")
    
    def victoria(self):
        print("\n\n\n\n\n\n\n")
        print("    __________________")
        print("   /                  \\")
        print("  /                    \\")
        print(" /                      \\")
        print("|                        |")
        print("|        VICTORIA        |")
        print("|                        |")
        print(" \\                      /")
        print("  \\                    /")
        print("   \\__________________/")
        print("\n\n\n\n\n\n\n")
    
    def derrota(self):
        print("\n\n\n\n\n\n\n")
        print("    __________________")
        print("   /                  \\")
        print("  /                    \\")
        print(" /                      \\")
        print("|                        |")
        print("|        DERROTA!        |")
        print("|                        |")
        print(" \\                      /")
        print("  \\                    /")
        print("   \\__________________/")
        print("\n\n\n\n\n\n\n")
