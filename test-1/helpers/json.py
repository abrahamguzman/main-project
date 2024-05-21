import json


def leer_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return json.load(f)


def generar_json(data, nombre_archivo):
    ruta_archivo = generar_ruta_json(nombre_archivo)
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Privado
def generar_ruta_json(nombre_archivo):
    nombre_archivo_limpio = nombre_archivo.split(".")[0]
    extension = ".json"
    carpeta = "respuestas/json/"
    return f"{carpeta}{nombre_archivo_limpio}{extension}"
