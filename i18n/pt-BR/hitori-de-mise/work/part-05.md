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
