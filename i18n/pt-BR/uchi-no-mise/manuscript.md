# Feito para o Nosso Bar

Como quem toca um bar de 19 lugares construiu com IA tudo, das reservas às ferramentas

Raku Bonta

A série Agenda: https://bontallc.com/agenda?via=b2-pt-{{FMT}}

Instagram do Tamuro: https://www.instagram.com/tamuro.higashinakano/

Site de reservas do Tamuro: https://tamuroreservation.vercel.app/?src=b2-pt-{{FMT}}

## Introdução

Este livro é um relato simples de como o bar de 19 lugares que administro em Higashi-Nakano *(um bairro residencial a oeste de Tóquio, logo depois de Shinjuku)* funciona com a ajuda da IA.

O bar se chama "Tamuro". O nome quer dizer um lugar onde as pessoas se reúnem. Abriu em novembro de 2018, um espaço pequeno com 11 lugares no balcão e 8 no salão de tatame. De dia, no mesmo espaço, um integrante da equipe toca um restaurante de curry com bife de hambúrguer estilo japonês chamado "Quatre Épices".

No livro anterior, *Subgerente de IA*, escrevi sobre a própria IA generativa. No ano ou pouco mais que passou desde então, a IA deixou de ser uma ferramenta que responde perguntas e virou uma ferramenta que faz o trabalho por você. Você dá uma instrução, e ela escreve o programa, testa, corrige os próprios erros e conclui o serviço. Chamamos esse tipo de IA de IA agêntica.

Com a IA agêntica, eu mesmo construí o sistema de reservas do Tamuro. Construí um sistema de descontos para acompanhar um aumento de preços. Construí um sistema para cultivar a clientela fiel. Construí uma IA que responde às dúvidas de quem vem ao bar. E, por fim, cheguei ao ponto em que um cliente pode fazer uma pergunta ao Tamuro a partir da própria IA e seguir adiante até fazer a reserva.

Também peguei as ferramentas práticas que criei para o meu estabelecimento, ajustei para que outros também pudessem usá-las e comecei a oferecê-las por algumas centenas de ienes por mês. Essa é a série Agenda.

Este livro descreve o que construí no caminho, onde errei e o que precisei reaprender. Não são só histórias de sucesso. Eu continuava construindo coisas que funcionavam, guiado pela intuição, e as contradições se acumularam. Descobri depois que dados pessoais de clientes podiam ser lidos de fora. A IA escreveu informações que o estabelecimento nunca havia declarado. Incluí essas falhas do jeito que aconteceram.

### Como ler este livro

Este livro tem cinco capítulos.

| Capítulo | Conteúdo | Indicado para |
| --- | --- | --- |
| Capítulo 1 | Um estabelecimento que recebe reservas por IA (o lado do negócio no sistema de reservas) | Todo mundo |
| Capítulo 2 | Por trás do sistema de reservas (técnico) | Quem constrói e quem tem curiosidade sobre tecnologia |
| Capítulo 3 | Distribuir as ferramentas do nosso estabelecimento para outros estabelecimentos (o lado do negócio na série Agenda) | Todo mundo |
| Capítulo 4 | Um sistema para construir produtos sem ajuda (técnico) | Quem constrói e quem tem curiosidade sobre tecnologia |
| Capítulo 5 | O futuro dos pequenos estabelecimentos | Todo mundo |

Os capítulos 2 e 4 são técnicos e usam mais termos especializados. Cada um começa com um resumo de três linhas com os pontos principais; se tecnologia não é a sua praia, leia só isso e passe para o capítulo seguinte. Lendo os capítulos 1, 3 e 5 em ordem, a história continua fazendo sentido como uma linha só.

Sempre que pude, coloquei ao lado de cada termo técnico uma explicação em linguagem simples. Mesmo que você nunca tenha escrito um programa, espero que sinta o que significa tocar um estabelecimento com a ajuda da IA.

### Sobre o autor

Trabalhei cerca de 16 anos em TI, principalmente em planejamento de sistemas e como ponte entre o pessoal da operação e as empresas de desenvolvimento, e depois entrei no ramo de comidas e bebidas. Então esta não é a história de alguém que nunca tinha escrito uma linha de código e construiu tudo com IA, sem ajuda. Faço questão de ser honesto quanto a isso.

Mesmo assim, hoje consigo construir e manter, por conta própria e trabalhando no salão, algo de uma escala que antes exigia uma equipe e investimento. Alguns anos atrás, isso seria impensável. Quero descrever a realidade dessa mudança da forma mais concreta que eu puder.

### Como este livro foi feito

Fiz este livro também com a IA. A partir dos registros que guardo do meu trabalho diário de desenvolvimento, a IA escreveu os rascunhos, e eu li, revisei e tomei as decisões. Também pedi à IA que tirasse as capturas de tela usadas como ilustração.

Li tudo, mas texto escrito por IA pode trazer coisas que não são verdade. Como digo no corpo do livro, a IA diz "está pronto", e conferir isso é trabalho de uma pessoa. Pode haver erros neste livro que passaram despercebidos.

Além disso, as especificações das ferramentas e dos serviços de IA mudam em poucos meses. Os passos, os preços e a situação de suporte de cada empresa descritos neste livro são de outubro de 2026. Quando for experimentar por conta própria, confira as informações oficiais da época.

Se você encontrar algum erro, ficarei feliz se me avisar pelo note ou pelo X. Vou corrigindo conforme for descobrindo.

### As três saídas deste livro

Este livro pode ser lido de graça em PDF, no note e no Google Play. (Só no Kindle, as regras da loja exigem um preço mínimo.) Em troca, preparei três lugares aonde você pode ir depois de terminar a leitura. Se pelo menos um deles for útil para você, escrever este livro terá valido a pena.

