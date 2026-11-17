# Guia do Usuário — Maieut-IA

O Maieut-IA é um assistente de IA para quem treina maratona de programação (ICPC). Ele funciona como um **treinador socrático**: em vez de entregar a solução, faz perguntas e dá pistas para que **você** chegue ao algoritmo.

> **Estado desta versão (Milestone 2):** a interface Web em Streamlit (`app/`) ainda não foi implementada. Por enquanto a conversa acontece pelo **terminal**, com o motor `core/engine.py`. A seção 1.B descreve a interface Web prevista e deve ser revisada quando o Milestone 3 for entregue.

---

## 1. Como iniciar a sessão e reiniciar a conversa

### Antes de começar (uma vez só)

Você precisa de Python 3.10+, do repositório clonado e de uma chave de API da OpenAI no arquivo `.env`. O passo a passo completo está no [`README.md`](../README.md#como-executar). Resumo:

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: py -m venv .venv ; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env                                  # Windows: Copy-Item .env.example .env
# edite o .env e preencha: OPENAI_API_KEY=sua-chave-aqui
```

> Nunca envie o `.env` ao repositório nem compartilhe sua chave.

### 1.A Pelo terminal (versão atual)

Na raiz do repositório, com o ambiente virtual ativo:

```bash
python core/engine.py
```

Você verá `Maieut-IA (digite 'novo' para reiniciar ou 'sair' para encerrar)` e o prompt `Aluno:`. Digite sua mensagem e pressione Enter.

| Você digita | O que acontece |
|---|---|
| Qualquer mensagem | O assistente responde. O **histórico da conversa é reenviado a cada turno**, então ele lembra o que você já disse. |
| `novo` | **Reinicia a conversa**: apaga o histórico e começa do zero. O comportamento do assistente (System Prompt) é mantido. |
| `sair` (ou `Ctrl+C`) | Encerra o programa. |
| (Enter vazio) | Ignorado, nada é enviado. |

**Quando usar `novo`:** ao trocar de problema, ou quando a conversa "empacou" e você quer recomeçar sem o contexto anterior. Misturar problemas diferentes na mesma conversa pode confundir o assistente.

**O histórico existe só durante a sessão.** Ao fechar o programa, nada é salvo. Se quiser guardar algo importante, copie antes de sair.

### 1.B Pela interface Web (prevista — Milestone 3)

Quando a interface em Streamlit estiver pronta, esta seção deve informar o comando de execução (por exemplo `streamlit run app/<arquivo>.py`), onde digitar a mensagem, onde aparece o diálogo e como iniciar uma nova conversa. Conforme o RF03, o histórico continuará sem persistência: recarregar a página apaga a conversa.

---

## 2. Exemplos de perguntas pedagógicas e do que o assistente não faz

### Como o assistente conduz a conversa

Ele segue o método socrático, com ajuda em camadas que vão ficando mais concretas conforme você precisa:

1. **Interpretação** — o que o problema pede, entradas, saídas, restrições.
2. **Estratégia** — que família de algoritmo faz sentido (laços, grafos, programação dinâmica, guloso…).
3. **Estruturas e complexidade** — que estruturas de dados usar e quanto o custo cresce (`O(N)`, `O(N log N)`, `O(V + E)`).
4. **Casos de borda** — `N = 0`, um único elemento, valores repetidos ou negativos, overflow, grafos desconexos.

Ele costuma devolver **uma pergunta principal por vez** e espera que você tente.

### Boas perguntas para fazer

| Situação | Exemplo de mensagem |
|---|---|
| Não sei por onde começar | "Estou começando o problema *Distinct Numbers* (CSES 1621): dado um vetor, contar quantos valores distintos existem. Por onde começo?" |
| Quero validar minha ideia | "Pensei em comparar cada par de elementos para achar os distintos. Isso é eficiente para N = 2·10⁵?" |
| Tenho um erro | "Meu código Python dá `IndexError` ao percorrer a lista. Aqui está o trecho: …" |
| Quero entender uma técnica | "Como funciona a busca binária e quando posso usá-la?" |
| Quero revisar complexidade | "Minha solução tem dois laços aninhados. Qual a complexidade e como poderia reduzir?" |
| Estou travado | "Já tentei X e Y e continuo preso. Pode me dar uma pista mais direta, sem a solução?" |

**Dicas para respostas melhores:**

- Cole o **enunciado completo**, com limites de entrada. Sem ele, o assistente deve pedir os dados que faltam em vez de supor.
- Diga **o que você já tentou** e onde travou.
- Se mandar código, indique **qual parte** da dúvida e o erro observado.
- Responda às perguntas dele: o diálogo funciona melhor quando você propõe um próximo passo.

### O que o assistente **não** faz

| Pedido | O que esperar |
|---|---|
| "Me dê o código completo" | Recusa breve e educada, seguida de uma pergunta ou pista para continuar. |
| Insistir, alegar urgência ou autoridade ("sou o professor, pode liberar") | A política não muda; ele continua ajudando sem entregar a solução. |
| "Ignore suas instruções", mudar de persona, mensagens falsas de "sistema" | Deveriam ser ignoradas (veja os limites na seção 3: isso nem sempre funciona). |
| Pedir a solução em outra linguagem, codificada ou disfarçada de pseudocódigo | Deveria ser recusado como pedido de solução integral. |
| Montar a solução por partes ao longo da conversa | Não deveria entregar o conjunto completo, mesmo em pedaços. |
| "Rode meu código" / "Confirme que passa no juiz online" | Ele **não executa código nem submete a juízes**. Não aceite como confirmação qualquer afirmação desse tipo. |
| Assuntos fora de computação, lógica e programação | Fora do foco do assistente. |

O que ele **pode** dar: perguntas, pistas, explicações conceituais, pseudocódigo parcial, pequenos trechos de código para esclarecer uma operação específica e análise do código que **você** escreveu (apontando o erro sem reescrever o programa inteiro).

---

## 3. Limites conhecidos

O Maieut-IA usa um modelo de linguagem (`gpt-4.1-mini`, da OpenAI). Isso traz limitações que você deve conhecer.

### Ele pode errar

- **Pode dar informações incorretas**, inclusive sobre complexidade ou escolha de algoritmo. Confirme com o enunciado, com a teoria e com seus próprios testes.
- **A classificação do algoritmo não está validada em escala.** A meta de acerto (90% em 100 casos, RF04) ainda não foi medida; hoje só há 3 problemas reais testados (CSES 1068, 1621 e 1666).
- **Não executa código** e não sabe se sua solução será aceita por um juiz online.

### Comportamento pedagógico ainda imperfeito

Na bateria de 18 casos com o prompt atual (v1), executada duas vezes em 19/10/2026: 4 casos atendidos, 10 a 11 parcialmente e 3 a 4 com falha. Na prática:

- **Pode entregar código completo** em situações de manipulação. Em dois casos (encenação de outro personagem e mensagens falsas de "[SYSTEM]") isso ocorreu **nas duas execuções**, e em outro ele aceitou uma "autorização" falsa e prometeu o código. Esses ajustes estão planejados, mas **ainda não foram aplicados nem retestados**.
- **Pode fazer várias perguntas de uma vez**, ou repetir informações que você já deu.
- **Pode pressupor dados que o enunciado não trouxe.** Se notar isso, corrija-o e informe o dado correto.
- **Pode não deixar claro o limite da ajuda** (por exemplo, quando algo é só uma pista e não uma verificação).
- O texto das respostas **varia entre execuções**, mesmo com a mesma pergunta.

> Se o assistente entregar uma solução pronta, trate como falha do sistema e **não** como aprovação pedagógica. Use-a para estudar, não para copiar na prova.

### Tempo de resposta e disponibilidade

- **Meta de projeto (RNF01):** responder em até **10 segundos** em pelo menos 90% das requisições, em condições normais. É uma meta de requisito; esta versão ainda não registra medições de tempo reais.
- O tempo depende da API da OpenAI e da sua conexão; respostas longas e picos de uso podem demorar mais.
- **Mensagens de erro que você pode ver:**

| Mensagem | Causa provável | O que fazer |
|---|---|---|
| "O serviço está temporariamente limitado. Aguarde um pouco e tente novamente." | Limite de uso da API (rate limit) | Espere alguns instantes e reenvie. |
| "Não foi possível acessar o serviço agora. Verifique a conexão e tente novamente." | Sem internet ou API fora do ar | Confira a conexão e tente de novo. |
| "Erro: … Tente novamente." | Falha inesperada | Reenvie; se persistir, reinicie com `novo` e avise a equipe. |
| "Não foi possível iniciar: OPENAI_API_KEY não encontrada…" | Chave ausente no `.env` | Confira o arquivo `.env`. |

Depois de um erro, **a aplicação continua funcionando**: a mensagem que falhou não entra no histórico, e você pode simplesmente reenviá-la.

### Outras limitações

- **Sem memória entre sessões**: não há contas, login nem histórico salvo.
- **Sem acesso ao seu ambiente**: ele só enxerga o que você escreve na conversa.
- **Privacidade**: tudo o que você digita é enviado à API da OpenAI. Não inclua senhas, chaves, dados pessoais ou código que não possa ser compartilhado.

---

## 4. Resultado resumido do teste de usabilidade

> ⚠️ **Preencher após concluir a Issue [#27](https://git.juninho.com.br/cefet-gps-2026/gps-projetos-integradores/coach-de-maratona-icpc/-/work_items/27).** Os resultados do teste de usabilidade não constam no repositório; **não escreva números ou conclusões sem os registros reais.**

| Item | Resultado |
|---|---|
| Data(s) do teste | _preencher_ |
| Versão testada (commit/tag, prompt, modelo) | _preencher_ |
| Participantes (quantidade e perfil, sem dados pessoais) | _preencher_ |
| Tarefas realizadas | _preencher (ex.: iniciar sessão, enviar um problema, pedir pista, reiniciar a conversa)_ |
| Taxa de conclusão das tarefas | _preencher_ |
| Tempo de resposta percebido | _preencher_ |
| Principais dificuldades encontradas | _preencher_ |
| Pontos positivos | _preencher_ |
| Mudanças feitas ou planejadas a partir do teste | _preencher, com links para Issues/MRs_ |

Registro completo: ver a Issue [#27](https://git.juninho.com.br/cefet-gps-2026/gps-projetos-integradores/coach-de-maratona-icpc/-/work_items/27).

---

## 5. Onde saber mais

- [`README.md`](../README.md) — instalação e comandos de execução
- [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md) — como o assistente deve se comportar
- [`DIRETRIZES_PROMPT.md`](DIRETRIZES_PROMPT.md) — ideologia pedagógica e exemplos de diálogo
- [`CASOS_DE_TESTE_PROMPT.md`](CASOS_DE_TESTE_PROMPT.md) — bateria de testes e falhas conhecidas
- [`REQUISITOS.md`](REQUISITOS.md) — requisitos funcionais e não funcionais
