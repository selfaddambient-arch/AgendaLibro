### 1-6 Opções demais para escolher

Com o sistema de descontos montado, o que eu quis em seguida foi aumentar os horários e os planos que vendem.

O horário das 18h não enchia, então criei uma happy hour até as 19h. Para quem chega depois de ter comido, criei um plano só de bebidas, sem refeição. O menu fechado e a aula de culinária, antes mensais, viraram eventos sob demanda, que abrem quando alguém se inscreve, recebidos pelo site de reservas. Para vender os horários antes da abertura nos fins de semana, a partir das 15h30, criei um plano de festa para grupos de seis ou mais.

Cada um tem um motivo. O plano de festa, por exemplo: se eu o fizesse parecer uma pechincha no preço, só atrairia clientes que vinham escolhendo o plano padrão, e o faturamento cairia. Por isso, coloquei a diferenciação não no preço, mas no horário anterior à abertura, que nunca tinha trazido nenhuma venda. O desconto da happy hour não dá lucro se combinado com outros descontos, então decidi que ele não pode ser combinado.

E assim os planos se multiplicaram. Padrão, Premium, Prazer em Conhecer, Bem-vindo de Volta, Happy Hour, Só Bebidas, Menu Fechado, Aula de Culinária, Festa. Cada um tem condições de número de pessoas, alguns aceitam descontos e outros não, e há restrições de horário.

Um dia abri o formulário de reserva e percebi: com isso, o cliente não consegue escolher.

Eu, quem construiu, entendo cada diferença. Mas será que alguém abrindo o site de reservas pela primeira vez consegue comparar nove planos e suas condições de desconto e escolher o que combina? Se não consegue, desiste no meio da reserva. Os planos que me esforcei para acrescentar poderiam acabar reduzindo as reservas.

Eu poderia ter feito uma faxina. Mas cada plano tem um horário que quero vender e um tipo de cliente que quero receber. Não quis cortar nenhum.

Então pensei num sistema em que o cliente consulta a IA e decide o plano. Você informa o número de pessoas, a data e a hora em que gostaria de vir e como quer aproveitar a noite, e a IA indica o plano e o preço adequados e leva direto para a reserva. O estabelecimento assume a complexidade dos planos. O que sobra para o cliente é só uma conversa.

Esse sistema é o "T-AI-MURO" sobre o qual escrevo em 1-8. Antes disso, há mais uma coisa que notei nesse período.

【Figura 1-2】Seleção de plano no formulário de reserva. Tantas abas enfileiradas *(A tela está em japonês.)*

### 1-7 "Isso realmente atrai clientes?"

No dia em que acrescentei o plano de festa, passei o dia inteiro fazendo uma melhoria atrás da outra no site de reservas. Enxuguei o cabeçalho, alinhei o design dos e-mails e troquei a IA que cria os assuntos de conversa para os clientes no estabelecimento.

À noite, uma pergunta me veio de repente.

"Isso realmente ajuda a atrair mais clientes?"

Quando perguntei à IA, ela organizou com honestidade as melhorias do dia.

| Categoria | Melhorias do dia |
| --- | --- |
| Coisas que podem gerar novas reservas | Plano de festa, o horário das 15h30 em fins de semana e feriados |
| Coisas que aumentam a taxa de conclusão de quem chegou | Enxugar o cabeçalho, alinhar as abas |
| Coisas que incentivam o retorno | Unificar o design dos e-mails |
| Coisas que não ajudam a atrair clientes | Trocar a IA que cria os assuntos de conversa, o link para a próxima parada, o aviso da Agenda |

Das melhorias do dia, só o plano de festa e o horário das 15h30 levavam diretamente a atrair clientes. O resto eram melhorias para não perder quem já tinha chegado. Também importam, mas não aumentam a clientela.

Havia um problema maior. Para nenhuma das melhorias eu tinha um jeito de medir se funcionou. Não havia nenhum número ligando "eu melhorei" a "os clientes aumentaram".

Minha resposta foi uma frase: "Vamos construir um."

Então me pus a criar um relatório semanal de captação de clientes. O número de reservas, o número de pessoas, o valor total, os cancelamentos. Detalhamentos por dia da semana e por faixa de horário. A proporção entre clientes de primeira vez e os que voltam. As contagens dos horários de festa e das 15h30. De onde vieram as reservas (o formulário de reserva, a janela de chat, reservas feitas por IA, lançamentos manuais do estabelecimento). Contagem de cliques nos e-mails e o número de reservas nos sete dias seguintes a esses cliques.

