import tkinter as tk
from utils.openai.assistant import listar_asistentes
from config.colors import BG_COLOR, TEXT_COLOR
from config.fonts import FONT, FONT_BOLD, FONT_TITLE
from config.openai import client


class PlayAssistantPage(tk.Frame):
    def __init__(self, parent, assistant_id):
        super().__init__(parent)
        print(assistant_id)
        self.configure(bg=BG_COLOR)

        self.title = tk.Label(self, text="CHAT", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR)

        self.pack()

    
