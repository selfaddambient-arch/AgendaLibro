O MCP (Model Context Protocol) é um conjunto comum de convenções para a IA usar ferramentas e dados externos. Proposto pela Anthropic, hoje é compatível com muitas IAs, incluindo o ChatGPT e o Claude.

Numa analogia, o MCP é um padrão de tomada elétrica, para a IA. Como o formato da tomada é fixo, aparelhos de qualquer fabricante funcionam quando ligados. Do mesmo modo, se você constrói uma janela no formato do MCP, qualquer IA pode usá-la.

Um servidor MCP diz à IA "o que você pode fazer por esta janela". O servidor MCP do Tamuro, por exemplo, enfileira ferramentas como as seguintes.

- Ler as informações do estabelecimento (horário de funcionamento, número de lugares, regras da casa, clima)
- Ler os planos e os preços (o resultado do cálculo dos descontos por número de pessoas e data)
- Ler os horários livres (os horários disponíveis para reserva em um dia especificado)
- Criar a URL de uma página de reserva com as condições preenchidas

Quando um cliente pergunta à própria IA "Tem mesa no Tamuro hoje à noite?", a IA se conecta ao servidor MCP do Tamuro, escolhe "ler os horários livres" entre as ferramentas enfileiradas e a chama. O servidor do Tamuro devolve o resultado, e a IA o põe em palavras para o cliente.

O que importa é que a IA não confirma reservas por conta própria. Na primeira versão, deixei de propósito a confirmação de reservas fora das ferramentas. Tudo o que a IA pode fazer é ler e guiar as pessoas até uma página de reserva com as condições preenchidas. O botão de confirmar é apertado pelo próprio cliente na página do Tamuro. O perigo de a IA criar grandes quantidades de reservas erradas ou de trote é evitado pelo projeto desde o início.

O cálculo de preços usa o mesmo mecanismo de cálculo do site de reservas. Os preços mostrados no formulário de reserva, na janela de conversa e pelo MCP saem todos de um único programa. Esse é o outro significado da tarefa sobre a qual escreverei adiante, "concentrar o cálculo dos descontos em um só lugar".

【Figura 2-1】Da IA do cliente até a página de reservas do Tamuro. O cliente aperta o botão de confirmar

### 2-2 Como funciona a janela de conversa "T-AI-MURO"

#### Os preços vêm do programa, as palavras vêm da IA

O T-AI-MURO divide os papéis em dois. O programa gera preços e horários livres com cálculos fixos, e a IA os põe em palavras para o cliente.

A IA é boa em produzir texto, mas não há garantia de que calcule corretamente toda vez. Como os descontos se acumulam, as faixas por número de pessoas, o número de dias do desconto por reserva antecipada, se pode ser combinado com o happy hour. Se você deixa todas essas regras com a IA, ela certamente errará em algum ponto. E um erro de preço é o que mais prejudica a confiança do cliente.

Por isso, as partes que não podem errar ficam com o programa, e as partes que transmitem as coisas com suavidade ficam com a IA. Essa divisão é o primeiro princípio na construção da janela de conversa.

#### Para um pequeno estabelecimento, não é preciso RAG

Para fazer a IA responder sobre o estabelecimento, é preciso entregar a ela o conhecimento do estabelecimento. Um método muito usado é o RAG (geração aumentada por recuperação). Você corta o conhecimento em pedacinhos e os armazena e, a cada pergunta que chega, encontra só as partes que parecem relevantes e as entrega à IA. Quando o conhecimento é vasto, esse método é indispensável.

Mas o conhecimento do Tamuro não é tão grande. A história do estabelecimento, a comida, as regras, o clima, o modo de pensar de quem o comanda. Tudo junto cabe com folga no que a IA consegue ler de uma vez.

