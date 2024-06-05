from utils.logger import logger


def crear_vector_store(client, name):
    try:
        response = client.beta.vector_stores.create(name=name)
        return response
    except Exception as e:
        logger.error(f"Error al crear vector store: {e}")
        return None


def subir_archivo_a_vector_store(client, id_archivo, id_vector_store):
    response = client.beta.vector_stores.files.create(
        vector_store_id=id_vector_store, file_id=id_archivo
        )
    return response


def subir_archivos_a_vector_store(client, ids_archivos: list, id_vector_store):
    try:
        response = client.beta.vector_stores.file_batches.create(
            vector_store_id=id_vector_store, file_ids=ids_archivos
            )
        return response
    except Exception as e:
        logger.error(f"Error al subir archivos a vector store: {e}")
        return None

