from openai import OpenAI
from utils.window import abrir_archivo
from utils.openai.file import subir_archivo
from utils.openai.vector_store import crear_vector_store, subir_archivo_a_vector_store
from utils.openai.assistant import crear_asistente
from utils.openai.run import crear_run
from utils.openai.thread import añadir_mensaje_hilo, crear_hilo, eliminar_hilo, obtener_ultimo_mensaje_hilo

client = OpenAI()


""" 
# Subir archivo a OpenAI
ruta_archivo = abrir_archivo(extension=".docx", titulo="Seleccionar archivo para vectorizar (.docx o .pdf)")
archivo_subido = subir_archivo(client=client, ruta_archivo=ruta_archivo)

# Crear vector store y añadir archivo subido a vector store
#vector_store = crear_vector_store(client=client, name="vs_prueba")
vector_store_id = "vs_ZOYSsOlWh8Pae323oc6HA4aY"
subir_archivo_a_vector_store(client=client, id_archivo=archivo_subido.id, id_vector_store=vector_store_id) 
"""

# Crear asistente
""" asistente = crear_asistente(
    client=client,
    nombre="asistente_prueba",
    instrucciones="Eres un experto lingüista en idioma español",
    vector_store_id=vector_store.id
)
 """
#print(asistente) 


#thread = crear_hilo(client=client)
thread_id = "thread_PibRbqq0ltxL0nIWn1r9hQTa"

message = añadir_mensaje_hilo(
  client=client,
  thread_id=thread_id,
  content="continua por favor"
)

id_asistente = "asst_4lwYsJmPWAX92B2roX221UED"
run = crear_run(client=client,thread_id=thread_id, assistant_id=id_asistente)

if run: 
  print(obtener_ultimo_mensaje_hilo(client=client, thread_id=thread_id))