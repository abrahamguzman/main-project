import tkinter as tk


class VectorStorePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lb = tk.Label(self, text="Tienda de vectores")
        self.lb.pack()
        
        self.pack(pady=5)