from juego import Juego
import tkinter as tk
import os
from GUI import GUI
import sys

def mainTerminal():
    
    gui = GUI()
    juego = Juego()
    juego.fase.ui = TUI()
    juego.fase.iniciar(juego)

def mainGUI():

    root = tk.Tk()
    file_path = os.path.join(os.path.dirname(__file__), 'laberintos', 'lab4HabIzd4Bichos.json')

    gui = GUI(root, file_path)
    root.mainloop()

import cProfile
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "terminal":
        mainTerminal()
    else:
        #profiler = cProfile.Profile()
        #profiler.enable()
        mainGUI()
        #profiler.disable()
        #profiler.dump_stats('profiling_data.prof')


