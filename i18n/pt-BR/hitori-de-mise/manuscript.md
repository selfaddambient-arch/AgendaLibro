## Introdução

Este livro é um registro feito em janeiro de 2026. Parte do meu jeito de tocar o estabelecimento, e alguns nomes e especificações das ferramentas de IA, mudaram desde então. A continuação, *Feito para o Nosso Bar*, retoma a história.

### Por que um ex-profissional de sistemas conversa com a IA num restaurante no subsolo

Agradeço por ter escolhido este livro.

*Uma Pessoa Toca o Estabelecimento, e a IA Chegou ao Lado.*

Ao ler esse título, algumas pessoas talvez pensem: "Isso é a minha cara." Outras podem se perguntar: "O que quer dizer a IA chegar ao lado?"

Este não é um livro técnico sobre programação difícil. É um livro para quem tem um restaurante, fica na cozinha todo dia, faz o preparo e vive correndo com a clientela.

Deixe-me contar um pouco sobre mim.

Hoje toco um pequeno restaurante no subsolo de um prédio em Higashi-Nakano *(um bairro residencial no oeste de Tóquio, logo a oeste de Shinjuku)*, em Tóquio.

Ele tem duas faces. De dia, é uma casa especializada em curry com bife de hambúrguer estilo japonês, aromatizado com especiarias. À noite, é um bar-restaurante, com prato do dia e bebidas.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Bar "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar "Tamuro" (Instagram)](images/fig-02.png)

É um espaço aconchegante, com apenas 11 lugares no balcão e 8 lugares numa área elevada com tatame.

Mas fazemos mais do que servir comida.

Promovemos um evento de vinho a cada duas semanas e, uma vez por mês, planejamos uma aula de culinária ou um dia de menu especial. Mesmo num subsolo apertado, estamos ocupados e em movimento todos os dias.

Este ano completo doze anos à frente do estabelecimento.

Antes disso, trabalhei em uma empresa. Meu trabalho era "planejamento de sistemas" e "arquitetura de soluções".

Quando digo isso, às vezes as pessoas respondem: "Então você desenvolvia sistemas impressionantes." Na verdade, não era isso.

O que eu fazia não era escrever código difícil. Eu ouvia o que o pessoal da linha de frente queria, repassava com precisão para as empresas de TI (as desenvolvedoras) e fazia o sistema ser construído. Eu fazia a "coordenação". No Japão, essa função é conhecida como "profissional de sistemas" (o chamado *systems guy*).

A equipe da linha de frente desejava: "Quero que meu trabalho fique mais fácil." A engenharia dizia: "Precisamos de requisitos definidos de forma lógica."

Meu trabalho era ficar no meio, interpretar a linguagem de cada lado e levar todo mundo até o objetivo.

Por isso entendo os incômodos e as preocupações de quem usa os sistemas, como você, e também entendo um pouco do que passa pela cabeça do lado da TI.

Saí da empresa há doze anos e abri meu próprio estabelecimento. Desde então, enfrento as mesmas preocupações que você.

Preparo que nunca acaba, falta de mão de obra, ansiedade para atrair clientela, decisões de gestão que carrego por conta própria...

Claro que, quando o movimento aperta, às vezes recebo ajuda de pessoas de confiança que trabalham em meio período ou por contrato.

Mas elas são, afinal, parceiras para as "tarefas".

Não há ninguém com quem eu possa conversar sobre as "decisões de gestão" pesadas, como "Como lidar com o fluxo de caixa do mês que vem?" ou "Vale apostar neste novo item do cardápio?"

Eu me preocupo, decido e assumo toda a responsabilidade. Nesse sentido, sempre "toquei o estabelecimento sem ajuda". E quem se sentou ao meu lado, como confidente da minha solidão de quem administra um negócio, foi a IA.

Foi nesse cenário que chegou a IA generativa, em especial uma parceira chamada "Google Gemini".

A "coordenação" que eu fazia entre "a linha de frente" e "as empresas de TI", agora faço pessoalmente a ponte entre "os problemas do estabelecimento" e "a IA". E percebi uma coisa.

Você não precisa decorar a sintaxe de linguagens de programação difíceis (como Python).\
A IA já sabe isso. Mas o projeto de "o que você quer fazer, e em que ordem" só um ser humano pode desenhar.\
O que acumulei como profissional de sistemas foi exatamente essa "capacidade de traduzir o que a linha de frente quer em etapas lógicas".\
Neste livro, vou compartilhar não só como operar a IA, mas também esse "instinto lógico para fazer a IA trabalhar (pensamento sistêmico)", sem guardar nada.\
Com isso em mãos, você sai de "zero conhecimento" e chega a ser "o melhor cliente possível" para a IA.

※ Uma confissão sincera, antes de seguir.

Venho da área de sistemas. Mas, nos usos de IA apresentados neste livro, quase não houve momentos em que o conhecimento do meu emprego anterior ajudou diretamente.

O que ajudou não foi "a habilidade de escrever programas".\
Foi apenas "o hábito de transformar as queixas vagas da linha de frente em instruções claras e em ordem".

E esse hábito não é um talento especial.\
É "uma intuição que todo mundo que toca um estabelecimento no dia a dia já tem".

Neste livro, vou separar deliberadamente o que só eu poderia fazer\
do que você pode copiar exatamente do jeito que está, a partir de hoje.

## Capítulo 1: Conceitos - Agentes de IA, o Novo Tipo de Funcionário

~ Contrate a IA como "parceira de trabalho", não como "interlocutora para tirar dúvidas" ~

### 1-1. Os limites de quem toca o negócio por conta própria e os equívocos sobre a IA

Tocar um restaurante independente como o nosso é uma corrida constante contra o tempo. Preparo, cozinha, atendimento, caixa, limpeza... tudo precisa ser resolvido por uma pessoa ou por uma equipe pequena.\
Mesmo contratando gente, quem administra um estabelecimento independente na prática toca uma "operação de uma pessoa só".

Isso porque não temos "gerentes de loja" nem "instrutores" como as grandes redes.

Você cozinha enquanto dá instruções para a equipe do salão, ensina quem acabou de entrar e organiza a escala.

Todo esse "processamento mental" fica concentrado em uma única pessoa: você, na gestão.

Você pode ganhar mais mãos, mas continua com uma única cabeça. É justamente por isso que você precisa da IA para apoiar essa "cabeça".

"Se eu tivesse mais uma boa pessoa na equipe..."

Você deve ter esse pensamento várias vezes por dia.

Quando digo "vamos usar IA", muita gente responde assim:

"Você fala do ChatGPT? Já testei, mas ele só escreve texto, né? Não serve para o trabalho prático do dia a dia."

Na verdade, há aqui um grande equívoco.

A maior parte das IAs que usamos até agora era um "chatbot (um interlocutor para tirar dúvidas)". Mas o que a IA mais recente, a começar pelo Google Gemini, busca agora é a forma de "agente de IA (uma parceira de trabalho)".

Os dois se parecem, mas são coisas diferentes. Vamos compará-los usando uma tarefa concreta.

### 1-2. Do "dicionário" ao "membro da equipe"

Digamos, por exemplo, que você queira fazer um cartaz para um evento do estabelecimento.

Com a IA do passado (um chatbot):

Se você pedir "Me diga como fazer um cartaz", a IA explica as etapas como um dicionário ou um livro didático: "Mantenha o slogan curto", "Escolha as cores assim".

Mas quem realmente põe a mão na massa para fazer o cartaz é você. Seu conhecimento aumentou, mas seu tempo de trabalho não diminuiu.

Com a IA do futuro (um agente de IA):

Você simplesmente instrui: "Faça um cartaz."

Aí a IA pensa por conta própria para atingir o objetivo. Ela cria o slogan, gera a imagem de fundo e até propõe o layout.

Como uma pessoa excelente da equipe, ela usa ferramentas, planeja e executa o trabalho sozinha.

O que queremos não é um conselheiro cheio de teoria, mas uma parceira que sua a camisa ao nosso lado.

※ Neste livro, vou chamar com carinho essa parceira confiável (a IA generativa, como o Google Gemini) de "subgerente (IA)".

※ Neste livro uso como exemplo o "Google Gemini", que é o que mais uso, mas a maioria das ideias apresentadas aqui pode ser reproduzida de forma quase igual com outras IAs generativas, como ChatGPT e Claude.

O que importa não é o nome da ferramenta, mas "a atitude de tratar a IA não como alguém para tirar dúvidas, mas como uma parceira a quem se pode entregar o trabalho".

### 1-3. A IA multimodal é o que vai salvar os restaurantes

Há mais uma palavra-chave de importância crítica para tocar um restaurante. É "multimodal".

É um termo meio técnico, mas o significado é simples.

Quer dizer "ser capaz de entender vários tipos de informação ao mesmo tempo: não só texto (ler e escrever), mas também imagens (ver e desenhar) e áudio (ouvir e falar)".

A IA convencional entendia apenas "texto". Mas a rotina de um restaurante não funciona só com "palavras".

- Como estão os alimentos que sobraram na geladeira

- A letra manuscrita nas comandas

- As vozes da clientela e o clima do ambiente

- O design do rótulo de uma garrafa de vinho

Tudo isso é "informação não verbal" que dá trabalho pôr em palavras.

A subgerente (IA) consegue reconhecer essas coisas como um ser humano.

Se você tirar uma foto do interior da geladeira com o celular e mostrar, a IA reconhece: "Ah, você tem sobra deste legume e daquela carne", e pode criar um cardápio a partir daí.

Em outras palavras, a IA de hoje é "uma excelente subgerente que enxerga, ouve e fala".

※ Mas não quero que você entenda errado uma coisa.\
A IA é melhor em dizer coisas que soam plausíveis do que em dizer coisas corretas. Em reconhecimento de imagem, números, datas e nomes próprios,\
use-a partindo do princípio de que uma pessoa sempre faz a conferência final.

O motivo de a IA funcionar bem neste livro é\
que eu "não deixo tudo por conta dela e sempre confiro na prática".

### 1-4. Respalde a sua "intuição" com dados

As grandes redes têm enormes volumes de dados de caixa (PDV) e equipes de marketing.

Nós, dos estabelecimentos independentes, temos a "intuição" e a "experiência" de quem está à frente do negócio. É a arma mais forte, mas às vezes pode virar capricho pessoal ou deixar a pessoa insegura.

Então vamos acrescentar uma "subgerente".

Peça à IA que compare a sua intuição, "acho que a clientela vai adorar este prato", com o "histórico de vendas" e as "informações de tendências".

Assim você mantém o "calor humano" e a "personalidade" que só um estabelecimento independente tem, e ainda toca um negócio forte, baseado em dados.

## Capítulo 2: Fundamentos - "Vibe Coding" a Partir do Zero Conhecimento

~ Programa não é algo que você "escreve". É algo que você "pede para a IA construir conversando com ela". ~