Então, no Tamuro, escolhi fazer a IA ler o texto inteiro do conhecimento do estabelecimento toda vez. Não é preciso construir o mecanismo de busca que o RAG exige, e nada se perde na busca. No início planejei reaproveitar um mecanismo de RAG, mas no meio do caminho passei para a abordagem do texto completo.

Fazer a IA ler o texto inteiro toda vez custa mais em tarifas de IA. Por isso uso um mecanismo que reaproveita o mesmo texto para reduzir o custo de entrada (cache de prompt: em vez de fazer a IA reler toda vez o mesmo preâmbulo, ela se lembra do que já leu). Só vale trazer o RAG quando o conhecimento crescer muito.

#### Um programa que sobrescreve respostas por conta própria

No Capítulo 1, escrevi que só 9 de 36 passaram no primeiro teste. Parte da causa estava na forma como o programa foi construído.

Ao investigar, encontrei um mecanismo que tinha ficado ali em que o programa julgava por palavras-chave a resposta que a IA havia dado e a trocava por uma frase fixa. Quando apareciam palavras como "reserva" ou "hoje", ele jogava fora a resposta da IA e colocava no lugar uma lista de horários livres. Mesmo quando a IA respondia corretamente, a resposta nunca chegava ao cliente.

Além disso, descobri que o corpo principal do conhecimento do estabelecimento (33 seções) não estava incluído nas instruções para a IA. A IA vinha respondendo sem conhecer o estabelecimento.

A qualidade das conversas da IA foi decidida menos pela esperteza da própria IA do que pelos fatos do estabelecimento entregues a ela e por um programa sobrescrever, ou não, as respostas da IA por conta própria.

#### Completar as perguntas e respostas esperadas por contagem

Aumentei os cenários de teste dos 36 iniciais para 110 e depois para 355. Mas, se as pessoas acrescentam cenários por impulso, não há como saber se falta alguma coisa. À pergunta "Isso é abrangente?", a resposta honesta era "Não, não é".

Então, em vez de ampliar a cobertura pela imaginação, transformei isso numa questão de contar por máquina os lugares por onde ainda não se passou e preenchê-los. Para quatro coisas: as 33 seções do conhecimento do estabelecimento, as transições entre opções, as faixas dos descontos e as combinações de horários e dias da semana. Conto quantas vezes cada uma foi percorrida nos testes e acrescento automaticamente cenários onde a contagem é zero.

Também usei um método de cruzar seis eixos (número de pessoas, finalidade, jeito de beber, data e hora, formulação, cardápio) e criar cenários de modo que toda combinação de dois itens seja percorrida pelo menos uma vez.

Também encontrei uma brecha relacionada ao tempo. "Hoje" e "daqui a pouco" são determinados pela hora real em que o teste roda, então os resultados de uma rodada ao meio-dia e de uma à noite diferem. Por isso, fixei o relógio durante os testes e fiz rodar em cinco momentos: antes da abertura, durante o expediente, pouco antes do fechamento, num dia de folga regular e num feriado.

As respostas da IA variam um pouco a cada vez, mesmo para a mesma pergunta. Para os cenários ligados diretamente às vendas, estabeleci a condição de que precisam passar nas três vezes quando rodados três vezes.

#### Quando sai um número ruim, suspeite primeiro do teste

No teste que rodou 355 cenários em 5 momentos, de 1.775 conversas, 28,5% passaram.

Em vez de começar a corrigir de imediato, primeiro isolei o problema: "Esse número é mesmo uma fraqueza do T-AI-MURO, ou o teste está errado?" Se você corrige enquanto o teste está errado, acaba "corrigindo" até as respostas certas.

| Causa do erro | Quantidade |
| --- | --- |
| Uma frase fixa sequestra a pergunta | 276 |
| Não responde à pergunta, passa para o fluxo de reserva ou para as recomendações | 266 |
| Falha do ambiente de teste (o T-AI-MURO não conseguiu gerar resposta por causa do limite de custo) | 211 |
| Erros de datas, dias da semana, feriados, dias de folga | 142 |
| Inventar ou afirmar fatos que o estabelecimento não tem, prometer repassar recados | 119 |

