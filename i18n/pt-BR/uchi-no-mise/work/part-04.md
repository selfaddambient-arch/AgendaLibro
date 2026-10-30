Também montei um mecanismo que coloca o próprio procedimento em um documento e o entrega à IA. Assim, esse jeito de construir pode ser repetido da mesma forma a cada novo produto que eu lançar. Escreverei sobre isso no Capítulo 4.

【Figura 2-4】Sumário do documento de requisitos do T-AI-MURO (versão 3) *(A tela está em japonês.)*

### 2-6 Aprender a linguagem da interface

Há mais uma coisa que precisei reaprender: os nomes dos componentes de tela.

Mesmo quando eu dizia à IA "faça isso aqui", a tela muitas vezes não saía como eu esperava. Ao pensar na causa, percebi que eu não sabia os nomes dos componentes de tela. Por mais que eu descrevesse "uma janelinha que aparece por cima" ou "um aviso que some depois de alguns segundos", era difícil para a IA entender o que eu queria dizer.

Então li um livro de referência sobre UI (interface do usuário, a aparência e o funcionamento de uma tela) e aprendi os nomes dos componentes e os termos técnicos de design.

| Componente | O que é |
| --- | --- |
| Modal | Uma janelinha que aparece sobre a tela. Você não consegue usar a tela por trás dela até fechá-la |
| Toast | Um aviso que aparece na borda da tela por alguns segundos e some sozinho |
| Aba | Um mecanismo em que, ao tocar em um título, o conteúdo muda |
| Acordeom | Um mecanismo em que, ao tocar em um título, o conteúdo abre e fecha |
| Gaveta (drawer) | Um menu que desliza para fora pela lateral da tela, como uma gaveta |
| Outros | Breadcrumbs (a trilha que mostra onde você está agora), carrosséis (itens que rolam para o lado), bottom sheets (um painel que sobe da parte de baixo da tela) e assim por diante. Cada nome que você aprende permite instruir a IA com uma única expressão |

Quando você se comunica pelos nomes, as telas que a IA produz chegam perto do esperado de primeira. Se você diz "Mostre a tela de confirmação da reserva como um modal", a IA não hesita.

#### A IA vai de um extremo ao outro entre acrescentar e cortar

Mesmo depois de aprender as palavras, construir telas com IA tinha outro tipo de dificuldade. A IA oscila muito.

Quando pedi um cabeçalho "elegante" para o site de reservas, recebi um cabeçalho imponente e alto. Mas o objetivo de um site de reservas é, justamente, reservar. Para a clientela fiel que reserva sempre, um cabeçalho grosso com explicações longas só atrapalha. Mandei reduzir a altura pela metade, mantendo a mesma quantidade de informação.

Quando padronizei o rodapé dos e-mails e acrescentei um link para o Guia da Próxima Parada, o texto do corpo ficou simples e pobre em comparação. Então acrescentei ao corpo também um título, uma tabela com os pontos principais e um botão para tocar. Quando coloquei no rodapé uma entrada para a janela de chat, ficou poluído. Quando comprimi tudo em duas linhas de links separados por filetes, ficou arrumado, mas discreto demais. No fim, a solução foram dois cartões que mostram o papel de cada um por "quando usar". O da esquerda é "para a sua próxima reserva", o da direita é "depois da refeição".

Alto demais, enxuto demais, vistoso demais. O que definia o ponto certo era, a cada vez, a palavra de quem administra o estabelecimento.

#### Uma proposta de design sem imagens

Isso também aconteceu. Pedi à IA que escreve programas que criasse propostas de melhoria para a janela de chat usando uma IA de design (Claude Design), e voltou um relatório dizendo: "Fiz propostas para oito telas." Mas, ao abrir, havia apenas descrição em texto. A IA não tinha conseguido desenhar, e só restou o relatório de "concluído".

No fim, a IA do chat desenhou quatro propostas diretamente na tela de design. Ela pegou as cores da tela atual a partir de uma captura de tela, colocou a história do estabelecimento em uma linha do tempo, dividiu a explicação do sabor em dois quadros, "modo de preparo" e "gosto", transformou os planos em cartões explicativos e unificou os preços em um resumo da reserva.

Quando você pede à IA para rodar um teste, ela diz "passou". Quando você pede um design, ela diz "pronto". Conferir o que há dentro é trabalho de gente. O critério de julgamento é algo que só as pessoas podem continuar mantendo.

