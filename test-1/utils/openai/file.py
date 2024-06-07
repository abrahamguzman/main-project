from openai import OpenAI
from utils.logger import logger
from config.openai import client_ai



def subir_archivo(client, ruta_archivo):
    response = client.files.create(
        file=open(ruta_archivo, "rb"), 
        purpose="assistants"
        )
    return response


def subir_archivos(client, rutas_archivos: list):
    id_archivos = []
    for ruta_archivo in rutas_archivos:
        try:
            response = client.files.create(
                file=open(ruta_archivo, "rb"), 
                purpose="assistants"
                )
            id_archivos.append(response.id)
            logger.info(f"Archivo subido: {response.id}")
        except Exception as e:
            logger.error(f"Error al subir archivo: {e}")
            continue
    return id_archivos


def listar_archivos():
	response = client_ai.files.list()
	return response
