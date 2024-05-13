from openai import OpenAI
import json
from helpers.file import lee_archivo_docx
from helpers.text import dividir_texto_por_tokens

# Instancia de la clase OpenAI, para usar los métodos de la API.
client = OpenAI()
# Lee el archivo .docx y devuelve una lista con los párrafos del archivo.
texto = lee_archivo_docx(ruta_archivo='docs/res-5.docx')
# Divide el texto en subtextos de máximo 3000 tokens.
texto_dividido = dividir_texto_por_tokens(texto=texto, max_tokens=3000)

# Leer el archivo messages.json (contiene mensajes base)
with open("messages.json", "r", encoding='utf-8') as f:
    messages = json.load(f)

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
        model="gpt-3.5-turbo",
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

# Guardar la lista de diccionarios en un archivo .json
with open("respuestas.json", "w", encoding='utf-8') as f:
	json.dump(list_of_dicts, f, ensure_ascii=False, indent=4)
    