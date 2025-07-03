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
        if event['type'] == 'atacado':
            self._on_atacado(event['data'])
        elif event['type'] == 'caminar':
            self._on_caminar(event['data'])
        elif event['type'] == 'bicho_muere':
            self._on_bicho_muere(event['data'])

    def _on_bicho_muere(self, ente):
        self.ui.draw_bicho_muere(ente)
        if self.esGameOver(ente):
            ente.juego.terminarJuego(self.ui) 

    def _on_atacado(self, ente):
        self.ui.draw_atacado(ente)

    def _on_caminar(self, ente):
        self.ui.draw_caminar(ente)
        if ente.esPersonaje():
             ente.posicion.aceptar(self.ui.visitor)


    def esGameOver(self, ente):
        return len(ente.juego.bichos) == 0 or ente.juego.personaje.vidas == 0
