import csv


def generar_csv(data, nombre_archivo):
    ruta_limpia = generar_ruta_csv(nombre_archivo)
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
def generar_ruta_csv(nombre_archivo):
    nombre_archivo_limpio = nombre_archivo.split(".")[0]
    extension = ".csv"
    carpeta = "respuestas/csv/"
    return f"{carpeta}{nombre_archivo_limpio}{extension}"
