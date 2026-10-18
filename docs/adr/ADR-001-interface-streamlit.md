# ADR-001: Interface Web em Streamlit em vez de bot Telegram/Discord

- **Status:** Aceita
- **Decisores:** equipe (Arthur, Bianca e João)
- **Registro:** decisão tomada no Módulo 1 e documentada retroativamente em 18/10/2026. Contexto e consequências foram redigidos pela Scrum Master e devem ser confirmados por Bianca e João.
- **Vínculos:** `docs/PROJECT_CHARTER.md` (Escopo dentro do MVP), `docs/EAP.md` (pacote 1.1), RF01, CHANGELOG (CH-002)

## Contexto

O enunciado do trabalho permite que a interface do assistente seja um bot de chat (Telegram ou Discord) ou uma aplicação Web mínima (como Streamlit), e deixa claro que a avaliação foca o processo de gestão e a rastreabilidade, não a complexidade da interface.

A equipe precisava escolher cedo, porque a decisão define o pacote 1.1 da EAP, o formato do histórico de conversa (RF03) e o que será demonstrado na apresentação. Restrições do projeto: equipe de 3 pessoas, prazo de 29/08 a 30/11/2026, custo inicial de R$ 0,00 e Python como linguagem principal.

## Opções consideradas

| Opção | Pontos a favor | Pontos contra |
|---|---|---|
| **Bot no Telegram** | Interface familiar ao aluno; sempre disponível depois de hospedado | Exige token de bot, configuração de webhook ou polling e uma dependência externa além da OpenAI |
| **Bot no Discord** | Interface familiar a comunidades de estudo | Mesmas exigências do Telegram, com permissões e servidor próprios |
| **Web mínima em Streamlit** | Interface construída em Python puro, sem infraestrutura de mensageria; roda localmente para desenvolvimento e demonstração | Menos familiar que um app de chat; exige decidir como e onde hospedar |

## Decisão

Adotar uma interface Web mínima em Streamlit.

## Consequências

**Positivas**
- A interface (entrada de texto ou código e área do diálogo) é construída na mesma linguagem do restante do sistema, o que simplifica o desenvolvimento e a revisão cruzada.
- Não há token, webhook nem conta de plataforma de mensageria para gerenciar, o que reduz a superfície de segredos além da chave da OpenAI (RNF02, RNF03, RNF07).
- A demonstração local é simples.

**Negativas e riscos aceitos**
- O aluno não usa um aplicativo de chat que já conhece; precisa abrir uma página.
- Não há infraestrutura de hospedagem definida. Sem ela, o acesso depende de executar a aplicação localmente.
- O Streamlit reexecuta o script a cada interação; o histórico da conversa precisa ser mantido explicitamente no estado da sessão. Isso é compatível com o RF03, que define histórico apenas durante a sessão ativa, sem persistência.

**Reversibilidade**
A decisão é reversível com custo moderado: a EAP separa a interface (1.1) do Core Lógico (1.2). Trocar por um bot exigiria reescrever apenas a camada de interface.

## Revisão

Reavaliar esta decisão se a equipe decidir testar o assistente com alunos reais (o que alteraria o quadrante do stakeholder "usuários" no mapa de `docs/RISCOS_E_COMUNICACAO.md`).