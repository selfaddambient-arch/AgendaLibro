Então construí uma entrada que emite contas sintéticas (personas) utilizáveis apenas no ambiente de teste. Ela não funciona em produção. O banco de dados do ambiente de teste é um projeto separado da produção e contém apenas dados sintéticos. A IA entra por essa porta, opera as telas e confirma que as coisas funcionam. As contas de teste são recriadas todos os dias, e as antigas são apagadas.

Com isso, a IA consegue fazer sozinha até a verificação final, em um ambiente montado exatamente como a produção, sem tocar na produção.

### 4-4 A navegação comum e o fracasso da expressão "porta de entrada"

Para que as pessoas consigam ir de qualquer produto aos outros, dei a todos os produtos um menu de navegação compartilhado. É o caminho que permite a quem tem um bar e usa o Livro de Ponto tirar uma dúvida no Guia de Suporte ou ir ver os outros cadernos.

Por trás dessa navegação compartilhada há uma pequena história de fracasso.

Na primeira versão, eu havia colocado um link que dizia "Voltar à porta de entrada". Isso porque, internamente, eu chamava o AgendaHub de "porta de entrada". Mas, quando conferi em um aparelho de verdade, havia algo errado. Dois links, "Voltar à porta de entrada" e "Ver a série Agenda", levavam ao mesmo lugar. Além disso, o link de suporte ficava acima do menu do trabalho do dia a dia, de modo que a ordem de importância estava invertida. E, acima de tudo, as palavras "porta de entrada" não significam nada para quem está usando o produto pela primeira vez. Era a linguagem interna de quem faz.

Então refiz os princípios. Ordene os itens pela proximidade com o objetivo de quem usa: o trabalho do dia a dia no topo e os links que levam para fora na parte mais baixa. Mesmo um link feito para conquistar novas pessoas nunca fica acima do trabalho. A fronteira deve poder ser explicada em uma única linha. Escreva os textos na linguagem de quem usa, não na linguagem interna. Nunca coloque mais de um link que leve ao mesmo lugar. Descartei o "Voltar à porta de entrada" e reuni tudo em um único link, "Ver os outros cadernos da série Agenda".

No Capítulo 2, escrevi sobre aprender a linguagem da interface. Aquela era a linguagem para quem administra usar ao falar com a IA. Esta é o oposto: a linguagem que quem faz usa para falar com quem usa. Nos dois casos, tratava-se de ajustar as palavras a quem está do outro lado.

【Figura 4-4】A navegação compartilhada depois da correção. O trabalho fica no topo, e os links que levam para fora ficam na parte mais baixa *(A tela está em japonês.)*

### 4-5 A base custa US$ 35 por mês

O custo de banco de dados de toda a base descrita neste capítulo é de cerca de US$ 35 por mês. O plano pago que inclui o projeto de produção custa US$ 25, e o projeto do ambiente de teste, US$ 10.

Isso também não foi o valor desde o início. Em certo momento eu pagava US$ 45 por mês. O banco de dados de desenvolvimento de um produto de reconhecimento facial continuava sendo cobrado mesmo sem eu usá-lo. Passei-o para o plano gratuito e o pausei, apaguei outro projeto que eu não usava, e foi assim que se chegou ao valor atual.

Também fico de olho no custo da IA. O trabalho da IA que escreve programas é cobrado pela quantidade de tokens (a unidade de texto que a IA lê e escreve). Evito concentrar custos fazendo a janela de trabalho se limitar ao papel de coordenação e deixando a implementação em si para outra IA, com uma cota de custo separada. Para o modelo generativo da janela de chat, também olho o preço e escolho o necessário e suficiente. Mesmo que um modelo de nível superior custe só US$ 1 a mais por mês, escolho perguntando "isso basta?"

Se você constrói pequeno, mesmo vendas pequenas sustentam. A história da monetização no Capítulo 3 se apoia no quanto o custo dessa base é pequeno.

### 4-6 A IA de coordenação e a pessoa que decide

Por fim, vou descrever o formato do meu dia de trabalho.

Mantenho várias janelas de trabalho de IA abertas ao mesmo tempo. Há uma janela para o sistema de reservas, uma janela para cada produto e uma janela de coordenação que envia instruções a elas e reúne os resultados. Dei à janela de coordenação o nome AgendaRegia (o caderno de coordenação).

