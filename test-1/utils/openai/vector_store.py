def crear_vector_store(client, name):
	response = client.beta.vector_stores.create(name=name)
	return response


def subir_archivo_a_vector_store(client, id_archivo, id_vector_store):
    response = client.beta.vector_stores.files.create(
        vector_store_id=id_vector_store, file_id=id_archivo
    )
    return response