Onde há números, o tempo vem junto. No mesmo dia, eu tinha encontrado outra brecha. Eu havia definido a aula de culinária e o horário das 15h30 da festa como "fins de semana", mas, ao me perguntar "e nos feriados nacionais?" e investigar, vi que o sistema de reservas não tinha nenhum conceito de feriado. Numa segunda-feira de feriado o estabelecimento abre, e mesmo assim o horário das 15h30 não aparecia. Dei a ele uma lista de feriados e corrigi para tratá-los como fim de semana. Era uma brecha que ninguém notaria até que quem construiu notasse.

Antes de construir o relatório, tapei primeiro as brechas relacionadas ao tempo.

Até quem frequenta desde antes de eu começar a usar o sistema de reservas aparece como "cliente de primeira vez" nos registros. Por isso, no relatório escrevo "primeira visita registrada" e sempre anexo a data em que os registros começaram. Para julgar se uma melhoria funcionou, é preciso ter o quadro de antes dela. No primeiro relatório, somei as últimas oito semanas e usei isso como referência. Numa semana em que o estabelecimento fecha temporariamente, por viagem ou outros motivos, as reservas naturalmente caem. Por isso, listo também o número de dias de funcionamento, para que as comparações possam ser feitas por dia de funcionamento.

Na seção "Mudanças notáveis", deixei de pedir à IA que escrevesse e passei a usar cálculos e frases fixos. Isso é para manter o custo semanal em zero. Nomes e contatos dos clientes não aparecem no relatório; só contagens e proporções.

Depois que construí um jeito de medir, a própria forma de construir melhorias mudou. Comecei a decidir, desde o início, uma melhoria e o método de medir seu efeito juntos. A medição não é algo em que se pensa depois da melhoria; ela entra no mesmo documento de instruções que a melhoria. Foi isso que aprendi naquele dia.

【Figura 1-6】O relatório semanal de captação de clientes que chega toda semana (dados fictícios) *(A tela está em japonês.)*

### 1-8 Uma janela que conversa pelo estabelecimento: "T-AI-MURO"

Como escrevi em 1-6, os planos tinham se multiplicado, e o formulário de reserva ficou difícil de escolher para quem vem pela primeira vez. E os clientes de primeira viagem querem saber mais do que os planos e as datas. Que clima o lugar tem? Vou me sentir deslocado indo sozinho? Que tipo de pessoa comanda o bar? Posso levar crianças? Se você enfileira botões de reserva sem responder a perguntas como essas, não consegue dar o empurrão de que precisa quem está em dúvida.

Então decidi colocar no site de reservas uma "janela que conversa pelo estabelecimento". Quando um cliente escreve uma pergunta, a IA responde como o estabelecimento. Se o número de pessoas e a data forem definidos durante a conversa, o cliente pode ir direto para a tela de confirmação da reserva. Ela se chama "T-AI-MURO" e, na conversa, se apresenta como "Tamuro". O T-AI-MURO fala como o próprio estabelecimento e se refere a quem comanda o bar na terceira pessoa.

Os clientes quase não digitam. Eles só tocam nas opções que o T-AI-MURO oferece, e a conversa avança. Isso significa que as opções oferecidas em seguida decidem a qualidade da conversa. Sempre misturo três tipos de movimento nas opções: movimentos em direção a uma reserva (número de pessoas, preço, horários livres, data e hora), movimentos em direção a conhecer o estabelecimento (clima, quem comanda o bar, quem são os clientes, se dá para conversar com quem está ao lado) e movimentos que surgem do fluxo da conversa. Levar as pessoas a uma reserva não é o único objetivo. Deixá-las conhecer o clima do estabelecimento e quem o comanda também é o coração dessa janela.

Só os preços, decidi, não seriam calculados pela IA. Não há garantia de que a IA consiga calcular corretamente, toda vez, como os descontos se acumulam ou como valem as faixas por número de pessoas. O programa gera preços e horários livres com cálculos fixos, e a IA se limita ao trabalho de pô-los em palavras.

#### O primeiro conhecimento veio das minhas próprias publicações antigas

Para o T-AI-MURO responder a perguntas sobre o estabelecimento, ele precisa conhecê-lo. Como material, exportei todas as publicações que eu havia escrito até então no Instagram e no X (antigo Twitter) e as usei. A partir delas, montei as perguntas que os clientes provavelmente fariam e as respostas.

Quando experimentei de verdade, as publicações do X se mostraram mais úteis como material do que as do Instagram. O Instagram é quase todo foto, com poucas palavras. No X, eu tinha deixado registros escritos, com as minhas palavras, sobre a comida, o estabelecimento e o que eu pensava.

