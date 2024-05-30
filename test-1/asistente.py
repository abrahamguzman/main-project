from openai import OpenAI
from helpers.window import abrir_archivo
from helpers.openai.file import subir_archivo
from helpers.openai.vector_store import crear_vector_store, subir_archivo_a_vector_store
from helpers.openai.assistant import crear_asistente

client = OpenAI()

""" 
# Subir archivo a OpenAI
ruta_archivo = abrir_archivo(extension=".docx", titulo="Seleccionar archivo para vectorizar (.docx o .pdf)")
archivo_subido = subir_archivo(client=client, ruta_archivo=ruta_archivo)

# Crear vector store y añadir archivo subido a vector store
vector_store = crear_vector_store(client=client, name="vs_prueba")
subir_archivo_a_vector_store(client=client, id_archivo=archivo_subido.id, id_vector_store=vector_store.id)

# Crear asistente
asistente = crear_asistente(
    client=client,
    nombre="asistente_prueba",
    instrucciones="Eres un experto lingüista en idioma español",
    vector_store_id=vector_store.id
)

print(asistente) 
"""

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="tienes algún vector store subido?"
)

id_asistente = "asst_4lwYsJmPWAX92B2roX221UED"
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=id_asistente,
  instructions="veo que tienes un vector store registrado, ¿puedes decirme cuál es su nombre?",
)



if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages.data[0].content[0].text.value)
else:
  print(run.status)