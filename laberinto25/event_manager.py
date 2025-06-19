# event_manager.py
class EventManager:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def notify(self, event):
        for listener in self.listeners:
            listener.update(event)

# event_listener.py
class EventListener:
    def __init__(self, ui):
        self.ui = ui

    def update(self, event):
        # Actualiza el canvas según el evento recibido
        if event['type'] == 'bicho_muere':
            self.ui.draw_bicho_muere(event['data'])
            if self.esGameOver(event):
                event['data'].juego.terminarJuego(self.ui)
        elif event['type'] == 'caminar':
            self.ui.draw_caminar(event['data'])
            if event['data'].esPersonaje():
                event['data'].posicion.aceptar(self.ui.visitor)

    def esGameOver(self, event):
        return len(event['data'].juego.bichos) == 0 or event['data'].juego.personaje.vidas == 0
