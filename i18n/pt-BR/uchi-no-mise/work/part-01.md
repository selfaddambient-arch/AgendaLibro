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
