from openpyxl import Workbook
from openpyxl.cell.text import InlineFont
from openpyxl.cell.rich_text import TextBlock, CellRichText


def generar_xlsx(data, ruta_archivo):
    ruta_limpia = limpiar_ruta(ruta_archivo)
    data_limpia = preparar_data_xlsx(data)
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Archivo analizado"
    ws.append(list(data_limpia[0].keys()))
    
    for row in data_limpia:
        new_row = []
        for value in row.values():
            new_row.append([generar_negritas(value)])
        ws.append(new_row)
        
    wb.save(ruta_limpia)


def preparar_data_xlsx(data, key="respuestas_etiquetas"):
    resultado = [item for d in data for item in d[key]]
    return resultado

# Privado
def limpiar_ruta(ruta_archivo):
    extension = ".xlsx"
    return f"{ruta_archivo}{extension}"

def generar_negritas(texto):
    cell_text = []
    for word in texto.split():
        if word.startswith("*") and word.endswith("*"):
            cell_text.append(TextBlock(InlineFont(b=True), word[1:-1]))
        else:
            cell_text.append(word)
    return CellRichText(cell_text)