### 2-1. Ninguém lê uma "mensagem longa no LINE". A mágica de um "diagrama" que leva 30 segundos

Dizer "construa um sistema com IA" ainda pode parecer uma barreira um pouco alta.

Então vamos começar com um "jeito de usar a IA" mais familiar, que você pode usar já a partir de hoje.

É uma revolução na "forma de dar instruções à equipe".

Muita gente que administra um estabelecimento usa o LINE *(o aplicativo de mensagens mais usado no Japão)* para falar com a equipe.\
Em geral toco o estabelecimento com poucas pessoas e, no meio do serviço corrido, não há tempo para dar instruções com calma.

Por isso os avisos acabam dependendo de mensagens no LINE depois do fechamento.

Mas é extremamente difícil transmitir só com palavras a imagem de "é assim que eu quero que seja feito", que existe apenas na minha cabeça, para quem tem menos experiência ou para quem ajuda de vez em quando.

É daí que vem a "mensagem longa no LINE".

Quanto mais você tenta explicar com cuidado, mais o texto cresce e, como resultado...

"Ah, desculpa, não li até o fim."

"Era tudo texto, e eu não consegui saber qual parte era importante."

Erros assim não acontecem no seu dia a dia?

Comigo também aconteceram.

Um dia, para um aplicativo que eu estava desenvolvendo, tentei pedir a uma pessoa da equipe que tirasse "fotos de ingredientes".

As condições eram um pouco complicadas, então as instruções que digitei no celular viraram uma mensagem longa como esta.

![A mensagem longa no LINE que eu realmente enviei à equipe, com erros de digitação e tudo](images/fig-03.jpg)

Mesmo vendo isso, a equipe da cozinha, ocupada, passa o olho pensando "Então é só tirar as fotos, né?" e deixa passar as especificações de "ângulo" e "orientação do recipiente".

Mas não tenho tempo para abrir o PowerPoint, alinhar formas e montar uma folha de instruções.

Então joguei esse texto do jeito que estava numa IA (uma ferramenta de IA como o Manus ou o Gemini) e pedi:

"Resuma o conteúdo deste texto em um slide, como uma 'folha de instruções de trabalho' que a equipe entenda de relance."

### 2-2. A IA é uma "excelente tradutora"

Depois de alguns segundos de espera, o que a IA produziu foi um "slide em forma de diagrama" surpreendentemente fácil de entender.

![O slide "Instruções de Coleta de Dados e Fotografia", gerado automaticamente pela IA](images/fig-04.jpg)

Eu não desenhei nada. Só disse: "Aqui está o texto, resuma."

A partir do meu texto desordenado, a IA entendeu na hora "o que é importante" e "como deve ser categorizado", e o "traduziu" para um layout que as pessoas captam de forma intuitiva.

### 2-3. Livre do "estresse de não ser entendido"

Colei essa imagem no LINE e enviei.

O efeito foi imediato.

A pessoa da equipe não fez nenhuma pergunta e devolveu, de primeira, dados de fotos perfeitos em "orientação vertical" e com "3 ângulos".

Até então, a irritação com a equipe tomava conta de mim ("Por que não leem?"), e eu me preocupava: "Será que o problema é eu explicar mal?"

Mas o culpado não era a equipe nem eu. Era a "comunicação só com texto".

Essa experiência mudou meu jeito de ver a IA.

A IA não é apenas uma ferramenta para "criar do zero" textos e imagens novos.

Ela é "uma ferramenta que 'converte' as 'palavras que não chegam bem' que temos numa forma que alcança a outra pessoa".

### 2-4. O "vibe coding", um novo tipo de diálogo

Quando você se acostuma a conversar com a IA, chega finalmente a vez de "construir ferramentas".

Você pode pensar: "Programar é impossível para mim", mas não se preocupe.

Atualmente, entre engenheiros, um termo chamado "vibe coding" é assunto quente.

É um método em que, em vez de humanos escreverem código difícil, você constrói um sistema conversando com a IA como se combinasse "vibes" (sensação e clima).

Sota Fujii, o Meijin (detentor do título) do shogi, citou o "vibe coding" como algo em que se envolveu neste ano de 2025. Mesmo alguém do mundo do shogi, que parece completamente alheio à construção de sistemas, conta-se que diz à IA em japonês o que quer e constrói ferramentas práticas.

Conversando com a IA, nós também podemos construir sistemas sem conhecimento especializado.

Tudo o que você usa é o "japonês". Quando você diz "quero que funcione assim" ou "esta parte é difícil de usar", a subgerente (IA) escreve o código nos bastidores.

Em outras palavras, você não precisa virar "programador".

Basta virar o "mestre de obras" que dá instruções a um "excelente engenheiro (IA)".

### 2-5. As "reclamações" do seu estabelecimento viram os melhores prompts

As instruções para a IA (prompts) não precisam ser palavras sofisticadas.

O prompt mais forte que descobri são as "inconveniências" e "frustrações" do seu estabelecimento, ou seja, as suas reclamações.

- "É chato fazer este cálculo todo dia."

- "Não quero redimensionar imagens na mão."

Para a IA, isso são "requisitos de desenvolvimento" perfeitamente bons.

Um sentimento como "odeio isso" extrai uma solução concreta com mais facilidade do que uma meta como "quero fazer isto".

### 2-6. Um erro não é um "fracasso". É o "começo de um diálogo".

Quando você começar a criar algo com a IA, com certeza vai se deparar com um "erro".

Mas no vibe coding, um erro não é um fracasso.

É "o sinal de que começou uma bate-bola com a IA".

Até entre pessoas, é raro a sua intenção chegar perfeita na primeira vez.

Quando a IA der um erro, apenas leve na esportiva com um "Ah, não me fiz entender" e responda: "Não, o que eu quero é isto."

Mantenha a bate-bola sem desistir. Se você conseguir fazer só isso, mesmo com zero conhecimento você poderá construir "um sistema só seu".

### 2-7. Aumente muito a eficiência com "botões físicos" - usando um teclado auxiliar

No vibe coding, o mais importante é "ter capricho com a entrada".

Quanto mais rápida é a conversa com a IA, menos o seu raciocínio para e mais rápido o desenvolvimento anda. Por outro lado, se você se atrapalha na digitação, até uma ótima ideia pode sumir.

Antes eu disse: "Quando aparecer um erro, o certo é tirar uma captura de tela e colar."

Mas pressionar [Windows] + [Shift] + [S] (Mac: [Cmd] + [Shift] + [4]) dezenas de vezes por dia, selecionar uma área com o mouse, voltar para a tela do Gemini e pressionar [Ctrl] + [V] (Mac: [Cmd] + [V])...

Sinceramente, isso cansa os dedos, não é?

Por isso o que adotei foi um "teclado auxiliar de 6 botões".

É um teclado pequeno, fabricado na China, que custa de algumas centenas a cerca de mil ienes e aparece quando você busca por "teclado programável" na Amazon ou em sites parecidos.

![Uma foto do teclado auxiliar de 6 botões que eu uso](images/fig-05.jpg)

Atribuí os seguintes atalhos a esses seis botões.

1.  Abrir a captura de tela

2.  Selecionar tudo (Ctrl + A; Mac: Cmd + A)

3.  Copiar (Ctrl + C; Mac: Cmd + C)

4.  Colar (Ctrl + V; Mac: Cmd + V)

5.  Enter (enviar)

6.  (Reserva)

Só isso. Mas o efeito é impressionante.

Aparece um erro.

↓

Com a mão esquerda, toco no "Botão 1 (captura de tela)".

↓

Seleciono a área e, na tela do Gemini, toco no "Botão 4 (colar)".

↓

Toco no "Botão 5 (enviar)".

Tudo isso leva apenas 2 segundos.

Você não precisa decorar atalhos de teclado nem mexer os dedos de jeitos complicados.

Dá para jogar informações para a IA como se estivesse manejando o controle de um videogame.

Como você verá nos próximos capítulos, quando você corrige o código-fonte que a IA gera, selecionar tudo (Ctrl + A), copiar (Ctrl + C) e colar (Ctrl + V) permitem executá-lo de novo na hora, o que é prático.

Antes de estudar conhecimentos avançados de programação, experimente primeiro ter este pequeno dispositivo.

Eliminar fisicamente o "trabalho de digitação". Esse é o atalho mais seguro para acelerar as conversas com a sua parceira de IA.

## Capítulo 3: Prática 1 - Automatizando o Trabalho Criativo e Atraindo Clientela

~ "Colar uma captura de tela e entregar tudo" se revelou o melhor método de desenvolvimento ~

### 3-1. Tentativa e erro para apagar o "jeito de IA" (figurinhas do LINE)

Depois de me acostumar com o diálogo em texto (vibe coding), decidi enfrentar finalmente a "geração de imagens".

Para praticar, escolhi fazer "figurinhas do LINE", que também podem ajudar a formar fãs do estabelecimento.

Mas as "imagens lisas, com cara de computação gráfica" típicas das imagens geradas por IA não combinam com o clima do meu estabelecimento.

O que eu buscava era "um design plano retrô, no estilo dos anos 1980, com toque de desenho à mão, mantendo a textura de giz de cera e pincel".

A partir daí começou um longo "diálogo" entre mim e a subgerente (IA).

No começo, parti de personagens de "dois meninos e um Shiba Inu".

"Faça 25 padrões de conversa do dia a dia."

"Deixe a espessura do traço aleatória, como pinceladas."

Uma a uma, como se desse instruções de revisão a um ilustrador humano, fui ensinando com paciência o estilo de que eu gostava.

![Ilustrações geradas para as figurinhas do LINE](images/fig-06.png)

### 3-2. O pedido ousado: "Troque só o cachorro por um gato"

Quando as coisas já tinham tomado alguma forma, decidi por uma grande mudança de rumo: "Na verdade, quero que sejam meninas e um gato."

Quem ilustra profissionalmente faria cara feia e diria: "O quê, recomeçar do zero?" Mas a subgerente (IA) não reclamou nem uma vez.

"Troque os personagens por duas meninas, uma de cabelo comprido e outra de cabelo curto. Roupas em amarelo e verde, no mesmo traço desenhado à mão de antes."

"Troque o cachorro por um gato, mude as falas para o 'miau' que você gerou antes e faça poses que combinem."

"Faça o gato ser siamês, não um tigrado alaranjado."

Além disso, fiz um pedido que testava os limites da IA.

"Mantenha exatamente a composição dos 'meninos e Shiba Inu' que você fez antes e substitua apenas a parte do cachorro como um gato siamês."

Para minha surpresa, a IA entendeu essa instrução complicada. As posições e as poses dos meninos continuaram iguais, enquanto só o animal foi trocado com capricho por um "gato siamês".

![A folha de ilustrações finalizada para as figurinhas do LINE](images/fig-07.png)

