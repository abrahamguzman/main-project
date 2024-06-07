from openai import OpenAI
from utils.window import abrir_archivo
from utils.openai.file import subir_archivo
from utils.openai.vector_store import crear_vector_store, subir_archivo_a_vector_store
from utils.openai.assistant import crear_asistente, modificar_asistente
from utils.openai.run import crear_run
from utils.openai.thread import (
    añadir_mensaje_hilo,
    crear_hilo,
    eliminar_hilo,
    obtener_ultimo_mensaje_hilo,
)

client = OpenAI()

""" 
# Subir archivo a OpenAI
ruta_archivo = abrir_archivo(
    extension=".docx", titulo="Seleccionar archivo para vectorizar (.docx o)"
)
archivo_subido = subir_archivo(client=client, ruta_archivo=ruta_archivo)

# Crear vector store y añadir archivo subido a vector store
# vector_store = crear_vector_store(client=client, name="vs_prueba")
vector_store_id = "vs_ZOYSsOlWh8Pae323oc6HA4aY"
subir_archivo_a_vector_store(
    client=client, id_archivo=archivo_subido.id, id_vector_store=vector_store_id
)
 """


# MODIFICAR SOLO LO DE ABAJO


# Crear asistente y guardar su ID
""" asistente = crear_asistente(
    client=client,
    nombre="asistente_Jessica",
    instrucciones="Eres un experto lingüista en idioma español, segmentarás y etiquetarás los segmentos de un texto segun las instrucciones dadas.",
    vector_store_id="vs_gWWBzdq03YldgIPmqqW6Z0cg"
)
print(asistente.id) """

# Modificar asistente (RECOMENDADO)
modificar_asistente(
    id_asistente="asst_6i37B4mjWIaPV5k9K26LkwKb",
    instrucciones="Eres un experto lingüista en idioma español, segmentarás y etiquetarás los segmentos de un texto segun las instrucciones dadas.",
)


# FUNCIONMIENTO PRINCIPAL (solo modificar el ID del asistente)

# ASISTENTE A USAR (ID)
id_asistente = "asst_6i37B4mjWIaPV5k9K26LkwKb"


# Crear hilo y guardar su ID
hilo = crear_hilo(client=client)
#hilo.id = "Insertar ID del hilo (Si es necesario)"


# Prompt para el asistente
while True:
    prompt = input("Prompt: ")

    message = añadir_mensaje_hilo(client=client, thread_id=hilo.id, content=prompt)

    run = crear_run(client=client, thread_id=hilo.id, assistant_id=id_asistente)

    if run:
        print(obtener_ultimo_mensaje_hilo(client=client, thread_id=hilo.id))