Os dois primeiros tinham a mesma raiz: "reagir a palavras e fazer um movimento fixo antes de responder à pergunta do cliente". Os 211 do terceiro lugar não eram erros do T-AI-MURO. O limite de custo foi atingido no meio do teste, e o T-AI-MURO simplesmente não conseguiu gerar respostas. Excluindo esses, a taxa de aprovação passa a ser 32,4%.

A IA que julga também pode errar. Quando separei 20 casos e conferi, 2 eram erros do lado do teste. Em um deles, quem julgava não sabia que "este site de reservas tem cadastro de membros". Quem julga também não sabe nada além do material que recebeu. A precisão do teste é decidida pela completude das regras do estabelecimento entregues a quem julga.

No reteste depois das correções, a taxa de aprovação da orientação sobre preços e planos subiu de 29,4% para 42,7%. Ainda não rodei o teste final que passa todos os casos de novo. Para manter os custos baixos, decidi que o teste de todos os casos roda só uma vez, antes de pôr uma mudança grande em produção. A taxa de aprovação continua sendo elevada enquanto escrevo este livro.

#### O teste parou a produção

Testes de IA custam dinheiro. O primeiro teste de 36 cenários custou cerca de ¥426 (cerca de US$ 2,8). A maior parte foi para o "esforço de raciocínio" da IA que faz o papel do cliente, e, quando o desativei, 3 cenários custaram cerca de ¥6 (cerca de US$ 0,04).

Mas então, um dia, no meio de um teste, o saldo de uso da IA acabou e tudo parou. Num único dia eu havia usado cerca de 35 milhões de tokens (a unidade de texto que uma IA lê e escreve). A causa foi rodar o teste de 221 cenários repetidas vezes e rodar quatro vezes cada um os cenários ligados diretamente às vendas.

O que assustou foi que o teste e a produção usavam a mesma carteira. Quando o saldo acaba, até a janela de conversa em produção para. Em outro dia, desta vez atingi um limite mensal que eu mesmo havia definido, e a janela de conversa em produção e a IA que cria os assuntos de conversa para os clientes no estabelecimento pararam ao mesmo tempo.

O perigo real de um orçamento de testes não era a conta, mas o fato de a produção usar a mesma carteira.

A partir daí, as regras mudaram. Fazer primeiro as verificações que não custam nada (testes do programa e verificações automáticas de tela). Limitar os testes que chamam a IA aos relacionados ao que foi corrigido. Rodar o teste de todos os casos uma só vez, antes de ir para produção. Escrever nas instruções a estimativa de custo e um limite, e parar se parecer que ele vai ser atingido. Para preservar fundos para a produção, parar os testes quando o uso de toda a organização chegar perto do limite.

Houve também uma lição sobre como os custos incham. Uma vez, o custo da IA que julga chegou a 2,6 vezes a estimativa. A causa era que o longo preâmbulo entregue a quem julga toda vez (o conhecimento e as regras do estabelecimento) não estava sendo reaproveitado, então uma cobrança por reprocessamento era gerada a cada vez. Quando corrigi para gravar o preâmbulo uma vez e reaproveitá-lo, o custo por conversa caiu para cerca de um terço. O custo da IA incha não com quantas vezes você a chama, mas com quantas vezes o mesmo preâmbulo precisa ser reprocessado.

O mesmo teste completo de 221 cenários caiu de cerca de ¥1.040 (cerca de US$ 6,9) para cerca de ¥400 (cerca de US$ 2,7) com melhorias repetidas. Troquei a IA que faz o papel do cliente por um roteiro fixo e dividi a informação entregue à IA em um "núcleo enviado toda vez" e "seções lidas só quando necessário".

Por causa das restrições de orçamento, o projeto mudou no sentido de aumentar as partes que podem ser verificadas a custo zero, isto é, as partes decididas pelo programa. Como resultado, a precisão também subiu. O dinheiro muda o projeto.

