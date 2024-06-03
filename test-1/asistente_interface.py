import tkinter as tk
from openai import OpenAI
from utils.window import abrir_archivos
from utils.openai.file import subir_archivos
from utils.openai.vector_store import crear_vector_store, subir_archivos_a_vector_store
from utils.openai.assistant import crear_asistente
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
        self.geometry("300x200")
        self.label = tk.Label(self, text="Nombre de Vector Store:")
        self.label.pack()
        self.nombre_vector_store = tk.Entry(self)
        self.nombre_vector_store.pack()
        self.create_vs_button = tk.Button(self, text="Crear", command=self.on_create_vs_button_click)
        self.create_vs_button.pack()
        self.output = tk.Label(self, text="")
        self.output.pack()

    def on_create_vs_button_click(self):
        nombre_vector_store = self.nombre_vector_store.get()
        archivos_locales = abrir_archivos(extension=".docx", titulo="Seleccionar archivos para vectorizar (.docx)")
        ids_archivos_subidos = subir_archivos(client=client, rutas_archivos=archivos_locales)
        vector_store = crear_vector_store(client=client, name=nombre_vector_store)
        subir_archivos_a_vector_store(client=client, ids_archivos=ids_archivos_subidos, id_vector_store=vector_store.id)
        
        self.output.config(text=f"Vector Store creado: {vector_store.id}")


if __name__ == "__main__":
    app = AsistenteInterface()
    app.mainloop()