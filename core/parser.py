
def processar_entrada(texto: str) -> str:
    """
    Normaliza a entrada do aluno preservando sua formatação.

    - Normaliza diferentes tipos de quebra de linha.
    - Preserva indentação e espaços internos.
    - Rejeita entradas vazias ou malformadas.
    """

    if not isinstance(texto, str):
        raise TypeError("A entrada deve ser um texto.")

    if not texto.strip():
        raise ValueError("A entrada não pode estar vazia.")

    if "\0" in texto:
        raise ValueError("A entrada contém caracteres inválidos.")

    # Normaliza quebras de linha sem alterar a indentação.
    texto = texto.replace("\r\n", "\n")
    texto = texto.replace("\r", "\n")

    return texto
