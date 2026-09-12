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

## Diagrama de Classes

O diagrama de classes representa a estrutura estática planejada para o Maieut-IA, destacando as classes responsáveis pela interface, pelo processamento lógico das perguntas e pela integração com a API de inteligência artificial.

```mermaid
classDiagram

    %% =========================
    %% INTERFACE
    %% =========================

    class InterfaceChat {
        +iniciar()
        +receber_pergunta() String
        +exibir_resposta(resposta)
        +exibir_erro(mensagem)
    }

    %% =========================
    %% CORE LÓGICO
    %% =========================

    class Assistente {
        -parser: Parser
        -cliente_api: ClienteAPI
        -processador: ProcessadorResposta
        +processar_pergunta(pergunta) Resposta
    }

    class Parser {
        +validar(pergunta) Boolean
        +processar(pergunta) String
        +montar_prompt(pergunta) String
    }

    class ProcessadorResposta {
        +processar(resposta) String
        +preparar_exibicao(resposta)
    }

    %% =========================
    %% INTEGRAÇÃO COM API
    %% =========================

    class ClienteAPI {
        -api_key: String
        -modelo: String
        -api_url: String
        +enviar_prompt(prompt) String
        +tratar_erro(erro)
    }

    %% =========================
    %% OBJETO DE RESPOSTA
    %% =========================

    class Resposta {
        -conteudo: String
        -sucesso: Boolean
        -erro: String
        +obter_conteudo() String
        +foi_bem_sucedida() Boolean
    }

    %% =========================
    %% RELACIONAMENTOS
    %% =========================

    InterfaceChat --> Assistente : utiliza

    Assistente *-- Parser : possui
    Assistente *-- ClienteAPI : utiliza
    Assistente *-- ProcessadorResposta : possui

    Assistente --> Resposta : gera

    Parser --> ClienteAPI : prepara chamada
```