#### O que você pode levar deste capítulo

- Construir algo que funciona e conseguir operá-lo com segurança são coisas diferentes.
- Confira o resultado da IA não pelas palavras dela, mas por testes. Um teste só merece confiança depois que você verifica que ele falha quando você quebra algo.
- Cálculos que não podem errar, como preços, não devem ficar a cargo da geração de texto da IA. Entregue-os ao programa.

A continuação deste capítulo (novas falhas encontradas e os passos que dei para corrigi-las) está no note e no X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Capítulo 3: Distribuindo as ferramentas do meu estabelecimento para outros estabelecimentos

### 3-1 A pequena placa verde na página de reservas

Abra a página de reservas do Tamuro e você verá uma pequena placa verde perto do topo. Enquanto o estabelecimento está aberto, ela diz "OPEN", e quando fecha, diz "CLOSED". Quando quem administra aperta o botão de prorrogar, o horário de fechamento se desloca 30 minutos e um toque de vermelhão aparece na placa.

Restaurantes independentes têm um traço em comum. Abrem quase exatamente na hora, mas o fechamento costuma atrasar. Se a conversa com a clientela está animada, as luzes continuam acesas depois do último pedido, às 22h30.

Só que, do lado de quem está de fora, isso não dá para saber. O aviso de "Aberto" no Google Maps é definido apenas pelo horário cadastrado, então não reflete prorrogações, fechamentos antecipados nem folgas temporárias. Ninguém caminha até um estabelecimento depois do horário de fechamento pensando "talvez ainda esteja aberto". Ligar para confirmar também é constrangedor.

Esta placa é uma ferramenta que responde a essa pergunta, "ainda está aberto?". Ela se chama "AgendaLuce (Caderno de Luzes)". Luce significa "luz" em italiano.

O Caderno de Luzes foi feito para funcionar quase sem atenção de quem administra. Cadastre uma vez os horários de abertura e fechamento de cada dia da semana, e a placa liga e desliga sozinha. A pessoa só mexe nela para prorrogar, fechar mais cedo ou tirar um dia de folga. Para prorrogar, basta apertar um botão no celular. A equipe também pode operar a placa por um link exclusivo que funciona sem login.

A clientela não precisa de login nem de cadastro. Abra a página pública e você vê o estado atual da luz. Se você a adicionar à tela inicial do celular, ela funciona como um aplicativo. O componente da pequena placa também pode ser incorporado a outros sites. O que aparece na página de reservas do Tamuro é esse componente.

O Caderno de Luzes é gratuito. Se você só incorporar o componente da placa ao seu site, a configuração leva cerca de 10 minutos.

E aqui vem o ponto importante. Este Caderno de Luzes não é só para o Tamuro. Qualquer estabelecimento pode usá-lo.

Deixei de propósito o nome do estabelecimento fora do design da placa. Se eu colocasse um nome, ela viraria a placa do Tamuro. Também dá para escolher o idioma de exibição. Fiz o componente pequeno para que possa ser incorporado ao site de qualquer estabelecimento.

Uma ferramenta nascida do problema do Tamuro, "o fechamento atrasa", feita desde o início em um formato que qualquer pessoa possa usar. Esse é o Caderno de Luzes. E o conjunto de ferramentas como ele é a "série Agenda".

【Figura 3-1a】A placa do Caderno de Luzes no topo da página de reservas (aberto) *(A tela está em japonês.)*

【Figura 3-1b】Um toque de vermelhão aparece durante uma prorrogação *(A tela está em japonês.)*

【Figura 3-6a】A tela de quem administra. Para prorrogar, basta apertar o botão uma vez *(A tela está em japonês.)*

【Figura 3-6b】Logo após apertar prorrogar. O horário de fechamento avança 30 minutos *(A tela está em japonês.)*

【Figura 3-6c】A página pública que a clientela vê (durante uma prorrogação) *(A tela está em japonês.)*

### 3-2 Tudo começou com o caderno de couro preto

A série Agenda não foi planejada como série. Ela começou com um único sistema, que ainda nem foi lançado.

O que me propus a construir primeiro foi um mecanismo que reconhece o rosto da clientela e recebe bem quem é habitual. Uma câmera na entrada do estabelecimento distingue quem chega pelo rosto e avisa quem administra: "Essa é a pessoa que pediu tonteki da última vez, a que não víamos há três meses." Eu queria que uma máquina ajudasse no trabalho que quem cuida de um estabelecimento pequeno faz de cabeça: lembrar de rostos, nomes e preferências.

