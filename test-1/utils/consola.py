import inquirer
from utils.docs import listar_archivos

def seleccionar_archivo(directorio):
    archivos = listar_archivos(directorio)
    questions = [
        inquirer.List(
            name='archivo',
            message="Por favor, selecciona un archivo",
            choices=archivos,
            ),
        ]

    answers = inquirer.prompt(questions)

    return answers["archivo"]

def seleccionar_asistente(asistentes):
    questions = [
        inquirer.List(
            name='asistente',
            message="Por favor, selecciona un asistente",
            choices=asistentes,
            ),
        ]

    answers = inquirer.prompt(questions)

    return answers["asistente"]