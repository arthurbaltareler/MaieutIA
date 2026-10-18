# Riscos e Comunicação — Maieut-IA

> Documento vivo da Sprint 2 (Milestone 2). Responde à Issue #41.
> **Última atualização:** 14/10/2026 | **Próximas revisões:** 19/10/2026 (fechamento do M2) e 16/11/2026 (fechamento do M3)
>
> Mitigações reduzem riscos, mas não garantem sua ausência. Os limiares de gatilho abaixo são propostas da equipe e podem ser ajustados nas revisões.

---

## 1. Escala de classificação

- **Probabilidade:** Baixa, Média ou Alta (chance de o evento ocorrer até o fim do semestre).
- **Impacto:** Baixo, Médio ou Alto (efeito sobre escopo, prazo, qualidade ou nota).
- **Nível** (cruzamento P×I):

| Nível | Combinações | Postura |
|---|---|---|
| **Crítico** | Alta/Alto | Ação imediata, acompanhamento diário |
| **Alto** | Alta/Médio, Média/Alto | Mitigação ativa, revisão a cada Milestone |
| **Médio** | Média/Médio, Alta/Baixo, Baixa/Alto | Monitorar; mitigar quando o custo for baixo |
| **Baixo** | Demais combinações | Monitorar |

*Exceção deliberada:* riscos de impacto Alto recebem mitigação mesmo com probabilidade Baixa quando a resposta é barata (caso do R03).

## 2. Matriz de Probabilidade × Impacto

| Probabilidade ↓ / Impacto → | Baixo | Médio | Alto |
|---|---|---|---|
| **Alta** | R01 | R04 | **R07, R08** |
| **Média** | — | R02, R09 | R05, R06 |
| **Baixa** | — | — | R03 |

## 3. Registro de riscos

| ID | Categoria | Risco | P | I | Nível | Dono | Estratégia | Estado | Próx. revisão |
|---|---|---|---|---|---|---|---|---|---|
| R01 | Técnico | Latência elevada ou rate limit da API | Alta | Baixo | Médio | João | Mitigar | Em monitoramento | 19/10/2026 |
| R02 | Técnico | Estouro de cota/limite de tokens | Média | Médio | Médio | João | Mitigar | Em monitoramento | 19/10/2026 |
| R03 | Técnico | Perda de acesso à chave de API (acesso concentrado em um integrante) | Baixa | Alto | Médio | João | Mitigar | Em monitoramento | 19/10/2026 |
| R04 | Técnico | Desligamento do `gpt-3.5-turbo` na data indicada de 23/10/2026 (confirmar em fonte oficial) | Alta | Médio | Alto | João | Mitigar (preparar migração) | Plano documentado; modelo proposto, aprovação pendente | 19/10/2026 |
| R05 | Pedagógico | Alucinação: informação algorítmica incorreta ou resposta a enunciado ambíguo sem reconhecer incerteza | Média | Alto | Alto | Bianca | Mitigar | Em monitoramento | 19/10/2026 |
| R06 | Pedagógico | Assistente entrega a solução completa quando pressionado (pedido direto ou prompt injection) | Média | Alto | Alto | Bianca | Mitigar | Em monitoramento | 19/10/2026 |
| R07 | Escopo/Cronograma | Sobrecarga ou indisponibilidade de membros; conhecimento técnico concentrado (Fator Ônibus) | Alta | Alto | Crítico | Arthur | Mitigar | Aberto | 19/10/2026 |
| R08 | Escopo/Cronograma | Atraso no caminho crítico do Milestone 2 | Alta | Alto | Crítico | Arthur | Mitigar | Aberto | 19/10/2026 |
| R09 | Escopo/Cronograma | Scope Creep ou Gold Plating (pedidos informais, funcionalidades fora do MVP) | Média | Médio | Médio | Bianca | Evitar | Em monitoramento | 19/10/2026 |

### Detalhamento

**R01 — Latência elevada ou rate limit da API**
- **Gatilho:** resposta acima de 10 s (RNF01) nos testes ou erro HTTP 429.
- **Mitigação:** tratamento controlado de rate limit e erros (RNF04, RNF05, RNF06); `max_tokens` fixo por chamada para limitar tamanho e tempo de resposta.
- **Contingência:** informar ao usuário que o serviço está temporariamente limitado e permitir nova tentativa sem reiniciar a aplicação; manter registro (log/print) de um diálogo bem-sucedido como evidência para demonstrações.

**R02 — Estouro de cota/limite de tokens**
- **Gatilho:** consumo acumulado acima de 70% do crédito disponível no painel da OpenAI (limiar proposto) ou erro de cota.
- **Mitigação:** consulta semanal ao painel de consumo; `max_tokens` fixo; modelo de menor custo como padrão.
- **Contingência:** pausar testes extensivos e priorizar apenas os casos obrigatórios do Módulo; acionar a chave de backup (R03).

**R03 — Perda de acesso à chave de API**
- **Gatilho:** erro de autenticação (401) ou aviso de suspensão da conta.
- **Mitigação:** segunda chave vinculada a outro integrante; chaves apenas em variável de ambiente ou CI/CD Variables mascaradas, nunca no repositório (RNF02, RNF03, RNF07).
- **Contingência:** ativar a chave de backup; se houver vazamento, **revogar a chave imediatamente** antes de qualquer limpeza do histórico do Git.

**R04 — Possível desligamento do `gpt-3.5-turbo` (data indicada: 23/10/2026; confirmar em fonte oficial)**
- **Gatilho:** erro de "modelo não encontrado" na chamada ou aproximação da data indicada de 23/10/2026, após confirmação em fonte oficial.
- **Mitigação:** o plano está documentado em `docs/MIGRACAO_MODELO.md`. `gpt-4o-mini` é o modelo proposto, com aprovação da equipe pendente; validar disponibilidade, custo, latência, endpoint e comportamento socrático antes da adoção. O mapeamento atual registra `gpt-4.1-mini` no motor e nos testes de diálogo/prompt, e `gpt-4o-mini` no teste isolado da API.
- **Contingência:** retornar à última configuração funcional que use um modelo ainda disponível; não depender de `gpt-3.5-turbo`. Se necessário, selecionar outro modelo compatível e repetir a bateria de testes.

**R05 — Alucinação e resposta sem reconhecer incerteza**
- **Gatilho:** resposta com informação algorítmica incorreta em qualquer caso registrado em `CASOS_DE_TESTE_PROMPT.md`, ou relatada por um usuário.
- **Mitigação:** testes com problemas reais (básico, intermediário e grafos); revisão humana das respostas dos casos de teste; instrução no prompt para reconhecer limites e incertezas; aviso de limitação exibido ao usuário (seção 4).
- **Contingência:** registrar o caso (versão do prompt, entrada, resposta, ajuste), corrigir o prompt via Merge Request e reexecutar o teste correspondente.