#### Só 9 de 36 passaram

Antes de pôr o T-AI-MURO em produção, testei com que correção ele conseguia responder. Os testes também foram feitos pela IA. Dei a uma IA que faz o papel do cliente um personagem e um objetivo e pedi que conversasse com o T-AI-MURO. Preparei 36 cenários: "sozinho hoje à noite", "4 pessoas daqui a duas semanas", "com criança", "alergias", "reserva do espaço inteiro", "aviso de atraso", "a origem do nome do estabelecimento", "que tipo de pessoa comanda o bar" e assim por diante.

O resultado da primeira rodada: 9 aprovados em 36.

A resposta mais comum era "Sinto muito, não consegui responder bem a isso". Essa resposta aparecia até para perguntas sobre o clima do estabelecimento e sobre quem o comanda. Sempre que surgiam palavras como "reserva", "hoje", "reserva do espaço inteiro" ou "mestre", aparecia uma lista de horários livres, qualquer que fosse o assunto real da pergunta. Em algumas conversas, uma mensagem sobre atraso foi tratada como uma nova reserva. Para um cliente vegetariano, deu como exemplos um refogado com flocos de bonito e sopa de missô. Chegou a dar, em inglês, informações sobre uma compra coletiva que já tínhamos encerrado.

#### Respondi a 11 perguntas com uma linha cada

Parte da causa estava na forma como o programa foi construído. Deixo essa história para o Capítulo 2. A outra causa era simples: faltavam fatos sobre o estabelecimento. Uma IA não consegue responder ao que não sabe.

Então reuni as perguntas que a IA não conseguiu responder e decidi respondê-las eu mesmo, uma linha cada.

Pode entrar sem reserva. Receber crianças que ainda não estão no ensino fundamental é complicado. Cancelamentos e mudanças até o dia anterior, por e-mail, telefone ou mensagem nas redes sociais. Para avisar de atraso, por favor, ligue. Há uma área para fumantes do lado de fora. É permitido trazer a própria bebida, com taxa de rolha. A reserva do espaço inteiro é possível conforme a faixa de preço e o horário, com no máximo 19 pessoas. Restrições alimentares e comemorações atendemos na medida do possível, então consulte-nos antes. Quem comanda o bar está no estabelecimento quase todos os dias de funcionamento. Um festival de yukata é planejado cerca de uma vez por ano.

Só isso. Apenas por responder a 11 perguntas com uma linha cada, 24 de 36 passaram no segundo teste.

| Pergunta | Primeira resposta | Segunda resposta |
| --- | --- | --- |
| Pode ir com crianças? | Sinto muito, não consegui responder bem a isso | Crianças em idade de ensino fundamental ou mais velhas podem ser atendidas se consultarem antes. Abaixo da idade do ensino fundamental é difícil |
| Dá para entrar sem reserva? | (lista de horários livres) | Pode entrar sem reserva |
| Quem comanda o bar está hoje? | (lista de horários livres) | Quem comanda o bar está no estabelecimento quase todos os dias de funcionamento. Hoje é dia de funcionamento, então está prevista a presença |
| É um lugar tranquilo? Só clientela fiel? | Sinto muito, não consegui responder bem a isso | É um lugar para relaxar. A conversa entre os clientes surge com facilidade e não é um lugar barulhento |

Aqui começou a surgir um padrão. A IA cria as perguntas que esperamos, o T-AI-MURO responde, e corrigimos os erros. Depois, só as perguntas que não podem ser respondidas porque faltam fatos do estabelecimento são passadas para quem comanda o bar. O esforço dessa pessoa é apenas uma linha para cada pergunta sem resposta. Todo o resto, a IA toca.

#### A cena em que o "orçamento de ¥5.000 (cerca de US$ 33)" falhou

Também coloquei um veredito da IA nos testes de IA. Uma IA diferente lê o registro da conversa e decide se passou ou falhou.

Entre eles havia um cenário com um cliente cujo "orçamento é de ¥5.000 (cerca de US$ 33)". O veredito da IA foi aprovado. O T-AI-MURO havia apresentado com educação planos dentro do orçamento.

Mas, quando li, era uma reprovação. Ele não tinha perguntado o número de pessoas. O Tamuro tem desconto para grupos. Dependendo do tamanho do grupo, os planos que se podem escolher com o mesmo orçamento mudam.

Nesse ponto, reformulei o objetivo.

"Mire no maior grupo possível, para garantir o maior valor total. Confirme o número de pessoas. O objetivo final é fazer os clientes virem. Quanto mais, melhor. Para aumentar o faturamento."