Mas logo depois de começar a construir, percebi que aquele era um sistema que carregava algo muito pesado. Rostos. Atributos. Histórico de visitas. O jeito de cada cliente. Tudo isso é informação que não tem volta depois de vazar.

O que me veio à mente então foi o "Caderno de Couro Preto", de Seicho Matsumoto. Um registro que não se mostra a ninguém, mas que existe com certeza. Um livro-caixa que, uma vez aberto, põe em movimento a vida e a morte das pessoas. Não é exatamente isso que estou tentando construir?

Em italiano, "caderno" é Agenda e "preto" é Nera. Juntando: AgendaNera. O caderno de couro preto. Foi assim que o primeiro nome foi decidido.

O AgendaNera ainda está em construção. É o que estou construindo com mais cuidado na série.

E esse nome foi o gatilho. Se existe um caderno preto, pode haver cadernos de outras cores. Eu reconstruiria os mecanismos que uso todos os dias no meu estabelecimento em formatos que qualquer estabelecimento possa usar, e os lançaria um caderno por vez. Essa é a [série Agenda](https://bontallc.com/agenda?via=b2-pt-{{FMT}}).

### 3-3 Acrescentando cadernos, um de cada vez

A série Agenda é um conjunto de pequenos aplicativos web, cada um respondendo a um problema de restaurante com uma ferramenta. Cada um tem um nome italiano e um apelido em japonês terminado em "caderno". Cada nome tem sua própria origem.

| Nome | Apelido | Origem do nome | O que faz |
| --- | --- | --- | --- |
| AgendaTimbro | Livro de Ponto | Timbro significa "carimbo". É o próprio registro de ponto | Registra a entrada e a saída da equipe |
| AgendaOro | Livro de Lucros | Oro significa "ouro". O caderno do dinheiro | Estima a rentabilidade de abrir um estabelecimento ou de um novo item do cardápio (gratuito) |
| AgendaBis | Guia da Próxima Parada | Bis significa "bis". O "Bis!" gritado pela plateia em um show | Guia a clientela até uma próxima parada nas redondezas (gratuito) |
| AgendaQA | Guia de Suporte | Qua significa "aqui". Se tiver dúvidas ou problemas, é aqui | O balcão de ajuda compartilhado da série (gratuito) |
| AgendaLuce | Caderno de Luzes | Luce significa "luz" | Mostra se o estabelecimento está aberto (gratuito) |
| AgendaRicetta | Livro de Custos | Ricetta significa "receita" | Calcula o custo de uma receita e a proporção de custo (gratuito) |
| AgendaNera | Livro de Clientes Fiéis | Nera significa "preto". O caderno de couro preto | Recebe bem a clientela habitual com reconhecimento facial (em construção) |
| AgendaTurno | Livro de Escalas | Turno em italiano é "vez" ou "turno de trabalho" | Reúne os pedidos de turno da equipe e entrega a escala montada pela própria IA de quem administra (em breve) |

Qual caderno serve para qual tipo de estabelecimento? O Livro de Ponto é para quem tem duas ou mais pessoas na equipe e controla a presença no papel ou no LINE *(o aplicativo de mensagens mais usado no Japão)*. O Livro de Lucros é para quem está prestes a abrir um estabelecimento e para quem quer rever os números porque o aluguel ou os custos mudaram. O Guia da Próxima Parada é para estabelecimentos focados em refeições que querem encaminhar a clientela cedo para o lugar seguinte. O Caderno de Luzes é para estabelecimentos independentes cujo fechamento acontece mais tarde ou mais cedo do que o planejado. O Livro de Custos é para estabelecimentos em que as receitas estão na cabeça, mas nunca se calculou a proporção de custo.

#### O Livro de Ponto não calcula a folha de pagamento

O Livro de Ponto transforma o tablet do estabelecimento ou os celulares da equipe em um relógio de ponto, do jeito que estão. Basta tocar no próprio nome. A folha de presença é somada automaticamente e pode ser exportada em CSV (um formato que abre em programas de planilha). O dia de trabalho começa às 5h da manhã, então, mesmo com expediente de madrugada, a data não vira no meio.

Mas este Livro de Ponto, de propósito, não calcula a folha de pagamento.

Valor da hora, adicionais e datas de fechamento variam demais de um estabelecimento para outro. Madrugada com 25% a mais, feriados em uma categoria à parte, transporte por valor diário. Do jeito que eu construísse, não serviria para o estabelecimento de alguém.

Então, em vez de calcular, preparei "um modelo de instruções para entregar a uma IA". Quem administra cola o CSV de presença baixado e esse modelo, do jeito que estão, na IA que já usa no dia a dia, seja ChatGPT, Claude ou Gemini. Aí a IA calcula adicional noturno, pagamento de feriado e transporte e lista tudo. As regras de cada estabelecimento, como "fechamos as contas no fim do mês, a madrugada tem 25% a mais e os domingos são uma categoria à parte", podem ser acrescentadas ao modelo e serão refletidas do jeito que estão. O CSV inclui colunas com o dia da semana e o nome do feriado para que a IA calcule corretamente.

Eu mesmo não guardo o mecanismo de cálculo; cada estabelecimento mantém suas regras nas próprias mãos. Achei que esse é o jeito mais difícil de quebrar.

#### Guie a clientela até a próxima parada e deixe o seu estabelecimento na memória dela

O Guia da Próxima Parada é uma ferramenta para criar uma "página de guia da próxima parada" para entregar à clientela. A quem terminou a refeição, ela indica um bar ou um lugar para uma última porção por perto, junto com quantos minutos leva a pé.

Parece uma ferramenta para mandar a clientela para outro lugar, mas há um pequeno truque nela. Indicar uma segunda parada implica que a primeira foi o seu estabelecimento. Ao parecer mandar a clientela embora, ela na verdade grava na memória de cada pessoa que "a primeira parada foi este lugar". O desenho é esse.

#### Três princípios de projeto: automático, força emprestada, função única

Todos os cadernos da série Agenda compartilham três princípios.

O primeiro é "automático". Ele deve funcionar sem que quem administra precise mexer todo dia. No Caderno de Luzes, depois de cadastrar o horário, a luz liga e desliga sozinha. Quem cuida de um restaurante não tem tempo de mexer em uma tela durante o serviço. Uma ferramenta que só funciona se você mexe nela acaba, mais cedo ou mais tarde, sem uso.

O segundo é "força emprestada". Não construa tudo por conta própria; deixe com as ferramentas e a IA que a pessoa já usa. A folha de pagamento do Livro de Ponto é o caso-modelo. O caderno de escalas é igual: ele cuida apenas de reunir as preferências da equipe e deixa o trabalho de montar os turnos para a IA de quem administra. Ele não carrega um mecanismo complicado próprio, nem o custo de chamar uma IA. Por isso o preço pode ser mantido baixo.

O terceiro é "função única". Um caderno faz só uma coisa, e a faz com segurança. Um sistema multifuncional é pesado demais para um estabelecimento independente. Se você continua acrescentando recursos, fica mais difícil de usar, e as contradições do lado de quem constrói se multiplicam. Foi o que aprendi na pele com o sistema de reservas, no Capítulo 2. Por isso acrescento cadernos um de cada vez, cada um fazendo "só esta coisa, e bem feita".

#### Por que o sistema de reservas não está na série

Neste ponto, imagino uma pergunta óbvia. O que o Tamuro mais trabalhou foi o sistema de reservas. Por que ele não está na série Agenda?

Na verdade, eu já tive essa intenção. O plano era transformar o sistema de reservas em algo que outros restaurantes pudessem usar e lançá-lo como um caderno da série. Mas, em agosto de 2026, cancelei esse plano.

O motivo é exatamente o que escrevi no Capítulo 1. O sistema de reservas do Tamuro está repleto do jeito de trabalhar do Tamuro. Que quem vem sozinho responde por metade da clientela. Que quase 90% das reservas são feitas no mesmo dia. Que quero vender os horários antes da abertura. Que quero que as pessoas venham em grupo. Que quero criar clientela habitual. Construí as combinações de desconto, a ordem dos e-mails e o jeito de o chat recomendar, tudo para se encaixar nisso.

Se eu o diluísse até virar algo que qualquer um pudesse usar, ele viraria um sistema de reservas comum, que serve mais ou menos para todo estabelecimento. Aí a força do Tamuro desapareceria. O sistema de reservas e o CRM são o jeito de o estabelecimento se vender. Em vez de encaixar o estabelecimento em um sistema genérico, encaixe o sistema no estabelecimento. O nosso estabelecimento, com as nossas especificações. Por isso decidi manter o sistema de reservas do Tamuro só do Tamuro.

Então não há nada para distribuir além do estabelecimento? Há, sim. Em volta do sistema de reservas existem muitos pequenos problemas comuns a todo estabelecimento. Mantenha o núcleo do estabelecimento com as suas próprias especificações. Construa as ferramentas que resolvem os problemas ao redor em um formato que todos possam usar desde o início, e distribua. A página de reservas do Tamuro é um exemplo com as duas coisas lado a lado em uma única tela. Sobre um sistema de reservas só do Tamuro está a placa do Caderno de Luzes, que qualquer pessoa pode usar.

【Figura 3-2】A página de apresentação da série Agenda *(A tela está em japonês.)*

【Figura 3-3a】Apresentação do Livro de Ponto *(A tela está em japonês.)*

【Figura 3-3b】Apresentação do Livro de Lucros *(A tela está em japonês.)*

【Figura 3-3c】Apresentação do Guia da Próxima Parada *(A tela está em japonês.)*

【Figura 3-4】A tela de registro de ponto do Livro de Ponto. Basta tocar no próprio nome (dados fictícios) *(A tela está em japonês.)*

### 3-4 Construir para todos desde o início

Faço uma ferramenta para o meu estabelecimento e depois a distribuo também para outros. Dito assim parece simples, mas, para fazer isso, o jeito de decidir as coisas antes de começar a construir precisa mudar.

Se eu estivesse construindo só para o Tamuro, o caminho mais rápido seria escrever o horário de funcionamento e o nome do Tamuro direto no programa. Mas aí nenhum outro estabelecimento poderia usá-lo. Se você tenta torná-lo genérico depois, acaba caçando cada trecho fixo e corrigindo um por um.

Por isso as ferramentas da série Agenda são especificadas desde o começo na premissa de que todos possam usá-las. Parto de um problema do Tamuro, mas, na etapa de requisitos, separo duas perguntas: "Isso vale só para o Tamuro ou vale para todo estabelecimento?" Não coloque o nome do estabelecimento na placa. Deixe as pessoas escolherem o idioma. Faça de um jeito que possa ser colado em qualquer site. Decisões como essas eu fechei enquanto escrevia o documento de requisitos do Caderno de Luzes.

Este é mais um uso da definição de requisitos que reaprendi no Capítulo 2. Se você decide essas coisas primeiro, pode usar a ferramenta no Tamuro e distribuí-la para outros estabelecimentos do jeito que ela está.

Os problemas do meu estabelecimento também são os problemas de outros. Não sou a única pessoa que quer avisar a clientela de que o fechamento está atrasando. Quem cuida de um estabelecimento independente constrói uma ferramenta a partir do próprio problema e depois a distribui para outros estabelecimentos. Essa é a ideia por trás da série Agenda.

### 3-5 A democratização da tecnologia

A série Agenda já tem mais de 10 produtos. Eu os construo e os opero sem ajuda, enquanto fico atrás do balcão.

Alguns anos atrás, isso seria impensável. Para construir um produto, era preciso alguém para planejar, alguém para desenhar as telas, alguém para escrever o código, alguém para testar e alguém para operar. Sem uma equipe e sem dinheiro, não dava para pôr um produto no mundo.

Isso não é mais verdade. Quem administra conta os requisitos à IA, a IA escreve o código, a IA o testa e outra IA o audita. O que a pessoa faz é decidir o que construir, avaliar se os resultados da IA combinam com a finalidade do estabelecimento e executar apenas as operações que só humanos podem fazer.

Esse tipo de mudança costuma ser chamado de "democratização da tecnologia". O poder de construir deixou de ser propriedade de poucas pessoas ou empresas.

Mas falo com franqueza aqui. Como escrevi na Introdução, trabalhei em TI por cerca de 16 anos, principalmente em planejamento de sistemas e fazendo a ponte entre as pessoas da operação e as empresas de desenvolvimento. Conhecia a definição de requisitos, o raciocínio por trás de bancos de dados e o modo de conduzir testes, tudo por experiência. Portanto, não vou afirmar que alguém que nunca escreveu uma linha de código conseguiria fazer o mesmo a partir de amanhã.
