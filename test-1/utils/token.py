import tiktoken

""" 
    Función que cuenta el número de tokens en una cadena de texto, hace uso de biblioteca tiktoken, oficial de OpenAI.
    
    Args: (Argumentos)
        string (str): Cadena de texto a contar.
        encoding_name (str): Nombre del encoding a utilizar. Por defecto, se utiliza "cl100k_base" (gpt-4, gpt-3.5-turbo, text-embedding-ada-002, text-embedding-3-small, text-embedding-3-large)

    Returns: (Retorna)
        int: Número de tokens en la cadena de texto.
    
    Nota:
        Para más información sobre esta función, visite: https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
"""
def numero_tokens_por_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens