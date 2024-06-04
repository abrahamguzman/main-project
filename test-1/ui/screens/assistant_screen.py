import tkinter as tk

def assistant_screen(parent):
    assistant_screen = tk.Frame(parent)
    lb = tk.Label(assistant_screen, text="Asistentes")
    lb.pack()
    
    assistant_screen.pack(pady=5)