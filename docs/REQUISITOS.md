RNF01 — Tempo máximo de resposta
O assistente deverá apresentar uma resposta ao usuário em, no máximo, 10 segundos após o envio de uma pergunta, considerando condições normais de funcionamento e disponibilidade da API de inteligência artificial.
Critério de aceitação: em pelo menos 90% das requisições, o tempo entre o envio da pergunta e a apresentação da resposta deverá ser inferior ou igual a 10 segundos. O sistema deverá informar o usuário caso a requisição ultrapasse esse limite.

RNF02 — Segurança das chaves de API
As chaves de acesso às APIs utilizadas pelo sistema deverão ser armazenadas exclusivamente por meio de variáveis de ambiente ou mecanismo equivalente de configuração segura, não podendo ser inseridas diretamente no código-fonte.
Critério de aceitação: nenhuma chave de API deverá estar presente no código-fonte, arquivos versionados ou commits do repositório. O sistema deverá obter as credenciais a partir das variáveis de ambiente durante sua execução.

RNF03 — Proteção contra exposição de credenciais
O sistema não deverá exibir, registrar ou retornar chaves de API e outras credenciais em mensagens destinadas ao usuário, logs ou mensagens de erro.
Critério de aceitação: ao ocorrer uma falha relacionada à API, a mensagem apresentada deverá conter apenas informações necessárias para orientar o usuário, sem expor tokens, chaves, credenciais ou outros dados sensíveis.

RNF04 — Tratamento de rate limit
Quando a API de inteligência artificial retornar uma resposta indicando limite de requisições (rate limit), o sistema deverá tratar a falha de forma controlada, evitando o encerramento inesperado da aplicação.
Critério de aceitação: diante de um erro de rate limit, o chatbot deverá informar ao usuário que o serviço está temporariamente indisponível ou limitado e solicitar que tente novamente posteriormente. O erro não deverá causar o encerramento da aplicação.

RNF05 — Tratamento de erros da API
O sistema deverá tratar erros de comunicação ou indisponibilidade da API de inteligência artificial de maneira controlada, apresentando uma mensagem compreensível ao usuário.
Critério de aceitação: em caso de erro da API, o sistema deverá capturar a falha, evitar a exibição de mensagens técnicas ou credenciais e apresentar uma mensagem de erro ao usuário sem interromper o funcionamento das demais funcionalidades do chatbot.

RNF06 — Resiliência da aplicação
O chatbot deverá permanecer disponível após falhas individuais em requisições à API, permitindo que o usuário realize novas tentativas sem necessidade de reiniciar manualmente a aplicação.
Critério de aceitação: após uma requisição malsucedida, uma nova pergunta deverá poder ser enviada normalmente, desde que a API esteja novamente disponível e os demais recursos do sistema estejam funcionando.

RNF07 — Configuração segura do ambiente
As configurações sensíveis ou específicas do ambiente de execução deverão ser mantidas fora do código-fonte principal, permitindo sua alteração sem modificar a implementação da aplicação.
Critério de aceitação: informações como chaves de API deverão ser fornecidas por variáveis de ambiente ou arquivo de configuração local não versionado, como .env, devidamente incluído nas regras de exclusão do controle de versão.