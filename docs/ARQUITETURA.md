## Diagrama de Sequência — Interação com o Assistente

O diagrama abaixo representa o fluxo temporal de uma interação entre o aluno e o Maieut-IA, desde o envio do problema até a exibição incremental da resposta na interface.

```mermaid
sequenceDiagram
    actor Aluno
    participant Interface as InterfaceChat
    participant Assistente as Assistente
    participant Parser as Parser
    participant Cliente as ClienteOpenAI
    participant API as OpenAI API
    participant Processador as ProcessadorResposta

    Aluno->>Interface: Envia problema
    Interface->>Assistente: Encaminha pergunta
    Assistente->>Parser: Solicita parsing da pergunta
    Parser-->>Assistente: Retorna pergunta processada

    Assistente->>Cliente: Envia prompt processado
    Cliente->>API: Requisição à API
    API-->>Cliente: Retorna resposta

    Cliente-->>Assistente: Entrega resposta recebida
    Assistente->>Processador: Processa resposta
    Processador-->>Assistente: Retorna resposta pronta

    Assistente->>Interface: Inicia exibição da resposta

    loop Exibição incremental
        Interface-->>Aluno: Exibe próximo trecho da resposta
    end

    Interface-->>Aluno: Resposta completa
```