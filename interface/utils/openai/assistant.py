from config.openai import client
from utils.openai.run import crear_run
from utils.openai.thread import (
    crear_hilo,
    añadir_mensaje_hilo,
    obtener_ultimo_mensaje_hilo,
)


def crear_asistente(
    nombre, instrucciones, temperatura=0, model="gpt-4o", vector_store_id=None
):
    response = client.beta.assistants.create(
        name=nombre,
        model=model,
        instructions=instrucciones,
        temperature=temperatura,
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
    )
    return response


def listar_asistentes():
    response = client.beta.assistants.list(order="desc")
    return response


"""  
FUNCIONAMIENTO:
Fución encargada de crear un hilo con el id del asistente y ejecutarlo
para recibir una respuesta
"""
def preguntar_asistente(assistant_id, text):
    hilo = crear_hilo() # Crear hilo para almacenar mensajes
    añadir_mensaje_hilo(hilo.id, text) # Añadir mensaje al hilo

    if crear_run(hilo.id, assistant_id):
        message = obtener_ultimo_mensaje_hilo(hilo.id)
        return message
    else:
        return None
