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
    def __init__(self, gui):
        self.gui = gui

    def update(self, event):
        # Actualiza el canvas según el evento recibido
        if event['type'] == 'bicho_muere':
            self.gui.draw_bicho_muere(event['data'])
        elif event['type'] == 'caminar':
            self.gui.draw_caminar(event['data'])
            if event['data'].esPersonaje():
                event['data'].posicion.aceptar(self.gui)
