from userInterface import UserInterface

class TUI(UserInterface):
    def __init__(self):
        super().__init__()
    
    def dibujarHabitacion(self, hab):
        print(f"Habitacion: {hab}")
        for ente in hab.entidades:
            print(f"\tEnte: {ente}")
        
        for orientacion in hab.forma.orientaciones:
            print(f"\tOrientacion: {orientacion}")
            print(f"\t\tElemento: {orientacion.elemento}")
    