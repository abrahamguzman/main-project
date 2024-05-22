from openai import OpenAI
from helpers.file import lee_archivo_docx
from helpers.text import dividir_texto_por_tokens
from helpers.array import format_list_of_dicts
from helpers.json import crear_json, leer_json
from helpers.consola import seleccionar_archivo

# Instancia de la clase OpenAI, para usar los métodos de la API.
client = OpenAI()

# Lee el archivo .docx y devuelve una lista con los párrafos del archivo.
ruta_archivo = seleccionar_archivo(directorio="docs/")
print("Archivo seleccionado: ", ruta_archivo)
print("Procesando...")

texto = lee_archivo_docx(ruta_archivo="docs/" + ruta_archivo)

# Divide el texto en subtextos de máximo 3000 tokens.
texto_dividido = dividir_texto_por_tokens(texto=texto, max_tokens=1000) # Cambiar a 3500 tokens

# Lee archivo que contiene mensajes base
historial_mensajes = leer_json(nombre_archivo="entrenamiento_base/T_SyE_Jessica.json")

# Lista de diccionarios con el texto y la respuesta de cada subtexto
list_of_dicts = []

""" 
    PASO PRINCIPAL:
    Se envía cada subtexto a OpenAI para obtener una respuesta.
"""

for i in texto_dividido:
    prompt_para_openai = ' '.join(i)
    
    # Agregar el prompt al historial de mensajes
    historial_mensajes.append({
		"role": "user", 
		"content": prompt_para_openai
		})
    
    response = client.chat.completions.create(
        model="gpt-4o", # Cambiar a gpt-4o para pruebas -> $5 prompt - $15 completion (1M tokens)
        temperature=0,
        messages=historial_mensajes
        )
    
    # Accede a la respuesta generada por OpenAI
    respuesta_de_openai = response.choices[0].message.content
    
    # Guarda la respuesta en historial de mensajes
    historial_mensajes.append({
        "role": "assistant",
        "content": respuesta_de_openai
        })
    
    """ 
        FUNCION SECUNDARIA
        Guarda el texto y la respuesta en un diccionario para generar json
    """
    
    # Crear un diccionario con el texto y la respuesta de cada subtexto.
    dict_de_texto_y_respuesta = {
        "texto": prompt_para_openai, 
        "respuesta": respuesta_de_openai
        }
    
    # Agregar el diccionario a la lista -> Para generar json
    list_of_dicts.append(dict_de_texto_y_respuesta)


""" 
	FINALMENTE:
"""

# Formatear la lista de diccionarios (Ver helpers/array.py)
format_list_of_dicts(list_of_dicts)
 
# Guardar la lista de diccionarios en un archivo .json
crear_json(data=list_of_dicts, nombre_archivo="respuestas/"+ruta_archivo.split(".")[0]+"-4o.json")

print("Archivo procesado con éxito.")
    