from openai import OpenAI

client = OpenAI()


def subir_archivo(client, ruta_archivo):
    response = client.files.create(
        file=open(ruta_archivo, "rb"), 
        purpose="assistants"
        )
    return response

def listar_archivos(client):
	response = client.files.list()
	return response
