import csv


def generar_csv(data, nombre_archivo):
    ruta_limpia = generar_ruta_csv(nombre_archivo)
    data_limpia = list_dict_to_list(data)
    with open(ruta_limpia, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data_limpia[0].keys())
        for row in data_limpia:
            writer.writerow(row.values())


def list_dict_to_list(data, key="respuestas_etiquetas"):
    resultado = [d[key] for d in data]
    return resultado

# Privado
def generar_ruta_csv(nombre_archivo):
    nombre_archivo_limpio = nombre_archivo.split(".")[0]
    extension = ".csv"
    carpeta = "respuestas/csv/"
    return f"{carpeta}{nombre_archivo_limpio}{extension}"