Com essa única frase, todo o projeto da conversa mudou. Sempre confirmar o número de pessoas antes de responder sobre preços e responder com o valor total. Logo antes de uma faixa do desconto para grupos, acrescentar "com mais uma pessoa vocês ganham tantos por cento de desconto". Quando houver um orçamento, mostrar primeiro o melhor plano dentro dele. No entanto, quem vem sozinho representa metade da clientela, então, para um cliente de uma pessoa, não sugerir aumentar o grupo.

Quando você pede à IA para rodar os testes de IA, eles rodam rápido. Mas quem decide o critério de aprovação é uma pessoa. Se você consegue declarar o objetivo em uma frase. Isso decidiu a qualidade das conversas da IA.

#### O desejo do cliente tem prioridade sobre a recomendação do estabelecimento

Houve ainda uma cena em que tracei uma linha importante.

Durante os testes, encontrei um problema: todas as reservas estavam sendo encaminhadas para o plano mais barato. Quando corrigi, desta vez quase todas viraram o plano Padrão, e o valor total médio saltou para cerca do dobro. Fiquei quase contente, mas, olhando de perto, a IA que fazia o papel do cliente simplesmente apertava toda vez a primeira opção. Até clientes que diziam "o mais barato está ótimo" recebiam a recomendação do Padrão.

Aqui estabeleci um princípio. O que o cliente declara claramente como desejo (a opção mais barata, um orçamento, o nome de um plano) sempre tem prioridade sobre a recomendação do estabelecimento. A recomendação do estabelecimento é só para quando o cliente não disse nada.

O objetivo do estabelecimento de aumentar o faturamento e a confiança do cliente podem colidir numa única forma de recomendar. Se a confiança se perde, as próprias visitas diminuem. Quem podia traçar essa linha era a pessoa que comanda o bar, não a IA.

Mais tarde, quando retreinei o T-AI-MURO com um grande número de perguntas, a causa mais comum de erros era "reagir a palavras e fazer um movimento fixo antes de responder à pergunta". No instante em que ouvia palavras como "número de pessoas", "quanto custa" ou "sozinho", pulava a pergunta e ia para o fluxo de reserva ou para as recomendações. Em termos de atendimento, é um atendente que empurra a venda sem escutar o cliente. Responder primeiro à pergunta do cliente. Esse básico da hospitalidade foi o maior desafio até para a IA.

Na noite de 6 de outubro de 2026, o T-AI-MURO apareceu no topo do site de reservas como a porta de entrada de verdade. Como alguns clientes não querem reservar por conversa, mantive ao lado o formulário de reserva anterior.