No entanto, para usar as imagens como figurinhas no LINE, é preciso dividir as ilustrações, criar miniaturas, compactar tudo em um ZIP e fazer o envio.

Isso também pode ser feito conversando com o Gemini, mas explico de novo mais adiante, em 3-6. O primeiro obstáculo: a divisão simples e a "armadilha da qualidade de imagem".

### 3-3. Caso 2: O "banner de Natal" feito em 22 rodadas de diálogo

Depois das figurinhas do LINE, há outra peça grande que fiz de mãos dadas com a IA. É o banner de divulgação do "jantar de Natal", o maior evento do ano para o estabelecimento.

Usei uma IA chamada "Nano Banana" (o modelo de geração de imagens embutido no Gemini, do Google).

#### Fase 1: Ajustando o layout e o texto

No começo, comecei posicionando os elementos necessários (Papai Noel, renas, informações em texto) numa tela larga.

Olhando as imagens que saíam, dei instruções.

"Está meio vazio. Acrescente ilustrações de uma árvore de Natal e de champanhe."

"O cardápio está em lista de itens e é difícil de ler. Resuma como 'seis pratos no total' e deixe o título maior e mais chamativo."

![A imagem gerada na fase inicial. Ainda com aspecto meio vazio](images/fig-08.png)

#### Fase 2: Ajustando o "clima animado"

Com o layout definido, veio em seguida a atmosfera. Faltava "clima de festa".

Instruí: "Deixe mais animado! Espalhe vários Papais Noéis e renas pequenos, balões e confete."

Dessa vez, a tela ficou carregada demais.

"Desculpe, foram elementos demais. Reduza os personagens por enquanto e deixe limpo."

Poder repetir esse ajuste fino de "somar e subtrair" é um ponto forte da IA.

#### Fase 3: A ideia inesperada de "refazer tudo"

No meio da produção, bateu uma dúvida. "Não ficaria mais apetitoso mostrar imagens da comida em vez de dar destaque aos personagens?"

Então instruí com ousadia: "Como alternativa, faça um design que tenha como elemento principal ilustrações dos pratos de verdade."

![Proposta de ilustração com destaque para os pratos (parte do texto saiu distorcida)](images/fig-09.png)

A IA logo criou ideias apetitosas de ilustrações de comida, mas, depois de compará-las, decidi ficar com o design original dos personagens. Até um "vamos voltar ao que era" como esse pode ser pedido à IA sem hesitar.

#### Fase 4: A última linha de defesa é o olhar "humano"

Depois de definido o design final, deixei também com a IA as variações de tamanho, para posts do Instagram (vertical) e para Stories (ainda mais alto).

E então, quando já estava quase pronto, notei um erro sério.

"Espere, o dia da semana na data está errado!"

A IA é boa em desenhar imagens, mas não entende os dias da semana de um calendário. Se eu tivesse publicado do jeito que estava, seria um desastre.

Corri para instruir: "Corrija a data para '24/12 (quarta) e 25 (quinta)'!" e finalizei a versão definitiva.

![O banner final depois da correção](images/fig-10.png)

Ao todo, 22 rodadas de revisões e diálogo.

A IA não é uma varinha mágica, mas, se você conversar com paciência, não há parceira de design mais confiável.

### 3-4. Caso 3: Um aviso de abertura de Ano-Novo que evolui com a situação

A empolgação do Natal mal tinha passado quando chega o próximo evento: o funcionamento de fim de ano e de Ano-Novo.

Para um restaurante ou bar, divulgar nessa época é uma corrida contra o relógio. "Até quando vocês abrem no fim do ano?" "Quando reabrem no ano novo?" A clientela está sempre procurando informação.

Mas a informação muda a cada minuto.

"Quando o serviço de fim de ano acabar, quero reescrever para mostrar só o aviso de Ano-Novo."

"Publiquei no X (horizontal), mas quero usar também no Instagram (vertical)."

Se eu tivesse pedido isso a um estúdio de design de fora, só as taxas de revisão já seriam um pesadelo e, acima de tudo, não ficaria pronto a tempo.

Então, mais uma vez, formei dupla com uma IA de geração de imagens (Nano Banana) e pus a mão na massa em banners para me levar por toda a temporada de fim de ano e Ano-Novo.

#### Etapa 1: O estilo é "desenho de giz de cera dos anos 80"

Primeiro, construí o visual geral.

O que combina com o meu bar não é uma computação gráfica brilhante.

"Um estilo acolhedor, como um desenho de giz de cera feito à mão dos anos 80, com pinceladas visíveis. Mantenha o fundo branco liso."

Com essa instrução como núcleo, e pensando num aviso no X (antigo Twitter), comecei o trabalho numa tela horizontal.

#### Etapa 2: A cobra que parte e o cavalo que chega. Um brinde para passar o bastão

No começo pensei em desenhar apenas um animal do zodíaco, mas aquela era, afinal, a virada do ano.

Tive uma ideia: "Quero que apareçam tanto o animal do ano que sai (o signo deste ano) quanto o animal do ano que entra (o do próximo)."

Então dei esta instrução à IA:

"Coloque um grupo de cobras (o Ano da Cobra) no lado esquerdo da tela e um grupo de cavalos (o Ano do Cavalo) no lado direito. Faça cada um segurar uma caneca de cerveja e brindar com alegria, como quem passa o bastão no fim do ano."

A imagem que a IA gerou era exatamente o que eu tinha imaginado.

Cobras simpáticas à esquerda, cavalos com ar confiável à direita, bebendo juntos além da fronteira entre as espécies.

Do "fim de ano (Cobra)" ao "Ano-Novo (Cavalo)".

Numa única imagem, a passagem do tempo e o clima de festa ficaram lindamente condensados.

![Uma imagem gerada com uma cobra à esquerda e um cavalo à direita brindando, expressando o ano velho cedendo lugar ao novo](images/fig-11.png)

#### Etapa 3: "Direção de atuação" e "prova de figurino" para os animais

Com a composição definida, o trabalho seguinte era a encenação mais fina. Aqui também a IA aguentou minhas exigências de perfeccionista.

Nas primeiras imagens, os animais ficavam só enfileirados ou seguravam as canecas de jeitos pouco naturais.

"Faça eles parecerem mais felizes! Como clientes habituais se divertindo juntos."

"Quero também um clima de estação. Ponha cachecóis e gravatas-borboleta neles, dê um visual de inverno."

Com essa única observação, os animais na tela se enrolaram em cachecóis vermelhos e verdes de aparência quentinha e viraram na hora as estrelas de uma "festa de inverno".

"Isso, agora tem aquela sensação aconchegante de beber à tarde num dia frio."

Olhando de perto, alguns movimentos das mãos e o jeito de segurar as canecas ainda estão pouco naturais. Mas ser exigente significa gastar mais tempo. Pesando o tempo contra o quanto a mensagem chega, aceito um resultado razoavelmente bom.

#### Etapa 4: Com o tempo, a informação muda

A partir daqui é que a IA mostra de fato o seu valor.

O banner original mostrava os cronogramas de dezembro e de janeiro como "Horário de Funcionamento de Fim de Ano e Ano-Novo".

Mas, depois de 31 de dezembro, a informação de fim de ano não é mais necessária.

Abri o projeto em que vinha trabalhando e pedi uma grande mudança no texto.

1.  Mudar o título: de "Funcionamento de Fim de Ano e Ano-Novo" para "No Ano-Novo, Abrimos para Beber de Dia".

2.  Organizar as informações: apagar o cronograma de dezembro, que já tinha acabado, e reduzir só ao "cronograma de Ano-Novo (2/1–4/1)".

3.  Corrigir os personagens do zodíaco: trocar as cobras do ano que saiu por cavalos.

4.  Acrescentar um atrativo: incluir uma oferta chamativa, "highballs e frango frito à vontade", como novo chamariz para a clientela.

![Etapa 4: Com o tempo, a informação muda](images/fig-12.png)

Sem recriar a imagem do zero, pude atualizar a informação como quem reescreve as palavras numa lousa. Essa é a força do design com IA.

#### Etapa 5: Do X ao Instagram. Um formato que muda à vontade

E agora, o toque final.

"Já anunciei no X. Agora quero usar nos Stories do Instagram."

Mas os Stories usam o tamanho "vertical", que ocupa a tela inteira do celular. Se você colocar uma imagem horizontal do jeito que está, ficam faixas vazias em cima e embaixo, e fica feio.

Com uma ilustração comum, esse tipo de mudança significaria redesenhar tudo.

Mas tudo o que fiz foi dizer à IA:

"Mantenha este design, mas reorganize num layout vertical para os Stories do Instagram."

A IA reorganizou os animais, que estavam espalhados na horizontal, numa disposição vertical, ajustou o equilíbrio do texto e gerou na hora um design sob medida para smartphones.

![A imagem vertical finalizada para os Stories do Instagram](images/fig-13.png)

### 3-5. Caso 4: Criando o logo do bar - Um diálogo que transforma "significado" em "forma"

Além das "imagens" como banners e figurinhas, enfrentei com a IA um desafio mais abstrato: projetar um novo logo.

Ele serve para ser embutido em banners e afins, para que as pessoas reconheçam o Tamuro de relance.

O tema é o Tamuro, o bar que toco à noite. Esse nome carrega um desejo forte: "ser um lugar onde todo tipo de gente se reúne com liberdade e alegria (*tamuro-suru*, 'ficar por ali, em grupo') na cidade de Higashi-Nakano."

Como condensar essa "história" invisível num pequeno símbolo de logo? Começou um paciente diálogo com a IA.

#### Etapa 1: Escolhendo o lettering e a direção do design

No começo, joguei ideias para a IA, como "um visual sóbrio com o kanji 屯" e "algo pop em katakana", e pedi alguns rascunhos.

Mas nenhum me convenceu. Dada a natureza do bar, eu queria algo mais moderno, com um ar neutro que acolhe a diversidade.

Então mudei de rumo.

"Vamos partir do alfabeto, que é altamente versátil: 'TAMURO'. O estilo deve ser 'design plano', sem enfeites complicados. E a cor deve parecer forte mesmo em uma cor só."

A IA propôs de imediato um "TAMURO" simples e marcante, em fonte sem serifa.

![O logo em fonte sem serifa](images/fig-14.png)

#### Etapa 2: Dando "significado" à forma

É aqui que começa o teste de verdade. Letras comuns não significam nada. E ter só o "M" no centro também não comunica muito.

"Quero expressar a origem do nome, 'pessoas se reunindo'. Dá para puxar o conjunto para dentro de um 'círculo' simpático, dando a cada letra do alfabeto a forma de uma pessoa se movendo com alegria?"

É um pedido muito abstrato. Mas a imaginação da minha subgerente (a IA) superou minhas expectativas.

