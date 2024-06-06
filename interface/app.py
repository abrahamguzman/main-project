import tkinter as tk
from pages.assistant.assistants import AssistantsPage
from pages.file.file import FilePage
from pages.vector_store.vector_store import VectorStorePage
from config.colors import BG_COLOR, TEXT_COLOR


title = "App"
geometry = "1000x600"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

        navbar_frame = tk.Frame(self, bg="#c3c3c3")
        navbar_frame.pack(side="left", fill="y")
        navbar_frame.pack_propagate(False)
        navbar_frame.configure(width=200)

        self.main_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1, bg=BG_COLOR)
        self.main_frame.pack(side="right", fill="both")
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=800)

        options = {
            "assistant": {"name": "Asistentes", "page": AssistantsPage},
            "vector_store": {"name": "Tienda de vectores", "page": VectorStorePage},
            "archivos": {"name": "Archivos", "page": FilePage},
        }

        for option in options.values(): 
            button = tk.Button(
                navbar_frame,
                text=option["name"],
                command=lambda option=option: self.select_page(option["page"]),
            )
            button.pack(fill="x")


    def select_page(self, page):
        self.delete_pages()
        page = page(self.main_frame)
        
        
    def delete_pages(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
            

if __name__ == "__main__":
    app = App()
    app.mainloop()