Quem toma as decisões, isto é, define "para que lado ir", sou eu e a IA do lado do chat. A IA do lado do chat encontra com antecedência lacunas e contradições nas especificações, anexa a cada uma uma decisão padrão e propõe tudo de uma vez. Eu leio e decido. O que foi decidido é reunido em uma folha de instruções chamada Goal e colado na janela de trabalho. Ela inclui aprovações antecipadas e condições de aprovação que uma máquina pode julgar. A janela de trabalho lê, segue até o fim e para somente quando algo falha.

Também faço a folha de instruções incluir uma estimativa de quando o trabalho estará pronto. Encaixo esse trabalho entre os horários de funcionamento do bar, então, se não sei quanto tempo algo vai levar, não consigo planejar meu dia.

O papel de quem administra não é ler, mas decidir. Não preciso ler todos os 1.775 registros de conversa. Respondo a perguntas sobre fatos do bar. Decido sobre o que só a política do bar pode definir. Depois que algo entra no ar, eu mesmo mexo cinco ou seis vezes para ver se alguma coisa parece estranha. É só isso.

Antes de chegar a esse formato, refiz o trabalho muitas vezes. A IA acrescentava recursos por conta própria e as telas ficavam instáveis. O trabalho crescia sem limite a partir de uma única instrução. Esperar aprovação a cada etapa fazia com que nada andasse. A cada vez, acrescentei uma regra, e foi assim que se chegou ao formato atual. Isso também ainda está crescendo.

#### O que você pode levar deste capítulo

- Para o trabalho repetido, transforme o próprio procedimento em um documento e entregue à IA. Se você corrigir o manual a cada falha, da próxima vez fica mais fácil
- Construa as partes comuns (login, cobrança, navegação) uma só vez e reaproveite em todos os produtos. Se a base é pequena, mesmo vendas pequenas sustentam
- Os humanos fazem apenas o julgamento e as operações que só pessoas podem fazer. Se a IA passar qualquer outra coisa para você, acrescente ao manual

A continuação deste capítulo (os próximos cadernos que vou construir e as lições que acrescentei ao manual) está no note e no X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Capítulo 5: O futuro de um bar pequeno

### 5-1 Do Zatta Gohan ao Tamuro

Entrei no ramo de comidas e bebidas aos 39 anos.

O gatilho foi um bar de bairro chamado Zatta. Uma vez por mês, às vezes a cada duas semanas, deixavam-me servir refeições lá. Eu havia aprendido a cozinhar por conta própria durante muito tempo, mas agora tinha um lugar onde as pessoas comiam a minha comida e ficavam felizes. Essa foi a minha experiência original.

Em 2014, abri um restaurante chamado Zatta Gohan em Arai-Yakushi. Era um lugar pequeno que servia refeições completas do dia a dia, no formato de prato-feito (teishoku). Toquei por sete anos.

Em Arai-Yakushi, porém, senti um limite no número de clientes. Então encontrei um imóvel em Higashi-Nakano. Leva menos de um minuto a pé da saída leste da estação. Mesmo em dia de chuva, dá para chegar sem se molhar muito.

Em novembro de 2018, abri ali o Tamuro. "Tamuro" significa um lugar onde as pessoas se reúnem. Tem 11 lugares no balcão e 8 lugares no tatame, 19 no total. Durante três anos toquei dois lugares em paralelo, Arai-Yakushi e Higashi-Nakano. No período da covid, manter os dois ficou difícil, então fechei o estabelecimento de Arai-Yakushi e fiquei só com o Tamuro.

#### O bar de curadoria

O Tamuro se apresenta como um "bar de curadoria".

Curadoria significa ter um olhar criterioso. Antes de cozinhar, quero fazer curadoria. A comida, as bebidas, o clima do bar: faço tudo selecionando com um olhar criterioso. Isso é o Tamuro.

Viajo muitas vezes para comer, tanto no exterior quanto no Japão. Vietnã, Camboja, Itália, Xangai, Pequim, México. Sair comendo pelo caminho é um prazer e, ao mesmo tempo, um jeito de encontrar o que servir no Tamuro. Recrio ingredientes caros com ingredientes ao alcance da mão. Por exemplo, se você seca gema de ovo e a rala, obtém um sabor próximo ao da bottarga. Penso nesse tipo de substituição (localização) como o meu papel.