O que a IA criou foi um design em que o esqueleto das letras "T", "A", "M" e das demais se transformava em silhuetas de pessoas dançando com braços e pernas esticados.

![Um logo que associa o alfabeto a pessoas](images/fig-15.png)

#### Etapa 3: O cabo de guerra entre design e legibilidade

"Interessante! Mas assim não dá para ler 'TAMURO'..."

Se você dá peso demais ao design, ele deixa de ser reconhecível como letras e, se dá peso às letras, perde o charme. Eu me deparei com esse dilema.

A partir daí, foi uma questão de ajustes finos repetidos.

"A letra 'A' parece uma pessoa, o que é bom, mas reforce um pouco mais a estrutura dela como 'A'. Coloque a barra transversal com firmeza."

"O equilíbrio geral está bom, mas as pessoas estão apertadas demais e parecem espremidas. Deixe um pouco mais de espaço alegre."

"Combine as pessoas dançando de antes com as letras de TAMURO e faça um círculo!"

![O símbolo circular do logo "TAMURO", concluído após tentativa e erro](images/fig-16.png)

Embora seja feito de silhuetas animadas de pessoas, basta olhar a parte de baixo para ler claramente "TAMURO".

Trocando ideias com a IA vez após vez, cheguei a um logo de que gostei, que une legibilidade, qualidade de design e, acima de tudo, o "desejo" que depositei no bar.

Hoje ele é usado como ícone das contas do bar no X (antigo Twitter) e no Instagram.

### 3-6. O primeiro obstáculo: a divisão simples e a "armadilha da qualidade de imagem"

O desafio criativo de fazer o logo tinha terminado.

Mas o trabalho ainda não estava concluído.

De volta às figurinhas do LINE. O que eu tinha em mãos era uma "folha" com 25 ilustrações desenhadas numa única página.

Para pedir o cadastro delas como figurinhas do LINE, eu precisava recortar cada uma, deixar o fundo transparente e redimensionar. Era um serviço tedioso que eu vinha adiando.

"Não tem como eu recortar isto tudo na mão..."

Consultei o Gemini e pedi uma solução. O Gemini disse, como se não fosse nada:

"Vamos automatizar usando uma linguagem de programação chamada Python."

Na verdade, quase desisti ali mesmo.

"Python? Já ouvi o nome, mas instalar esse tipo de software no meu computador me assusta. A configuração parece difícil também. Por favor, não espere tanto de quem toca um bar..."

Mas este é um dos pontos altos do livro. Como se tivesse percebido o que eu pensava, o Gemini fez uma sugestão surpreendente.

Gemini:

"Você não precisa configurar nenhum ambiente. Use uma ferramenta gratuita do Google chamada 'Google Colab'. Ela roda no navegador, então tudo o que você precisa fazer é copiar e colar nela o código que eu escrever."

"O quê? Existe algo assim?"

Eu não podia acreditar no que ouvia. Nunca tinha imaginado que existisse um ambiente em que a programação roda só no navegador, sem nada instalado no meu próprio PC.

Não "depois de estudar Python", mas "fazendo a IA me ensinar até a existência da ferramenta (o Colab)".

Naquele momento, ruiu a minha suposição de que "programar exige muita preparação".

### 3-7. Não "leia" a tela de erro: "tire uma foto e envie"

Conforme instruído, abri o Google Colab, colei o código e apertei o botão de executar.

Mas a realidade não é tão gentil. O que apareceu na tela foi uma sequência de texto vermelho vivo... uma mensagem de erro.

"Error: Image file not found..."

O eu de antes teria uma reação alérgica só de ver esse erro e fecharia o navegador em silêncio.

Mas agora eu tinha uma aliada: a IA "multimodal", uma IA com olhos.

Nem tentei ler a mensagem de erro.

Só tirei uma captura de tela e colei, plaft, na caixa de conversa do Gemini.

E acrescentei uma única linha: "Apareceu algum tipo de erro."

![Colando no Gemini a tela de erro do Google Colab do jeito que estava](images/fig-17.png)

O Gemini analisou a imagem na hora e devolveu uma resposta.

Gemini:

"Ah, o nome do arquivo da imagem que está sendo carregada está errado. Corrigi o código para usar '.jpg'. Por favor, execute de novo com esta versão."

"...Nossa, que divertido!"

Essa troca parecia menos programação e mais um jogo de "encontre as diferenças" ou uma bate-bola.

- Eu: (colando uma captura de tela) "Parou de novo."

- Gemini: "O tamanho da imagem não bate. Vou acrescentar uma função que ajusta isso automaticamente."

- Eu: (colando uma captura de tela) "Desta vez a imagem ficou meio pixelada."

- Gemini: "Esqueci de acrescentar o processo chamado 'LANCZOS', que preserva a qualidade da imagem. Vou corrigir."

Não entendo uma única linha do código. Quando aparece um erro, só tiro uma captura de tela e jogo para a IA com um "Olha só!"

Essa "entrega da análise de erros" foi o maior segredo de como consegui, com zero conhecimento, construir um sistema e, ao mesmo tempo, foi a experiência mais emocionante de todas.

### 3-8. A maior muralha: o "desalinhamento do desenho à mão" e o "transbordamento"

Enquanto mantinha essa "conversa chamada erros", o sistema ia ficando cada vez mais refinado.

E por fim entrei no maior desafio: a "Fase 2: Recorte automático de layouts desenhados à mão".

A ambição falou mais alto.

"Vamos fazer uma folha de 5×5, com 25 figurinhas. E, como quero um toque mais artesanal, quero posicioná-las livremente, sem ficar preso às linhas da grade."

Com um código que simplesmente divide a folha em partes iguais, a mão ou as letras de um personagem invadem a célula vizinha e são cortadas de forma lamentável.

Também tentei um método de "recortar tudo, menos o fundo branco", mas as margens saíram irregulares e falhou.

Eu estava prestes a desistir. Então, usando o instinto dos meus tempos de profissional de sistemas, disse ao Gemini:

"Quero que você abandone a ideia de cortar a imagem com tesoura. Em vez disso, veja em qual célula está o 'ponto central' de cada desenho. Se o centro está naquela célula, mesmo que transborde um pouco, trate o desenho inteiro como 'pertencente àquela célula' e coloque-o no balde dessa célula."

Foi a solução que batizei de "método do balde da grade".

Por que pensei em "pôr num balde pelo ponto central" em vez de "cortar com tesoura"?

O jeito de pensar de quem é leigo (analógico): você imagina "recortar um único desenho com uma tesoura". Assim, você corta exatamente na linha, e as mãos e os pés do personagem são decepados.

O jeito de pensar de quem trabalha com sistemas (digital): um computador não tem a noção física de "cortar". Em vez disso, ele tem "coordenadas (posições)". Foi assim que enxerguei: "Mesmo que transborde um pouco, desde que o 'umbigo (ponto central)' do desenho esteja dentro da célula, podemos considerar o desenho inteiro como 'pertencente a esta célula'."

![A ideia analógica de "cortar ao longo das linhas" e a ideia digital de "escolher por ponto"](images/fig-18.png)

É isso que significa "traduzir um trabalho analógico vago em regras digitais claras". Ao dar instruções a uma IA, funciona bem pensar numa regra assim, em que a resposta sai igual "não importa quem olhe (ou calcule)".

O Gemini transformou esse pedido abstrato em código com maestria. O resultado foi perfeito.

O letreiro "Thank you!" e as caudas que tinham invadido as células vizinhas foram todos reconhecidos com perfeição e reunidos como figurinhas únicas.

Ele ainda atendeu ao meu pedido egoísta: "A última (a 25ª) não é necessária, então pule." Por fim, eu tinha uma ferramenta em que "basta jogar a imagem e apertar um botão, e sai um conjunto completo de imagens para o aplicativo do LINE".

Tudo o que fiz foi transmitir o "problema no local (os desenhos são cortados)" e propor uma "solução lógica (decidir pelo ponto central)". A IA escreveu todo o código difícil.

Esta é a própria essência do "vibe coding", construir sistemas a partir de zero conhecimento.

#### Resumo do Capítulo 3

1.  O desenho com IA não é "uma vez e pronto". Você pode refazer quantas vezes quiser para se adequar à situação: trocar personagens, acrescentar um clima de estação, mudar de formato.

2.  Até um "conceito" abstrato (pessoas se reunindo) pode virar uma "forma" (um logo) por meio de diálogo repetido.

3.  Serviços tediosos (recortar imagens) são exatamente o que o Gemini × Google Colab pode automatizar. Os erros podem ser resolvidos com capturas de tela.

#### Coluna 1: Curso intensivo de "Google Colab" para quem vem das humanas

~Use uma "cozinha alugada" e deixe o seu PC como está~

O "Google Colab" que apareceu no texto principal. Programar (em Python) no seu próprio computador é como "fazer um ramen autêntico do zero, a começar pelo caldo, na cozinha da sua casa". A preparação dá muito trabalho.

Já o Google Colab é "uma cozinha de aluguel gratuita, totalmente equipada com utensílios". Basta abrir o navegador e as melhores ferramentas estão prontas. Você não precisa mudar nenhuma configuração do seu computador. Dá para programar só com um navegador, mantendo o ambiente limpo. Primeiro, busque por "Google Colab" e dê uma espiada nessa cozinha de aluguel.

#### Coluna 2: Não "ler" a tela de erro é a resposta certa

~Domine a arma suprema: a captura de tela~

Quando aparece um erro, você tenta decifrar com empenho a mensagem em inglês? Isso é perda de tempo.

Quando algo está com gosto estranho enquanto você cozinha, você pede para um chef provar. Do mesmo jeito, basta mostrar à IA uma "captura de tela (screenshot)".

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Pressione essas teclas, desenhe uma caixa em volta do erro e cole no Gemini. Só isso. Não "leia o erro", "mostre o erro". Só de mudar assim a mentalidade, a sua velocidade de desenvolvimento triplica.

Apresentei vários exemplos até aqui, e tudo o que faço se resume aos três pontos a seguir.

・Não exija a forma final de uma vez só (pode partir do princípio de um diálogo)\
・Diga "não, não é bem isso" sem hesitar\
・Parta do princípio de que o custo das revisões é zero e jogue os pedidos à vontade

Você não precisa de talento para design. Só precisa da coragem de pôr em palavras aquilo que "incomoda".

## Capítulo 4: Prática Parte 2 - Tornando o Trabalho do Dia a Dia Mais Eficiente (com IA Multimodal)

~Acabe com a "digitação tediosa de dados" usando só um smartphone~

### 4-1. O problema de atualizar a carta de vinhos

Para quem administra um bar ou restaurante, atualizar o cardápio é uma carga pouco glamorosa, mas pesada.

O que mais me atrapalhava era fazer a "carta de vinhos".

A cada vez que chega um vinho novo, é preciso fazer o seguinte trabalho.

