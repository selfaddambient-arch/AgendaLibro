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
