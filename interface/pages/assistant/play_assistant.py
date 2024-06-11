import tkinter as tk
from config.colors import BG_COLOR, TEXT_COLOR, BG_GRAY
from config.fonts import FONT, FONT_BOLD
from utils.openai.assistant import preguntar_asistente


class PlayAssistantPage(tk.Tk):
    def __init__(self, assistant_id):
        super().__init__()
        self.assistant_id = assistant_id

        self.title("Chat")
        self.configure(width=1000, height=600, bg=BG_COLOR)
        
        # head label
        head_label = tk.Label(self, bg=BG_COLOR, fg=TEXT_COLOR, text="Chat", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = tk.Label(self, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = tk.Text(self, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state="disabled")
        
        # scroll bar
        scrollbar = tk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = tk.Label(self, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = tk.Button(bottom_label, text="Enviar", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, "end")
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", msg1)
        self.text_widget.configure(state="disabled")
        
        msg2 = f"{"Asistente"}: {preguntar_asistente(self.assistant_id, msg)}\n\n"
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", msg2)
        self.text_widget.configure(state="disabled")
        
        self.text_widget.see("end")
