import tkinter as tk
from openai import OpenAI
from utils.window import abrir_archivos
from utils.openai.file import subir_archivos
from utils.openai.vector_store import crear_vector_store, subir_archivos_a_vector_store
from utils.openai.assistant import crear_asistente, listar_asistentes
from utils.openai.run import crear_run
from utils.openai.thread import (
    añadir_mensaje_hilo,
    crear_hilo,
    eliminar_hilo,
    obtener_ultimo_mensaje_hilo,
)

client = OpenAI()

class AsistenteInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Asistente")
        self.geometry("600x400")
        self.label = tk.Label(self, text="Nombre de Vector Store:")
        self.label.pack()
        self.nombre_vector_store = tk.Entry(self)
        self.nombre_vector_store.pack()
        self.create_vs_button = tk.Button(self, text="Crear", command=self.on_create_vs_button_click)
        self.create_vs_button.pack()
        self.output = tk.Label(self, text="")
        self.output.pack()
        self.show_assistents()

    def show_assistents(self):
        self.table_assistants = tk.Frame(self)
        self.table_assistants.pack()
        assistants = listar_asistentes(client=client)
        
        for i, assistant in enumerate(assistants):
            self.indice = tk.Label(self.table_assistants, text=i)
            self.assistant_name = tk.Label(self.table_assistants, text=assistant.name)
            self.assistant_id = tk.Label(self.table_assistants, text=assistant.id)
            self.play_assistant_button = tk.Button(self.table_assistants, text="Usar", command=self.on_play_assistant_button_click(assistant.id))
            self.edit_assistant_button = tk.Button(self.table_assistants, text="Editar", command=self.on_edit_assistant_button_click(assistant.id))
            
            self.indice.grid(row=i, column=0, sticky="nsew", pady=5)
            self.assistant_name.grid(row=i, column=1, sticky="nsew", pady=5)
            self.assistant_id.grid(row=i, column=2, sticky="nsew", pady=5)
            self.play_assistant_button.grid(row=i, column=3, sticky="nsew", pady=5)
            self.edit_assistant_button.grid(row=i, column=4, sticky="nsew", pady=5)
        
    def on_play_assistant_button_click(self, assistant_id):
        print(assistant_id)
    
    def on_edit_assistant_button_click(self, assistant_id):
        print(assistant_id)
    
    
    
    
    def on_create_vs_button_click(self):
        nombre_vector_store = self.nombre_vector_store.get()
        archivos_locales = abrir_archivos(extension=".docx", titulo="Seleccionar archivos para vectorizar (.docx)")
        ids_archivos_subidos = subir_archivos(client=client, rutas_archivos=archivos_locales)
        vector_store = crear_vector_store(client=client, name=nombre_vector_store)
        subir_archivos_a_vector_store(client=client, ids_archivos=ids_archivos_subidos, id_vector_store=vector_store.id)
        
        self.output.config(text=f"Vector Store creado: {vector_store.name}")


if __name__ == "__main__":
    app = AsistenteInterface()
    app.mainloop()