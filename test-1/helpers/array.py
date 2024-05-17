def format_list_of_dicts(
    list_of_dicts, 
    incluir_respuestas = False, 
    incluir_respuestas_etiquetas = False,
    incluir_texto = False):
    for i in list_of_dicts:
        lines = i["respuesta"].split("\n\n")
        
        if incluir_respuestas:
            i["respuestas"] = lines
        
        if incluir_respuestas_etiquetas:
            lines_etiquetas = []
            for line in lines:
                texto_etiqueta = line.split("\n")
                lines_etiquetas.append({
                    "texto": texto_etiqueta[0],
                    "etiquetas": texto_etiqueta[1]
                })
            i["respuestas_etiquetas"] = lines_etiquetas
        
        if incluir_texto == False:
            del i["texto"]   