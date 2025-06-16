from .estado_ente import Vivo, Muerto
from .norte import Norte
from .sur import Sur
from .este import Este
from .oeste import Oeste
from .orientacion import Orientacion
import logging
from threading import Lock
from .lock_singleton import get_global_lock
class Ente:
    _id_counter = 0
    def __init__(self):
        self.id = Ente._id_counter
        Ente._id_counter += 1
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()
        self.lock = get_global_lock()
        self.event_manager = None
        
    def clonarLaberinto(self,tunel):
        pass
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def esAtacadoPor(self, atacante):
        print(f"Ataque: {self}  es atacado")
        self.vidas -= atacante.poder
        print(f"Vidas restantes: {self.vidas}")
        if self.vidas <= 0:
            print("MUERTO EN: ", self.posicion.num)
            self.estadoEnte.morir(self)

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
        self.vidas = vidas * 100
        self.juego = juego
        self.poder = poder
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("personaje")
        self.lock = get_global_lock()

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
    
    def actua(self):
        from pynput import keyboard
        move_key = ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D', keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right]
        attack_key = [keyboard.Key.space]
        def on_press(key):
            if key in move_key:
                print(f"Tecla presionada: {key}")
                self.movimiento(key)
            elif key in attack_key:
                with self.lock:
                    self.atacar()
                    
        with keyboard.Listener(on_press=on_press) as listener:
            while self.estaVivo():
                listener.join()

    def movimiento(self, key):
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

    def __str__(self):
        return self.nombre