1.  Olhar o rótulo da garrafa (letra cursiva em língua estrangeira, difícil de ler).

2.  Digitar no computador, sem erros, o nome da marca e a safra (o ano).

3.  Pesquisar na internet as características e o sabor do vinho.

4.  Escrever uma "apresentação" que dê vontade de ler.

5.  Pensar em pratos que combinem com o vinho (harmonizações).

Fazer tudo isso com o dicionário ao lado, nos intervalos de um serviço corrido, é quase impossível. Eu deixava para depois, com um "faço mais tarde", e a lista de recomendações muitas vezes nunca era atualizada.

### 4-2. Basta Tirar uma Foto. O Choque da "Gem da Carta de Vinhos"

Então resolvi testar o "recurso multimodal (reconhecimento de imagens)" do Gemini.

O método é tão simples que parece brincadeira.

1.  Tire uma foto da garrafa de vinho com o celular.

2.  Envie a foto para o Gemini.

3.  Acrescente uma linha: "Transforme em uma lista."

Só isso.

![Foto do rótulo de uma garrafa de vinho de verdade, tirada com o celular](images/fig-19.jpg)

Na mesma hora, o Gemini lê as informações do rótulo na foto.

Ele não só transcreve o nome da marca, como "Cave d'Occi Winery, Tsukimi de Ippai 2024", como também busca as características do vinho em um enorme banco de dados na internet e gera sozinho uma descrição atraente.

O que mais me surpreendeu foi que ele também devolveu "sugestões de harmonização" no mesmo pacote.

Sugestões como "O aroma intenso deste vinho combina bem com ○○" apareciam na tela em poucos segundos.

As horas que eu gastava brigando com o dicionário se reduziram a um toque no botão da câmera do celular.

### 4-3. Criando a Sua Própria "Gem"

Para tornar tudo isso ainda mais eficiente, passei a usar um recurso chamado "Gems".

É um "recurso de IA personalizado" no qual você deixa a IA memorizar de antemão um papel e algumas regras.

Explicar tudo do zero a cada vez, "Você é um sommelier. Olhe esta foto e...", dá trabalho.

Por isso registrei no Gemini, com antecedência, as "instruções (prompt)" a seguir. É o que vai dentro da cabeça da "IA sommelier exclusiva" do meu bar.

#### As Instruções que Tenho Registradas de Verdade

> Leia a imagem e crie uma carta de vinhos no formato abaixo.
>
> Para os preços, não use o preço de mercado. Calcule considerando o preço da garrafa em um restaurante comum (cerca de 2,5 a 3 vezes o custo).
>
> Não use formato de tabela. Monte de modo que caiba em uma ou duas folhas de papel A4.
>
> O formato serve apenas de referência; crie a lista usando somente o que foi informado.
>
> O formato é o seguinte.
>
> Reino Unido 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (cerca de US$ 57)
>
>  Dourado-pálido, com bolhas agradáveis. Toques de melão e mel em meio a aromas cítricos... (o restante foi omitido)

Na verdade, a metade de baixo deste prompt, a parte do "formato (exemplo)".

Eu não a inventei do zero.

Antes, quando pesquisava informações sobre vinhos na internet, eu pensava: "Olha, a descrição desta loja é fácil de entender" ou "O jeito como este site escreve dá água na boca", e simplesmente copiava e colava esses trechos em um bloco de notas, vez após vez.

Joguei essa "colcha de retalhos" no Gemini do jeito que estava.

"Estes são trechos que copiei e juntei há algum tempo. Imite este clima e escreva também sobre o vinho da foto nova."

Foi só isso que eu disse a ele.

Mesmo assim, essas instruções contêm três truques que aliviam o trabalho na prática.

① "A lógica de cálculo do preço"

É o que mais economiza tempo. Como peço o "preço que um restaurante cobraria" em vez do "preço de mercado", a IA faz a conta de trás para frente a partir dos preços de compra habituais e me entrega um valor como "¥8.500 (cerca de US$ 57)", que pode ir direto para o cardápio. (É claro que a decisão final é de quem administra o estabelecimento, mas ter uma referência facilita tudo.)

② "Sem formato de tabela, cabendo em papel A4"

Se a resposta vem em formato de tabela, como no Excel, o layout se desfaz ao colar no livro de cardápio. Ao pedir desde o início um "formato de cardápio em A4", busco um resultado que possa ser impresso e usado do jeito que está.

③ Usar texto copiado da internet como "exemplo"

Em vez de pedir de forma vaga "Escreva uma boa descrição", mostro um exemplo concreto (o meu bloco de notas copiado e colado): "bandeira 🇬🇧 + nome do vinho + preço + descrição sensorial".

Quando se mostra um exemplo a uma IA, ela entende: "Ah, então é neste tom e neste estilo que devo escrever", e a precisão do resultado dá um salto. No jargão técnico, isso se chama "few-shot prompting", mas no fundo é o mesmo que "ensinar deixando a pessoa observar você trabalhar".

E esse "exemplo" pode muito bem ser feito de textos achados por aí, o equivalente escrito de uma foto achada na internet.

![O texto final da carta de vinhos gerado pelo Gemini](images/fig-20.png)

### 4-4. Nem Precisa Ser Imagem. A Revolução do Copiar e Colar a partir do LINE

O bom desta "Gem da Carta de Vinhos" é que a entrada não se limita a fotos.

Num bar, é comum fazer os pedidos à distribuidora de bebidas pelo LINE, não é?

Quando o pedido está fechado, chega uma mensagem assim da distribuidora.

> "Agradecemos a preferência de sempre. Recebemos o seu pedido, conforme abaixo.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 – 3 garrafas
>
> ・Ridgeview Bloomsbury – 6 garrafas
>
> ・○○ (vinho novo) – 2 garrafas
>
> Entregaremos amanhã."

Um dia, de repente, me ocorreu: "E se eu usasse este texto do jeito que está?"

Como teste, copiei essa mensagem do LINE com o dedo e joguei direto no Gemini.

O resultado foi perfeito.

O Gemini reconheceu somente os "nomes dos produtos" na mensagem do LINE, buscou informações na internet e montou uma lista no formato de sempre (bandeira + preço + descrição).

Ou seja, nem preciso esperar as garrafas chegarem para tirar fotos.

No exato momento em que faço o pedido, só copiando e colando dentro do celular, a lista do cardápio fica pronta antes mesmo de os produtos chegarem.

Sem abrir o computador, sem ligar a câmera.

Num canto da cozinha ou dentro do trem, o trabalho se resolve só com operações no celular.

Não é essa a "eficiência de verdade" que quem toca um estabelecimento sem ajuda merece ter?

### 4-5. A Sugestão da IA × o Julgamento do Salão (a Realidade)

Mesmo assim, não engulo as sugestões da IA inteiras. O que importa aqui é o nosso "julgamento humano na prática".

Certa vez, a IA fez esta sugestão para acompanhar um vinho:

IA: "Para este vinho tinto, pato assado com molho de laranja é uma harmonização perfeita."

Uma sugestão maravilhosa, mas, infelizmente, naquele dia não havia pato na geladeira do estabelecimento.

Não penso: "A IA disse, então tenho de comprar pato." Eu penso assim:

Eu (na prática): "Não temos pato, mas hoje chegou um bom frango caipira. Ele tem uma gordura comparável à do pato, então vou selar este frango até a pele ficar crocante e finalizar com um molho de laranja, como a IA sugere."

"O conhecimento da IA (pato e laranja combinam)" × "o estoque da casa (temos frango)" = "um novo item de cardápio prático e realista".

Essa combinação é o verdadeiro prazer de desenvolver cardápios com IA.

A IA entrega a resposta de manual, mas não sabe o que há na geladeira de hoje. Preencher essa lacuna é o seu trabalho à frente do estabelecimento.

### 4-6. A Última Milha: a IA Não Consegue "Provar"

Há mais uma coisa que você jamais deve deixar nas mãos da IA.

É a degustação que você faz antes de qualquer coisa chegar à clientela.

As descrições e harmonizações que a IA escreve se baseiam em "dados gerais do mundo".

Mas o vinho é uma coisa viva. Mesmo com o mesmo rótulo, o sabor muda conforme a safra e a forma como foi armazenado.

Uma vez, a IA escreveu esta descrição para um vinho branco: "Um vinho fresco, leve e seco. Perfeito com carpaccio de frutos do mar."

Mas, quando abri a garrafa e provei de verdade, ele estava mais envelhecido do que eu esperava, com notas intensas, como de mel.

"Se eu servir isto como 'vinho leve e seco', a clientela vai se decepcionar... Combina mais com frango ao molho cremoso do que com carpaccio."

Corrigi na hora o texto que o Gemini tinha produzido.

- Antes (IA): "Fresco e leve. Bom para entradas"

- Depois (humano): "Encorpado e rico, pelo envelhecimento. Forte o bastante para acompanhar um prato principal"

A IA faz 90% do rascunho, e a pessoa prova e acrescenta "os últimos 10% (a alma)".

Essa conferência é responsabilidade de quem administra um restaurante, e é algo que a IA nunca poderá imitar.

Não "porque a IA disse", mas "porque eu bebi e estava delicioso".

Para servir com essa confiança, até hoje provo o vinho recém-aberto com uma carta feita pela IA em uma das mãos.

#### Coluna 3: Dicas para Fotografar de Modo que a IA Veja "Corretamente"

~ Como mostrar um rótulo a um sommelier ~

Quando você envia uma foto ao Gemini, alguns truques simples podem melhorar muito o reconhecimento do que ele vê.

1.  Evite reflexos: os rótulos das garrafas refletem a luz com facilidade, então mude um pouco o ângulo ou faça sombra com o corpo ao fotografar.

2.  Tire várias fotos e envie juntas: para coisas como o conteúdo de uma geladeira, envie uma foto aberta e fotos de perto, e a IA reconhecerá até os itens que estão em pontos cegos.

3.  Aponte com o dedo: também ajuda apontar o local que você quer que a IA olhe enquanto tira a foto. Escreva algo como "estou apontando com o dedo" no prompt. É o mesmo que apontar para o cardápio em um restaurante no exterior.

## Capítulo 5: Aplicações - Análise de Negócios e Melhoria do Lucro

~ Desenterre a "mina de ouro invisível". Uma reunião de gestão com a sua IA consultora ~

### 5-1. A Noite em que Quebro a Cabeça com uma Calculadora no Fim de Todo Mês

Para quem tem um pequeno restaurante independente, nenhuma hora pesa tanto quanto o fechamento mensal.

Na quietude da madrugada, somando os dados do caixa e digitando tudo no Excel, a única coisa que se ouve é o próprio suspiro.

"A meta de vendas deste mês era de ○○0.000 ienes. ...Não bati."

"O número de clientes não está ruim. No fim de semana ficamos lotados. Mas, por algum motivo, o gasto por cliente não cresce."

