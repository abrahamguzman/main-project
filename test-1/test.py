from openai import OpenAI
from utils.file import lee_archivo_docx
from utils.text import dividir_texto_por_tokens
from utils.array import formatear_archivo
from utils.json import generar_json, leer_json
from utils.consola import seleccionar_archivo
from utils.csv import generar_csv
from utils.xlsx import generar_xlsx
from utils.window import abrir_archivo, guardar_archivo




archivo_procesado = leer_json("respuestas/json/prueba.json")
ruta_guardar_archivos = guardar_archivo()

generar_xlsx(
    data=archivo_procesado,
    ruta_archivo=ruta_guardar_archivos,
)


print("Archivo procesado con éxito.")