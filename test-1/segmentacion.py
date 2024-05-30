from openai import OpenAI
from nltk.tokenize import sent_tokenize
from helpers.json import generar_json

client = OpenAI()

# Descargar recursos necesarios para NLTK
# nltk.download('punkt')


def generar_embeddings(texto):
    response = client.embeddings.create(model="text-embedding-ada-002", input=texto)
    return response.data[0].embedding


# Función para segmentar el texto por oraciones
def segmentar_texto(texto):
    return sent_tokenize(texto)


# Función para etiquetar segmentos
def etiquetar_segmentos(segmentos):
    etiquetas = []
    for segmento in segmentos:
        embedding = generar_embeddings(segmento)
        etiquetas.append({
            "Segmento": segmento, 
            "Vector": embedding, 
            "Etiqueta": "N/A"
        })
    return etiquetas


""" 
    EJEMPLO DE USO
"""

document_text = """
        En el año 2021, la empresa XYZ S.A firmó un contrato con ABC Ltda para la prestación de servicios de consultoría.
        El contrato estipula que el plazo de ejecución es de seis meses.
        Además, ambas partes acordaron una cláusula de confidencialidad para proteger la información sensible.
    """

segmentos = segmentar_texto(document_text)
etiquetas = etiquetar_segmentos(segmentos)

generar_json(etiquetas, "etiquetas.json")
