# Project Charter — Maieut-IA

## 1. Nome do Projeto
**Maieut-IA — Assistente Socrático de Maratona de Programação**

*(Nome inspirado na maiêutica socrática: o assistente não entrega respostas prontas, ajuda o aluno a "dar à luz" a solução que ele já tem em potencial, por meio de perguntas e dicas guiadas.)*

## 2. Justificativa (Business Case)
Alunos que treinam para maratonas de programação — usando juízes online como Beecrowd, LeetCode e Codeforces, visando competições como o ICPC — frequentemente travam em problemas de lógica e algoritmos e recorrem a soluções prontas na internet (fóruns como Stack Overflow, repositórios de soluções no GitHub, ou até assistentes de IA generalistas como o ChatGPT), sem desenvolver o raciocínio necessário para competições reais. O Maieut-IA existe para resolver essa dor: um assistente de IA que atua como tutor socrático, guiando o aluno até a solução por meio de perguntas e dicas — apontando a classe do algoritmo e falhas de complexidade — sem nunca entregar o código pronto.

## 3. Objetivos SMART
Desenvolver e integrar, via API da OpenAI, um Assistente Socrático:

1. **Específico (S):** acessível por interface Web mínima em Streamlit, capaz de identificar a classe do algoritmo (ex: Programação Dinâmica, Grafos) e apontar falhas de complexidade (ex: O(N²) em vez de O(N log N)) em problemas de programação competitiva.
2. **Mensurável (M):** validado em pelo menos 90% dos casos testados pela equipe, em um conjunto de 100 testes de dificuldade variada — quantidade e proporção definidas pelo Scrum Master —, coletados manualmente pelo PO em ao menos duas plataformas de juízes online, comprovando que o assistente identifica corretamente a classe do algoritmo e a complexidade.
3. **Atingível (A):** viável dentro do escopo restrito ao MVP (interface simples, API já madura, sem necessidade de treinar modelo do zero) e dos recursos disponíveis à equipe.
4. **Relevante (R):** reduz a dependência do aluno por soluções prontas em juízes online, reforçando o desenvolvimento do raciocínio algorítmico — a dor de negócio descrita na Justificativa.
5. **Temporal (T):** MVP funcional entregue até o fim do Milestone 4 do calendário letivo.

## 4. Escopo (In / Out)

**Dentro do MVP (In):**
- Interface Web mínima em Streamlit
- Integração com a API da OpenAI
- Recebimento do código/descrição do problema em qualquer linguagem pelo aluno
- Identificação da classe do algoritmo e da complexidade
- Dicas socráticas
- System Prompt versionado e documentado na Wiki

**Fora do MVP (Out — vai para o Backlog futuro):**
- Histórico de conversas por usuário / autenticação
- Suporte simultâneo a múltiplos juízes online (parsing/integração automática com Beecrowd, Codeforces, etc.)
- Interface de voz, gráficos 3D ou qualquer "enfeite" (Gold Plating)
- Análise de performance em tempo real

## 5. Premissas
- A API da OpenAI terá tier gratuito ou créditos suficientes disponíveis durante o semestre.
- Python + Streamlit são suficientes para atender aos requisitos de performance esperados.
- O professor disponibiliza o Template Repository a tempo do Sprint 1.

## 6. Restrições
- Equipe de 3 pessoas.
- Prazo: 29/08/2026 – 30/11/2026 (93 dias), divididos em 4 Milestones.
- Custo: R$ 0,00 a princípio, via acesso do João ao modelo GPT-3.5. O `gpt-3.5-turbo` tem desligamento programado pela OpenAI para 23/10/2026 — dentro da janela do projeto —, mas a equipe optou por aceitar esse risco (ver Risco 5) em vez de migrar preventivamente, dado o custo zero.

## 7. Riscos Iniciais

1. **Alucinação do LLM**: a IA pode entregar a solução completa apesar do prompt proibir isso.
   *Mitigação:* criar uma bateria de testes automatizados do System Prompt (ex: 10-15 prompts adversariais que tentam "forçar" a resposta pronta), rodada a cada alteração do prompt, verificando se a resposta contém código completo. Revisão do prompt pelo Tech Lead antes de qualquer merge que o altere.

2. **Estouro de cota/limite de tokens** da API da OpenAI.
   *Mitigação:* monitorar consumo semanalmente no painel da OpenAI, definir um `max_tokens` de saída fixo nas chamadas da API, e usar o modelo GPT-3.5 (mais barato) como padrão, reservando modelos mais caros só para testes pontuais.

3. **Engenharia de prompt consumir muito mais tempo** do que estimado.
   *Mitigação:* reservar buffer de tempo explícito no Milestone 2 (dedicado à engenharia de prompt), e versionar cada iteração do prompt na Wiki com data e resultado do teste — evitando retrabalho por perda de histórico.

4. **Dependência de acesso individual à API**, sem redundância na equipe.
   *Mitigação:* criar, até o fim do Sprint 1, uma segunda chave de API vinculada a outro integrante da equipe (backup), armazenada como variável de ambiente (nunca commitada no repositório) e documentada na Wiki para acesso de toda a equipe em caso de indisponibilidade da conta do João.

5. **Obsolescência programada do modelo**: o `gpt-3.5-turbo` será desligado pela OpenAI em 23/10/2026, antes do fim do projeto (30/11/2026).
   *Resposta ao risco: Aceitação.* A equipe optou por manter o GPT-3.5 como padrão pelo custo zero, assumindo o risco da migração forçada. *Mitigação:* quando o desligamento ocorrer, migrar para a linha mais barata disponível na época (ex: `gpt-4o-mini` ou equivalente futuro) e ajustar as dependências de código afetadas pela troca de modelo.

## 8. Equipe e Papéis
| Papel | Responsável |
|---|---|
| Scrum Master | Arthur Baltar Eler |
| Product Owner | Bianca Barros |
| Tech Lead / Dev | João Carlos |

---

# Avaliação de Viabilidade — TELOS (Maieut-IA)

| Dimensão | Avaliação |
|---|---|
| **Técnica** | Viável. Streamlit e a API da OpenAI são tecnologias maduras e bem documentadas; a equipe não precisa treinar modelo do zero, apenas orquestrar chamadas de API. O João declarou experiência técnica real com essas duas ferramentas. Arthur e Bianca conhecem o conceito e o negócio do projeto, pela experiência vivenciada na startup "Mundo do Código". |
| **Econômica** | Condicional. Depende do tier gratuito/créditos da OpenAI cobrirem o volume de testes do semestre — e, hoje, esse acesso está vinculado à conta pessoal do João, o que amplia o risco (ver Risco 4). |
| **Legal** | Baixo risco, já que o Escopo (seção 4) exclui armazenamento de dados de usuário. Ainda assim, exige atenção aos Termos de Uso da API da OpenAI quanto ao processamento (não ao armazenamento) dos dados enviados nas requisições — os problemas e códigos dos alunos trafegam pela API mesmo sem serem persistidos pelo Maieut-IA. |
| **Operacional** | A adoção depende da simplicidade da interface — um Streamlit mínimo, direto ao ponto, favorece a aceitação do aluno em vez de resistência. |
| **Cronograma** | Viável dentro do escopo restrito ao MVP definido acima; se o escopo crescer (Gold Plating), o cronograma de 4 Milestones fica em risco. |

**Conclusão TELOS:** Go, desde que o escopo se mantenha estritamente dentro do MVP definido na seção 4 e a equipe monitore o consumo de tokens da API como risco econômico ativo.