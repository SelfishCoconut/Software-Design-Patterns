from laberinto25.gui import MazeGUI
import tkinter as tk
import os


def main():
    root = tk.Tk()
    file_path = os.path.join(os.path.dirname(__file__), 'laberintos', 'lab4HabIzd4Bichos.json')

    gui = MazeGUI(root, file_path)
    root.mainloop()

if __name__ == '__main__':
    main()

