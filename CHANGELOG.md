# CHANGELOG — Maieut-IA

Registro das mudanças de escopo, requisitos, decisões técnicas e planejamento do projeto, com motivo, impacto, responsável e vínculo rastreável.

**Como ler:** o registro é organizado por Milestone. A data exata de cada mudança está no histórico da Issue, do MR ou do commit indicado na coluna *Vínculo*. Itens marcados com † tiveram o motivo redigido pela Scrum Master a partir do contexto do projeto e devem ser confirmados pelo responsável.

**Como atualizar:** toda mudança de escopo, requisito, modelo, arquitetura ou prazo entra aqui no mesmo MR que a realiza, com um vínculo (`#N` ou `!N`).

---

## Módulo 2 — Gestão, Requisitos e Prompt Base (prazo: 19/10/2026)

| ID | Mudança | Motivo | Impacto | Responsável | Vínculo |
|---|---|---|---|---|---|
| CH-011 | Backlog do Milestone 2 criado e distribuído: #14 a #17 (João), #18 e #19 (Bianca), #20 (Arthur) | Cobrir os entregáveis do Módulo 2 e manter todos os membros com tarefas atribuídas | Define a carga de cada integrante até 19/10 | Arthur | #14, #15, #16, #17, #18, #19, #20 |
| CH-012 | `docs/RISCOS_E_COMUNICACAO.md` criado: registro ampliado de 5 para 9 riscos (mais 1 oportunidade), RACI, mapa de stakeholders e plano de comunicação | Atender ao entregável de riscos e comunicação do Módulo 2 e dar dono, gatilho e contingência a cada risco | Riscos passam a ter revisão por Milestone; surgem dois riscos críticos (sobrecarga de membros e atraso no caminho crítico) | Arthur | #41 |
| CH-013 | ADR-001 registrada: interface Web em Streamlit | Formalizar uma decisão tomada no Módulo 1 que ainda não estava documentada † | Preserva o "porquê" da escolha e as alternativas descartadas | Arthur | `docs/adr/ADR-001-interface-streamlit.md` |
| CH-014 | Este CHANGELOG criado | Exigência do controle de mudanças do Módulo 2 | Mudanças futuras passam a ter registro obrigatório | Arthur | CHANGELOG.md |

### Mudanças propostas, aguardando decisão da equipe

| Proposta | Motivo | Impacto previsto | Decisor |
|---|---|---|---|
| Mover #15 (parsing), #16 (validação anti-vazamento) e #19 (100 casos de teste) para o Milestone 3 | A rubrica do M2 não exige essas entregas; reduzir a carga do caminho crítico (ver R07 e R08 em `RISCOS_E_COMUNICACAO.md`) | Reduz a carga do M2 e aumenta a do M3; a #19 alimenta a métrica final do M4 | Bianca (PO), com consulta a João |
| Alinhar a estrutura de pastas ao enunciado (`src/prompts/`, `src/core/`, `src/tests/`) ou documentar o mapeamento no README | A árvore do enunciado do M2 usa `src/` e a estrutura planejada usava pastas na raiz | Evita divergência de caminhos na avaliação | João (Tech Lead) |
| Definir política sobre pseudocódigo e trechos de código nas respostas | O M2 exige essa política explícita no `SYSTEM_PROMPT.md`; o M1 dizia apenas "nunca código completo" | Altera o texto do System Prompt | Bianca (PO) |

---

## Módulo 1 — Iniciação e Planejamento (prazo: 14/09/2026)

| ID | Mudança | Motivo | Impacto | Responsável | Vínculo |
|---|---|---|---|---|---|
| CH-001 | Repositório criado no GitLab em 23/08/2026 | Início do projeto integrador | Base para toda a rastreabilidade | Arthur | Repositório |
| CH-002 | Interface definida como Web mínima em Streamlit (em vez de bot Telegram/Discord) | Menor complexidade de infraestrutura para uma equipe de 3 pessoas † | EAP 1.1 passa a tratar de Streamlit; sem webhooks nem tokens de mensageria | Equipe | ADR-001, `docs/EAP.md` |
| CH-003 | Provedor de LLM definido como OpenAI, com custo inicial de R$ 0,00 via acesso do João | Custo zero para o semestre | Cria dependência de um acesso individual (riscos R03 e R04) | Equipe | Charter, #9 |
| CH-004 | Project Charter, TELOS e README publicados | Entregáveis de Iniciação do Módulo 1 | Escopo, restrições e riscos passam a ter referência formal | Arthur | #8, #9, #10 |
| CH-005 | Escopo "Fora do MVP" definido: histórico/autenticação, suporte a múltiplos juízes online, interface de voz e gráficos 3D, análise de performance em tempo real | Prevenir Scope Creep e Gold Plating | Pedidos nessas áreas exigem renegociação formal | Equipe | Charter, #9 |
| CH-006 | Entrada do assistente ampliada de "código em C++" para "qualquer linguagem"; removido o corte "outras linguagens além de C++" | Decisão da equipe na revisão do Charter † | Prompt e testes devem cobrir linguagens diversas | Equipe | Charter, #9 |
| CH-007 | Objetivo Mensurável reescrito: de "90% dos casos testados" para "90% de 100 casos, coletados pelo PO em ao menos duas plataformas de juízes online" | O critério original não dizia quantos casos nem a origem deles; precisava ser testável | Cria a tarefa de coletar os casos e fixa a métrica final | Arthur, Bianca | Charter, #9 |
| CH-008 | Restrição de custo reescrita e Risco 5 criado: o `gpt-3.5-turbo` será desligado pela OpenAI em 23/10/2026, dentro da janela do projeto | Data confirmada na página oficial de depreciações da OpenAI | Decisão de **aceitar o risco** conscientemente e migrar quando necessário; plano de migração planejado | Equipe | Charter, #17 |
| CH-009 | Risco 4 criado (dependência de acesso individual à API) e mitigação adicionada a cada risco do Charter | Riscos sem resposta definida não orientam ação | Chave de backup de outro integrante passa a ser necessária | Arthur | Charter, #9 |
| CH-010 | EAP publicada com 18 pacotes-folha, Dicionário da EAP e classificação Produto/Projeto; documentação dividida em cinco sub-pacotes | Atender à Regra dos 100% e tornar cada pacote estimável | Base para criar as Issues e as estimativas | Arthur | #11, `docs/EAP.md` |
| CH-015 | Requisitos definidos: RF01 a RF05 e RNF01 a RNF07, com critério de aceitação em cada um | Entregável de requisitos do Módulo 1 | RNF01 fixa tempo de resposta em 10 s; RNF02 proíbe chaves no código-fonte | Bianca (RFs), João (RNFs) | #1, #5 |
| CH-016 | Diagramas UML criados como issues opcionais, com arquitetura em `docs/ARQUITETURA.md`, separada dos requisitos | Separar "o que o sistema faz" de "como é estruturado" † | Acrescenta trabalho opcional, fora da rubrica obrigatória | Arthur | #2, #3, #4 |
| CH-017 | Spike técnico de conexão com a API aberto em MR; a revisão questionou o uso da Responses API com o `gpt-3.5-turbo` | Não aprovar sem evidência de execução real | Pode exigir troca para a API de Chat Completions. Resultado da verificação: PASSED | João (autor), Arthur (revisor) | #7, !1 |
| CH-018 | Atas de Sprint removidas do RISCOS_E_COMUNICACAO.md; alinhamento passa a ser assíncrono | A equipe não faz reuniões formais | Decisões ficam registradas nas Issues e no CHANGELOG | Arthur | #41 |