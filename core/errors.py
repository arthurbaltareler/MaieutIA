
from openai import (
    APIConnectionError,
    APITimeoutError,
    RateLimitError,
)


def mensagem_fallback(erro: Exception) -> str:
    """Converte erros técnicos em mensagens amigáveis ao usuário."""

    if isinstance(erro, RateLimitError):
        return (
            "O serviço está temporariamente ocupado. "
            "Aguarde um pouco e tente novamente."
        )

    if isinstance(erro, APITimeoutError):
        return (
            "O assistente demorou para responder. "
            "Tente novamente em instantes."
        )

    if isinstance(erro, APIConnectionError):
        return (
            "Não foi possível conectar ao assistente. "
            "Verifique sua conexão e tente novamente."
        )

    return (
        "Ocorreu um erro ao processar sua solicitação. "
        "Tente novamente mais tarde."
    )
