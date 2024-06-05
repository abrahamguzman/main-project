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