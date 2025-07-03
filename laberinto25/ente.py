from laberinto25.estado_ente import Vivo, Muerto
from laberinto25.norte import Norte
from laberinto25.sur import Sur
from laberinto25.este import Este
from laberinto25.oeste import Oeste
from laberinto25.orientacion import Orientacion
from laberinto25.lock_singleton import get_global_lock
import logging
from threading import Lock
from pynput import keyboard
from skin import Skin

class Ente:
    _id_counter = 0
    def __init__(self):
        self.id = Ente._id_counter
        Ente._id_counter += 1
        self.vidas = None
        self.vidasTotales = self.vidas
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()
        self.lock = get_global_lock()
        self.event_manager = None
        self.skin = None
        
    def clonarLaberinto(self,tunel):
        pass
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def esAtacadoPor(self, atacante):
        self.vidas -= atacante.poder
        if self.vidas <= 0:
            self.vidas = 0
            self.estadoEnte.morir(self)
        self.event_manager.notify  ({'type': 'atacado', 'data': self})

    def esPersonaje(self):
        return False

    def actua(self):
        pass
    def estaVivo(self):
        return self.vidas > 0
    def aceptar(self, unVisitor):
        raise NotImplementedError

    def agregarEvent_manager(self, event_manager):
        self.event_manager = event_manager
    
    def __hash__(self):
        return hash((self.__class__, self.id))
class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):
        super().__init__()
        self.nombre = nombre
        self.vidas = 100
        self.vidasTotales = self.vidas
        self.juego = juego
        self.poder = 1
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("personaje")
        self.lock = get_global_lock()
        self.skin = Skin(self, '@')
    def clonarLaberinto(self,tunel):
        tunel.puedeClonarLaberinto()

    def esPersonaje(self):
        return True

    def atacar(self):
        enemigo = self.posicion.buscarEnemigo(self)
        if enemigo is None:
            return
        enemigo.esAtacadoPor(self)
    
    def aceptar(self, unVisitor):
        unVisitor.visitarPersonaje(self)
    
    def _handle_movement(self, key):
        from pynput import keyboard
        if key == keyboard.Key.up:
            puerta = self.posicion.obtenerElementoEnOrientacion(Norte())
        elif key == keyboard.Key.down:
            puerta = self.posicion.obtenerElementoEnOrientacion(Sur())
        elif key == keyboard.Key.left:
            puerta = self.posicion.obtenerElementoEnOrientacion(Oeste())
        elif key == keyboard.Key.right:
            puerta = self.posicion.obtenerElementoEnOrientacion(Este())
        else:
            return

        if puerta.esPuerta() and puerta.esAbierta() and not self.posicion.buscarEnemigo(self):
            puerta.entrar(self)
            self.event_manager.notify({'type': 'caminar', 'data': self})
        else:
            self.logger.info("No se puede mover en esa dirección")


    def _handle_attack(self):
        with self.lock:
            self.atacar()

    def _on_press(self, key):
        move_key = ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D', keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right]
        attack_key = [keyboard.Key.space]

        if key in move_key:
            self._handle_movement(key)
        elif key in attack_key:
            self._handle_attack()


    def actua(self):
        listener = keyboard.Listener(on_press=self._on_press)
        listener.start()  # Start the listener in a non-blocking way

        while self.estaVivo() and self.juego.fase.running:
            pass # Keep the thread alive while the character is alive.  The listener handles input.
        
        listener.stop() # Stop listening when the character dies.


    def __str__(self):
        return self.nombre