**R06 — Vazamento da solução completa sob pressão**
- **Gatilho:** qualquer resposta com código completo ou solução integral nos testes adversariais.
- **Mitigação:** política de ajuda graduada no System Prompt; bateria adversarial (Issue #18) a cada alteração do prompt; revisão do prompt pelo Tech Lead antes do merge; validação determinística de saída (Issue #16).
- **Contingência:** reverter para a versão anterior do prompt (versionado no repositório), registrar o caso e abrir issue de correção.

**R07 — Sobrecarga ou indisponibilidade de membros**
- **Gatilho:** issue em "Doing" sem commit ou MR por 3 dias (limiar proposto), ou membro sinalizando indisponibilidade por carga de disciplinas.
- **Mitigação:** Code Review cruzado em todo MR; redistribuição de issues; documentação viva na Wiki; uso do Escopo como variável de ajuste (mover issues entre Milestones).
- **Contingência:** reatribuir a issue a outro integrante e cortar escopo secundário, com registro no `CHANGELOG.md`.

**R08 — Atraso no caminho crítico do Milestone 2**
- **Caminho crítico:** System Prompt (#14) → motor de diálogo → testes em problemas reais → README e fechamento do M1.
- **Gatilho:** motor de diálogo sem Merge Request aberto até 16/10/2026 (limiar proposto).
- **Mitigação:** acompanhamento diário das issues do caminho crítico; mover para o Milestone 3 o que a rubrica do M2 não exige.
- **Contingência:** entregar versão mínima do protótipo (terminal), com evidência de contexto multi-turn e limitações documentadas.

**R09 — Scope Creep e Gold Plating**
- **Gatilho:** pedido de funcionalidade fora do Escopo do Charter sem Issue ou registro de mudança.
- **Mitigação:** Charter (seção Fora do Escopo) como referência; toda mudança registrada com motivo, impacto e responsável.
- **Contingência:** mover o pedido para o Backlog futuro ou renegociar prazo e escopo formalmente.

### Oportunidade (risco positivo)

| ID | Oportunidade | P | I | Resposta | Dono |
|---|---|---|---|---|---|
| O01 | Surgimento de modelo mais barato ou mais capaz durante o semestre | Média | Médio | **Explorar:** o plano de migração (Issue #17) permite adotá-lo sem retrabalho grande | João |

### Riscos que se confirmaram na Sprint 2

> [PREENCHER ao fechar a sprint: quais riscos viraram problema, quando, e qual resposta foi aplicada.]

## 4. Limites comunicados ao usuário e protocolo de resposta inadequada

**Aviso exibido na interface (texto proposto):**

> O Maieut-IA é um tutor de apoio e pode errar. Confira as orientações com o enunciado do problema. Ele guia seu raciocínio com perguntas e pistas, mas não entrega código pronto para submissão. As respostas podem levar alguns segundos e variar entre tentativas.

**Protocolo quando houver alucinação ou ajuda inadequada:**
1. Registrar o caso em `docs/CASOS_DE_TESTE_PROMPT.md` (versão do prompt, modelo, data, entrada, resposta, comportamento esperado).
2. Abrir issue de correção com a label `Risco`, vinculada ao risco correspondente (R05 ou R06).
3. Ajustar o System Prompt em uma branch e abrir Merge Request com revisão cruzada.
4. Reexecutar o teste que falhou e a bateria adversarial completa antes do merge.
5. Registrar a mudança no `CHANGELOG.md`.

## 5. Matriz RACI

**Regra:** um único **A** (Accountable) por atividade. O **A** aprova o merge e é sempre diferente do autor: nos MRs de João e Bianca, Arthur; nos MRs de Arthur, Bianca.

| Atividade | João (Dev) | Bianca (PO) | Arthur (SM) | Professor |
|---|---|---|---|---|
| Implementar System Prompt e motor de diálogo (código) | R | C | **A** | I |
| Escrever `docs/SYSTEM_PROMPT.md` | C | R | **A** | I |
| Executar e registrar testes de prompt | C | R | **A** | I |
| Atualizar `REQUISITOS.md` | C | R | **A** | I |
| Plano de migração de modelo e gestão de chaves | R | C | **A** | I |
| Escrever `RISCOS_E_COMUNICACAO.md` | C | **A** | R | I |
| Escrever `CHANGELOG.md` e ADRs | C | **A** | R | I |
| Decisão de escopo (aceitar, adiar ou cortar item) | C | **A** | R | I |

*R = Responsável, A = Aprovador, C = Consultado, I = Informado. O professor é informado pela rastreabilidade pública do repositório.*

## 6. Mapa de stakeholders

> A classificação é uma hipótese de engajamento, revisada quando requisitos, riscos ou recursos mudarem. Professor, cliente e patrocinador são funções distintas e não são presumidas como coincidentes.

| Stakeholder | Papel no projeto | Poder | Interesse | Quadrante | Premissa da classificação | Informação necessária | Canal | Cadência / revisão |
|---|---|---|---|---|---|---|---|---|
| **Prof. Aléssio Miranda Júnior** | Avaliador de conformidade acadêmica (não é cliente nem patrocinador) | Alto | Alto | Gerenciar de perto | Define a nota e publica as regras de avaliação | Evidências por Módulo: documentos, issues, MRs, testes | GitLab (Issues, MRs, Wiki) | Por Milestone; revisar se as regras mudarem |
| **Estudantes de maratona (usuários)** | Usuário final; necessidades representadas pela PO | Baixo | Alto | Manter informados | Não decidem escopo, mas definem o valor do produto | Versão testável, limites do assistente | Feedback coletado pela equipe | Por Milestone, quando houver versão testável; sobe para "Gerenciar de perto" se houver testes com alunos reais |
| **OpenAI (provedor da API)** | Fornecedor externo | Alto | Baixo | Manter satisfeitos | Pode alterar preços, limites e modelos sem aviso direto à equipe (ver R04) | Avisos de depreciação, limites, preços | Página oficial de deprecations/changelog | Verificação a cada fechamento de Milestone |

## 7. Plano de comunicação (proposta a validar com a equipe)

| Informação | Para quem | Canal | Cadência | Registro |
|---|---|---|---|---|
| Decisões de escopo, requisitos e riscos | Equipe | Issue, MR ou ADR no GitLab | Sempre que ocorrerem | Obrigatório |
| Alertas rápidos (bloqueios, indisponibilidade) | Equipe | Chat | Imediato | Resumo na Issue em até 24 h |
| Alinhamento de Sprint | Equipe | Reunião curta | Semanal | Ata na seção 8 |
| Progresso do Milestone | Professor | Board, Issues e Wiki | Contínuo | Repositório |

**Regras:** o GitLab é a fonte do registro; o chat é só para alertas e nunca recebe credenciais ou dados pessoais; ADRs ficam em `docs/adr/` (a ser criada junto com o `CHANGELOG.md`).

## 8. Atas e alinhamentos da Sprint 2

### Pontos em aberto para decidir e registrar na próxima ata

- Mover as Issues #15, #16 e #19 para o Milestone 3 (a rubrica do M2 não exige essas entregas).
- Alinhar a estrutura de pastas com a árvore do enunciado (`src/prompts/`, `src/core/`, `src/tests/`) ou documentar o mapeamento no README.
- Definir a política sobre pseudocódigo e trechos de código nas respostas do assistente.

### Registro de atas

| Nº | Data | Participantes | Tema | Decisões | Ações (responsável / prazo) | Vínculo (Issue ou MR) |
|---|---|---|---|---|---|---|
| 01 |  |  |  |  |  |  |

## 9. Histórico de revisões

| Data | Mudança | Responsável |
|---|---|---|
| 14/10/2026 | Criação do documento a partir dos riscos do Charter e dos novos riscos do Milestone 2 | Arthur |