1. Experimente no seu estabelecimento. Você pode começar a série Agenda com o caderno gratuito. https://bontallc.com/agenda?via=b2-pt-{{FMT}}
2. Acompanhe o que eu faço. No note e no X, escrevo sobre as próximas ferramentas que construo e sobre o dia a dia do estabelecimento. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Se algum dia você estiver em Tóquio, visite o Tamuro. A um minuto da saída leste da estação de Higashi-Nakano. Pode entrar sem reserva. Site de reservas https://tamuroreservation.vercel.app/?src=b2-pt-{{FMT}}

## Capítulo 1: Um Estabelecimento que a IA Reserva

### 1-1 A era de perguntar à IA: "Tem algum lugar aberto hoje à noite?"

Numa sexta-feira à noite, alguém que acabou de sair do trabalho fala com o celular.

"Em Higashi-Nakano, tem algum lugar onde eu possa tomar uma sozinha hoje à noite? Algum lugar que não seja muito barulhento."

Quem responde não é um amigo. É a IA que essa pessoa usa todo dia. A IA lista os estabelecimentos candidatos, descreve o clima de cada um e informa os horários livres e os preços de hoje à noite. Se algo chama a atenção, a pessoa pode ir direto para a tela de reserva.

Isso não é uma história sobre o futuro.

Em 10 de agosto de 2026, a OpenAI incluiu um recurso de reserva de restaurantes no ChatGPT. Segundo as notas de lançamento oficiais, ele se conecta aos serviços de reserva OpenTable, Resy e Yelp, e os horários disponíveis aparecem diretamente nas respostas do ChatGPT. Também é possível fazer perguntas para restringir as opções e, depois de escolher um horário conveniente, seguir direto para a reserva. Cobre a OpenTable no mundo todo, a Resy nos Estados Unidos e a Yelp nos Estados Unidos e no Canadá.

Ou seja, a porta de entrada que as pessoas usam para escolher onde comer está começando a sair dos mecanismos de busca e dos sites de avaliação de restaurantes e a ir para "a minha própria IA".

Mas há uma condição. Os únicos estabelecimentos que dá para reservar pelo ChatGPT são os cadastrados nos grandes serviços de reserva. Os pequenos que não estão listados lá ficam invisíveis para a IA.

Então o que deve fazer um bar de 19 lugares em Higashi-Nakano que não usa os grandes serviços de reserva?

O Tamuro escolheu outro caminho. Sem passar pelos grandes serviços, conectou o próprio sistema de reservas diretamente à IA.

Quando um cliente pergunta ao seu próprio ChatGPT ou Claude "Tem mesa no Tamuro hoje à noite?", a IA consulta diretamente o sistema de reservas do Tamuro, confere os horários livres e os preços, e responde. Estabelecidas as condições, ela leva o cliente à página de reservas do Tamuro com o número de pessoas e a data e a hora já preenchidos. É o próprio cliente quem aperta o botão final de confirmação.

Esse "ponto de conexão entre a IA e o sistema de um estabelecimento" se chama servidor MCP. MCP é a sigla de Model Context Protocol, um conjunto comum de acordos que permite à IA usar ferramentas e dados externos. Explico os detalhes no Capítulo 2.

Os grandes serviços de reserva, aliás, também passam o cliente para as próprias telas no final. Nas reservas que exigem cartão de crédito, o processo termina na tela da OpenTable, e as mudanças ou cancelamentos depois da reserva são tratados no lado de cada serviço. A IA é a porta de entrada, e a tela do serviço de reservas é onde se confirma. O que o Tamuro faz tem a mesma estrutura. A única diferença é que nenhuma grande empresa fica no meio.

E quem construiu esse sistema não foi uma empresa de desenvolvimento de fora. Fui eu mesmo, quem toca o bar. Dei as instruções à IA, pedi que ela escrevesse os programas e pedi que ela rodasse os testes.

Claro que não cheguei aqui de uma vez. Começou com um formulário de reserva bem simples. Depois veio um aumento de preços, depois ideias de descontos, depois um sistema para cultivar a clientela fiel, depois falhas e reconstrução.

Primeiro, deixe-me descrever em cinco linhas que tipo de lugar é o Tamuro. A um minuto a pé da saída leste da estação de Higashi-Nakano. 19 lugares, 11 no balcão e 8 no salão de tatame. Cerca de metade da clientela vem sozinha, e o balcão facilita puxar conversa com a pessoa do lado. A comida é uma combinação de quatro entradas e um prato principal, e o prato mais popular é um tonteki (bife de porco) adocicado e com alho. Os vinhos são principalmente da Espanha e da Itália, e há cerca de 20 tipos de gin artesanal japonês. Pode entrar sem reserva.

Quero dizer também uma coisa que eu buscava. Não queria apenas receber reservas. Queria que até um pequeno estabelecimento pudesse construir com as próprias mãos todo o fluxo de ser conhecido, atrair visitas e fazer as pessoas voltarem. Os descontos, os e-mails e a janela de chat que aparecem neste capítulo são todos peças a serviço desse único objetivo.

Neste capítulo, volto no tempo e acompanho como o sistema de reservas do Tamuro cresceu.

【Figura 1-1】A tela depois de conectar o ChatGPT ao servidor MCP do Tamuro (10 de outubro de 2026). Ele lê as informações do estabelecimento e responde que consegue tratar de horários livres, menus fechados, preços e direcionamento para a página de reservas *(A tela está em japonês.)*

### 1-2 O ponto de partida: apenas receber reservas

