import json
from helpers.window import guardar_archivo


def leer_json(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return json.load(f)


def generar_json(data, ruta_archivo):
    ruta_archivo_limpia = limpiar_ruta(ruta_archivo)
    with open(ruta_archivo_limpia, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Privado
def limpiar_ruta(ruta_archivo):
    extension = ".json"
    return f"{ruta_archivo}{extension}"
