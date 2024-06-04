import tkinter as tk

def file_screen(parent):
    file_screen = tk.Frame(parent)
    lb = tk.Label(file_screen, text="Asistentes")
    lb.pack()
    
    file_screen.pack(pady=5)