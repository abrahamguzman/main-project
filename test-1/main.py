from openai import OpenAI
from helpers.file import lee_archivo_docx
from helpers.text import dividir_texto_por_tokens
from helpers.array import formatear_archivo
from helpers.json import generar_json, leer_json
from helpers.consola import seleccionar_archivo
from helpers.csv import generar_csv

# Instancia de la clase OpenAI, para usar los métodos de la API.
client = OpenAI()

# Lee el archivo .docx y devuelve una lista con los párrafos del archivo.
nombre_archivo_original = seleccionar_archivo(directorio="docs/")
print("Archivo seleccionado: ", nombre_archivo_original)

texto = lee_archivo_docx(ruta_archivo="docs/" + nombre_archivo_original)

# Divide el texto en subtextos de máximo 3000 tokens.
texto_dividido = dividir_texto_por_tokens(texto=texto, max_tokens=1000)

# Lee archivo que contiene mensajes base
nombre_archivo_entrenamiento_base = seleccionar_archivo(
    directorio="entrenamiento_base/"
)
historial_mensajes = leer_json(
    nombre_archivo="entrenamiento_base/" + nombre_archivo_entrenamiento_base
)
print("Archivo seleccionado: ", nombre_archivo_entrenamiento_base)

# Lista de diccionarios con el texto y la respuesta de cada subtexto
archivo_final = []

""" 
    PASO PRINCIPAL:
    Se envía cada subtexto a OpenAI para obtener una respuesta.
"""

for index, i in enumerate(texto_dividido):
    prompt_para_openai = " ".join(i)

    # Agregar el prompt al historial de mensajes
    historial_mensajes.append({"role": "user", "content": prompt_para_openai})

    response = client.chat.completions.create(
        model="gpt-4o",  # Cambiar a gpt-4o para pruebas -> $5 prompt - $15 completion (1M tokens)
        temperature=0,
        messages=historial_mensajes,
    )

    # Accede a la respuesta generada por OpenAI
    respuesta_de_openai = response.choices[0].message.content

    # Guarda la respuesta en historial de mensajes
    historial_mensajes.append({"role": "assistant", "content": respuesta_de_openai})

    """ 
        FUNCION SECUNDARIA
        Guarda el texto y la respuesta en un diccionario para generar json
    """

    # Crear un diccionario con el texto y la respuesta de cada subtexto.
    dict_de_texto_y_respuesta = {
        "texto": prompt_para_openai,
        "respuesta": respuesta_de_openai,
    }

    # Agregar el diccionario a la lista -> Para generar json
    archivo_final.append(dict_de_texto_y_respuesta)

    print(f"Texto {index + 1} de {len(texto_dividido)} procesado.")
""" 
	FINALMENTE:
"""

formatear_archivo(
    archivo=archivo_final, incluir_respuesta=False, incluir_respuestas_etiquetas=True
)

generar_json(
    data=archivo_final,
    nombre_archivo=nombre_archivo_original,
)
generar_csv(
    data=archivo_final,
    nombre_archivo=nombre_archivo_original,
)

print("Archivo procesado con éxito.")