【Figura 2-2】Resultados dos testes de IA. A taxa de aprovação e a divisão das causas dos erros

### 2-3 Pedir à IA que audite o que construí

#### Os nomes dos clientes podiam ser lidos de fora

Em agosto de 2026, enquanto eu revisava o funcionamento do sistema de reservas, fiz uma descoberta que me deu um calafrio.

Os dados de reservas dos clientes podiam ser lidos por qualquer pessoa, de fora. Nomes, telefones, endereços de e-mail, o campo de pedidos. Tudo o que era digitado em uma reserva podia ser extraído por inteiro, sem nenhuma autenticação.

Há uma coisa que devo dizer com honestidade. É verdade que os dados podiam ser lidos de fora. Na época, o site de reservas tinha muito pouco tráfego, e acredito que seja improvável que alguém tenha realmente lido. Mas não tenho nenhum registro que possa provar que não foram lidos. "Poderiam ter sido obtidos" e "foram realmente obtidos" são duas coisas diferentes, mas só a primeira já era uma falha grave para um estabelecimento.

Quando rastreei a causa, ela se resumia à forma como o formulário de reserva foi construído. Para calcular os lugares livres, o formulário carregava 35 dias de dados de reservas diretamente a partir da tela. Se a tela consegue ler, qualquer pessoa que saiba como telas desse tipo são construídas consegue ler os mesmos dados. Era o resultado de uma primeira base construída no feeling, que alcançou o objetivo de "mostrar os lugares livres" pelo caminho mais curto.

Também descobri que o endereço de e-mail para avisar a administração do estabelecimento estava público e que qualquer pessoa podia escrever no lugar onde as traduções eram guardadas, o que significava que os dados podiam ser vandalizados ou os custos inflados.

A ordem da correção importava. Se eu proibisse a leitura de uma vez, o formulário de reserva não conseguiria mais mostrar os lugares livres e pararia de funcionar. Então, primeiro movi o cálculo dos lugares livres para um endpoint no lado do servidor. Depois, mudei a tela de reserva concluída para que ela também obtivesse do servidor apenas as informações de que precisa. Por último, fechei a leitura de fora. Fiz a correção em quatro etapas, nessa ordem, e a apliquei em produção.

Depois da correção, usei uma máquina para conferir que estava mesmo fechado. Preparei um teste que tenta ler os dados de reservas sem autenticação e o rodo automaticamente depois de cada mudança, para confirmar que sempre é recusado. Não corrigi uma vez e dei por encerrado. Configurei para que uma verificação fique de vigia, garantindo que nunca volte a abrir.

#### Dados reais de clientes ficaram no histórico de desenvolvimento

Em seguida, pedi à IA que auditasse o repositório inteiro (o local de armazenamento do programa), e surgiu um problema mais grave.

Durante o desenvolvimento, um arquivo contendo dados reais de clientes (endereços de e-mail e telefones de 55 reservas) tinha sido enviado ao repositório e continuava incluído no histórico de alterações do programa. O repositório era privado, mas, como o arquivo permanecia no registro, eu não podia deixar assim.

Removi o arquivo de todo o histórico de alterações, reescrevi o histórico e o guardei de novo. Mesmo assim, os registros antigos de antes da reescrita ainda poderiam permanecer do lado do GitHub, que hospeda o repositório. Então pedi ao suporte do GitHub que os apagasse e confirmei que foi feito.

A auditoria também encontrou outros problemas: o endpoint de tradução podia ser usado sem autenticação, o login da administração podia ser atacado por força bruta e havia uma janela de tempo em que, se o pagamento fosse reativado, uma reserva podia ser confirmada ainda sem pagamento. Corrigi um por um, começando pelo mais grave.

#### Havia zero testes automatizados

A auditoria revelou mais um fato. O sistema de reservas não tinha um único teste automatizado.

