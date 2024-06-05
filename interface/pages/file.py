import tkinter as tk


class FilePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lb = tk.Label(self, text="Archivos")
        self.lb.pack()
        
        self.pack(pady=5)