Estudei culinária de novo durante a covid. Fiz um curso de culinária francesa de oito aulas no total e também frequentei um curso de culinária japonesa. O uso do umami e o controle do fogo. O que aprendi ali é a base da minha cozinha de hoje.

O cardápio do Tamuro é composto por quatro entradas e um prato principal. Dou a ele uma variedade de ingredientes para que quem mora sozinho consiga comer bastante verdura. Monto de modo que os modos de preparo (frito, em conserva de vinagre, cozido, grelhado) e os sabores (doce, picante, azedo) não se repitam. O prato mais popular é o tonteki, bife de porco. Tem um molho levemente adocicado, feito com shoyu de Kyushu, com bastante alho.

#### Um lugar onde as pessoas se reúnem

Cerca de metade da clientela do Tamuro vem sozinha. São principalmente pessoas de 30 a 50 anos, e muitas são vizinhas de Higashi-Nakano, mas também vêm pessoas de Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo e Eifukucho. 

O que distingue o bar é o quanto a clientela conversa entre si. Montei o balcão de modo que seja fácil falar com a pessoa ao lado, e eu ou a equipe decidimos os lugares avaliando quem vai se dar bem. Quem veio sozinho às vezes volta depois acompanhado. Como o nome diz, virou um lugar onde as pessoas se reúnem. Publico como são os dias do bar no [Instagram](https://www.instagram.com/tamuro.higashinakano/).

No jantar de menu degustação, realizado cerca de uma vez por mês, sirvo de sete a oito pratos ao longo de duas a três horas, junto com harmonização de vinhos. A cada mês o tema muda: italiano, francês, japonês. As aulas de culinária são oficinas de três horas, e, depois de cozinhar, todo mundo brinda, come e vai embora. Há o aperitivo, que serve vinho e petiscos no início da noite, antes da abertura. Há um churrasco cerca de duas vezes por ano. Há uma confraternização de fim de ano uma vez por ano. E há a festa de yukata que descrevi no Capítulo 1.

O sistema de reservas sobre o qual escrevi no Capítulo 1, a janela de chat e o MCP são todos ferramentas para trazer gente a este bar. A IA é um meio de reunir pessoas, não o objetivo.

### 5-2 O curry com bife de hambúrguer do Quatre Épices

O Tamuro é um bar noturno. De dia, o espaço fica vazio.

Aproveitando esse tempo, comecei o Quatre Épices em janeiro de 2024. É uma casa de curry com bife de hambúrguer estilo japonês que funciona só na hora do almoço, no mesmo local, e é tocada pela equipe.

Quatre Épices significa "quatro especiarias" em francês. Fiel ao nome, em vez de empilhar muitas especiarias, escolhemos e reduzimos para deixar nítido o contorno do sabor. O curry não usa farinha; é finalizado com a consistência natural dos próprios legumes e da carne. Satisfação ao terminar de comer, e nenhum peso no estômago. E harmonia com o bife de hambúrguer. Projetei com base nessas três premissas.

Somos criteriosos com o ponto e o controle do fogo do bife de hambúrguer. Definimos a mistura para que saia crocante por fora e macio por dentro, e cozinhamos de acordo com essa mistura. O modo de cozinhar com o calor que aprendi à noite no Tamuro serve também ao prato do dia.

Preços, dias e horários de funcionamento podem mudar, então consulte o Instagram do Tamuro (https://www.instagram.com/tamuro.higashinakano/) para as informações mais recentes.

O Quatre Épices também mantém, no mesmo local, uma refeição comunitária para crianças (kodomo shokudo). É uma atividade que usa as instalações e as compras do bar já existente para servir refeições às crianças do bairro. Por meio dessa ligação, construímos também uma relação com o centro comunitário local. Às vezes servimos curry e sanduíches em eventos esportivos locais, eventos do centro comunitário e festivais de Bon Odori.

Para falar a verdade, aproveitar o horário diurno nem sempre deu certo. Criei dias de bebida durante o dia e aluguei o espaço a outras pessoas, mas a clientela não veio como eu esperava. O encanto do bar chega de maneira diferente quando eu estou lá à noite e quando só a equipe do dia está. Fazer crescer o estabelecimento diurno com um atrativo diferente do noturno ainda é uma tarefa inacabada.

### 5-3 Bonta LLC: dois pilares

A pequena empresa que toca o Tamuro e o Quatre Épices é a Bonta LLC. Respondo pela administração.

A empresa tem dois pilares. Um é comida e bebida: o Tamuro e o Quatre Épices. O outro é TI: o desenvolvimento da série Agenda e a consultoria.

Comida e bebida e ferramentas se diferenciam no modo de gerar receita. Sustentar a empresa com dois pilares de natureza diferente é o formato que tenho em mente.

E os dois pilares se abastecem de material. Um problema no bar vira semente de uma ferramenta. O que aprendo construindo ferramentas volta para a operação do bar. O Caderno de Luzes nasceu do fechamento que atrasava, e os registros de horário prorrogado do Caderno de Luzes viram base para estimativas de lucro e escalas. As "perguntas que não conseguimos responder", que se acumulam na janela de chat, melhoram o atendimento do bar. Esse ciclo é o motivo de eu conseguir cuidar sem ajuda tanto do bar quanto do desenvolvimento.

Não penso em tornar a empresa maior. Pequeno, variado e barato. Esse é o formato desta empresa.

### 5-4 Escrevendo como Raku Bonta

Quando escrevo e publico, uso o pseudônimo "Raku Bonta". Escrevi este livro também com esse nome.

Meu livro anterior, *Subgerente de IA*, era um livro sobre IA generativa. Ficou em primeiro lugar na categoria de gestão do tempo da Amazon e foi lido por muita gente. Este livro é a sequência.

Além de livros, também escrevo no note. Escrevo sobre as iniciativas do bar com IA, o que descobri em uma viagem de aprendizado, o andamento da publicação dos meus livros e a série Agenda. Você pode acompanhar no note (https://note.com/bontallc) a continuação que não coube neste livro.

Para mim, escrever é também um modo de colocar em palavras o bar e o desenvolvimento e conferi-los. Como escrevi no Capítulo 1, o primeiro conhecimento da janela de chat "T-AI-MURO" foi construído a partir de palavras que eu vinha deixando no X. O que eu havia escrito virou material para a IA. Daqui para a frente, o que escrevo também voltará tanto para o bar quanto para a IA.

Há mais uma coisa que decidi sobre escrever. Não anuncio coisas inacabadas com "em breve". Termino, faço uma página de apresentação e só então publico. Acredito que manter essa ordem é o que faz uma empresa pequena merecer confiança.

### 5-5 O futuro do estabelecimento independente

Por fim, vou reunir em um único quadro o que escrevi neste livro.

【Figura 5-1】O quadro geral do que este livro descreveu. Um bar pequeno abre a própria janela (a primeira história) e transforma seus problemas em ferramentas para entregar a outros bares (a segunda história) *(A tela está em japonês.)*

A clientela passará a pedir à própria IA que encontre um bar e faça a reserva. Em agosto de 2026, tornou-se possível reservar restaurantes pelo ChatGPT por meio de um grande serviço de reservas. A porta de entrada está passando dos sites de busca e de avaliação gastronômica para a IA de cada pessoa.

Nesse ponto, um bar que não está listado no grande serviço de reservas fica invisível para a IA. Mas, mesmo sem estar no grande serviço, existe um caminho para um bar se conectar diretamente à IA. O Tamuro escolheu esse caminho abrindo uma janela chamada MCP. Um bar pequeno abrindo por conta própria a sua janela. Essa é a primeira história deste livro.

Quem tem um bar poderá transformar os próprios problemas em ferramentas e distribuí-las a outros bares. O Caderno de Luzes nasceu do problema do Tamuro, de querer avisar que o fechamento ia atrasar, e pode ser usado em qualquer bar. O poder de construir está deixando de ser algo só de certas pessoas ou empresas. Quem tem um bar pequeno passa do lado de quem usa ferramentas para o lado de quem as constrói e distribui. Essa é a segunda história deste livro.

O que as duas têm em comum é que, quanto menor o bar, mais marcante pode ser a sua identidade.

As grandes redes generalizam seus sistemas para que todas as unidades entreguem a mesma qualidade. O Tamuro é o contrário. Quem vem sozinho responde por metade, quase 90% das reservas são feitas no mesmo dia e a clientela conversa entre si. Para se encaixar nesse caráter do Tamuro, construí em detalhes o sistema de reservas, os descontos e a janela de chat. Por não generalizar, é afiado. Por ser afiado, vira um motivo para a clientela escolher.

E, quanto mais afiado o bar, mais sementes de ferramentas ele encontra. Quanto mais você encara o caráter do bar, mais específicos ficam os seus problemas. Problemas específicos viram ferramentas específicas. Ferramentas específicas ajudam outros bares que têm o mesmo problema.

A IA tornou possível que uma única pessoa faça as duas coisas. Afiar o bar e distribuir ferramentas. Antes, era preciso escolher uma ou outra. Agora dá para fazer as duas.

Claro, ainda é um trabalho em andamento. A taxa de aprovação da janela de chat ainda está sendo elevada. O manual recebe um acréscimo a cada falha. Como fazer o estabelecimento diurno crescer continua sendo um desafio. As pessoas que reservam por IA ainda não são muitas.

Mesmo assim, acredito que o futuro do bar pequeno é promissor. Ser pequeno não é uma fraqueza. Por sermos pequenos, podemos testar rápido, abandonar rápido e corrigir rápido. Por sermos pequenos, podemos ser afiados. E os problemas de um bar afiado viram ferramentas e passam para outros bares pequenos.

Escrevi este livro em um bar de 19 lugares em Higashi-Nakano.

## Posfácio

Agradeço por ter lido até aqui.

O que escrevi neste livro é um registro de outubro de 2026. As ferramentas de IA mudam de forma em questão de meses. Alguns dos mecanismos que descrevi podem já ter assumido outra forma quando este livro for publicado. Mesmo assim, escrevi acreditando que o registro do que um bar pequeno construiu com IA e de que modo, onde falhou e o que aprendeu deve continuar útil por algum tempo.

A série Agenda: https://bontallc.com/agenda?via=b2-pt-{{FMT}}

Acompanhe minhas atividades: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Se um dia você passar por Higashi-Nakano, apareça no Tamuro. Dá para reservar pelo site de reservas, pela janela de chat "T-AI-MURO" no site e, claro, pela sua própria IA.

Site de reservas do Tamuro: https://tamuroreservation.vercel.app/?src=b2-pt-{{FMT}}

Instagram do Tamuro: https://www.instagram.com/tamuro.higashinakano/

Para quem quiser experimentar reservar por IA. O endereço de conexão do servidor MCP do Tamuro é o URL a seguir.

https://tamuroreservation.vercel.app/api/mcp

Nas configurações da sua IA (como Claude ou ChatGPT), abra a tela de adição de ferramentas externas (conectores, servidores MCP) e registre este URL. O modo de registrar varia conforme a IA e com o tempo, então o mais seguro é pesquisar "MCP" ou "conector" na ajuda de cada IA. Dependendo do plano que você tem, talvez não seja possível conectar um servidor MCP de sua escolha. Depois de registrado, pergunte à sua IA: "Tem mesa no Tamuro hoje à noite?" Ela vai verificar os horários livres e os preços e conduzir você até a página de reservas. Quem aperta o botão de confirmar é você.

Para quem veio depois de ler o livro. Ao reservar, digite o código de cupom "BOOK". Serviremos uma bebida por conta da casa na sua primeira rodada. Se você veio sem reserva, basta dizer "vi no livro" ao fazer o primeiro pedido. Serviremos a mesma bebida. É um pequeno artifício para eu contar quantas pessoas vieram por causa do livro.

Você pode entrar sem reserva. Mesmo vindo só, você não vai se sentir fora de lugar. Pode até acabar conversando animadamente com a pessoa ao lado.

Estou esperando você em um lugar onde as pessoas se reúnem.

Raku Bonta

### Referências

- OpenAI Help Center, "ChatGPT — Release Notes", 10 de agosto de 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (um exemplo de servidor MCP nos Estados Unidos que permite à IA fazer ordens de compra de ações e outros valores mobiliários) https://docs.alpaca.markets/docs/alpaca-mcp-server
- O debate sobre a "morte do SaaS": as declarações de Satya Nadella no podcast BG2 (dezembro de 2024), a forte queda das ações de software em fevereiro de 2026 e o nome que ela recebeu, e a refutação de Jensen Huang foram extraídos das seguintes reportagens e comentários. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
