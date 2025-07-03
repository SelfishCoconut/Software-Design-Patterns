from laberinto25.juego import Juego
from laberinto25.GUI import GUI
from laberinto25.TUI import TUI
import tkinter as tk
import os
import sys

def mainTerminal(file_path):
    TUI(file_path)


def mainGUI(file_path):

    root = tk.Tk()
    gui = GUI(root, file_path)
    root.mainloop()

import cProfile
if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'laberintos', 'lab4HabIzd4Bichos.json')
    
    if len(sys.argv) > 1:
        mainTerminal(file_path)
    else:
        mainGUI(file_path)


