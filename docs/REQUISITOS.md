## REQUISITOS FUNCIONAIS

## RF01 - Disponibilização da interface de interação

O sistema deverá disponibilizar uma interface Web em Streamlit para acesso ao Maieut-IA. A interface deverá conter os componentes necessários para a interação com o assistente, incluindo uma área destinada à entrada de texto ou código e uma área destinada à visualização do diálogo.

**Critério de aceitação:** a interface deverá ser carregada sem erros e apresentar de forma visível e utilizável o campo de entrada e a área de exibição da conversa.

## RF02 - Submissão do problema ou código para análise

O sistema deverá permitir que o aluno envie ao Maieut-IA a descrição de um problema de programação e/ou o código desenvolvido durante sua tentativa de resolução. Após a submissão, o conteúdo informado deverá ser encaminhado ao Core Lógico do sistema para processamento e posterior análise pelo assistente.

**Critério de aceitação:** ao realizar uma submissão, todo o conteúdo informado pelo aluno deverá ser capturado e encaminhado ao Core Lógico sem perda ou alteração indevida do texto ou código enviado.

## RF03 - Manutenção e exibição incremental do diálogo da sessão

O sistema deverá apresentar a interação entre o aluno e o Maieut-IA em turnos sucessivos, adicionando cada nova mensagem ao diálogo e mantendo visíveis as interações anteriores da sessão atual, de forma a representar o histórico da conversa em andamento. Esse histórico é mantido apenas durante a sessão ativa da aplicação, sem persistência entre sessões, contas de usuário ou mecanismos de autenticação.

**Critério de aceitação:** após cada interação, a nova mensagem do aluno e a respectiva resposta do Maieut-IA deverão ser incorporadas ao diálogo sem substituir os turnos anteriores da sessão atual, permitindo acompanhar a evolução da conversa enquanto a aplicação estiver em execução. Ao encerrar ou recarregar a aplicação, o histórico não deverá ser recuperado, uma vez que não há persistência de dados entre sessões.

## RF04 - Identificação da classe do algoritmo e análise de complexidade

O sistema deverá analisar o problema e/ou código submetido pelo aluno e, sempre que for possível identificar uma classe ou estratégia algorítmica associada à solução, indicá-la ao aluno. O sistema também deverá analisar aspectos de complexidade computacional, identificando possíveis limitações de eficiência na abordagem apresentada pelo aluno.

**Critério de aceitação:** a identificação da classe do algoritmo e a análise da complexidade deverão ser avaliadas separadamente, estando corretas em pelo menos 90% de um conjunto de 100 casos de teste de dificuldade variada definidos pela equipe.

## RF05 - Condução socrática da resolução

O sistema deverá atuar como tutor durante a resolução do problema, conduzindo o aluno por meio de perguntas, pistas e orientações progressivas. O sistema deverá estimular o aluno a explicar o raciocínio já desenvolvido, verificar sua compreensão do problema e de suas restrições e utilizar essas informações para orientar os próximos passos, sem fornecer diretamente a solução completa ou código-fonte pronto.

**Critério de aceitação:** nas interações da bateria de testes adversariais utilizada para validação do prompt, o sistema não deverá apresentar solução completa ou código-fonte integral em nenhum momento da condução, devendo restringir-se a perguntas, pistas e orientações.



## REQUISITOS NÃO FUNCIONAIS

## RNF01 - Tempo máximo de resposta
O assistente deverá apresentar uma resposta ao usuário em, no máximo, 10 segundos após o envio de uma pergunta, considerando condições normais de funcionamento e disponibilidade da API de inteligência artificial.
Critério de aceitação: em pelo menos 90% das requisições, o tempo entre o envio da pergunta e a apresentação da resposta deverá ser inferior ou igual a 10 segundos. O sistema deverá informar o usuário caso a requisição ultrapasse esse limite.

## RNF02 - Segurança das chaves de API
As chaves de acesso às APIs utilizadas pelo sistema deverão ser armazenadas exclusivamente por meio de variáveis de ambiente ou mecanismo equivalente de configuração segura, não podendo ser inseridas diretamente no código-fonte.
Critério de aceitação: nenhuma chave de API deverá estar presente no código-fonte, arquivos versionados ou commits do repositório. O sistema deverá obter as credenciais a partir das variáveis de ambiente durante sua execução.

## RNF03 - Proteção contra exposição de credenciais
O sistema não deverá exibir, registrar ou retornar chaves de API e outras credenciais em mensagens destinadas ao usuário, logs ou mensagens de erro.
Critério de aceitação: ao ocorrer uma falha relacionada à API, a mensagem apresentada deverá conter apenas informações necessárias para orientar o usuário, sem expor tokens, chaves, credenciais ou outros dados sensíveis.

## RNF04 - Tratamento de rate limit
Quando a API de inteligência artificial retornar uma resposta indicando limite de requisições (rate limit), o sistema deverá tratar a falha de forma controlada, evitando o encerramento inesperado da aplicação.
Critério de aceitação: diante de um erro de rate limit, o chatbot deverá informar ao usuário que o serviço está temporariamente indisponível ou limitado e solicitar que tente novamente posteriormente. O erro não deverá causar o encerramento da aplicação.

## RNF05 - Tratamento de erros da API
O sistema deverá tratar erros de comunicação ou indisponibilidade da API de inteligência artificial de maneira controlada, apresentando uma mensagem compreensível ao usuário.
Critério de aceitação: em caso de erro da API, o sistema deverá capturar a falha, evitar a exibição de mensagens técnicas ou credenciais e apresentar uma mensagem de erro ao usuário sem interromper o funcionamento das demais funcionalidades do chatbot.

## RNF06 - Resiliência da aplicação
O chatbot deverá permanecer disponível após falhas individuais em requisições à API, permitindo que o usuário realize novas tentativas sem necessidade de reiniciar manualmente a aplicação.
Critério de aceitação: após uma requisição malsucedida, uma nova pergunta deverá poder ser enviada normalmente, desde que a API esteja novamente disponível e os demais recursos do sistema estejam funcionando.

## RNF07 - Configuração segura do ambiente
As configurações sensíveis ou específicas do ambiente de execução deverão ser mantidas fora do código-fonte principal, permitindo sua alteração sem modificar a implementação da aplicação.
Critério de aceitação: informações como chaves de API deverão ser fornecidas por variáveis de ambiente ou arquivo de configuração local não versionado, como .env, devidamente incluído nas regras de exclusão do controle de versão.