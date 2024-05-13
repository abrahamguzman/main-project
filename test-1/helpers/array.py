def format_list_of_dicts(list_of_dicts):
    for i in list_of_dicts:
        lines = i["respuesta"].split("\n")
        i["respuestas"] = lines
        lines_etiquetas = []
        for line in lines:
            etiquetas_juntas = line.split("&")
            if len(etiquetas_juntas) > 1:  # Check if there is anything after "&"
                etiquetas_separadas = etiquetas_juntas[-1].split("-")
                etiquetas_finales = [x.strip() for x in etiquetas_separadas]
                lines_etiquetas.append({
                    "texto": line,
                    "etiquetas": etiquetas_finales
                })
        i["respuestas_etiquetas"] = lines_etiquetas