[O site de reservas do Tamuro](https://tamuroreservation.vercel.app/?src=b2-pt-{{FMT}}) era muito simples no começo. Escolher data, horário e número de pessoas, informar nome e contato, e enviar. Uma notificação chega ao estabelecimento. Só isso.

Construí a primeira base com a ferramenta de desenvolvimento com IA do Google (Antigravity). Contei à IA cada função em que pensava e, quando funcionava, passava para a próxima. É o que se chama de vibe coding (dizer à IA o que vier à cabeça e deixar que ela construa no feeling).

Para mim, na época, era uma surpresa atrás da outra. Descreva o layout de uma tela com palavras, e ela ganha forma em minutos. Diga que quer um calendário, e um calendário aparece. Nos intervalos do trabalho no estabelecimento, um site de reservas foi tomando forma.

O Tamuro é um lugar onde se pode entrar sem reserva. Na verdade, a maioria das reservas é feita no mesmo dia, e muita gente simplesmente chega. Mesmo assim, construí um sistema de reservas porque queria um jeito de me conectar com os clientes antes da visita. Uma vez que a pessoa reserva, o nome e o contato ficam registrados. Com o contato registrado, posso convidar a pessoa a voltar.

Um sistema de reservas não é só uma recepção. Ele se torna a porta de entrada para um relacionamento com o cliente. Essa ideia levou, mais tarde, ao sistema de descontos e ao sistema para cultivar a clientela fiel.

Mas uma base construída na intuição me custou caro depois. Vou escrever sobre isso no Capítulo 2.

### 1-3 Construindo juntos um aumento de preços e os descontos

Para um restaurante ou um bar, o aumento de preços é uma decisão inevitável. Ingredientes, contas de consumo e mão de obra continuam ficando mais caros. O Tamuro também aumentou os preços. Aumentei cada menu fechado em cerca de ¥400–¥500 (cerca de US$ 2,7–US$ 3,3).

O aumento era grande, então era óbvio que, se eu o divulgasse assim, a clientela fiel se afastaria. Por isso, ao mesmo tempo que o aumento de preços, decidi incluir um sistema de descontos no sistema de reservas. Ele não serve só para baratear. Ele recompensa com descontos os clientes que agem de maneira boa para o estabelecimento.

O primeiro é o desconto para grupos. Quanto mais gente no grupo, menor o preço por pessoa. Cerca de metade da clientela do Tamuro vem sozinha, mas, se vierem em grupos, o faturamento cresce bastante. Mesmo subtraindo o desconto, o estabelecimento sai ganhando. Para os clientes, também é um motivo para chamar amigos. De fato, aumentou o número de clientes que vêm em grupo usando o desconto por número de pessoas do site de reservas.

O segundo é o desconto para quem reserva com antecedência. Reservando com até uma semana de antecedência, 2% de desconto; com até duas semanas, 4%. A maior parte das reservas do Tamuro é feita no mesmo dia, então não consigo prever o que vem pela frente. O desconto antecipado é um mecanismo para garantir faturamento futuro. Em dias de chuva e dias de frio, se já há reservas, o estabelecimento pode se preparar com tranquilidade.

Em terceiro lugar, construí também um mecanismo de compra coletiva. Se um número definido de pessoas se reunisse em data e hora definidas, um menu fechado seria oferecido com desconto. A ideia era um mecanismo com o espírito do Tamuro, em que desconhecidos se reúnem ao mesmo tempo.

Mas o plano de compra coletiva não foi usado nem uma vez. Zero resultados. Em agosto de 2026, encerrei esse plano e decidi não usá-lo mais.

Jogar fora algo que você fez dá a sensação de desperdício. Mas, se você constrói com IA, o custo e o tempo de construir são pequenos. Construa pequeno, experimente e, se não funcionar, jogue fora. Acredito que essa velocidade é a maior vantagem de tocar um estabelecimento com IA.

Há mais um truque na definição de preços. Entre os planos, coloco de propósito um plano premium caro. Não tem problema se quase ninguém escolher o plano premium. Com um plano caro ao lado, o padrão parece acessível. Ele faz o papel do que se chama de âncora (um ponto de referência para comparação).

【Figura 1-7】Quanto mais gente, menor o preço por pessoa (comparação entre 1, 4 e 6 pessoas)

### 1-4 Um sistema para cultivar a clientela fiel

Depois que nomes e contatos ficam registrados no sistema de reservas, a próxima coisa que se quer fazer é cultivar o relacionamento com os clientes. Um sistema que gerencia as informações dos clientes e aprofunda os relacionamentos se chama CRM (gestão de relacionamento com o cliente). Aos poucos, fui acrescentando recursos de CRM ao sistema de reservas do Tamuro.

Quando os clientes se cadastram como membros, podem ver o histórico de reservas na área Minha Conta. Se registram o aniversário, chega um mimo de aniversário. Membros que não aparecem há algum tempo recebem uma mensagem chamando de volta. Também há um cartão de carimbos. Três visitas valem uma bebida, cinco valem um bife e outros mimos, e depois de chegar a cinco a contagem recomeça. Também há um recurso para indicar amigos.

Projetei com atenção especial o mecanismo para convidar a uma segunda visita. Em restaurantes e bares, diz-se que o fato de um cliente novo voltar uma segunda vez decide se ele vai se tornar fiel. No Tamuro, envio dois e-mails de convite, sete dias e 21 dias depois da primeira visita. O primeiro não tem cupom; só o segundo tem. Em vez de atrair com desconto desde o início, primeiro ajudo a pessoa a se lembrar. Se mesmo assim ela não vier, dou um empurrãozinho.

Também tomei cuidado para que os e-mails não se acumulassem. Os clientes recebem no máximo uma mensagem por dia. Quando há sobreposição, a prioridade segue esta ordem: aniversário, convite para a segunda visita, chamada de volta a membros afastados, outros avisos. Membros que já têm a próxima reserva não recebem e-mails convidando a visitar.

O consentimento para receber e-mails vem desativado por padrão. Deixá-lo ativado aumentaria o número de destinatários, mas um projeto em que as pessoas consentem sem saber poderia ser um problema perante a lei de defesa do consumidor. Conquistar confiança em vez de números. Foi o meu julgamento.

Há outro pequeno detalhe nos e-mails. Um "Assunto do Dia" entra no e-mail de confirmação da reserva. Algo sobre a estação do ano, o vinho ou a comida. A IA escreve automaticamente um assunto curto a cada dia.

O objetivo é entregar ao cliente uma semente de conversa antes da visita. O Tamuro é um estabelecimento com muita conversa entre os clientes. Um assunto lido no e-mail vira a primeira coisa que a pessoa diz a quem está ao lado no balcão. Por isso, não deixei o e-mail de confirmação terminar em "Sua reserva foi recebida" e fiz com que ele entregasse com antecedência um pouco do clima do estabelecimento.

Troquei uma vez a IA que escreve os assuntos. Passei para uma que produz assuntos mais naturais e mais próximos do tom do estabelecimento. No entanto, isso não é um mecanismo para aumentar clientes. É um mecanismo para melhorar um pouco a experiência de quem vem. Voltarei a falar dessa distinção na segunda metade deste capítulo.

Entre esses mecanismos, o que passou a mostrar resultados aos poucos foram os planos "Prazer em Conhecer" e "Bem-vindo de Volta". São planos de entrada fácil e preço razoável que só podem ser escolhidos por clientes de primeira viagem e por quem não visita há mais de um ano. Eles dão um motivo para ir ao bar tanto a clientes novos quanto a clientes que estão se afastando.

Por outro lado, também houve um problema. Muitos clientes reservam como convidados, sem se cadastrar como membros. Se eu exigisse o cadastro a cada reserva, talvez desistissem de reservar. Por isso, depois de concluída a reserva, mostro uma sugestão, "Quer vincular esta reserva a uma conta de membro?", e criei um jeito de virar membro depois. Isso não cria obstáculo para reservar e amarra o relacionamento mais tarde.

【Figura 1-8】Planos que só podem ser escolhidos por clientes de primeira viagem e por quem não visita há mais de um ano *(A tela está em japonês.)*

【Figura 1-9】O cartão de carimbos na Minha Conta (dados fictícios) *(A tela está em japonês.)*

【Figura 1-5】E-mail de confirmação de reserva. Inclui um "Assunto do Dia" (dados fictícios) *(A tela está em japonês.)*

### 1-5 Pelos números: cerca de 88% das reservas são feitas no mesmo dia

Conforme eu acrescentava mecanismos, percebi uma coisa. Eu não conseguia saber quais deles estavam funcionando.

Então contei os dados de reservas. Das 244 reservas dos últimos 90 dias, 215 foram feitas no mesmo dia. São 88,1%. A média é de 2,71 reservas por dia.

O Tamuro não era um lugar para o qual as pessoas reservam, mas um lugar aonde elas vão por impulso. Isso só ficou claro depois que coloquei em números.

Duas coisas ficaram visíveis a partir desses números.

Uma é como montar o formulário de reserva. Se a maioria das reservas é para o mesmo dia, é mais prático que o horário livre mais próximo de hoje já venha selecionado quando a tela de reserva abre. Por outro lado, algumas pessoas que querem reservar para uma data mais adiante vão enviar sem perceber para hoje. Por isso, fiz o dia de hoje se destacar no calendário e, na tela de confirmação, mostro a data e a hora em tamanho grande com "Hoje". Mantive a praticidade de escolher o mesmo dia e facilitei perceber os enganos.

A outra é o sentido do desconto antecipado. Muitas reservas no mesmo dia significam que não conseguimos prever o faturamento futuro. Só o mau tempo já basta para reduzir o movimento. Para aumentar um pouco que seja as reservas antecipadas, mais gente precisa usar o desconto antecipado. Essa percepção levou depois à história da construção de uma IA que publica em nome de quem toca o estabelecimento.

Para olhar números, é preciso um sistema para contar. O site de reservas não tinha nenhuma análise de acessos. Eu não sabia quantas pessoas chegavam à página de reserva, quantas desistiam no meio e quantas concluíam. Por isso, acrescentei um sistema que conta três etapas: chegou à página, definiu os detalhes, concluiu a reserva. Ele não registra quem veio, apenas a etapa e o horário.

Mais tarde ainda, também construí um sistema que envia por e-mail um relatório semanal resumindo os números de reservas. Descrevo como isso surgiu em 1-7.

【Figura 1-3a】O dia de hoje se destaca no calendário *(A tela está em japonês.)*

【Figura 1-3b】Na tela de confirmação, a data e a hora aparecem em tamanho grande como "Hoje" *(A tela está em japonês.)*

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

Mesmo assim, muita coisa mudou. Hoje consigo construir sem ajuda, nas brechas entre o trabalho principal, coisas numa escala que antes exigia uma equipe. E, para quem não tem experiência, a porta de entrada certamente ficou mais baixa. A IA ensina quando você pergunta sobre o que não entende. Ela dá forma ao que você diz em palavras. O que falta não é técnica, mas a capacidade de decidir o que construir e as palavras para dizer à IA. São habilidades que quem cuida de um estabelecimento já usa todos os dias.

### 3-6 O debate sobre a "morte do SaaS"

Software que as pessoas usam pela internet mediante mensalidade, como a série Agenda, é chamado de SaaS (Software as a Service, software como serviço). Contabilidade, controle de ponto, gestão de reservas. Os restaurantes de hoje usam muito SaaS no dia a dia.

A IA vai pôr fim ao SaaS? Em 2026, esse debate pegou fogo.

Um dos gatilhos foi uma declaração de Satya Nadella, CEO da Microsoft. Em um podcast em dezembro de 2024, Nadella disse que os aplicativos SaaS entrariam em colapso na era dos agentes de IA. O raciocínio: quando os agentes de IA assumirem a parte de decisão do trabalho empresarial, o software feito para as pessoas operarem por telas deixará de ser necessário.

Então, em fevereiro de 2026, a Anthropic anunciou o Claude Cowork (uma ferramenta de IA que executa tarefas de trabalho de forma autônoma), e as ações de empresas americanas de software sofreram uma forte venda. Em Wall Street, a queda passou a ser chamada de "SaaSpocalypse". O que os investidores temiam era que, se os agentes de IA fazem o trabalho, o modelo de SaaS de cobrar por pessoa (preço por usuário) desmoronaria.

Também há contra-argumentos. Jensen Huang, CEO da Nvidia, disse que os agentes de IA não substituirão o software, mas usarão o software em nome das pessoas, e chamou a venda de exagero. Não são poucos os que veem o SaaS que absorve a IA até saindo mais forte.

O SaaS vai mesmo morrer? Eis o que penso.

O que morre é a camada intermediária do SaaS: aquele tipo que cobra uma mensalidade alta por usuário e supõe que as pessoas o operem por telas. Se a IA faz o trabalho no lugar das pessoas, não é preciso pagar uma licença por pessoa. Se ninguém opera uma tela, não é preciso uma tela elaborada.

O que sobra são ferramentas baratas que fazem uma coisa com segurança. E ferramentas que a IA usa com facilidade.

Esses são exatamente os três princípios da série Agenda. Ela funciona automaticamente, é deixada à IA de quem administra (apoiar-se nos outros) e faz uma coisa só (função única). O AgendaTurno deixa o trabalho de montar a escala de turnos para a IA de quem administra, que é justamente a forma "a IA usa o software" descrita por Huang. O sistema de reservas do Tamuro abre uma janela via MCP para as IAs da clientela, e a ideia é a mesma.

Claro, pode parecer haver uma contradição aqui. Falo da morte do SaaS, mas a série Agenda é, ela mesma, SaaS. Só que a série Agenda é um conjunto de ferramentas que alguém que cuida de um estabelecimento construiu para o próprio negócio e depois tornou públicas a preço baixo. Não é um modelo que cobra mensalidade alta por usuário, e não pressupõe que as pessoas fiquem coladas numa tela todos os dias. Foi construída desde o início na premissa de que a IA a usará.

#### A "morte do SaaS" para os restaurantes

Esse debate pode soar como uma conversa de investidores e do setor de TI. Mas, para os restaurantes, a mesma coisa está prestes a acontecer de uma forma muito mais familiar.

Muitos estabelecimentos independentes pagam mensalidade a sites de gastronomia e de reservas e, além disso, pagam comissão de indicação por cada reserva. Em troca de trazer clientela, o site fica com o vínculo com a clientela, e não é raro que o estabelecimento nem tenha o contato de quem reservou. Se os preços sobem, o estabelecimento não tem escolha a não ser acompanhar, e, se o sistema de ranking muda, o fluxo de clientela muda.

Como escrevi no Capítulo 1, em 2026 começou a era em que a clientela tem a própria IA para procurar estabelecimentos. Se a porta de entrada passar para a IA, todo o arranjo de pagar mensalidades e comissões a um site para ficar bem posicionado na listagem começa a balançar. Se um estabelecimento abre por conta própria uma janela para a IA, a clientela consegue chegar até ele sem passar pelos grandes sites. Os registros de reservas e a relação com a clientela ficam nas mãos do estabelecimento.

Se eu pusesse "a morte do SaaS" nas palavras de um estabelecimento independente, seria "o fim da era em que pagar garantia um lugar na lista". O Tamuro abriu sua janela via MCP e mantém suas reservas e seu CRM com especificações próprias, como preparação para isso.

Se o SaaS vai morrer, ninguém sabe ainda. Mas o formato das ferramentas que permanecerão na era da IA vai aos poucos se desenhando. É o que penso.

### 3-7 Monetização: pequeno, muito e barato

Construo a série Agenda com o objetivo de fazê-la se sustentar como negócio. A meta é torná-la um segundo pilar de renda, separado do restaurante.

Defini valores baixos e acessíveis. As mensalidades começam em algumas centenas de ienes. O Livro de Ponto, por exemplo, custa ¥500 (cerca de US$ 3,3) por mês. Também misturo ferramentas gratuitas, como o Livro de Lucros, o Caderno de Luzes e o Livro de Custos. As ferramentas gratuitas servem de porta de entrada para as pessoas conhecerem a série Agenda. O Caderno de Luzes não usa API de mapas nem IA generativa, então custa quase nada para operar. Por isso posso oferecê-lo de graça.

Há uma só conta. Com uma conta compartilhada chamada AgendaID, você usa todas as ferramentas da série. Não é preciso se cadastrar de novo em cada ferramenta. As ferramentas pagas têm três meses de período gratuito e podem ser iniciadas sem cadastrar cartão. O período gratuito vale uma única vez para cada combinação de estabelecimento e produto. Se você indicar outro estabelecimento, ganha um bônus.

O motivo de eu conseguir manter os preços baixos está no meu jeito de construir. Construo sem ajuda, a IA faz a construção e reaproveito uma base compartilhada. O custo do banco de dados fica em cerca de US$ 35 por mês para a série inteira. Se o custo de construir e o de operar são pequenos, um negócio se sustenta mesmo com vendas pequenas.

Falo com franqueza. No momento em que escrevo este livro, alguns estabelecimentos testaram as ferramentas, mas quase não há cadastros pagos. O sistema para construir está pronto, mas o sistema para se tornar conhecido ainda está por vir. Este livro também pretende ser um volume para esse fim, o de se tornar conhecido.

#### Construir algo e fazer com que continuem usando são coisas diferentes

Falo com franqueza sobre mais uma coisa. Conseguir construir uma ferramenta e ter alguém que continue a usá-la são assuntos distintos.

Construir ficou mais rápido graças à IA. Mas fazer as pessoas continuarem usando exige outro trabalho. Responder a dúvidas sobre como usar (o Guia de Suporte existe para isso). Enviar um aviso antes de o período gratuito acabar. Explicar o motivo quando um preço sobe. Apagar corretamente os dados quando alguém pede para cancelar. E, acima de tudo, mantê-la funcionando sem que quem administra precise mexer.

Dos três princípios da série Agenda, o "automático" é o princípio para esse "fazer continuarem usando". Uma ferramenta que não funciona se quem administra não mexe nela todos os dias acaba sendo cancelada. Não basta construir a ferramenta. Ela só vira negócio quando continua sendo usada. Acrescentar, um a um, estabelecimentos que continuem usando: esse é o meu trabalho depois de publicar este livro.

#### Se você quiser começar no seu estabelecimento

Para quem leu este livro e quer experimentar no próprio estabelecimento, são três passos.

1. Abra https://bontallc.com/agenda?via=b2-pt-{{FMT}} e entre com uma conta Google (o AgendaID será criado. Não é preciso cadastrar cartão)
2. Primeiro, adicione um caderno gratuito. Recomendo o Caderno de Luzes. Basta colar o componente da placa no seu site, e funciona em 10 minutos. Se você ainda não abriu, experimente o Livro de Lucros
3. Se parecer combinar com você, experimente o Livro de Ponto por três meses grátis. Um aviso chega quando o prazo se aproximar, então não haverá cobrança mesmo que você deixe parado

Se tiver dúvidas, pergunte pelo Guia de Suporte (AgendaQA). A IA responde na hora às dúvidas de operação, e eu mesmo leio as perguntas sobre especificações e bugs.

As vendas de um restaurante dependem do clima e da estação. O número de lugares e o horário de funcionamento têm limites. As vendas de ferramentas, por outro lado, não têm limite de lugares. Tocar um estabelecimento enquanto se distribuem ferramentas nascidas dos problemas do próprio estabelecimento, e ver isso virar renda aos poucos: acredito que pode ser mais um jeito de um estabelecimento independente ganhar dinheiro.

#### Continuar uma empresa pequena e ir para o mundo

Há mais uma coisa que decidi sobre a série Agenda desde o início. Não a construiria só em japonês.

O Livro de Ponto, o Livro de Lucros e o Guia de Suporte podem ser usados em 20 idiomas. Os textos de tela e as perguntas frequentes, tudo. Uma ferramenta feita para um bar de 19 lugares em Tóquio funciona do mesmo jeito em inglês, em coreano, em vietnamita.

Há dois motivos. Um é que os problemas dos restaurantes não mudam quando o país muda. Você quer registrar quando a equipe chega e sai. Quer saber a rentabilidade antes de abrir. Quer avisar a clientela de que o horário de fechamento foi prorrogado. São todos problemas que estabelecimentos independentes do mundo inteiro compartilham. O outro é que o número de estabelecimentos independentes no Japão não para de cair. Se eu atendesse só o mercado de língua japonesa, as vendas de ferramentas teriam um teto.

No passado, para uma empresa pequena vender produtos no exterior, eram necessários representantes locais, agências de tradução e entidades jurídicas. Hoje a IA ajuda com tradução e revisão. Sistemas de pagamento compartilhados funcionam no mundo todo. Para a distribuição, basta um servidor, e não há estoque nem armazém em cada país. Uma ferramenta feita por uma só pessoa pode estar nas prateleiras do mundo em 20 idiomas no dia seguinte ao dia em que foi feita. No passado, só grandes empresas conseguiam isso.

Uma empresa minúscula que faz negócios com vários países desde o início: empresas assim às vezes são chamadas de micromultinacionais (empresas multinacionais minúsculas). A Bonta LLC mira exatamente isso, com um estabelecimento em Higashi-Nakano e uma só pessoa à frente.

Claro, traduzir para 20 idiomas não significa que quem administra estabelecimentos no exterior vá começar a usar de imediato. Algumas traduções ainda aguardam revisão por falantes nativos para soarem naturais. Mesmo assim, ao eliminar a barreira do idioma desde o início, o teto de alcance das ferramentas desaparece, assim como o teto de lugares.

Como estou construindo essa base é a história do Capítulo 4.

【Figura 3-5】Troca de idioma no Guia de Suporte. Os 20 idiomas estão listados *(A tela está em japonês.)*

## Capítulo 4: Tecnologia - Um sistema para construir produtos sem ajuda, de forma contínua

Pontos principais deste capítulo

- Transformei o procedimento de lançamento de um novo produto em um documento, em um formato (uma skill) que uma IA consegue ler e executar. O que as pessoas fazem é apenas o julgamento e as operações que só pessoas podem fazer
- As partes compartilhadas, como login, cobrança, páginas de apresentação e guias para outros produtos, são construídas uma vez e reaproveitadas em todos os produtos. O custo de banco de dados dessa base é de cerca de US$ 35 por mês
- O sistema ainda está crescendo. Continuo acrescentando ao documento de procedimento as falhas, como um design ter sido rejeitado cinco vezes seguidas

(Este é um capítulo com muitos termos técnicos. Se você não se interessa por tecnologia, pode pular para o Capítulo 5 e você acompanha a história sem problemas.)

### 4-1 ProductBootstrap: entregando à IA o próprio procedimento de lançamento

Toda vez que construí um produto, repeti a mesma preparação e os mesmos erros. Criar um repositório (um depósito para programas). Conectar o login. Decidir as cores do design. Montar o sistema de testes. Preparar o ambiente de produção. Eu com certeza já tinha feito tudo isso no produto anterior, mas esquecia os detalhes e tropeçava nos mesmos lugares.

Então transformei o procedimento de lançamento de um novo produto em um documento. A forma dele que a IA que escreve código (Claude Code) consegue ler e executar é o que chamo de "skill". O nome dessa skill é ProductBootstrap. "Bootstrap" é um termo comum no mundo da computação para começar a funcionar sozinho a partir de um mecanismo mínimo, e eu o apliquei ao lançamento de produtos.

Não mantenho um programa-modelo. Copio o produto concluído mais recentemente e começo o novo produto a partir dele. Assim, as lições mais novas passam automaticamente para o produto seguinte. Também não é preciso continuar mantendo um modelo antigo.

#### O fluxo do procedimento

1. Entregar o documento de requisitos. Se os campos obrigatórios (nome do produto, o que faz, quem usa, preço, unidade de preço, cor de identificação, local do design de referência e assim por diante) ficarem em branco, a IA não começa. A regra é que ela não faz perguntas no meio do caminho a quem administra. Se tudo não estiver pronto no início, ela não começa
2. Decidir a cor do produto. Cada produto da série Agenda tem uma cor de identificação. A IA mede as cores dos produtos existentes, propõe cerca de quatro candidatas que não se sobreponham, e a pessoa escolhe
3. Fixar o design. Peço a uma IA de design (Claude Design) que crie propostas para as telas. A IA faz a própria verificação em até três rodadas, e só as propostas que passam na verificação são mostradas a quem administra
4. Deixar a implementação com a IA até o fim. A IA constrói e corrige por conta própria até cumprir as condições de aceitação definidas (verificação de tipos, verificação de estilo, todos os testes verdes, aprovação em todas as verificações de tela e alterações no banco de dados passando sem problemas no ambiente de teste)
5. Quem administra aprova somente na hora de ir para produção. Tudo até o ambiente de teste avança sem supervisão, e a pessoa julga apenas a operação de produção

Construí a etapa de implementação para que ela não pare no meio esperando a aprovação de quem administra. No começo, eu avançava pedindo aprovação a cada etapa, mas nada andava assim. Quando há várias janelas de trabalho de IA, cada uma para esperando aprovação, e a pessoa tem que passar por todas as janelas tomando decisões. Então mudei: entrego de antemão o intervalo já aprovado e as condições de aceitação que uma máquina pode julgar, e ela só para em caso de falha.

As condições de parada também estão definidas. Quando o documento de procedimento e a decisão de quem administra entram em conflito. Quando se torna necessária uma operação que só um humano pode fazer. Quando ela não avança no mesmo erro por três vezes seguidas. Quando a autenticação expira, as permissões são insuficientes ou é preciso uma operação irreversível. Fora isso, a IA prossegue por conta própria. O estado do trabalho é registrado em um arquivo pequeno, então, mesmo que ela trave no meio, pode retomar dali.

#### Os humanos fazem apenas duas coisas

Escrevi isto no documento de procedimento: a IA executa todas as etapas. Quem administra só pode ser solicitado a fazer as duas coisas seguintes.

- O julgamento em si. Aprovar, decidir, escolher qual de duas opções seguir
- Operações que só um humano pode fazer. Chaves que só podem ser emitidas pela tela de administração de um serviço externo, solicitações que envolvem verificação de identidade, operações em um aparelho real e julgamento visual

Se a IA passar qualquer outra coisa para a pessoa, isso é uma violação do documento de procedimento. Na tabela de procedimentos, acrescentei uma coluna "executor" a cada linha, e qualquer linha em que a entrada atribuída à pessoa não consiga declarar um motivo passa para o lado da IA.

Tive um motivo para criar essa regra. Quando organizei o trabalho restante de um produto, a IA listou "criar o projeto no servidor", "registrar o destino do login", "inserir as variáveis de ambiente" e "montar o ambiente de teste", tudo como tarefas de quem administra. Todas eram operações que a IA podia executar sozinha. "Por que sou eu que tenho de fazer isso?" foi a minha reação sincera na época. A IA faz as coisas sozinha se você pede. Mas, se você não pede, ela as passa para uma pessoa. Por isso precisei escrever isso no documento de procedimento.

Coloquei na lista de verificação deste documento de procedimento todas as falhas do sistema de reservas que descrevi no Capítulo 2. Colocar os testes primeiro. Não manter dados de produção no ambiente de desenvolvimento. Montar primeiro o ambiente de teste. O produto seguinte evita a mesma dor desde o início.

#### Ainda crescendo

Este documento de procedimento não é um produto acabado. É algo a que continuo acrescentando sempre que alguma coisa falha.

Por exemplo, houve uma vez em que pedi à IA de design que criasse a tela de um produto cinco vezes seguidas, e as cinco foram rejeitadas. Isso inclui as rodadas em que entreguei a ela as regras de design de toda a série (DESIGN.md).

No início, a IA diagnosticou a causa como "o próprio esquema de cores". Eu neguei. As causas reais eram duas. Uma era que cores sem definição nas regras estavam sendo usadas à vontade. A outra era que três seções com papéis diferentes estavam empilhadas na vertical com a mesma cor de fundo e as mesmas margens, sem fronteira entre elas. Nenhuma regra tinha sido violada, mas os papéis tinham desaparecido da aparência.

Então acrescentei cláusulas às regras de design. Não dê a mesma aparência a coisas com papéis diferentes. Não as separe só pela cor. O mais importante vem primeiro na linha de visão. Só coisas realmente iguais podem ser alinhadas com o mesmo peso. Não faça um layout que apenas empilha coisas na vertical.

Houve mais uma lição da falha. Se você transmite a "aparência padrão a evitar" apenas como uma lista de proibições, a IA oscila inteira para outro padrão que não está na lista. Quando proibi de uma vez cartões, sombras e cantos arredondados, o que voltou foi uma tela de jornal, feita só de filetes e margens. Desde então, peço que os materiais de solicitação sejam escritos em três colunas: "o padrão a evitar", "o que eu queria proibir" e "o que fazer no lugar".

Também mudei no meio do caminho o modo de decidir as cores de identificação. Mais ou menos quando os produtos passaram de oito, a faixa de cores escuras foi ocupada pelos produtos existentes, e do nono produto em diante não era mais possível obter uma cor escura para linhas e botões sem colidir com as existentes. Então revisei a regra: a cor de identificação de um produto é usada apenas em cores de superfície claras, e linhas, filetes, ícones e botões principais são todos unificados na tom de preto-carvão compartilhado da série. Era uma restrição que só ficou clara quando os produtos se multiplicaram.

Toda vez que algo falha, corrijo o documento de procedimento. O produto seguinte fica mais fácil na mesma medida. Acredito que fazer o documento de procedimento crescer é o melhor investimento para continuar construindo produtos sem ajuda.

【Figura 4-2】As etapas do procedimento de lançamento e quem as executa (a IA ou quem administra) *(A tela está em japonês.)*

【Figura 4-3】As cores de identificação da série Agenda. Uma cor por produto, usada apenas em superfícies *(A tela está em japonês.)*

### 4-2 AgendaHub: a porta de entrada

À medida que os produtos se multiplicam, você acaba construindo as mesmas coisas várias vezes. Login, cobrança, páginas de apresentação, guias para outros produtos. Para tocar isso sem ajuda, é preciso construir as partes compartilhadas uma vez e reaproveitá-las em todos os produtos.

O AgendaHub é o lugar onde essas partes compartilhadas se reúnem. Eu o chamo de "porta de entrada".

Primeiro, ele é a entrada que direciona de um único endereço para todos os produtos. Sob um único domínio, bontallc.com, há uma entrada para cada produto alinhada: /agendatimbro, /agendaoro, /agendaluce. Para a clientela parece que os produtos estão dentro de um mesmo site, mas na verdade um programa separado roda por trás de cada um.

Depois, é onde ficam as páginas de apresentação dos produtos. Há uma página de apresentação da série e, dentro dela, uma seção para cada produto. Cada seção traz o nome do produto e o apelido, o preço, um problema enunciado com as palavras de quem administra, começando com "Quando você...", uma descrição do que ele faz e um link para a página de detalhes. Quando lanço um novo produto, acrescentar essa seção faz parte do procedimento de lançamento.

E é a casa das regras de design e dos procedimentos de lançamento. O design de referência das cores de identificação, as regras de tela (DESIGN.md), a skill ProductBootstrap que descrevi em 4-1, a skill que verifica telas e a skill que faz alterações no banco de dados com segurança. Em todas as regras que atravessam a série, o conteúdo real fica aqui, e cada produto o lê por referência.

【Figura 4-1】A estrutura da série Agenda. Da porta de entrada (AgendaHub) a cada caderno, e todos os cadernos se ligam a uma única conta (AgendaID) *(A tela está em japonês.)*

### 4-3 AgendaID: contas e cobrança compartilhadas

O AgendaID é o sistema compartilhado de contas e cobrança da série.

Quem entra uma vez com uma conta Google pode usar todos os produtos. Não é preciso criar uma conta para cada produto. Também pretendo, no futuro, levar as configurações de idioma de um produto para outro.

A cobrança também é um sistema único. Em vez de construir a conexão com o serviço de pagamento (Stripe) para cada produto, o AgendaID assume tudo. Há quatro categorias de preço: um produto leve a ¥300 (cerca de US$ 2) por mês, um produto cobrado conforme o uso, um produto de compra única a ¥600 (cerca de US$ 4) e um produto gratuito. Os produtos pagos têm três meses de período gratuito sem cadastro de cartão, utilizável uma vez por combinação de estabelecimento e produto. Há também um mecanismo que acrescenta três meses de período gratuito a quem indica e a quem foi indicado.

Antes de o período gratuito acabar, chegam e-mails de aviso sete dias e um dia antes. Primeiro construí esses e-mails dentro do Livro de Ponto também, mas, à medida que os produtos se multiplicaram, percebi que era um desperdício dar o mesmo mecanismo a cada produto, então o consolidei no lado do AgendaID.

#### Cancelamento e exclusão também sob regras compartilhadas

Há uma parte simples, mas importante: o cancelamento e a exclusão de dados.

Quando alguém cancela, quais dados são excluídos e quando? Se você constrói separadamente para cada produto, algo com certeza será esquecido em algum lugar. Além disso, a série Agenda inclui produtos que lidam com dados especialmente sensíveis, como o que identifica a clientela habitual por reconhecimento facial.

Então dividi a granularidade da exclusão em quatro níveis e a transformei em uma regra compartilhada pela série. São eles: cancelar um produto, excluir um estabelecimento, encerrar uma conta (sair da série inteira) e um pedido de exclusão feito por uma pessoa da equipe. Os níveis superiores se propagam em cascata para os inferiores, e cada produto registra no sistema compartilhado o seu próprio procedimento de exclusão de dados. O prazo de carência para exclusão é de 30 dias, e nesse período é possível desfazer.

Junto vem um eixo de tempo. Os registros de presença, por exemplo, precisam ser guardados por cinco anos, por exigência legal. Mesmo que quem já saiu da equipe peça a exclusão, dentro do prazo de guarda o registro deve ser mantido, com nomes e afins anonimizados, em vez de apagado fisicamente. Precisei definir a linha entre "excluir" e "manter" conferindo com a lei.

#### Um login de teste para impedir que a IA contamine a produção

Acrescentei mais um mecanismo ao AgendaID, voltado para a IA: uma entrada de login de teste.

Para fazer a IA verificar que as coisas funcionam, a IA precisa entrar e operar as telas. Mas o login é feito com uma conta Google, então a IA não consegue entrar sozinha. E também não posso entregar à IA a conta de quem administra. Existe o perigo de os testes da IA contaminarem os dados de produção.

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
