from docx import Document 

""" 
  Lee un archivo .docx y devuelve una lista con los párrafos del archivo.
  
  Args: (Argumentos)
    ruta_archivo (str): Ruta del archivo .docx
    
  Returns: (Retorna)
    list[str]: Lista con los párrafos del archivo.
    
  Además, se eliminan:
    - Párrafos en blanco.
    - Espacios en blanco al inicio y al final de los párrafos.
"""
def lee_archivo_docx(ruta_archivo: str) -> list[str]:
    doc = Document(ruta_archivo)
    texto_completo = []
    for parrafo in doc.paragraphs:
        if parrafo.text.strip() != '':
            texto_completo.append(parrafo.text.strip())
    return texto_completo