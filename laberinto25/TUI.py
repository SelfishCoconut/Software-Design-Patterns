from laberinto25.userInterface import UserInterface
from laberinto25.puerta import Puerta

class TUI(UserInterface):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.init_ui()
    
    def init_ui(self):
        self.dibujarLaberinto()
    
    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self.visitor)

    def dibujarHabitacion(self, hab):
        alto = 10
        ancho = 20
        map = ""
        for i in range(0,alto):
            for j in range(0,ancho):
                if i==0 or i==alto-1 or j==0 or j==ancho-1:
                    if i==0 and j==0:
                        map+='╔'
                    elif i==0 and j==ancho-1:
                        map+='╗'
                    elif i==alto-1 and j==0:
                        map+='╚'
                    elif i==alto-1 and j==ancho-1:
                        map+='╝'
                    elif i==0:
                        if j==ancho/2-1:
                            if isinstance(hab.forma.norte, Puerta):
                                if hab.forma.norte.esAbierta:
                                    map+='╣  ╠'
                                else:
                                    map+='╣──╠'
                            else:
                                map+='════'
                        else: 
                            map+='═'
                    elif i==alto-1:
                        if j==ancho/2-1:
                            if isinstance(hab.forma.sur, Puerta):
                                if hab.forma.sur.esAbierta:
                                    map+='╠  ╣'
                                else:
                                    map+='╠──╣'
                            else:
                                map+='════'
                        else:
                            map+='═'
                    elif j==0 or j==ancho-1:
                        if i==alto/2-2:
                            if isinstance(hab.forma.oeste, Puerta):
                                map+='╩   '
                            else:
                                map+='║   '
                        elif i==alto/2-1:
                            if isinstance(hab.forma.oeste, Puerta):
                                if hab.forma.oeste.esAbierta:
                                    map+='|   '
                                else:
                                    map+='    '
                            else:
                                map+='║   '
                        elif i==alto/2-2:
                            if isinstance(hab.forma.oeste, Puerta):
                                map+='╦   '
                            else:
                                map+='║   '
                        else:
                            map+='║   '
                else:
                    if i == alto/2-1 and j == ancho/2-3:
                        map+='@'
                    else:
                        map+=" "
            map+="\n"
        
        print(map)

        print(f"\t**Entidades**")
        for ente in hab.entidades:
            print(f"\t\tEnte: {ente}")
        
    
    def draw_caminar(self, ente):
        print(f"Caminando: {ente}")