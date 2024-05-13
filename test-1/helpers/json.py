import json

def leer_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding='utf-8') as f:
        return json.load(f)

def crear_json(data, nombre_archivo):
    with open(nombre_archivo, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)