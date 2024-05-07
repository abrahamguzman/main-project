from helpers.token import numero_tokens_por_string

def dividir_texto_por_tokens(texto: str, max_tokens: int) -> list[list[str]]:
    lista = []
    sublista = []
    tokens = 0

    for i in texto:
        tokens += numero_tokens_por_string(i)
        if tokens >= max_tokens:
            lista.append(sublista)
            sublista = [i]
            tokens = numero_tokens_por_string(i)
        else:
            sublista.append(i)
    
    lista.append(sublista) # Agregar la última sublista (NOTA -> Verificar que no sobrepase el límite de tokens)

    return lista