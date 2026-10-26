# Maieut-IA

**Assistente Socrático de Maratona de Programação**

> Nome inspirado na maiêutica socrática: o assistente não entrega respostas prontas, ajuda o aluno a "dar à luz" a solução que ele já tem em potencial, por meio de perguntas e dicas guiadas — nunca revelando o código-fonte.

📄 Veja o [Project Charter e a Avaliação TELOS completos na Wiki](../../wikis/Project-Charter-%E2%80%94-Maieut-IA) deste repositório. O Charter também está em [`docs/PROJECT_CHARTER.md`](docs/PROJECT_CHARTER.md), e o histórico de mudanças em [`CHANGELOG.md`](CHANGELOG.md).

---

## Equipe e Papéis

| Nome Completo | Usuário GitLab | E-mail | Papel Principal na Equipe |
| :--- | :--- | :--- | :--- |
| Arthur Baltar Eler | `@ArchieBaltar` | `arthur.cefet.engcomputacao@gmail.com` | Scrum Master |
| Bianca Barros | `@biancaB` | `barrosbianca972@gmail.com` | Product Owner & Engenharia de Prompt |
| João Carlos | `@joaocarlos.fm` | `Joaocarlos12349@gmail.com` | Tech Lead / Dev |

## Stack Tecnológica

- **Linguagem:** Python
- **Framework/Interface:** Streamlit (Web mínima)
- **Provedor de LLM:** OpenAI

---

## Sobre o Projeto

O Maieut-IA é um assistente de IA que atua como treinador (coach) para estudantes de maratona de programação (ICPC). Diferente de um chatbot genérico, ele **nunca entrega o código-fonte pronto** — em vez disso, identifica a classe do algoritmo do problema (ex: Programação Dinâmica, Grafos) e aponta falhas de complexidade (ex: O(N²) em vez de O(N log N)), guiando o aluno até a solução por meio de perguntas e dicas.

Para mais detalhes sobre justificativa, escopo, riscos e viabilidade do projeto, consulte o Project Charter na Wiki.

## Estado atual (Milestone 2)

| Componente | Situação |
|---|---|
| System Prompt versionado | `prompts/system_prompt_v1.md`; especificação completa em [`docs/SYSTEM_PROMPT.md`](docs/SYSTEM_PROMPT.md) |
| Conversa com histórico (multi-turn) | `tests/test_dialogo.py` simula 4 turnos reenviando o histórico a cada chamada |
| Bateria de validação (18 casos) | `tests/executar_testes.py`; resultados em [`docs/CASOS_DE_TESTE_PROMPT.md`](docs/CASOS_DE_TESTE_PROMPT.md) |
| Classe DialogueEngine (core/engine.py) | separa o System Prompt do histórico e mantém o contexto entre turnos |
| Interface Streamlit (`app/`) | Não implementada; prevista para o Milestone 3 |

---

## Como executar

### Pré-requisitos

- Python 3.10 ou superior
- Git
- Uma chave de API da OpenAI

### 1. Clonar e criar o ambiente virtual

```bash
git clone https://git.juninho.com.br/cefet-gps-2026/gps-projetos-integradores/coach-de-maratona-icpc.git
cd coach-de-maratona-icpc
```

**Windows (PowerShell):**
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Se o PowerShell bloquear a ativação, rode antes `Set-ExecutionPolicy -Scope Process Bypass`.

**Linux ou macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configurar a chave de API

Copie o modelo e preencha a chave:

```powershell
Copy-Item .env.example .env      # Windows
```
```bash
cp .env.example .env             # Linux ou macOS
```

Edite o `.env` e coloque a chave depois do sinal de igual:

```
OPENAI_API_KEY=sua-chave-aqui
```

O arquivo `.env` está no `.gitignore`. **Nunca o envie ao repositório** (RNF02). Se uma chave vazar, revogue-a no painel da OpenAI antes de qualquer outra ação.

### 3. Executar

Rode os comandos a partir da raiz do repositório, com o ambiente virtual ativo:

| Objetivo | Comando | Chamadas à API |
|---|---|---|
| Testar a conexão com a API (spike) | `python spike/test_api.py` | 1 |
| Simular uma conversa de 4 turnos com histórico | `python tests/test_dialogo.py` | 4 |
| Conversar com o motor (histórico entre turnos) | python core/engine.py | uma por mensagem |
| Testar o prompt com 5 perguntas (saída em `tests/resultados.txt`) | `python tests/test_system_prompt.py` | 5 |
| Validar a estrutura da bateria sem chamar a API | `python tests/executar_testes.py --validar` | 0 |
| Executar um caso da bateria | `python tests/executar_testes.py --caso ADV-03` | um por turno do caso |
| Executar os 18 casos da bateria | `python tests/executar_testes.py` | veja o total em `--validar` |
| Registrar a revisão humana de uma execução | `python tests/executar_testes.py --revisar` | 0 |

Ao rodar `tests/test_dialogo.py`, o terminal mostra cada pergunta do aluno e a resposta do Maieut-IA. A conversa continua coerente porque o histórico inteiro é reenviado em cada turno.

### Avisos sobre a bateria de testes

- Cada execução da bateria **substitui a seção de resultados** de `docs/CASOS_DE_TESTE_PROMPT.md`. As execuções anteriores continuam em `tests/resultados_parte_b/` (um `registro.json` por execução), mas a revisão humana do documento precisa ser refeita.
- `tests/aplicar_revisao.py` aplica uma revisão já redigida à execução mais recente e exige os 18 casos concluídos. Use-o só logo após a execução a que aquele texto se refere. Para qualquer execução nova, use `--revisar`.
- Os scripts consomem tokens da API. Rode `--validar` primeiro para ver quantas chamadas a bateria faz.

---

## Estrutura do repositório

```
.
├── README.md
├── CHANGELOG.md          # Histórico de mudanças relevantes
├── requirements.txt      # openai, python-dotenv
├── .env.example          # Modelo do arquivo de configuração da chave
├── app/                  # Interface Streamlit (Milestone 3)
├── core/                 # Motor de diálogo (engine.py)
├── prompts/              # System Prompt versionado
├── spike/                # Spike do Módulo 1: conexão com a API
├── tests/                # Simulação multi-turn, bateria de 18 casos e registros
└── docs/                 # Documentação do projeto
```

As pastas ficam na raiz, sem o prefixo `src/`. A correspondência com a estrutura do enunciado do Módulo 2 é:

| Enunciado | Neste repositório |
|---|---|
| `src/prompts/` | `prompts/` |
| `src/core/` (ou `bot/`) com `engine.py` | `core/engine.py` |
| `src/tests/test_dialogo.py` | `tests/test_dialogo.py` |

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [`PROJECT_CHARTER.md`](docs/PROJECT_CHARTER.md) | Termo de abertura: justificativa, objetivos SMART, escopo, riscos |
| [`EAP.md`](docs/EAP.md) | Estrutura analítica do projeto e dicionário da EAP |
| [`REQUISITOS.md`](docs/REQUISITOS.md) | Requisitos funcionais (RF01 a RF05) e não funcionais (RNF01 a RNF07) |
| [`ARQUITETURA.md`](docs/ARQUITETURA.md) | Arquitetura e diagramas |
| [`SYSTEM_PROMPT.md`](docs/SYSTEM_PROMPT.md) | Especificação do System Prompt: persona, pistas em camadas e limites |
| [`DIRETRIZES_PROMPT.md`](docs/DIRETRIZES_PROMPT.md) | Ideologia pedagógica e exemplos de diálogo socrático |
| [`CASOS_DE_TESTE_PROMPT.md`](docs/CASOS_DE_TESTE_PROMPT.md) | Bateria de validação com problemas reais e testes adversariais |
| [`RISCOS_E_COMUNICACAO.md`](docs/RISCOS_E_COMUNICACAO.md) | Matriz de riscos, RACI e mapa de stakeholders |
| [`MIGRACAO_MODELO.md`](docs/MIGRACAO_MODELO.md) | Plano de migração de modelo |
| [`adr/`](docs/adr/) | Registros de decisões arquiteturais (ADR-001: interface Streamlit) |
