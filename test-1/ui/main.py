import tkinter as tk
from screens.assistant_screen import assistant_screen
from screens.file_screen import file_screen
from screens.vector_store_screen import vector_store_screen


title = "App"
geometry = "1000x600"

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        
        navbar_frame = tk.Frame(self, bg="#c3c3c3")
        navbar_frame.pack(side="left", fill="y")
        navbar_frame.pack_propagate(False)
        navbar_frame.configure(width=200)
        
        screen_options = {
            "assistant": {"name": "Asistentes", "screen": assistant_screen(main_frame)},
            "vector_store": {"name": "Tienda de vectores", "screen": vector_store_screen(main_frame)},
            "archivos": {"name": "Archivos", "screen": file_screen(main_frame)},
        } 
        
        for options in screen_options.items():
            button = tk.Button(navbar_frame, text=options["name"], command=lambda: self.show_screen(options["screen"]))
            button.pack(fill="x")
        
        main_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        main_frame.pack(side="right", fill="both")
        main_frame.pack_propagate(False)
        main_frame.configure(width=800)
        

if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()
        