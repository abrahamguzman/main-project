from config.openai import client

def crear_hilo():
    thread = client.beta.threads.create()
    return thread

def eliminar_hilo(thread_id):
    response = client.beta.threads.delete(thread_id=thread_id)
    return response
    
def añadir_mensaje_hilo(thread_id, content, role="user"):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=content
    )
    return message

def obtener_mensajes_hilo(thread_id):
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    return messages

def obtener_ultimo_mensaje_hilo(thread_id):
    messages = obtener_mensajes_hilo(thread_id)
    return messages.data[0].content[0].text.value if messages.data else None