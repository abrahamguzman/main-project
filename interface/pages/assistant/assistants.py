import tkinter as tk
from utils.openai.assistant import listar_asistentes
from config.colors import BG_COLOR, TEXT_COLOR
from config.fonts import FONT, FONT_BOLD, FONT_TITLE
from config.openai import client
from pages.assistant.play_assistant import PlayAssistantPage


class AssistantsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_parent = parent
        self.configure(bg=BG_COLOR)

        self.title = tk.Label(
            self, text="ASISTENTES", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR
        )
        self.title.pack()

        self.show_assistents()
        self.pack()

    
    # UI
    def show_assistents(self):
        assistants_table = tk.Frame(self, bg=BG_COLOR)

        # Cabezera de la tabla
        headers = ["N°", "Nombre", "ID", "Acciones"]
        for i, header in enumerate(headers):
            self.add_label_to_table(
                assistants_table, header, row=0, column=i, font=FONT_BOLD
            )

        # Contenido de la tabla
        assistants = listar_asistentes(client=client)
        for i, assistant in enumerate(assistants):
            labels = [i, assistant.name, assistant.id]
            buttons = [
                {
                    "name": "Usar",
                    "command": lambda: self.on_play_assistant_button_click(assistant.id),
                },
                {
                    "name": "Editar",
                    "command": lambda: self.on_edit_assistant_button_click(assistant.id),
                },
            ]
            # Agregar labels
            for j, label in enumerate(labels):
                self.add_label_to_table(assistants_table, label, row=i + 1, column=j)
            # Agrega botones
            for j, button in enumerate(buttons):
                self.add_button_to_table(
                    assistants_table,
                    button["name"],
                    button["command"],
                    row=i + 1,
                    column=j + len(labels),
                )

        assistants_table.pack()

    
    # Funciones
    def on_play_assistant_button_click(self, assistant_id):
        self.play_assistant_page = PlayAssistantPage(self.page_parent, assistant_id)
        self.play_assistant_page.pack()

    def on_edit_assistant_button_click(self, assistant_id):
        print(assistant_id)

    def add_label_to_table(self, table, text, row=0, column=0, font=FONT):
        tk.Label(table, text=text, font=font, fg=TEXT_COLOR, bg=BG_COLOR).grid(
            row=row, column=column, sticky="nsew", pady=5, padx=5
        )

    def add_button_to_table(self, table, text, command, row=0, column=0):
        tk.Button(table, text=text, command=command).grid(
            row=row, column=column, sticky="nsew", pady=5, padx=5
        )
