import csv
from helpers.window import guardar_archivo


def generar_csv(data, ruta_archivo):
    ruta_limpia = limpiar_ruta(ruta_archivo)
    data_limpia = preparar_data_csv(data)
    with open(ruta_limpia, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data_limpia[0].keys())
        for row in data_limpia:
            writer.writerow(row.values())


def preparar_data_csv(data, key="respuestas_etiquetas"):
    resultado = [item for d in data for item in d[key]]
    return resultado

# Privado
def limpiar_ruta(ruta_archivo):
    extension = ".csv"
    return f"{ruta_archivo}{extension}"
