def adicionar_mensagem(historico, role, content):
    """Adiciona uma mensagem sem remover as anteriores."""

    if role not in ("user", "assistant"):
        raise ValueError("Papel de mensagem inválido.")

    if not isinstance(content, str):
        raise TypeError("O conteúdo deve ser textual.")

    historico.append({
        "role": role,
        "content": content
    })

    return historico
