from openai import OpenAI
from helpers.file import lee_archivo_docx
from helpers.text import dividir_texto_por_tokens
from helpers.array import formatear_archivo
from helpers.json import generar_json, leer_json
from helpers.consola import seleccionar_archivo
from helpers.csv import generar_csv
from helpers.xlsx import generar_xlsx
from helpers.window import abrir_archivo, guardar_archivo




archivo_procesado = leer_json("respuestas/prueba/prueba.json")
ruta_guardar_archivos = guardar_archivo()

generar_xlsx(
    data=archivo_procesado,
    ruta_archivo=ruta_guardar_archivos,
)


print("Archivo procesado con éxito.")