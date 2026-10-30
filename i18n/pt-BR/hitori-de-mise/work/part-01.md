## Introdução

Este livro é um registro feito em janeiro de 2026. Parte do meu jeito de tocar o estabelecimento, e alguns nomes e especificações das ferramentas de IA, mudaram desde então. A continuação, *Feito para o Nosso Bar*, retoma a história.

### Por que um ex-profissional de sistemas conversa com a IA num restaurante no subsolo

Agradeço por ter escolhido este livro.

*Uma Pessoa Toca o Estabelecimento, e a IA Chegou ao Lado.*

Ao ler esse título, algumas pessoas talvez pensem: "Isso é a minha cara." Outras podem se perguntar: "O que quer dizer a IA chegar ao lado?"

Este não é um livro técnico sobre programação difícil. É um livro para quem tem um restaurante, fica na cozinha todo dia, faz o preparo e vive correndo com a clientela.

Deixe-me contar um pouco sobre mim.

Hoje toco um pequeno restaurante no subsolo de um prédio em Higashi-Nakano *(um bairro residencial no oeste de Tóquio, logo a oeste de Shinjuku)*, em Tóquio.

Ele tem duas faces. De dia, é uma casa especializada em curry com bife de hambúrguer estilo japonês, aromatizado com especiarias. À noite, é um bar-restaurante só por indicação, com prato do dia e bebidas.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Bar só por indicação "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar só por indicação "Tamuro" (Instagram)](images/fig-02.png)

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