Testes automatizados são um mecanismo em que uma máquina confere automaticamente se o programa funciona corretamente. Sem testes, quando você corrige algo, não tem como conferir se outra coisa quebrou. Cada vez que você acrescenta um recurso, em algum lugar algo quebra em silêncio. Era exatamente esse o estado das coisas no período em que eu construía no feeling.

Então reconstruí a base de testes do zero. Introduzi um sistema (CI) que roda automaticamente quatro verificações depois de cada alteração: verificação de tipos, verificação de estilo, testes e a compilação. Decisões importantes, como o cálculo de preços, o julgamento de reservas, a vinculação de membros e a emissão de cupons, foram separadas dos programas de tela para que possam ser verificadas por conta própria. As regras de leitura e gravação do banco de dados também são conferidas em um ambiente de teste que imita um banco de dados real. Os testes unitários começaram em 275 e depois passaram de 500.

Há uma condição que sempre imponho aos testes: "quebre e confirme que falha". Mesmo quando um teste fica verde (passa), você não sabe se ele consegue mesmo pegar um problema. Só depois de quebrar o programa de propósito e confirmar que o teste fica vermelho (falha) é que confio no teste. Isso porque testes escritos por IA às vezes não verificam absolutamente nada.

#### Oito brechas no formulário de reserva

Depois que a base de testes estava pronta, pedi à IA que examinasse de novo todo o fluxo de reserva. Ela encontrou oito problemas que causavam dano real.

O mais grave era que apertar o botão de enviar várias vezes criava uma reserva duplicada. Isso estava realmente acontecendo em produção. Corrigi com um mecanismo que processa a mesma ação uma única vez mesmo que ela chegue duas vezes (idempotência). Os outros problemas eram estes: uma reserva não podia ser confirmada se restassem informações de um item de cardápio excluído; havia uma falha na verificação de casa cheia que deixava margem para exceder a capacidade; ninguém percebia quando um e-mail de confirmação falhava ao ser enviado; a entrada não era validada no lado do servidor; textos internos apareciam na tela quando ocorria um erro; o texto nos campos de entrada era tão pequeno que a tela dava zoom sozinha no iPhone; e o preenchimento automático dos campos não funcionava.

Para as falhas de e-mail, tornei possível detectá-las na tela de administração e reenviar. Durante essa investigação, descobri também que o registro de auditoria que anota as confirmações de reservas vinha falhando toda vez, desde bem antes da correção, e não tinha registrado nada.

Corrigi esses problemas um por um e os apliquei em produção.

#### Nunca pule a verificação do código que a IA escreveu

O que aprendi com essa experiência é que, justamente porque um programa foi escrito por IA, você não deve pular a verificação.

A IA dá forma rapidamente ao que lhe dizem. Mas a atenção a coisas que não lhe dizem, como "faça de modo que não possa ser lido de fora" ou "trate um envio duplo como um só", não entra se você não instruir. E brechas como essas ficam quietas dentro de programas que parecem funcionar.

As pessoas não precisam ler todo o código. A correção do programa é vigiada por verificações de máquina e pela auditoria de outra IA. Se o resultado se encaixa no propósito do estabelecimento é vigiado por quem o comanda. Você não precisa ler, mas não deve pular a verificação. É isso que acredito que significa construir com uma IA do tipo agente.

【Figura 2-3】As regras de quando podia ser lido de fora e as regras depois da correção (trecho) *(A tela está em japonês.)*

### 2-4 Construir no feeling multiplica as contradições

Quanto mais recursos eu acrescentava, mais partes havia que colidiam com o que eu tinha decidido antes.

O caso típico foi o cálculo de descontos. No formulário de reserva, na tela de confirmação, no e-mail e na tela de administração, o cálculo de descontos estava escrito separadamente em cada lugar. Se eu mudava uma regra de desconto em um lugar, outro lugar continuava calculando com a regra antiga. Para a mesma reserva, a tela e o e-mail podiam mostrar valores diferentes.