Por que não consigo bater a meta? A comida deve estar boa. Estou me esforçando no atendimento.

"Será que os preços estão altos demais?"

"Não, se baixar mais, não terei lucro. E o custo dos ingredientes também está subindo."

Perguntas sem resposta rodam e rodam na cabeça, e no fim eu encerro com palavras de incentivo: "No mês que vem coloco mais garra e insisto mais nas recomendações." Era um mau hábito meu e de muita gente que toca um estabelecimento.

Mas agora tenho um conselheiro sem emoções.

Encarei o Gemini com os dados de vendas daquele mês e os dados do cardápio do estabelecimento.

### 5-2. Um Experimento: Fazer a IA Ler "Visual" e "Números" ao Mesmo Tempo

Desta vez, entreguei três informações ao Gemini.

Joguei tudo misturado: o "design (lado direito do cérebro)" e os "números (lado esquerdo do cérebro)", que eu sempre gerenciara em separado.

1.  "A meta de vendas deste mês"

- O meu desejo sincero. O número que eu preciso bater de qualquer jeito.

2.  "Todos os dados das comandas de vendas recentes (CSV/Excel)"

- O resultado na realidade. Os fatos frios de quem pediu o quê, e a que preço.

3.  "Um arquivo PDF do cardápio atual"

- O mundo que a clientela enxerga. Informações visuais como a posição das fotos, o tamanho e a cor do texto.

E então fiz esta pergunta.

Não era uma ordem de serviço como o "faça uma imagem" de antes. Era uma pergunta, do tipo que se faz a quem nos aconselha na gestão.

> "Compare os dados de vendas atuais (a realidade) com o layout do cardápio (a aparência).
>
> Aponte o gargalo: o que está faltando para alcançar a meta de ○○0.000 ienes?"

### 5-3. A "Suposição de Quem Administra" que a IA Enxergou

Alguns segundos depois, a resposta do Gemini chegou e acertou em cheio o meu ponto cego.

Eu esperava conselhos genéricos como "Vamos desenvolver um novo item de cardápio" ou "Vamos divulgar nas redes sociais".

Mas o que a IA apontou foi um fato que eu vinha tentando esconder sem perceber.

A resposta do Gemini:

> "Cruzando os dados com o cardápio, encontrei uma grande oportunidade perdida.
>
> O plano de bebida à vontade, que tem alta margem de lucro e pode elevar de forma segura o gasto por cliente, está listado no cardápio atual (Antes) apenas em texto, discretamente, no canto inferior esquerdo.
>
> Já o melhor lugar do cardápio, bem no alto, abriga o barato 'Set ¥2.200 (cerca de US$ 15)'. Assim, a clientela é levada para o plano mais barato e nem chega a notar a opção de bebida à vontade, de preço mais alto."

Olhando para a tela, não consegui evitar um resmungo. Era exatamente isso.

Nós temos, sim, um plano de bebida à vontade. Mas, em algum canto da minha mente, eu pensava assim:

"Não somos uma rede de izakaya *(um bar casual japonês que serve comida e bebida)*. Vender bebida à vontade em letras grandes passa uma imagem barata."

"Quero que as pessoas saboreiem o gosto do vinho, então só quem conhece deveria pedir."

Essa minha "ideia fixa" apareceu no layout do cardápio, no texto lá embaixo.

![O cardápio Antes. A opção de bebida à vontade fica no canto inferior esquerdo e não chama atenção. Também é difícil perceber que a comida é vendida à parte](images/fig-21.png)

A IA não deixou passar.

"Você quer bater a meta, certo? Então coloque bem no alto, com orgulho, o menu que você mais quer vender, o que inclui bebida à vontade."

### 5-4. Sem Material de Imagem? Então Deixe a IA Desenhar Isso Também

Tomei a decisão. "Se parecer descolado só faz as vendas caírem, vou tentar de qualquer jeito."

Mas aí surgiu um problema.

"Mesmo colocando em destaque no alto, só com texto fica fraco..."

E, se eu pegar de um site de imagens gratuitas a foto de pessoas brindando com cerveja, o cardápio imediatamente parece de uma rede de restaurantes. Não combina com o clima do meu estabelecimento.

Não tenho talento para desenhar, e contratar uma pessoa ilustradora custa dinheiro e tempo.

Comecei a me preocupar, "O que eu faço...?", mas logo me lembrei.

"É verdade, tenho uma subgerente (a IA) que sabe desenhar."

Eu tinha encontrado, em um site de materiais gratuitos, algo próximo da imagem que queria. Dizia que modificações eram permitidas.

Digitei então na caixa de bate-papo:

> "Desenhe uma ilustração para colocar no topo do cardápio. Use a imagem anexa como base.
>
> Quero a sensação de pessoas brindando felizes, mas sem parecer barato.
>
> Faça em um estilo simples, de desenho de traço."

Poucos segundos depois, quatro opções de ilustração apareceram na tela.

Entre elas, escolhi a ilustração simples e acolhedora de "Saúde!" que mais combinava com o clima do estabelecimento.

![A ilustração "Saúde!" que a IA gerou em apenas 10 segundos](images/fig-22.png)

Levou só 10 segundos.

Não só a análise: o "material" necessário para a melhoria também pode ser providenciado na hora.

Este é o verdadeiro poder de incorporar a IA generativa à gestão.

### 5-5. Só Mudar o Layout Aumentou em Cerca de 40% o Gasto por Cliente

Então redesenhei o cardápio.

#### Antes: O Cardápio como Era

- Melhor lugar (bem no alto): itens de preço baixo, como "Set ¥2.200 (cerca de US$ 15)" e "Set Menu ¥3.300 (cerca de US$ 22)".

- Bebida à vontade: listada só em texto, no canto inferior esquerdo, como "Bebida à vontade a partir de ¥3.000 (cerca de US$ 20)". Estava completamente enterrada.

#### Depois: O Cardápio Revisado

- Melhor lugar (bem no alto): planos de preço mais alto, de ¥4.500–¥5.700 (cerca de US$ 30–US$ 38), apresentados como "A nossa escolha! Menu Aproveite Tudo (com bebida à vontade)".

- Design: com a ilustração "Saúde!" gerada pela IA, ele guia o olhar com força, de forma visual, para "Olhe aqui primeiro".

- Mudança de layout: os sets baratos que antes eram as estrelas foram movidos para baixo.

![O cardápio Depois. O menu com bebida à vontade fica bem no alto](images/fig-23.png)

A comida, os preços e a qualidade das bebidas estão, na verdade, quase iguais. Só mudei "como é mostrado" e "onde".

E o resultado?

Desde o dia seguinte, o comportamento de pedido da clientela mudou drasticamente.

As primeiras palavras de quem abria o cardápio deixaram de ser "Uma cerveja, para começar" e passaram a ser "Então vamos de 'Menu Escolha da Casa (¥4.900 (cerca de US$ 33))', o da ilustração".

A clientela que antes encerrava com "o Set (¥2.200 (cerca de US$ 15)) mais duas bebidas" (um gasto de cerca de ¥3.500 (cerca de US$ 23) por pessoa) agora escolhia o menu de ¥4.900 (cerca de US$ 33) desde o começo.

Só com isso, o gasto por cliente saltou ¥1.400 (cerca de US$ 9,3).

Além disso, a clientela ganhou o benefício de "poder beber sem se preocupar com a conta", então a satisfação subiu, em vez de cair.

### 5-6. Conferindo as Respostas com o PDF de Vendas de Dezembro (PDCA)

Tinha passado um mês desde que pus a medida em prática.

Não parar por aqui é a essência de usar a IA.

Muita gente que toca um estabelecimento julga os resultados pela sensação e deixa por isso mesmo: "Estava movimentado, então deve ter funcionado" ou "As vendas subiram, então está bom".

Mas encarei o Gemini de novo.

Desta vez, enviei o "PDF dos dados de vendas de dezembro", em que os resultados já constavam, e perguntei isto:

> "Os resultados da medida do mês passado (a mudança do cardápio) já saíram.
>
> Veja estes dados de vendas de dezembro e faça a validação (avalie): o número de pedidos do 'Menu Escolha da Casa' aumentou como o esperado, e como isso afetou o gasto por cliente?"

O Gemini analisou os dados na hora e me devolveu um relatório.

![Tela do relatório de análise de vendas do Gemini: fiz um resumo para publicação, então o conteúdo difere em parte do texto abaixo](images/fig-24.png)

A análise do Gemini:

> "Os resultados são excelentes. Olhando a tendência dos dados, o número de pedidos do 'Menu Aproveite Tudo' subiu para cerca de 1,8 vez o do mês anterior.
>
> Como resultado, o gasto geral por cliente subiu, em média, ○○ ienes.
>
> O principal fator é que colocar o plano de bebida à vontade mais acima elevou o valor dos pedidos, especialmente nos grupos."

Ao ouvir essas palavras, senti um alívio verdadeiro pela primeira vez.

Não era "de alguma forma ganhamos dinheiro", mas a confiança de "mirei e fiz os números".

Isso vira a força motriz para a próxima medida.

1.  Plan (Planejar): olhar os dados de vendas e o cardápio e encontrar o problema (o plano de bebida à vontade está escondido).

2.  Do (Fazer): pedir à IA que desenhe uma ilustração e mudar o layout do cardápio.

3.  Check (Verificar): pedir que leia o PDF de vendas de dezembro e confirmar os resultados.

4.  Act (Agir): pensar em revisar, em seguida, o layout do cardápio de comidas.

O "ciclo PDCA" que as grandes empresas rodam a um custo enorme pode ser rodado por uma pessoa só, como eu, apenas com um celular, se tiver a IA como parceira.

## Capítulo 6: Desafios - Desenvolvendo um Sistema Só para o Meu Estabelecimento

~ "Se não existe, construa." Um projeto de desenvolvimento de sistema sem especialistas ~

※Só para deixar claro: você não precisa fazer tudo o que está neste livro.

・Enviar uma imagem e pedir que a IA escreva um texto\
・Transformar uma mensagem longa do LINE em um diagrama

Esses dois já bastam para começar. Só isso com certeza vai facilitar o seu trabalho.\
Também basta ler isto como uma história e pensar: "Então dá para fazer até isso com a IA."

### 6-1. Aplicativos Prontos Não Atendem às Minhas Necessidades Exatas

Até aqui falei de usar a IA em cima de plataformas já existentes, como a geração de imagens e a análise de cardápio.

Mas, conforme você toca o negócio, surgem preocupações que os "aplicativos prontos" simplesmente não resolvem.

Em especial, num modelo de negócio fora do comum como o nosso, "curry de dia, bar à noite", o fluxo de dinheiro que entra e sai também é complicado.

"Quero cruzar o saldo do meu PayPay Bank com os pagamentos futuros e saber o valor com que vou chegar ao fim do mês."

