from openai import OpenAI
import json
from helpers.file import lee_archivo_docx
from helpers.text import dividir_texto_por_tokens
  
client = OpenAI()  # Instancia de la clase OpenAI, para usar los métodos de la API.
texto = lee_archivo_docx(ruta_archivo='docs/res-5.docx') # Lee el archivo .docx y devuelve una lista con los párrafos del archivo.
texto_dividido = dividir_texto_por_tokens(texto=texto, max_tokens=3000) # Divide el texto en subtextos de máximo 3000 tokens.

# Leer el archivo messages.json
with open("messages.json", "r", encoding='utf-8') as f:
    messages = json.load(f)

list_of_dicts = [] # Lista de diccionarios con el texto y la respuesta de cada subtexto.

for i in texto_dividido:
    texto_para_content = ' '.join(i)
    print(texto)
    
    response = response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=messages.append({
                "role": "user", 
                "content": texto_para_content
                }),
        )
    
    # Crear un diccionario con el texto y la respuesta de cada subtexto.
    dict_de_texto_y_respuesta = {
        "texto": texto_para_content, 
        "respuesta": response.choices[0].message.content
        }
    # Agregar el diccionario a la lista.
    list_of_dicts.append(dict_de_texto_y_respuesta)

print(list_of_dicts)
    