Mais tarde, reuni o cálculo de preços em um único arquivo. O formulário de reserva, a janela de chat e o servidor MCP geram os preços a partir dali.

As regras de acúmulo de descontos também mudaram pelo caminho. Como escrevi no Capítulo 1, a happy hour originalmente seria combinável com outros descontos, mas percebi que não daria lucro e mudei para não combinável. A cada mudança de regra, uma pessoa precisava lembrar onde corrigir. Essa era a fraqueza de um sistema construído no feeling.

Havia também uma divergência entre o ambiente de teste e a produção. Ao testar a janela de chat, uma pergunta, "Não tinha algo como 10% de desconto?", revelou que as regras de desconto do ambiente de teste tinham se afastado das da produção. Se os valores do ambiente de teste diferem dos da produção, você pode passar nos testes e ainda assim estar errado em produção. O que decidi então foi o princípio de que "a produção está certa". Desde então, antes de cada rodada de testes, copio as configurações da produção para o ambiente de teste e confirmo que a divergência é zero antes de rodar.

A IA constrói o que lhe dizem. Mas não percebe contradições com decisões anteriores. O que previne contradições não é a IA. É decidir as coisas de antemão.

### 2-5 Reaprender a definição de requisitos

Depois de refletir sobre o sistema de reservas que construí no feeling, reaprendi a definição de requisitos. Definir requisitos significa decidir, antes de construir, o que será construído, o que não será construído e quem vai usar e como, e escrever isso em um documento.

Era algo que eu fazia como coisa natural quando era engenheiro de sistemas. Mas, quando passei a poder construir com IA, pulei essa etapa sem perceber. Você conta uma ideia e algo funcionando aparece em minutos. Nessa velocidade, eu tinha cortado o esforço de decidir.

Meu jeito de construir agora tem três etapas.

1. Primeiro, decidir os requisitos em detalhe. O que construir, o que não construir, quem vai usar. O comportamento de cada tela. Como tratar as exceções (erros, cliques duplos, expiração). Regras que facilmente acabam se contradizendo mais tarde, como preços e descontos, decido com detalhe especial. Esse trabalho também faço em diálogo com a IA de chat. Peço à IA que encontre antes as brechas e as contradições, e quem comanda o bar decide.
2. Escrever o que foi decidido como um "documento de requisitos". Não instruções faladas ou de improviso, mas reunidas em um só documento. Ele passa a ser o único padrão para conferir depois o que está correto.
3. Entregar o documento inteiro à IA e pedir que ela implemente. Entrego o documento inteiro à IA que escreve o programa (Claude Code), junto com as condições para aprovação (todos os testes passam, conferir no ambiente de teste antes da produção, e assim por diante). A IA constrói sozinha até cumprir as condições e confere sozinha. Quem comanda o bar só olha quando ela para no meio do caminho e na verificação final.

Por exemplo, o documento de requisitos da janela de chat "T-AI-MURO" foi reescrito da primeira versão até a terceira. Na segunda versão, decidi "não deixar a IA calcular preços", "colocar o conhecimento do estabelecimento e o cálculo de preços em uma só janela" e "manter também o formulário, para quem não quer reservar por chat". Na terceira versão, decidi "onde guardar a cópia mestra do conhecimento do estabelecimento", "só esta janela mostra horários livres", "fazer da primeira troca uma pergunta de quatro opções" e "não salvar registros de conversa; guardar apenas as perguntas que não puderam ser respondidas". Como as decisões permanecem em um documento, posso rastrear depois por que as coisas são como são.

Com esse jeito de construir, mesmo quando acrescento recursos, consigo perceber as contradições de imediato conferindo com o documento. Justamente numa era em que a IA faz a construção, é preciso o "poder de decidir" antes de construir. Essa foi a maior lição que aprendi com o sistema de reservas.
