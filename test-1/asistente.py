from openai import OpenAI
from utils.window import abrir_archivo
from utils.consola import seleccionar_asistente
from utils.openai.file import subir_archivo
from utils.openai.vector_store import crear_vector_store, subir_archivo_a_vector_store
from utils.openai.assistant import crear_asistente, modificar_asistente, listar_asistentes
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
    nombre="fiscal_trata_personas",
    instrucciones="Eres un fiscal peruano que solo le interesa encarcelar personas, para poder ascender en tu trabajo, no escatimas en mentir",
    temperatura=0.5
)
print(asistente.id) """

# Modificar asistente (RECOMENDADO)
modificar_asistente(
    id_asistente="asst_gd4kui7hcC0Pr9kGvIMoz8BE",
    temperatura=0,
)


# FUNCIONMIENTO PRINCIPAL (solo modificar el ID del asistente)

# ASISTENTE A USAR (ID)
#id_asistente = "asst_9vUC2xg3KmI6CoHgILMOhPmB"
vector_store_id = "vs_pK5oDUL60cyEfXcwFHH8LMPZ"

# Crear hilo y guardar su ID
hilo = crear_hilo(vector_store_id)
print(hilo.id)
hilo.id = "thread_u5It3UjSY9jtKUnMM43R14c2" # Pegar el ID del hilo a usar


# Prompt para el asistente
while True:
    asistentes = listar_asistentes()
    nombres_asistentes = [f"{i}-{asistente.name}" for i, asistente in enumerate(asistentes.data)]
    ids_asistentes = [asistente.id for asistente in asistentes.data]
    indice = seleccionar_asistente(nombres_asistentes).split("-")[0]
    id_asistente = ids_asistentes[int(indice)]
    while True:
        prompt = input("Prompt: ")
        if prompt == "s" or prompt == "S":
            break
        
        message = añadir_mensaje_hilo(client=client, thread_id=hilo.id, content=prompt)
        run = crear_run(thread_id=hilo.id, assistant_id=id_asistente)
        if run:
            print(obtener_ultimo_mensaje_hilo(client=client, thread_id=hilo.id))