> Experimente: abra o site de reservas do Tamuro (https://tamuroreservation.vercel.app/?src=b2-pt-{{FMT}}) e pergunte ao T-AI-MURO "sozinho hoje à noite". A conversa leva você até a disponibilidade e os preços de hoje.

【Figura 1-4】A tela de conversa do T-AI-MURO. A conversa avança só tocando nas opções *(A tela está em japonês.)*

【Figura 1-10】As perguntas que ele não soube responder se acumulam na tela de administração (dados fictícios) *(A tela está em japonês.)*

### 1-9 E então, a partir da IA do cliente

Ao construir o T-AI-MURO, o site de reservas do Tamuro ganhou a capacidade de "responder em conversa a perguntas sobre o estabelecimento, mostrar preços e horários livres e guiar as pessoas até a reserva".

O que pensei em seguida foi tornar possível fazer a mesma coisa a partir da própria IA dos clientes.

O T-AI-MURO só consegue conversar com quem vai ao site de reservas do Tamuro. Mas muita gente consulta primeiro a IA que usa todo dia. Se essa IA não conhece o Tamuro, o Tamuro nem entra na lista de candidatos. Em vez de esperar que os clientes venham ao site do Tamuro, abrir a janela do Tamuro do lado da IA do cliente. Esse é o servidor MCP.

Para ser honesto, hesitei no começo em construir isso. Neste momento, não são muitas as pessoas que reservam restaurantes pela própria IA. Julgando que não podia esperar um aumento direto de reservas, cheguei a baixar a prioridade e deixá-lo em espera.

Decidi construí-lo mesmo assim porque achei que era só questão de tempo até a porta de entrada mudar. Como escrevi no começo, em agosto de 2026 passou a ser possível fazer reservas pelo ChatGPT por meio de um grande serviço de reservas. Mais cedo ou mais tarde, pedir à IA que encontre um restaurante será o normal. Quando isso acontecer, os pequenos estabelecimentos que não estão listados nos grandes serviços sairão do campo de visão da IA. Então, abrir a janela antes que a porta de entrada mude.

O que decidi para a primeira versão era bem restrito. Bastava fazer o mesmo que a janela de conversa do site de reservas (o T-AI-MURO). Tudo o que ele faz é ler as informações do estabelecimento, os horários livres e os preços, e entregar a URL de uma página de reserva com as condições preenchidas. A confirmação da reserva é feita pelo próprio cliente na página do Tamuro. A IA do cliente não confirma uma reserva por conta própria. O empurrão final é dado por uma pessoa.

Voltemos à cena de abertura.

Numa sexta-feira à noite, um cliente pergunta à própria IA: "Em Higashi-Nakano, tem algum lugar onde eu possa tomar uma sozinha hoje à noite?" A IA consulta a janela do Tamuro. O sistema de reservas do Tamuro devolve os horários livres de hoje à noite, mais o plano e o preço que combinam com quem vem sozinho. A IA conta ao cliente e oferece uma página de reserva do Tamuro com a data, a hora e o número de pessoas preenchidos.

Tudo o que escrevi neste capítulo sustenta essa sequência de passos. O sistema de descontos construído junto com o aumento de preços. O sistema que cultiva a clientela fiel. Os dados que mostraram que a maioria das reservas é feita no dia. O conhecimento do estabelecimento que cresceu ao responder a 11 perguntas com uma linha cada. O princípio de pôr o desejo do cliente à frente da recomendação do estabelecimento.

Um estabelecimento que recebe reservas por meio da IA não foi construído da noite para o dia. Ele se apoia no acúmulo de pequenos sistemas acrescentados um de cada vez, testados, descartados e corrigidos.

> Experimente: registre o servidor MCP do Tamuro (https://tamuroreservation.vercel.app/api/mcp) na sua própria IA e pergunte: "Tem mesa no Tamuro hoje à noite?" Como registrar está escrito no Posfácio.

### 1-10 O que construímos e o que funcionou

Neste capítulo, falei sobre a construção de muitos sistemas. Mas "conseguimos construir" e "o negócio mudou" são coisas diferentes. No final do capítulo, vou separar as duas.

O que pôde ser confirmado com números. Que 88,1% das reservas são para o mesmo dia. Que a taxa de aprovação da janela de conversa subiu de 9 para 24 só por acrescentar 11 itens de fatos do estabelecimento. Que a taxa de aprovação da orientação sobre preços e planos subiu de 29,4% para 42,7% depois das correções. São fatos registrados.

O que parece estar funcionando, mas cuja causalidade não consigo provar. Que mais clientes vêm em grupo usando o desconto para grupos. Que o plano de primeira vez e de boas-vindas de volta está sendo escolhido. Que o assunto do e-mail de confirmação virou parte da conversa no balcão. Sinto isso no salão, mas não posso dizer "eles não teriam vindo sem esse sistema".

O que foi construído, mas cujo efeito ainda não conheço. Quantas reservas antecipadas a mais o desconto por reserva antecipada vai trazer. Quantas reservas realmente chegarão pelo MCP. Acabei de começar a medir com o relatório semanal, e os números virão depois.

Olhe separadamente para o espanto de "conseguimos construir tanto com a IA" e para o resultado de "como isso mudou o negócio". Sem essa distinção, o próprio ato de construir vira o objetivo. Eu mesmo quase caí nisso uma vez (como escrevi em 1-7).

A história do que há por trás desse sistema de reservas, a tecnologia, continua no Capítulo 2. Se tecnologia não interessa a você, pule para o Capítulo 3. Lá conto como as pequenas ferramentas nascidas em torno desse sistema de reservas estão sendo oferecidas também a outros estabelecimentos.

## Capítulo 2: Tecnologia - Por Trás do Sistema de Reservas

Pontos principais deste capítulo

- A qualidade das conversas da IA foi decidida menos pela esperteza da IA do que pelos "fatos do estabelecimento que entregamos" e por "um programa sobrescrever por conta própria as respostas da IA"
- O sistema de reservas que construí no feeling ainda tinha uma brecha que deixava os dados pessoais dos clientes serem lidos de fora, e zero testes automatizados. Pedi à IA que auditasse para encontrar isso e pedi à IA que corrigisse
- Dessa reflexão, mudei a forma de construir: definir os requisitos em detalhe antes de construir e entregar à IA a própria especificação para implementar

(Este capítulo tem muitos termos técnicos. Se tecnologia não interessa a você, pode pular para o Capítulo 3 e você acompanha a história sem problemas.)

### 2-1 Como funciona o servidor MCP