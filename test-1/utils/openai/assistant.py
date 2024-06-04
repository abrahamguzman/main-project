def crear_asistente(
  client, 
  nombre, 
  instrucciones, 
  temperatura=0,
  model="gpt-4o", 
  vector_store_id=None
  ):
    response = client.beta.assistants.create(
        name=nombre,
        model=model,
        instructions=instrucciones,
        temperature=temperatura,
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
    )
    return response
  
def listar_asistentes(client):
    response = client.beta.assistants.list(order="desc")
    return response
