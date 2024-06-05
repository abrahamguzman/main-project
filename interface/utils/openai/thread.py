def crear_hilo(client):
    thread = client.beta.threads.create()
    return thread

def eliminar_hilo(client, thread_id):
    response = client.beta.threads.delete(thread_id=thread_id)
    return response
    
def añadir_mensaje_hilo(client, thread_id, content, role="user"):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role=role,
        content=content
    )
    return message

def obtener_mensajes_hilo(client, thread_id):
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    return messages

def obtener_ultimo_mensaje_hilo(client, thread_id):
    messages = obtener_mensajes_hilo(client=client, thread_id=thread_id)
    return messages.data[0].content[0].text.value if messages.data else None