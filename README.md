# Maieut-IA

**Assistente Socrático de Maratona de Programação**

> Nome inspirado na maiêutica socrática: o assistente não entrega respostas prontas, ajuda o aluno a "dar à luz" a solução que ele já tem em potencial, por meio de perguntas e dicas guiadas — nunca revelando o código-fonte.

📄 Veja o [Project Charter e a Avaliação TELOS completos na Wiki](../../wikis/Project-Charter-%E2%80%94-Maieut-IA) deste repositório.

---

## Equipe e Papéis

| Nome Completo | Usuário GitLab | E-mail | Papel Principal na Equipe |
| :--- | :--- | :--- | :--- |
| Arthur Baltar Eler | `@ArchieBaltar` | `arthur.cefet.engcomputacao@gmail.com` | Scrum Master |
| Bianca Barros | `@biancaB` | `bianca@cefetmg.br` | Product Owner & Engenharia de Prompt |
| João Carlos | `@joaocarlos.fm` | `joao@cefetmg.br` | Tech Lead / Dev |

## Stack Tecnológica

- **Linguagem:** Python
- **Framework/Interface:** Streamlit (Web mínima)
- **Provedor de LLM:** OpenAI

---

## Sobre o Projeto

O Maieut-IA é um assistente de IA que atua como treinador (coach) para estudantes de maratona de programação (ICPC). Diferente de um chatbot genérico, ele **nunca entrega o código-fonte pronto** — em vez disso, identifica a classe do algoritmo do problema (ex: Programação Dinâmica, Grafos) e aponta falhas de complexidade (ex: O(N²) em vez de O(N log N)), guiando o aluno até a solução por meio de perguntas e dicas.

Para mais detalhes sobre justificativa, escopo, riscos e viabilidade do projeto, consulte o Project Charter na Wiki.