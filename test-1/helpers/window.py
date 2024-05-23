import tkinter as tk
from tkinter import filedialog


def abrir_archivo(extension=None, titulo="Seleccionar archivo"):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(defaultextension=extension, title=titulo)


def guardar_archivo(extension=None, titulo="Guardar archivo"):
    root = tk.Tk()
    root.withdraw()
    return filedialog.asksaveasfilename(defaultextension=extension, title=titulo)