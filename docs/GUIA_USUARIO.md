# Guia do Usuário — Maieut-IA

O Maieut-IA é um assistente de IA para quem treina maratona de programação (ICPC). Ele funciona como um **treinador socrático**: em vez de entregar a solução, faz perguntas e dá pistas para que **você** chegue ao algoritmo.

> **Estado desta versão:** a interface Web em Streamlit (`app/`) está disponível para execução local. Também é possível usar o motor pelo terminal (`core/engine.py`). Veja as instruções nas seções 1.A e 1.B.

---

## 1. Como iniciar a sessão e reiniciar a conversa

### Antes de começar (uma vez só)

Você precisa de Python 3.10+, do repositório clonado e de uma chave de API da OpenAI no arquivo `.env`. O passo a passo completo está no [`README.md`](../README.md#como-executar). Na raiz do repositório, siga as instruções do seu sistema operacional.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

**Linux/macOS (terminal):**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Depois, edite o `.env` e preencha `OPENAI_API_KEY=sua-chave-aqui`.

> Nunca envie o `.env` ao repositório nem compartilhe sua chave.

### 1.A Pelo terminal

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

### 1.B Pela interface Web (Streamlit)

Na raiz do repositório, com o ambiente configurado, execute no Windows:

```bash
py -m streamlit run app/main.py
```

O Streamlit abre a aplicação no navegador. Digite o enunciado, a dúvida ou o código no campo de entrada e envie; as mensagens do aluno e as respostas aparecem na área de diálogo. O histórico é mantido durante a conversa, mas **não é salvo entre sessões**: recarregar a página apaga as mensagens anteriores.

**Limitações da interface observadas no teste de 17/11/2026:** ainda não há botão de "Nova conversa"; o campo de entrada continua preenchido após o envio; o diálogo e o campo ficam em colunas separadas; e mensagens com código podem perder as quebras de linha na exibição. Evite clicar novamente enquanto aguarda uma resposta, pois isso pode duplicar o envio.

---

## 2. Exemplos de perguntas pedagógicas e do que o assistente não faz

### Como o assistente conduz a conversa

Ele segue o método socrático, com ajuda em camadas que vão ficando mais concretas conforme você precisa:

1. **Interpretação** — o que o problema pede, entradas, saídas, restrições.
2. **Estratégia** — que família de algoritmo faz sentido (laços, grafos, programação dinâmica, guloso…).
3. **Estruturas e complexidade** — que estruturas de dados usar e quanto o custo cresce (`O(N)`, `O(N log N)`, `O(V + E)`).
4. **Casos de borda** — `N = 0`, um único elemento, valores repetidos ou negativos, overflow, grafos desconexos.

O comportamento esperado é propor **uma pergunta principal por vez** e aguardar sua tentativa. Isso ainda não acontece de modo consistente: no teste de usabilidade de 17/11/2026, uma resposta trouxe cerca de sete perguntas (veja a seção 4).

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

Em uma bateria anterior de 18 casos, executada duas vezes em **19/10/2026**, houve 4 casos atendidos, 10 a 11 parcialmente atendidos e 3 a 4 com falha. Os itens abaixo descrevem limitações observadas nessa avaliação, não necessariamente reproduzidas no teste de usabilidade de novembro:

- **Pode entregar código completo** em situações de manipulação. Em outubro, dois casos (encenação de outro personagem e mensagens falsas de "[SYSTEM]") provocaram isso **nas duas execuções**, e em outro houve aceitação de uma "autorização" falsa e promessa de código. Em **17/11/2026**, o único pedido adversarial de código pronto foi recusado, mas isso não comprova que as falhas anteriores foram corrigidas.
- **Pode fazer várias perguntas de uma vez**, como ocorreu no teste de novembro com uma resposta de aproximadamente sete perguntas; a repetição de informações já dadas foi identificada nos testes anteriores, mas não nos quatro turnos do cenário 1 de novembro.
- **Pode pressupor dados que o enunciado não trouxe.** Se notar isso, corrija-o e informe o dado correto.
- **Pode não deixar claro o limite da ajuda** (por exemplo, quando algo é só uma pista e não uma verificação).
- O texto das respostas **varia entre execuções**, mesmo com a mesma pergunta.

> Se o assistente entregar uma solução pronta, trate como falha do sistema e **não** como aprovação pedagógica. Use-a para estudar, não para copiar na prova.

### Tempo de resposta e disponibilidade

- **Meta de projeto (RNF01):** responder em até **10 segundos** em pelo menos 90% das requisições, em condições normais. É uma meta de requisito; o teste de usabilidade de 17/11/2026 mediu seis respostas abaixo de 5 segundos, mas a amostra é insuficiente para comprovar a meta de 90% (veja a seção 4).
- O tempo depende da API da OpenAI e da sua conexão; respostas longas e picos de uso podem demorar mais.
- **Mensagens de erro que você pode ver:**

| Mensagem | Causa provável | O que fazer |
|---|---|---|
| "O serviço está temporariamente limitado. Aguarde um pouco e tente novamente." | Limite de uso da API (rate limit) | Espere alguns instantes e reenvie. |
| "Não foi possível acessar o serviço agora. Verifique a conexão e tente novamente." | Sem internet ou API fora do ar | Confira a conexão e tente de novo. |
| "Erro: … Tente novamente." | Falha inesperada | Reenvie; se persistir, avise a equipe. No terminal, `novo` reinicia a conversa; na Web, recarregar a página apaga o histórico, mas não é garantia de corrigir a falha. |
| "Não foi possível iniciar: OPENAI_API_KEY não encontrada…" | Chave ausente no `.env` | Confira o arquivo `.env`. |

Depois de um erro, **a aplicação continua funcionando**: a mensagem que falhou não entra no histórico, e você pode simplesmente reenviá-la.

### Outras limitações

- **Sem memória entre sessões**: não há contas, login nem histórico salvo.
- **Sem acesso ao seu ambiente**: ele só enxerga o que você escreve na conversa.
- **Privacidade**: tudo o que você digita é enviado à API da OpenAI. Não inclua senhas, chaves, dados pessoais ou código que não possa ser compartilhado.

---

## 4. Resultado resumido do teste de usabilidade (#27)

**Data:** 17/11/2026 | **Testadora:** Bianca da Silva Barros | **Ambiente:** Windows 11, Chrome, execução local (Streamlit), modelo gpt-4.1-mini

**Metodologia e escopo:** teste manual de usabilidade, realizado por uma testadora utilizando a aplicação como usuária final, em uma sessão. Foram percorridos o cenário 1 (REAL-01, Weird Algorithm, 4 turnos), o cenário 2 (ADV-01, pedido de código pronto) e o cenário 3 (5 casos de borda: campo vazio, código indentado, texto longo, pergunta fora do tema e recarregar a página).

### Resultado geral
O fluxo funciona de ponta a ponta: o histórico se mantém entre turnos, o assistente lembra do problema e não entregou código em nenhum caso testado. Os atritos estão na interface (falta de feedback, formatação do código, explicação do produto) e na primeira execução do projeto.

### Tempos de resposta (RNF01: ≤ 10 s)
| Caso | Tempo |
|---|---|
| Cenário 1, turnos 1 a 4 | 4 s, 4 s, 3 s, 2,56 s |
| Cenário 2 | 2,20 s |
| Cenário 3, texto longo | 4,46 s |
| Código indentado, fora do tema | não medidos |

Seis medições, todas abaixo de 5 s. Uma amostra pequena não comprova o critério de 90%. Em um teste anterior (descartado por erro de procedimento), houve uma resposta de 8 s, o que mostra variação entre chamadas.

### O que funcionou bem
- Histórico mantido em 4 turnos, sem repetir perguntas já respondidas (RF03).
- Pedido de código pronto recusado de forma pedagógica (ADV-01), sem vazamento de código.
- Respostas socráticas e tecnicamente corretas (O(n²) no código lento; alerta de estouro de `int` no 3n+1).
- Campo vazio tratado com aviso claro: "Digite um problema ou código antes de enviar."
- Interface limpa e com rótulos claros em português.

### Pontos de confusão/atrito

Os problemas abaixo foram observados no teste de **17/11/2026**. As falhas de manipulação do teste de **19/10/2026** são registros anteriores e estão descritas separadamente na seção 3.

| # | Onde | O que aconteceu | Severidade | Sugestão |
|---|---|---|---|---|
| 1 | Execução | `streamlit run app/main.py` falhou com `ModuleNotFoundError: No module named 'core'`. O comando que funcionou foi `py -m streamlit run app/main.py`. O README não traz esse comando e ainda diz que a interface não foi implementada | Alta | Documentar o comando que funciona e corrigir o caminho de importação; atualizar a seção "Estado atual" |
| 2 | Envio | Nenhum sinal percebido durante os ~8 s de espera. Cliquei duas vezes achando que não tinha enviado, e a mensagem foi enviada duas vezes (turno duplicado, resposta diferente, mais custo de API) | Alta | Indicador de carregamento (`st.spinner`) e botão desabilitado durante a chamada |
| 3 | Diálogo | Código colado perde quebras de linha e indentação no balão do aluno (vira um parágrafo único), embora o campo de entrada preserve | Média | Exibir a mensagem do aluno preservando as quebras (por exemplo, em bloco de código) |
| 4 | Campo de entrada | O texto enviado continua no campo depois do envio, o que facilita reenvio acidental e obriga a apagar à mão | Média | Limpar o campo após o envio (`clear_on_submit=True`) |
| 5 | Layout | Entrada e diálogo em colunas separadas; o diálogo cresce para baixo e a última resposta fica fora da vista, exigindo rolagem. "Resposta recebida!" fica longe da resposta e não distingue os turnos | Média | Layout de chat (campo abaixo do diálogo) ou diálogo com altura fixa e rolagem interna; remover a mensagem redundante |
| 6 | Primeira tela | Nada explica que o assistente nunca entrega código pronto. Ao pedir o programa completo, a recusa é implícita (só pergunta "Você já tentou alguma coisa?") | Média | Aviso curto na tela inicial e uma frase de explicação na primeira resposta |
| 7 | Pergunta fora do tema | "Qual é a capital da França?" gerou resposta confusa: devolveu a pergunta e ofereceu ensinar a achar a resposta com API ou banco de dados | Baixa | Ajustar o prompt para recusar com clareza e redirecionar para exercícios de programação |
| 8 | Respostas longas | Texto longo gerou resposta com cerca de sete perguntas em quatro parágrafos, difícil de responder de uma vez | Baixa | Limitar a 1 ou 2 perguntas por resposta no prompt |
| 9 | Nova conversa | Não há botão para reiniciar. Recarregar a página apaga o histórico sem nenhum aviso (comportamento esperado pelo RF03, mas pouco claro para o aluno) | Baixa | Botão "Nova conversa" (o motor já tem `limpar_historico()`) e aviso de que o histórico não é salvo |

### Limitações deste teste
Uma testadora, uma sessão, sem alunos reais de maratona. A recusa de código foi testada em um único caso adversarial.

### Prioridades recomendadas
1. Corrigir/documentar a execução e atualizar o README (#1).
2. Feedback durante a espera e proteção contra duplo envio (#2).
3. Preservar a formatação do código no diálogo e limpar o campo após o envio (#3, #4).
4. Explicar na tela o que o assistente faz e não faz (#6).

Os problemas de interface e execução listados acima são **recomendações de melhoria**, não correções já implementadas. O `README.md` também precisa ser atualizado para refletir a disponibilidade da interface Web e seu comando de execução.

Registro completo: ver a Issue [#27](https://git.juninho.com.br/cefet-gps-2026/gps-projetos-integradores/coach-de-maratona-icpc/-/work_items/27).

---

## 5. Onde saber mais

- [`README.md`](../README.md) — instalação e comandos de execução
- [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md) — como o assistente deve se comportar
- [`DIRETRIZES_PROMPT.md`](DIRETRIZES_PROMPT.md) — ideologia pedagógica e exemplos de diálogo
- [`CASOS_DE_TESTE_PROMPT.md`](CASOS_DE_TESTE_PROMPT.md) — bateria de testes e falhas conhecidas
- [`REQUISITOS.md`](REQUISITOS.md) — requisitos funcionais e não funcionais
