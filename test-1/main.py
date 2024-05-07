# importing required modules 
from docx import Document 
import pprint
from helpers.token import numero_tokens_por_string
from helpers.file import lee_archivo_docx
  
text = lee_archivo_docx(ruta_archivo='docs/res-5.docx')

lista = []
sublista = []
tokens = 0
max_tokens = 300

for i in text:
    tokens += numero_tokens_por_string(i)
    if tokens >= max_tokens:
        if sublista[-1][-1] == ':':
            y = sublista.pop()
            lista.append(sublista)
            sublista = [y]
        else:
            lista.append(sublista)
            sublista = [i]
        tokens = numero_tokens_por_string(sublista[0])
    else:
        sublista.append(i)
if lista == [] and sublista != []:
    lista.append(sublista)
    
pprint.pp(lista)

print("*"*50)

for i in text:
    print((numero_tokens_por_string(i), i))
    
    
