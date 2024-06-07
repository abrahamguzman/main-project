from config.openai import client_ai


def crear_asistente(
    client,
    nombre,
    instrucciones,
    temperatura=0,
    model="gpt-4o",
    vector_store_id=None,
    top_p=0,
):
    response = client.beta.assistants.create(
        name=nombre,
        model=model,
        instructions=instrucciones,
        temperature=temperatura,
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
        top_p=top_p,
    )
    return response


def listar_asistentes(client):
    response = client.beta.assistants.list(order="desc")
    return response


def modificar_asistente(id_asistente, instrucciones, model="gpt-4o"):
    client_ai.beta.assistants.update(
        id_asistente,
        instructions=instrucciones,
        model=model,
    )
    
    print("Asistente modificado con éxito.")
