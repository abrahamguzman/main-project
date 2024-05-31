from openai import OpenAI
from utils.file import lee_archivo_docx
from utils.text import dividir_texto_por_tokens
from utils.array import formatear_archivo
from utils.json import generar_json, leer_json
from utils.consola import seleccionar_archivo
from utils.csv import generar_csv
from utils.xlsx import generar_xlsx
from utils.window import abrir_archivo, guardar_archivo


client = OpenAI()


""" 
    PASO 1:
    - 1.1. Extraemos contenido del archivo a analizar (.docx) y lo dividimos por número de tokens.
    - 1.2. Leemos el archivo de entrenamiento base (.json)
"""


# 1.1.
ruta_archivo_analizable = abrir_archivo(extension=".docx", titulo="Seleccionar archivo a analizar (.docx)")
texto = lee_archivo_docx(ruta_archivo=ruta_archivo_analizable)
texto_dividido = dividir_texto_por_tokens(texto=texto, max_tokens=1000)

# 1.2.
ruta_entrenamiento_base = abrir_archivo(extension=".json", titulo="Seleccionar archivo de entrenamiento base (.json)")
historial_prompts = leer_json(ruta_archivo=ruta_entrenamiento_base)


""" 
    PASO 2:
    - Se envía cada subtexto a OpenAI para obtener una respuesta.
"""


archivo_procesado = []

for index, i in enumerate(texto_dividido):
    prompt_para_openai = " ".join(i)

    # Agregar el prompt al historial de mensajes
    historial_prompts.append({"role": "user", "content": prompt_para_openai})

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=historial_prompts,
    )

    # Accede a la respuesta generada por OpenAI
    respuesta_de_openai = response.choices[0].message.content

    # Guarda la respuesta en historial de mensajes
    historial_prompts.append({"role": "assistant", "content": respuesta_de_openai})

    # Guardar texto y respuesta en un diccionario
    dict_de_texto_y_respuesta = {
        "texto": prompt_para_openai,
        "respuesta": respuesta_de_openai,
    }

    # Agregar el diccionario a la lista -> Para generar json
    archivo_procesado.append(dict_de_texto_y_respuesta)

    print(f"Texto {index + 1} de {len(texto_dividido)} procesado.")
    
    
""" 
	FINALMENTE:
"""


formatear_archivo(
    archivo=archivo_procesado, incluir_respuesta=False, incluir_respuestas_etiquetas=True
)

ruta_guardar_archivos = guardar_archivo()
generar_json(
    data=archivo_procesado,
    ruta_archivo=ruta_guardar_archivos,
)
generar_csv(
    data=archivo_procesado,
    ruta_archivo=ruta_guardar_archivos,
)


print("Archivo procesado con éxito.")
