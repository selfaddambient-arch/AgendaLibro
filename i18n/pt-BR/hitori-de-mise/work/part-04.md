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