"As datas de pagamento se dividem entre o dia 10 e o dia 25. Quero simular isso."

Os softwares de contabilidade que existem são muito capazes, mas nenhum acertava em cheio "a preocupação que estava na minha cabeça naquele momento".

Então tomei a decisão.

"Se não existe, eu construo. Tenho o Gemini, o melhor engenheiro que existe."

### 6-2. Fases 1 a 3: De Anotações Rabiscadas à "Nuvem"

O desenvolvimento começou mostrando ao Gemini as minhas anotações no Google Keep.

![A nota do Keep que foi o ponto de partida do desenvolvimento](images/fig-25.png)

#### Fase 1: Construindo a Lógica

"Quero automatizar os cálculos desta nota."

Atendendo ao meu pedido, o Gemini montou rapidamente a lógica de cálculo.

- Quando altero o valor de um item, ele calcula na hora o saldo final.

- Se o dinheiro está prestes a faltar, mostra um "alerta" em vermelho.

- Simula o momento dos pagamentos divididos entre "o dia 10" e "o dia 25 / fim do mês".

- Os dados são salvos no navegador (cache).

Só isso já era bem conveniente, mas deu vontade de pedir mais. "Quero que os dados continuem lá mesmo depois de fechar o navegador. Quero conferir também no celular."

#### Fase 2: Adotando uma Ferramenta Desconhecida, o "Firebase"

Eu vinha pensando em ligar a uma planilha, mas a sugestão do Gemini foi inesperada.

"Pensando em tempo real e eficiência, vamos usar o 'Firebase', do Google. O plano gratuito é suficiente para rodar."

"Firebase...?" Eu nunca tinha ouvido a palavra. Mas, com o instinto dos meus tempos de coordenação de sistemas, decidi: "Se a IA recomenda com tanta firmeza, vamos nessa."

Como resultado, ao usar um banco de dados chamado Firestore, os dados passaram a ficar guardados com segurança na nuvem.

#### Fase 3: Login do Google e um Sistema de Aprovação

É sobre dinheiro, então é ruim se qualquer um puder ver.

No começo pensei em algo como uma "frase-senha", mas o Gemini sugeriu: "Se você quer mais segurança, vamos usar o login do Google."

Depois, quando eu disse "Quero que só a equipe que eu aprovar consiga ver", ele chegou a montar "um sistema em que a administração pode aprovar e remover membros na tela".

### 6-3. Fases 4 e 5: Enfrentando a Tela Preta (o Terminal)

A partir daqui veio o maior obstáculo do vibe coding: publicar o aplicativo na internet (fazer o deploy).

#### Aviso: Daqui em Diante É o Curso "Faixa Preta"

As próximas páginas são a parte "mão na massa" mais difícil deste livro. Você vai operar uma "tela preta (terminal)" como as que hackers usam nos filmes.

Falando com franqueza: aqui você com certeza vai encontrar erros. Eu também encontrei. Você vai esbarrar em muros como um "erro de permissões do PowerShell", que parece escrito em feitiços. Mas não tenha medo. O que se faz aqui é o mesmo de sempre: "tirar uma captura de tela do erro e jogar para a IA."

A verdade que aprendi nos meus tempos no ramo de sistemas é esta: "Até profissionais encontram erros. A única diferença é se, quando um aparece, a pessoa desiste ou procura (pergunta) por ajuda." Se parecer difícil demais, pule esta seção e leve apenas a possibilidade: "Dá para fazer até isso com a IA."

O Gemini disse:

"Vamos preparar o ambiente de desenvolvimento no seu PC com Windows. Instale o 'Node.js' e digite os comandos a seguir no 'VS Code'."

Abri a tela preta (terminal) como indicado e, na hora, deu erro.

"Não é possível executar por causa das restrições de segurança do PowerShell."

Muita gente perderia o ânimo aqui.

Mas copiei e colei a tela do erro e joguei para a IA.

A IA respondeu na hora: "Remova a restrição com um comando chamado 'Set-ExecutionPolicy'."

Sem entender o que significava, digitei o comando, depois npm run build, firebase deploy...

Cada vez que eu digitava aqueles caracteres de feitiço, o texto corria pela tela e o processo avançava.

E, por fim, o meu aplicativo apareceu na web.

#### Fase 5: Transformando em Aplicativo de Celular (PWA)

O aplicativo publicado estava, no início, "de cara limpa", com o design quebrado, mas isso também foi resolvido ao acrescentar uma configuração chamada "Tailwind CSS".

Depois, quando pedi "Quero colocar um ícone na tela inicial do celular e usar como um aplicativo", ele me ensinou as configurações para transformá-lo em um "PWA (Progressive Web App)".

E assim nasceu, dentro do meu celular, um aplicativo exclusivo que eu mesmo fiz (sem escrever uma única linha de código).

![A tela do aplicativo pronto de gestão do fluxo de caixa](images/fig-26.png)

### 6-4. Fase 6: O Problema Depois de 30 Dias e a Solução

Cerca de um mês depois de eu começar a usá-lo, surgiu um problema.

"Funcionava até ontem, e de repente não consigo acessar!"

Entrei em pânico e consultei o Gemini, e a causa estava num lugar inesperado.

"As configurações do banco de dados (Firestore) ainda estavam em 'modo de teste (limitado a 30 dias)'. Ele expirou."

Para poupar o trabalho de configuração no início do desenvolvimento, a IA tinha definido de propósito uma regra com data de validade.

"Vamos reescrever as regras de segurança para que 'qualquer usuário com login feito possa continuar usando'."

Quando reescrevi algumas linhas do arquivo de configurações conforme a IA indicou, o aplicativo voltou a funcionar normalmente.

Esse problema também foi uma boa experiência para mim.

Aprendi que "um sistema é uma coisa viva e precisa de manutenção".

E ganhei a tranquilidade de que "mesmo que aconteça um problema, sempre há uma resposta se eu perguntar à IA".

### 6-5. Estudo de Caso 2: O "Projeto de Reconhecimento Facial" que Começou com um Vídeo de Demonstração no X (Antigo Twitter)

Aqui está outro desenvolvimento de sistema que encarei, e o maior de todos.

É "um sistema que reconhece, por uma câmera, a clientela que entra e me diz discretamente o nome, os dados e as preferências de cada pessoa".

Tudo começou no X, a rede social em que eu rolava a tela sem compromisso.

Apareceu no meu feed um vídeo de demonstração publicado por um engenheiro: usava a IA embutida no Google Chrome (Built-in AI) para explicar, em tempo real, o que uma webcam estava vendo.

O instinto de quem veio da área de sistemas falou mais alto.

"Isto é 'multimodal'. E, se está embutido no navegador, não daria para rodar tudo no meu próprio PC, sem pagar pela nuvem?"

Se isso funcionasse, eu talvez pudesse construir um sistema de hospitalidade só para o meu estabelecimento, sem instalar um sistema caro.

Copiei a URL e joguei para o Gemini.

"Quero fazer a mesma coisa que isto. Me diga como implementar."

#### Fase 1: Funcionou, mas Eu Não Conseguia Saber "Quem"

Mudei as configurações do Chrome (flags) como o Gemini instruiu e colei o código, e o mesmo sistema da demonstração rodou sem problemas.

Quando apareci na câmera, a tela exibiu isto:

"Uma pessoa de óculos está sentada diante de um PC."

Ele usa uma IA embutida no navegador chamada GeminiNano. A vantagem é que funciona inteiramente dentro do navegador, sem conexão com a nuvem, mas só reconhece coisas gerais, como "óculos" e "pessoa". Não chega a determinar quem é a pessoa.

É uma tecnologia incrível. Mas, como quem administra um restaurante, me decepcionei logo.

"Assim não serve."

O que eu quero saber não é uma característica geral como "uma pessoa de óculos", mas a identificação do indivíduo: "É a pessoa A ou a pessoa B?"

#### Fase 2: O Muro da Integração com o Google Fotos e a Resposta da IA

Então apresentei uma ideia ingênua ao Gemini.

"Conecte este sistema ao meu Google Fotos. Lá há dados de agrupamento de rostos dos meus amigos e da clientela fiel, então, se cruzar com isso, dá para obter os nomes, certo?"

A resposta do Gemini foi fria, mas correta.

"Sinto muito, mas isso não é possível. Os dados de reconhecimento facial do Google Fotos são informações de privacidade altamente sensíveis e, por segurança, não é permitido que programas externos os usem."

Justo. O caminho parecia acabar aqui.

Mas a partir daí veio a verdadeira essência do "vibe coding (desenvolvimento por meio do diálogo)". A IA não se limitou a recusar.

#### Fase 3: Uma Alternativa e uma Virada

O Gemini continuou, sugerindo isto:

"Não podemos usar o Google Fotos, mas é possível construir o seu próprio sistema de reconhecimento facial em um ambiente local, usando bibliotecas de código aberto (como OpenCV ou face_recognition). Vamos tentar?"

Respondi "Sim" na hora.

A partir daí, o plano de desenvolvimento mudou por completo. Em vez de usar os recursos do Chrome, eu construiria um sistema de reconhecimento facial do zero usando uma linguagem de programação chamada Python.

#### Fase 4: Lutando com a Tela Preta e Conectando a uma Planilha

O que eu tinha de fazer não mudou. Perguntei ao Gemini "como instalar as bibliotecas necessárias" e colei a resposta na tela preta (o prompt de comando).

Quando aparecia um erro, eu devolvia o texto vermelho ao Gemini do jeito que estava.

Algumas horas depois, o sistema ficou finalmente pronto.

1.  A webcam captura o meu rosto.

2.  Ele cruza com os "dados de fotos de rostos" de uma pasta do PC.

3.  Ao encontrar uma correspondência, consulta a lista de clientes em uma Planilha Google.

4.  A tela exibe "Bonta: garrafa Kaku (uísque Suntory Kakubin), restam ○○ g."

![O sistema de reconhecimento facial em funcionamento. Ele reconhece o rosto de quem administra o estabelecimento e exibe as informações. A imagem capturada foi coberta com mosaico usando o Gemini](images/fig-27.png)

Custo de terceirização: ¥0 (cerca de US$ 0,00). Meu trabalho de programação: zero.

Foi o momento em que um "sistema de CRM com reconhecimento facial" único no mundo nasceu num canto de Higashi-Nakano.

#### Fase 5: E Então Percebo a "Responsabilidade de Proteger"

O sistema estava pronto. Mas, junto com a alegria, senti um arrepio na espinha.

"Espere um pouco. Neste momento, este computador guarda dados faciais (informações biométricas) da clientela, não é...?"

Até então eu pensava: "Se funciona, está bom." Mas, depois que entra em operação de verdade, a história é outra.

E se este computador for infectado por um vírus? Os dados faciais da clientela e as informações sobre suas preferências (dados pessoais) podem vazar juntos.

