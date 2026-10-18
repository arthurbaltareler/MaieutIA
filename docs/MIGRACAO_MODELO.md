# Plano de migração de modelo — Maieut-IA

## 1. Objetivo

Preparar a substituição de `gpt-3.5-turbo` antes do desligamento indicado nesta issue (23/10/2026), evitando interrupção do assistente e preservando a abordagem pedagógica socrática.

## 2. Modelo substituto e estado da decisão

**Modelo proposto:** `gpt-4o-mini`.

**Estado:** proposta técnica registrada; aprovação definitiva pela equipe ainda precisa ser confirmada. Antes de adotar o modelo, validar sua disponibilidade para a conta/projeto da API, custo, latência, compatibilidade com o endpoint usado e qualidade das respostas do Maieut-IA. A proposta não significa que a migração já foi implementada.

## 3. Mapeamento do estado atual do repositório

A busca por identificadores de modelo no código Python encontrou os seguintes usos. Não foi encontrada ocorrência de `gpt-3.5-turbo` nos arquivos Python analisados; as ocorrências encontradas estão na documentação histórica e neste plano.

| Arquivo | Modelo encontrado | Observação |
|---|---|---|
| `core/engine.py` | `gpt-4.1-mini` | Modelo padrão do motor de diálogo. |
| `tests/test_dialogo.py` | `gpt-4.1-mini` | Modelo especificado no teste de diálogo. |
| `tests/test_system_prompt.py` | `gpt-4.1-mini` | Modelo especificado no teste do prompt. |
| `spike/test_api.py` | `gpt-4o-mini` | Modelo utilizado no teste isolado da API. |
| `docs/PROJECT_CHARTER.md` | `gpt-3.5-turbo` | Referência histórica à premissa e ao risco original do projeto. |
| `docs/RISCOS_E_COMUNICACAO.md` | `gpt-3.5-turbo` | Registro do risco de desligamento e sua contingência. |
| `docs/EAP.md` | `gpt-3.5-turbo` | Referência ao plano de migração na EAP. |

Esse mapeamento representa os arquivos encontrados na revisão do repositório e deve ser refeito antes da migração, caso o código mude. A referência histórica ao modelo antigo não significa que ele seja atualmente usado pelo motor.

## 4. Passos da migração

1. Confirmar com a equipe a escolha de `gpt-4o-mini` ou registrar outro modelo substituto.
2. Confirmar disponibilidade, permissões de acesso, custo e compatibilidade do modelo com o endpoint utilizado.
3. Centralizar a identificação do modelo em uma configuração, se isso for adequado à arquitetura, evitando valores divergentes entre motor e testes.
4. Atualizar os pontos de configuração do motor, demonstrações e testes que precisem usar o modelo aprovado.
5. Executar os testes de chamada à API e de continuidade do histórico multi-turn.
6. Avaliar o comportamento socrático com problemas de programação, incluindo solicitações de solução completa.
7. Comparar custo e latência com os critérios do projeto e registrar os resultados.
8. Atualizar esta documentação e os registros de risco após a decisão e a validação.

## 5. Critérios de validação

- O modelo aprovado está disponível para a conta/projeto da API.
- As chamadas à API funcionam com o endpoint e os parâmetros utilizados pelo projeto.
- O histórico multi-turn continua funcionando.
- O System Prompt continua sendo aplicado.
- As respostas mantêm o comportamento pedagógico esperado nos casos de teste.
- Erros de API são tratados adequadamente.
- Custo e latência são avaliados e registrados antes da adoção definitiva.

## 6. Plano de retorno

Se o modelo proposto apresentar problemas, restaurar a última configuração funcional que use um modelo ainda disponível e compatível com a API. **Não depender da disponibilidade de `gpt-3.5-turbo` para o retorno.** Se não houver uma configuração anterior utilizável, selecionar outro modelo disponível, registrar a alteração e executar novamente os testes antes de liberar a mudança.

## 7. Prazo

Concluir a decisão, validação e eventual migração antes do desligamento indicado na issue: 23/10/2026. A data deve ser confirmada com a referência oficial do provedor antes de ser tratada como aviso técnico definitivo.
