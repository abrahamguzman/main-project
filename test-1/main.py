from openai import OpenAI
from helpers.file import lee_archivo_docx
from helpers.text import dividir_texto_por_tokens
from helpers.array import format_list_of_dicts
from helpers.json import crear_json, leer_json

# Instancia de la clase OpenAI, para usar los métodos de la API.
client = OpenAI()

# Lee el archivo .docx y devuelve una lista con los párrafos del archivo.
texto = lee_archivo_docx(ruta_archivo='docs/Propuesta de Sanción 1 3.docx')

# Divide el texto en subtextos de máximo 3000 tokens.
texto_dividido = dividir_texto_por_tokens(texto=texto, max_tokens=250) # Cambiar a 3500 tokens
#print(texto_dividido)

# Lee archivo que contiene mensajes base
messages = leer_json(nombre_archivo="entrenamiento_base/Ronald_Manchego_Queja.json")
# print(messages)

# Lista de diccionarios con el texto y la respuesta de cada subtexto
list_of_dicts = []

# Crea un bucle para iterar con cada subtexto y mandarlo como prompt
for i in texto_dividido:
    texto_para_content = ' '.join(i)
    
    messages.append({
		"role": "user", 
		"content": texto_para_content
		})
    
    response = client.chat.completions.create(
        model="gpt-4o", # Cambiar a gpt-4o para pruebas -> $5 prompt - $15 completion (1M tokens)
        temperature=0,
        messages=messages
        )
    
    # Crear un diccionario con el texto y la respuesta de cada subtexto.
    dict_de_texto_y_respuesta = {
        "texto": texto_para_content, 
        "respuesta": response.choices[0].message.content
        }
    # Agregar el diccionario a la lista.
    list_of_dicts.append(dict_de_texto_y_respuesta)


""" 
	Una vez recibidas y guardadas las respuestas,
	se procede con lo siguente
"""

# Formatear la lista de diccionarios (Ver helpers/array.py)
format_list_of_dicts(list_of_dicts)
 
# Guardar la lista de diccionarios en un archivo .json
crear_json(data=list_of_dicts, nombre_archivo="respuestas/Segm_Etiq_Propuesta de Sanción 1 3_gpt-4ooo.json")
    