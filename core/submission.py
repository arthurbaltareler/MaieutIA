def submeter_entrada(motor, entrada):
    """Encaminha integralmente a entrada do aluno ao motor."""

    if not isinstance(entrada, str):
        raise TypeError("A entrada deve ser um texto.")

    if not entrada.strip():
        raise ValueError("A entrada não pode estar vazia.")

    return motor.responder(entrada)