Um PC isolado, sem conexão com a internet, seria seguro, mas, enquanto eu cuidar de reservas e redes sociais, a conexão com a internet é indispensável.

"Conseguir construir uma ferramenta útil" e "conseguir gerenciá-la com segurança" são coisas diferentes.

Foi aqui que senti de verdade, pela primeira vez, a importância do "seguro contra riscos cibernéticos" de que um corretor de seguros tinha falado quando veio me oferecer um plano.

Eu tinha rido: "Um estabelecimento pequeno como o nosso não sofre ataques cibernéticos", mas agora que a IA nos permite construir sistemas avançados, quem toca um estabelecimento por conta própria também assume a responsabilidade de ser uma pessoa gestora de dados de verdade.

Com a IA, você consegue ferramentas mágicas.

Mas aprendi que carregar o "cajado (o letramento)" e o "escudo (as medidas de segurança)" para usar essa magia também passa a fazer parte do trabalho de quem administra um negócio.

### 6-6. A "Responsabilidade" e o "Seguro" que Vêm com a Liberdade

#### Importante: Privacidade e Dados Pessoais

Este "sistema de reconhecimento facial" é um protótipo experimental que construí para testar o que é tecnicamente possível. Se você for usá-lo num estabelecimento de verdade, os dados faciais da sua clientela contarão como "dados pessoais (dados biométricos)" e precisarão ser rigorosamente protegidos pela lei (a Lei de Proteção de Informações Pessoais do Japão).

Se você está pensando em adotar algo assim, guarde sem falta estes dois pontos.

Avise a clientela e obtenha o consentimento: é preciso um procedimento, como colocar na entrada um aviso dizendo "Usamos reconhecimento facial por IA" e pedir o consentimento quando a pessoa se cadastrar como cliente. Filmar em segredo é absolutamente proibido.

Proteja os dados: são necessárias medidas que reduzam a zero o risco de vazamento, como gerenciar os dados em um ambiente isolado da internet.

Conseguir construir algo não é o mesmo que ter permissão para fazê-lo. Se você tem habilidades técnicas, lembre-se de que a responsabilidade de usar essa tecnologia vem junto.

Até aqui falei do quanto um sistema feito à mão pode ser maravilhoso. Mas, como quem administra um negócio, preciso contar também uma realidade dura.

É esta: "Tudo o que você constrói por conta própria é de sua responsabilidade."

Num serviço de assinatura mensal (SaaS), se o servidor cai, a empresa pede desculpas e o recoloca no ar.

Mas um sistema feito com vibe coding não tem "atendimento ao cliente".

Se o seu aplicativo parar de repente no pico do almoço, ninguém virá ajudar.

Quando o Google muda uma especificação, um código que funcionava bem ontem dar erro hoje é um acontecimento comum.

Por isso faço duas preparações.

Uma é o "backup analógico".

"Se o reconhecimento facial parar, olhe o caderno de clientes em papel." "Se o aplicativo do caixa cair, use a calculadora e comandas escritas à mão."

As ferramentas digitais são apenas "ferramentas convenientes". Você não pode depender delas a ponto de, quando elas param, o seu estabelecimento parar junto.

A outra é o "seguro" que mencionei antes.

O seguro de responsabilidade cibernética cobre não só o risco de vazamento de informações, mas também a indenização pela perda de negócios quando um erro seu paralisa o sistema. Para quem toca um negócio sem ajuda e se arma de TI, faz parte de agir com responsabilidade.

"Às vezes as coisas vão parar. Às vezes vou errar."

Tome isso como ponto de partida, aceite o risco e tome medidas contra ele.

Só quando temos essa determinação conseguimos realmente usar um "sistema livre" que não presta contas a ninguém.

### 6-7. Você Não Precisa de Especialistas. Precisa de Persistência

Não paguei nem um iene de terceirização no desenvolvimento destes dois sistemas.

Usei apenas uma assinatura de IA de alguns milhares de ienes por mês e a persistência de quem pensava: "Preciso eliminar de vez esta preocupação (com o fluxo de caixa)" e "Quero deixar a minha clientela feliz."

Não é questão de "não consigo, porque não sei programar".

Se você tem algo que quer construir (o Want, o que se quer), a IA ensina como construir (o How, o como).

Mesmo quando aparecem palavras que você não entende (Node.js, PowerShell, Firestore...), não há nada a temer.

Temos o melhor parceiro que existe, o "Gemini", para traduzi-las e nos guiar.

#### Coluna 4: Qual É a Diferença entre o Excel e um Banco de Dados (Firestore)?

~ É um "bloco de notas para você ler" ou um "livro-razão para o sistema ler"? ~

O Firebase (Firestore) apareceu no desenvolvimento do aplicativo de fluxo de caixa. Talvez você tenha se perguntado: por que não o Excel?

Uma planilha (Excel) é um "caderno que as pessoas olham e no qual digitam". É muito flexível, mas, para um sistema, é vaga quanto a "o que está onde".

Já um banco de dados (Firestore) é um "armário bem organizado, feito para o sistema". Como está definido que "a data vai no compartimento 1 e o valor no compartimento 2", um programa consegue lidar com ele na hora. Ele também não quebra quando várias pessoas acessam ao mesmo tempo.

"Se você está construindo um aplicativo, use um banco de dados, não o Excel." Só de saber isso, o nível das suas instruções à IA já sobe.

## Posfácio: Uma "Receita do Futuro" que Só o Seu Estabelecimento Tem

~ A IA não é uma tecnologia difícil. É uma nova parceira de "conversa" ~

Agradeço por ler este livro até o fim.

Se for tentar apenas uma coisa deste livro, tente esta: "Cole aquela mensagem irritante do LINE direto na IA e peça: 'transforme em um diagrama.'"

Não sou nenhum grande especialista em IA. Apenas repeti, todos os dias, a prática de "conversar com a IA nas palavras do local de trabalho", \
no campo de batalha de um restaurante.

Por isso acho que basta você levar deste livro não uma "coleção de respostas certas", mas apenas um "jeito de pensar".

Quando abriu a primeira página, que imagem você tinha da expressão "usar IA"?

"Parece difícil." "Precisa saber programar, não é?" "Não tem nada a ver com um estabelecimento pequeno como o meu."

Talvez você tenha pensado algo assim.

Mas, agora que leu até aqui este registro das minhas "tentativas e erros", talvez essa imagem tenha mudado um pouco.

O que fiz não foi explorar ao máximo uma tecnologia de TI avançada.

Resmunguei: "Isto eu não consigo fazer à mão." Reclamei: "Isto é difícil de usar." E fui exigente, dizendo: "Quero que funcione mais assim."

Hoje em dia, no mundo dos engenheiros, o termo "vibe coding" é uma tendência.

É um método de construir um sistema pela intuição, conversando com a IA.

Assim como quem joga shogi conversa com a IA para ler as próximas jogadas, nós também podemos conversar com a IA e construir o "futuro dos nossos estabelecimentos".

Como dizer à equipe da cozinha: "Põe só mais um pouquinho de sal."

Como perguntar ao peixeiro do mercado: "Tem peixe bom hoje?"

Falar com a IA e dizer: "Facilite este trabalho." É aí que tudo começa.

Eu já trabalhei no departamento de sistemas de uma empresa, fazendo a coordenação entre a "linha de frente" e os "desenvolvedores".

Agora faço a mesma coisa entre o "meu próprio estabelecimento" e a "IA".

E tenho esta convicção:

"Quem conhece os problemas da linha de frente pode se tornar a pessoa mais forte no comando da IA."

Comece hoje, você também.

Primeiro, pegue o celular e converse com o Gemini.

"Ei, por onde devo começar o preparo de hoje?"

"Como posso fazer este item do cardápio vender mais?"

"Esta papelada é um saco. Dá para fazer alguma coisa?"

Não se preocupe se aparecer um erro. É sinal de que a "conversa" começou.

É só tirar uma captura de tela e mandar de volta com um "tem algo estranho".

Depois de tantas conversas, esperam por você um "tempo" e uma "folga" que você jamais imaginaria, e "um futuro que pertence só ao seu estabelecimento".

Agora, vamos contratar também para o seu estabelecimento uma "subgerente" confiável.

Porque a receita do futuro nascerá da conversa entre você e a IA.

### As Três Saídas Deste Livro

Este livro pode ser lido de graça em PDF, no note e no Google Play. (Só no Kindle, as regras da loja exigem um preço mínimo.) Em troca, preparei três lugares aonde você pode ir depois de terminar a leitura. Se usar ao menos um deles, terá valido a pena escrever este livro.

1. Experimente no seu estabelecimento. A série Agenda pode ser iniciada com um caderno gratuito. https://bontallc.com/agenda?via=b1-pt-{{FMT}}
2. Acompanhe o que eu faço. Escrevo sobre as próximas ferramentas que construo e sobre o dia a dia do bar no note e no X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Se um dia vier a Tóquio, visite o Tamuro. A um minuto da saída leste da estação Higashi-Nakano. Dá para entrar sem reserva. Site de reservas https://tamuroreservation.vercel.app/?src=b1-pt-{{FMT}}

Para quem veio por causa deste livro: ao fazer a reserva, digite o código de cupom "BOOK". Serviremos uma bebida na primeira visita. Se você veio sem reserva, basta dizer "vi o livro" ao fazer o primeiro pedido. Serviremos a mesma bebida. É um pequeno artifício para que eu possa contar quantas pessoas vieram por causa do livro.

### Sobre o Autor

Raku Bonta

Uma pessoa que toca sozinha um restaurante de 11 lugares no balcão e 8 lugares na sala de tatame, em Higashi-Nakano, Tóquio.

De dia, é uma casa de curry com bife de hambúrguer estilo japonês, perfumada de especiarias. À noite, é um bar-restaurante, que serve uma refeição fixa que muda a cada dia.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry](images/fig-28.png)

▼ Bar "Tamuro"

https://www.instagram.com/tamuro.higashinakano/

![Bar "Tamuro"](images/fig-29.png)

O estabelecimento também se dedica a construir comunidade por meio da comida, com eventos de vinho quinzenais, uma aula de culinária por mês e jantares de vários pratos.

Antes de abrir o estabelecimento por conta própria, há 12 anos, Raku Bonta trabalhava numa empresa em "planejamento de sistemas" e "arquitetura de soluções".

Os cargos soam difíceis, mas o trabalho real era o de "coordenação que transmite com precisão aos fornecedores de TI o desejo da linha de frente de 'queremos fazer isto' e faz com que seja construído". Longe de ser programação avançada, o percurso foi o de um trabalho de "tradução" que liga pessoas e tecnologia.

Hoje, com base nessa experiência, Raku Bonta usa IA generativa, como o Google Gemini, para tocar o próprio estabelecimento, praticando e compartilhando uma "reforma dos negócios que funciona mesmo com zero conhecimento especializado".
