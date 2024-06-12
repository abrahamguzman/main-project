from config.openai import client_ai


def crear_asistente(
    nombre,
    instrucciones,
    temperatura=0,
    model="gpt-4o",
    vector_store_id=None,
    top_p=0,
):
    file_search = None
    if vector_store_id is not None:
        file_search = {"file_search":{"vector_store_ids": [vector_store_id]}}
    
    response = client_ai.beta.assistants.create(
        name=nombre,
        model=model,
        instructions=instrucciones,
        temperature=temperatura,
        tools=[{"type": "file_search"}],
        tool_resources=file_search,
        top_p=top_p,
    )
    return response


def listar_asistentes():
    response = client_ai.beta.assistants.list(order="desc", limit=10)
    return response


def modificar_asistente(id_asistente, model="gpt-4o", temperatura=0):
    client_ai.beta.assistants.update(
        id_asistente,
        model=model,
        temperature=temperatura
    )
    
    print("Asistente modificado con éxito.")
