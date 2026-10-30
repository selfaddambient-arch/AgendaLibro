## Introducción

Este libro es un registro a enero de 2026. Algunas de mis formas de llevar el local, y algunos nombres y especificaciones de las herramientas de IA, han cambiado desde entonces. La historia continúa en el segundo libro, *Hecho a la medida de nuestro bar*.

### Por qué alguien que venía del mundo de los sistemas conversa con la IA en un restaurante subterráneo

Gracias por elegir este libro.

*Una sola persona atiende el local, y la IA apareció a mi lado.*

Al ver ese título, tal vez algunos de ustedes piensen: "Ese soy yo." Otros quizá se pregunten: "¿Qué significa que la IA aparezca a su lado?"

Este no es un libro técnico sobre programación difícil. Es un libro para personas como ustedes, quienes dirigen un restaurante, están cada día en la cocina, hacen la preparación y no dan abasto atendiendo a la clientela.

Permítanme contarles un poco sobre mí.

Ahora dirijo un pequeño restaurante en el sótano de un edificio en Higashi-Nakano *(un barrio residencial del oeste de Tokio, justo al oeste de Shinjuku)*, en Tokio.

Tiene dos caras. De día, es un local especializado en curry con hanbāgu *(bistec de carne picada a la plancha al estilo japonés, parecido al hamburg steak)*, con un aroma intenso a especias. De noche, es un bar-restaurante solo por recomendación, que ofrece un menú del día y bebidas.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Bar solo por recomendación "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar solo por recomendación "Tamuro" (Instagram)](images/fig-02.png)

Es un espacio acogedor, con apenas 11 asientos en la barra y 8 en una plataforma elevada de tatami.

Pero no nos limitamos a servir comida.

Hacemos un evento de vino cada dos semanas, y una vez al mes planeamos una clase de cocina o un día especial de menú de varios tiempos. Aunque estemos en un sótano estrecho, andamos ocupados y en movimiento todos los días.

Este año cumplo doce años al frente del local.

Antes trabajaba en una empresa. Mi trabajo era la "planificación de sistemas" y la "arquitectura de soluciones".

Cuando lo digo, a veces me responden: "O sea que desarrollaba sistemas impresionantes." En realidad no es así.

Lo que yo hacía no era escribir código difícil. Escuchaba lo que querían las personas que trabajaban en el local, se lo transmitía con precisión a los proveedores de TI (empresas de desarrollo) y lo hacía construir. Mi función era la de "coordinación". En Japón, a ese puesto se le conoce como "persona de sistemas".

El personal del local deseaba: "Quiero que mi trabajo sea más fácil." Los ingenieros decían: "Necesitamos requisitos definidos con lógica."

Mi trabajo era ponerme en medio, interpretar el idioma de cada lado y guiar a todos hacia la meta.

Por eso entiendo las incomodidades y preocupaciones de personas como ustedes, quienes usan los sistemas, y también entiendo un poco cómo piensan quienes trabajan en informática.

Dejé la empresa hace doce años y abrí mi propio local. Desde entonces he tenido las mismas preocupaciones que ustedes.

La preparación que nunca termina, la falta de personal, la ansiedad por atraer clientela, las decisiones de gestión que cargo solo...

Por supuesto, cuando hay mucho trabajo, a veces cuento con la ayuda de empleados a tiempo parcial y de personal por contrato, gente en quien se puede confiar.

Pero, al fin y al cabo, son compañeros para las "tareas".

No hay nadie con quien consultar esas "decisiones de gestión" de tanto peso, como "¿Cómo manejo el flujo de caja del mes que viene?" o "¿Apuesto por este nuevo plato?"

Me preocupo, decido y asumo toda la responsabilidad. En ese sentido, siempre he estado "atendiendo el local solo". Y a mi lado, como confidente de ese "yo, quien dirige un negocio" que se sentía solo, se sentó la IA.

En esa situación llegó la IA generativa, y en particular una compañera llamada "Google Gemini".

La "coordinación" que antes hacía entre "el día a día del local" y los "proveedores de TI", ahora la hago por mi cuenta entre "los problemas del local" y la "IA". Y me di cuenta de algo.

No hace falta memorizar la sintaxis de lenguajes de programación difíciles (como Python).\
La IA ya la conoce. Pero el plano de "qué quiere que se haga, y en qué orden" es algo que solo una persona puede dibujar.\
Lo que yo acumulé en el área de sistemas fue justamente esta "capacidad de traducir lo que se necesita en el local en pasos lógicos".\
En este libro compartiré, sin guardarme nada, no solo cómo manejar la IA, sino también este "instinto lógico para hacer que la IA trabaje (pensamiento sistémico)".\
Con esto, pueden pasar de "cero conocimientos" a ser "quien mejor sabe encargarle trabajo a la IA".

※ Aquí quiero hablar con franqueza de un punto.

Vengo del mundo de los sistemas. Pero en los usos de la IA que presento en este libro, en realidad casi no hubo momentos en que los conocimientos de mi trabajo anterior ayudaran de forma directa.

Lo que ayudó no fue la "habilidad de escribir programas".\
Fue solo "el hábito de convertir las incomodidades difusas del día a día del local en palabras ordenadas".

Y este hábito no es un talento especial.\
Es "una intuición que ya posee toda persona que atiende un local cada día".

En este libro separaré a propósito lo que solo yo podía hacer\
de lo que ustedes pueden copiar tal cual, desde hoy mismo.

## Capítulo 1: Conceptos - Los agentes de IA, el nuevo tipo de empleado

~ Contrate a la IA como "compañera de trabajo", no como "alguien a quien consultar" ~

### 1-1. Los límites de quien dirige solo y los malentendidos sobre la IA

Dirigir un restaurante independiente como el nuestro es una carrera constante contra el tiempo. Preparación, cocina, servicio, caja, limpieza... todo debe resolverlo una sola persona, o un equipo pequeño.\
Aun si contratamos personal, quienes dirigimos un local independiente trabajamos, en la práctica, como un "negocio de una sola persona".

Eso es porque no tenemos "gerentes de local" ni "capacitadores" como las grandes cadenas.

Usted cocina mientras da indicaciones al personal de sala, enseña a las nuevas incorporaciones y organiza los turnos.

Todo este "procesamiento mental" se concentra en una sola persona: usted, quien dirige el local.

Puede que tenga más manos, pero sigue teniendo una sola cabeza. Justamente por eso necesita a la IA para apoyar esa "cabeza".

"Si tuviera una persona más en el equipo, alguien realmente capaz..."

Seguro que tiene ese pensamiento muchas veces al día.

Cuando digo "Usemos la IA", muchas personas que dirigen un local responden así:

"¿Te refieres a ChatGPT? Lo probé, pero solo escribe textos, ¿no? No sirve para el trabajo en el local."

En realidad, aquí hay un gran malentendido.

La mayor parte de la IA que hemos usado hasta ahora ha sido un "chatbot (alguien a quien consultar)". Pero lo que busca hoy la IA más reciente, empezando por Google Gemini, es la forma de un "agente de IA (una compañera de trabajo)".

Los dos se parecen, pero son cosas distintas. Comparémoslos con un trabajo concreto.

### 1-2. De "diccionario" a "miembro del personal"

Digamos, por ejemplo, que quiere hacer un cartel para un evento del local.

Con la IA del pasado (un chatbot):

Si pregunta: "Dígame cómo hacer un cartel", la IA explica los pasos como un diccionario o un libro de texto: "Mantenga el eslogan corto", "Elija los colores así".

Pero quien realmente se pone manos a la obra para hacer el cartel es usted. Su conocimiento ha crecido, pero su tiempo de trabajo no se ha reducido.

Con la IA del futuro (un agente de IA):

Usted solo da la instrucción: "Haga un cartel."

Entonces la IA piensa por sí misma para lograr el objetivo. Se le ocurre el eslogan, genera la imagen de fondo e incluso propone la distribución.

Como un excelente miembro del personal, usa herramientas, planifica y lleva a cabo el trabajo por su cuenta.

Lo que queremos no es una persona que aconseja con discursos de manual, sino una compañera que arrime el hombro a nuestro lado.

※ En este libro, a esta compañera confiable (la IA generativa como Google Gemini) la llamaré con cariño "subgerente (IA)".

※ En este libro uso como ejemplo a "Google Gemini", que es la que más utilizo, pero la mayoría de las ideas que presento se pueden reproducir casi igual con otras IA generativas como ChatGPT y Claude.

Lo que importa no es el nombre de la herramienta, sino "la actitud de tratar a la IA no como alguien a quien consultar, sino como una compañera a quien se le puede encargar trabajo".

### 1-3. Lo "multimodal" es lo que salvará a los restaurantes

Hay una palabra clave más que es de importancia decisiva para dirigir un restaurante. Es "multimodal".

Es una palabra algo técnica, pero su significado es simple.

Significa "poder entender a la vez varios tipos de información: no solo texto (leer y escribir), sino también imágenes (ver y dibujar) y audio (escuchar y hablar)".

La IA convencional solo podía entender "texto". Pero el trabajo en un restaurante no funciona solo con "texto".

- El aspecto de los alimentos que quedan en el refrigerador

- La letra manuscrita en las comandas

- Las voces de la clientela y el ambiente del salón

- El diseño de la etiqueta de una botella de vino

Todo esto es "información no verbal" que da trabajo expresar en palabras.

El subgerente (IA) puede reconocerlo igual que una persona.

Si toma una foto del interior de su refrigerador con el teléfono y se la muestra, la IA reconoce: "Ah, le sobra esta verdura y esta carne", y a partir de ahí puede proponer un menú.

En otras palabras, la IA de hoy es "un excelente subgerente que puede ver, oír y hablar".

※ Pero no quiero que malinterprete una cosa.\
La IA es mejor para decir cosas que suenan plausibles que para decir cosas correctas. En el reconocimiento de imágenes, los números, las fechas y los nombres propios,\
por favor úsela partiendo de que una persona siempre hace la verificación final.

La razón por la que la IA funciona bien en este libro es\
que yo "no delego del todo, y siempre verifico en el lugar".

### 1-4. Respalde su "intuición" con datos

Las grandes cadenas tienen enormes cantidades de datos de las cajas registradoras (POS) y equipos de marketing.

En los locales independientes, en cambio, contamos con la "intuición" y la "experiencia" de quien lo dirige. Es el arma más fuerte, pero a veces puede volverse demasiado subjetiva o dejarle con dudas.

Así que sumemos un "subgerente".

Pida a la IA que compare su corazonada (intuición), "creo que a la clientela le va a encantar este plato", con los "datos de ventas anteriores" y la "información de tendencias".

Así puede conservar la "calidez" y la "individualidad" que solo tiene un local independiente, y aun así llevar un negocio sólido basado en datos.

## Capítulo 2: Fundamentos - "Vibe coding" desde cero conocimientos

~ Los programas no se "escriben". Se "hacen construir con la IA conversando con ella". ~

### 2-1. Nadie lee un "mensaje largo de LINE". La magia de un "diagrama" que toma 30 segundos

Decir "construir un sistema con la IA" tal vez todavía parezca un obstáculo algo alto.

Así que empecemos con una "forma de usar la IA" más cercana, que puede aprovechar desde hoy mismo.

Es una revolución en cómo "dar instrucciones al personal".

Muchas personas que dirigimos un local usamos LINE *(la aplicación de mensajería más usada en Japón)* para contactar al personal.\
Yo suelo llevar el local con un número limitado de personas, y en pleno servicio no hay tiempo para dar instrucciones con calma.

Por eso los avisos dependen inevitablemente de mensajes de LINE después del cierre.

Pero es sumamente difícil transmitir solo con palabras la imagen de "quiero que se haga así", que existe únicamente en mi cabeza, al personal con menos experiencia o a quien viene a ayudar de vez en cuando.

De ahí nace el "mensaje largo de LINE".

Cuanto más se esfuerza uno por explicar con cuidado, más largo se vuelve el texto, y como resultado...

"Ay, perdón, no lo leí hasta el final."

"Era todo texto y no supe qué parte era importante."

¿No les pasan errores como estos en su local?

A mí también me pasaron.

Un día, para una aplicación que estaba desarrollando, intenté pedirle a una persona del personal que tomara "fotos de ingredientes".

Las condiciones eran algo complicadas, así que las instrucciones que escribí en el teléfono se convirtieron en un mensaje largo como este.

![El largo mensaje de LINE que realmente envié al personal, con todo y errores de tipeo](images/fig-03.jpg)

Aun al ver esto, el personal de cocina, ocupado, lo recorrerá por encima pensando "O sea que solo tengo que sacar fotos, ¿no?" y pasará por alto las especificaciones de "ángulo" y "orientación del recipiente".

Pero no tengo tiempo para abrir PowerPoint, alinear figuras y hacer una hoja de instrucciones.

Así que pasé este texto tal cual a la IA (una herramienta de IA como Manus, o Gemini) y le pedí:

"Resuma el contenido de este texto en una diapositiva, como una 'hoja de instrucciones de trabajo' que el personal pueda entender de un vistazo."

### 2-2. La IA es una "excelente traductora"

Tras unos segundos de espera, lo que produjo la IA fue una "diapositiva con diagrama" sorprendentemente fácil de entender.

![La diapositiva "Instrucciones de trabajo para la recolección de datos y la toma de fotos", generada automáticamente por la IA](images/fig-04.jpg)

No diseñé nada. Solo dije: "Aquí está el texto, resúmelo."

A partir de mi texto divagante, la IA entendió al instante "qué es importante" y "cómo debía clasificarse", y lo "tradujo" a una disposición que las personas captan de forma intuitiva.

### 2-3. Libertad frente al "estrés de no hacerse entender"

Pegué esta imagen en LINE y la envié.

El efecto fue inmediato.

La persona del personal no hizo ninguna pregunta, y a la primera me envió fotos perfectas, en "orientación vertical" y con "3 ángulos".

Hasta entonces, me había irritado con el personal pensando "¿Por qué no lo leen?" y me había preocupado: "Quizá simplemente explico mal."

Pero la culpa no era ni del personal ni mía. Era de la "comunicación solo con texto".

Esta experiencia cambió mi manera de ver la IA.

La IA no es solo una herramienta para "crear desde cero" textos e imágenes nuevos.

Es "una herramienta que 'convierte' las 'palabras que no se transmiten bien' que tenemos en una forma que sí llega a la otra persona".

### 2-4. El "vibe coding", un nuevo tipo de diálogo

Una vez que se acostumbre a conversar con la IA, lo siguiente es, por fin, "construir herramientas".

Quizá piense: "Programar es imposible para mí", pero no se preocupe.

Hoy, entre los ingenieros, un término llamado "vibe coding" es tema candente.

Es un método en el que, en lugar de que las personas escriban código difícil, se construye un sistema conversando con la IA como quien sintoniza las "vibras" (la sensación y el ambiente).

Sota Fujii, titular del título Meijin de shogi *(el ajedrez japonés)*, mencionó el "vibe coding" como algo en lo que se metió este año, en 2025. Incluso alguien del mundo del shogi, que parece no tener nada que ver con construir sistemas, según se cuenta le dice a la IA en japonés lo que quiere y construye herramientas prácticas.

Conversando con la IA, nosotros también podemos construir sistemas sin conocimientos especializados.

Lo único que se usa es su propio idioma de todos los días (en mi caso, el "japonés"). Cuando usted dice "Quiero que funcione así" o "Esta parte es difícil de usar", el subgerente (IA) escribe el código detrás de escena.

En otras palabras, no necesita convertirse en "programador".

Solo necesita convertirse en la "persona a cargo de la obra" que da instrucciones a una "excelente persona ingeniera (IA)".

### 2-5. Las "quejas" de su local son los mejores prompts

Las instrucciones a la IA (prompts) no necesitan palabras elegantes.

El prompt más potente que descubrí consiste en "las 'incomodidades' y 'frustraciones' de su local; en otras palabras, sus quejas".

- "Es una lata hacer este cálculo todos los días."

- "No quiero cambiar el tamaño de las imágenes a mano."

Para la IA, frases como estas son "requisitos de desarrollo" perfectamente válidos.

Un sentimiento como "No soporto esto" extrae una solución concreta con más facilidad que una meta como "Quiero hacer esto".

### 2-6. Un error no es un "fracaso". Es el "comienzo de un diálogo"

Cuando empiece a hacer algo con la IA, seguramente se topará con un "error".

Pero en el vibe coding, un error no es un fracaso.

Es "la señal de que ha comenzado un intercambio de ida y vuelta con la IA, como lanzarse una pelota".

Incluso entre personas, es raro que la intención se transmita a la perfección a la primera.

Cuando la IA muestre un error, simplemente tómelo con ligereza: "Ah, no me hice entender", y vuelva a decirle: "No, lo que quiero es esto."

Siga con el intercambio sin rendirse. Si logra al menos eso, hasta usted, con cero conocimientos, podrá construir "un sistema que es solo suyo".

### 2-7. Aumente la eficiencia de forma drástica con "botones físicos": use un subteclado

En el vibe coding, lo más importante es "ser exigente con la entrada".

Cuanto más rápida sea su conversación con la IA, menos se detiene su pensamiento y más rápido avanza el desarrollo. Al contrario, si se enreda al ingresar datos, hasta una gran idea puede desvanecerse.

Antes le dije: "Cuando aparece un error, lo correcto es tomar una captura de pantalla y pegarla."

Pero presionar [Windows] + [Shift] + [S] (Mac: [Cmd] + [Shift] + [4]) decenas de veces al día, seleccionar un área con el mouse, volver a la pantalla de Gemini y presionar [Ctrl] + [V] (Mac: [Cmd] + [V])...

Seamos sinceros: cansa los dedos, ¿verdad?

Por eso incorporé un "subteclado de 6 botones".

Es un teclado pequeño, fabricado en China, que cuesta de unos cientos de yenes a cerca de mil, y que aparece al buscar "programmable keyboard" en Amazon o sitios similares.

![Una foto del subteclado de 6 botones que uso](images/fig-05.jpg)

A estos seis botones les he asignado los siguientes atajos.

1.  Iniciar la captura de pantalla

2.  Seleccionar todo (Ctrl + A; Mac: Cmd + A)

3.  Copiar (Ctrl + C; Mac: Cmd + C)

4.  Pegar (Ctrl + V; Mac: Cmd + V)

5.  Enter (enviar)

6.  (De reserva)

Eso es todo. Pero el efecto es drástico.

Aparece un error.

↓

Con la mano izquierda, toco el "Botón 1 (captura de pantalla)".

↓

Selecciono el área y luego toco el "Botón 4 (pegar)" en la pantalla de Gemini.

↓

Toco el "Botón 5 (enviar)".

Todo esto toma solo 2 segundos.

No necesita recordar atajos de teclado ni mover los dedos de forma complicada.

Puede lanzarle información a la IA como si manejara el control de un videojuego.

Como verá en capítulos posteriores, cuando corrija el código fuente que produce la IA, seleccionar todo (Ctrl + A), copiar (Ctrl + C) y pegar (Ctrl + V) le permiten volver a ejecutarlo de inmediato, lo cual resulta muy práctico.

Antes de estudiar conocimientos avanzados de programación, pruebe primero a conseguir este pequeño dispositivo.

Eliminar físicamente el "fastidio de la entrada de datos". Ese es el atajo más seguro para acelerar las conversaciones con la IA, su compañera de trabajo.

## Capítulo 3: Práctica 1 - Automatizar el trabajo creativo y atraer clientela

~ "Pegar una captura de pantalla y entregarlo todo" resultó ser el método de desarrollo más potente ~

### 3-1. Ensayo y error para borrar el "aspecto de IA" (stickers de LINE)

Habiéndome acostumbrado al diálogo con texto (vibe coding), decidí encarar por fin la "generación de imágenes".

Como práctica, elegí hacer "stickers de LINE", que además pueden ayudar a que más personas se encariñen con el local.

Pero las "imágenes lisas, como de gráficos por computadora" típicas de la IA no combinan con el ambiente de mi local.

Lo que buscaba era "un diseño plano retro, al estilo de los años 80, con un toque dibujado a mano, que conservara la textura del crayón y del pincel".

A partir de ahí comenzó un largo "diálogo" entre el subgerente (IA) y yo.

Al principio, partí con personajes de "dos niños y un Shiba Inu".

"Deme 25 frases de uso cotidiano."

"Haga que el grosor de las líneas sea aleatorio, como pinceladas."

Una a una, como quien da instrucciones de corrección a una persona ilustradora, le fui enseñando con paciencia el estilo que buscaba.

![Ilustraciones generadas para stickers de LINE](images/fig-06.png)

### 3-2. El pedido atrevido: "Cambie solo al perro por un gato"

Cuando las cosas ya habían tomado algo de forma, decidí hacer un gran cambio de rumbo: "En realidad, quiero que sean niñas y un gato."

Una persona ilustradora común pondría mala cara y diría: "¿Qué, empezar de nuevo desde el principio?" Pero el subgerente (IA) no se quejó ni una vez.

"Cambie los personajes a dos niñas, una de pelo largo y otra de pelo corto. Ropa en amarillo y verde, con el mismo estilo dibujado a mano de antes."

"Cambie el perro por un gato, cambie las frases por las expresiones gatunas que generó antes, y haga poses que combinen."

"Haga que el gato sea siamés, no un atigrado anaranjado."

Además, hice un pedido que ponía a prueba los límites de la IA.

"Mantenga exactamente la composición de los 'niños y el Shiba Inu' que hizo antes, y reescriba solo la parte del perro como un gato siamés."

Para mi sorpresa, la IA entendió esta instrucción complicada. Las posiciones y poses de los niños se mantuvieron iguales, mientras que las personas y el animal fueron reemplazados con pulcritud por un "gato siamés".

![La hoja de ilustraciones terminada para stickers de LINE](images/fig-07.png)

Sin embargo, para usarlos como stickers en LINE hay que dividir las ilustraciones, crear las miniaturas, comprimirlo todo en un ZIP y subirlo.

Esto también se puede hacer conversando con Gemini, pero lo explicaré en detalle más adelante, en 3-6. El primer obstáculo: la división sencilla y la "trampa de la calidad de imagen".

### 3-3. Caso 2: El "banner de Navidad" hecho en 22 rondas de diálogo

Después de los stickers de LINE, hay otra pieza grande que hice de la mano de la IA. Es el banner de anuncio de la "cena de Navidad", el evento más grande del año para el local.

Usé una IA llamada "Nano Banana" (el modelo de generación de imágenes integrado en Gemini, de Google).

#### Fase 1: Ajustar la distribución y el texto

Al principio, comencé colocando los elementos necesarios (Papá Noel, renos, información en texto) sobre un lienzo panorámico.

Al ver las imágenes que salieron, di instrucciones.

"Se siente algo vacío. Agregue ilustraciones de un árbol de Navidad y de champán."

"El menú es una lista con viñetas y cuesta leerlo. Resúmalo como 'seis tiempos en total', y haga el título más grande y llamativo."

![La imagen generada en la etapa inicial. Todavía se ve algo vacía](images/fig-08.png)

#### Fase 2: Afinar el "ambiente animado"

Una vez fijada la distribución, siguió el ambiente. Le faltaba "aire de fiesta".

Indiqué: "¡Hágalo más animado! Esparza muchos Papá Noel y renos pequeños, globos y confeti."

Esta vez, la pantalla quedó demasiado recargada.

"Perdón, eran demasiados elementos. Reduzca los personajes por ahora y deje la composición más despejada."

Poder repetir este ajuste fino de "sumar y restar" es la fortaleza de la IA.

#### Fase 3: La idea inesperada de un "rehacer por completo"

A mitad de la producción, me asaltó una duda. "¿No se vería más delicioso mostrar ilustraciones de la comida, en lugar de poner a los personajes como protagonistas?"

Así que ordené con audacia: "Como alternativa, haga un diseño que tenga como elemento principal ilustraciones de los platos reales."

![Propuesta de ilustración con los platos como protagonistas (parte del texto está distorsionado)](images/fig-09.png)

La IA ideó al instante unas apetitosas ilustraciones de comida, pero tras compararlas decidí quedarme, a fin de cuentas, con el diseño original de personajes. Incluso un "volvamos a como estaba" como este se le puede pedir a la IA sin dudarlo.

#### Fase 4: La última línea de defensa es la mirada "humana"

Una vez decidido el diseño final, también dejé en manos de la IA las variantes de tamaño, para publicaciones de Instagram (vertical) y para Stories (todavía más alto).

Y entonces, justo cuando estaba por terminar, noté un error grave.

"¡Espere, el día de la semana en la fecha está mal!"

La IA es buena para dibujar, pero no entiende los días de la semana de un calendario. Si lo hubiera publicado así, habría sido un desastre.

Ordené con urgencia: "¡Corrija la fecha a '24/12 (miércoles) y 25 (jueves)'!" y terminé la versión final.

![El banner final después de la corrección](images/fig-10.png)

En total, 22 rondas de correcciones y diálogo.

La IA no es una varita mágica, pero si conversa con ella con paciencia, no hay un socio de diseño más confiable.

### 3-4. Caso 3: Un aviso de apertura de Año Nuevo que evoluciona con la situación

Apenas se apaga la emoción de la Navidad, llega el siguiente evento: la temporada de fin de año y Año Nuevo.

Para un restaurante o un bar, dar a conocer la información en esta época es una carrera contra el reloj. "¿Hasta cuándo abren a fin de año?" "¿Cuándo reabren en el nuevo año?" La clientela siempre busca información.

Pero la información cambia minuto a minuto.

"Cuando termine el servicio de fin de año, quiero reescribirlo para que muestre solo el aviso de Año Nuevo."

"Lo publiqué en X (horizontal), pero quiero publicarlo también en Instagram (vertical)."

Si se lo hubiera pedido a un estudio de diseño externo, solo los costos de corrección serían una pesadilla y, sobre todo, no estaría listo a tiempo.

Así que una vez más me asocié con una IA de generación de imágenes (Nano Banana) y me puse a trabajar en banners que me acompañaran durante la temporada de fin de año y Año Nuevo.

#### Paso 1: El estilo es "dibujo en crayón de los años 80"

Primero, construí el aspecto y la sensación general.

Lo que le queda bien a mi bar no es el brillante estilo de gráficos por computadora.

"Un estilo cálido, como un dibujo en crayón hecho a mano de los años 80, con pinceladas visibles. Mantenga el fondo blanco liso."

Con esta instrucción como núcleo, y pensando en un anuncio en X (antes Twitter), comencé a trabajar en un lienzo horizontal.

#### Paso 2: La serpiente que se va y el caballo que llega. Un brindis por el relevo

Al principio pensé en dibujar un solo animal del zodiaco, pero esto era, al fin y al cabo, el cambio de año.

Se me ocurrió una idea: "Quiero que aparezcan tanto el animal del año que termina (el signo de este año) como el del año que empieza (el del próximo)."

Así que le di esta instrucción a la IA:

"Ponga un grupo de serpientes (el año de la Serpiente) en el lado izquierdo de la pantalla y un grupo de caballos (el año del Caballo) en el derecho. Haga que cada uno sostenga una jarra de cerveza y brinden con alegría, como pasándose el relevo al final del año."

La imagen que generó la IA era exactamente la que yo había imaginado.

Serpientes encantadoras a la izquierda, caballos de aspecto confiable a la derecha, brindando juntos más allá de las diferencias entre sus especies.

De "fin de año (Serpiente)" a "Año Nuevo (Caballo)".

En una sola imagen, el paso del tiempo y el ánimo festivo quedaron condensados con belleza.

![Una imagen generada con una serpiente a la izquierda y un caballo a la derecha brindando, que expresa el año viejo cediendo paso al nuevo](images/fig-11.png)

#### Paso 3: "Dirección actoral" y "prueba de vestuario" para los animales

Una vez definida la composición, el siguiente trabajo era la puesta en escena más fina. También aquí, la IA me acompañó con paciencia en mis exigencias de detalle.

En las primeras imágenes, los animales estaban simplemente parados en fila, o sostenían las jarras de maneras poco naturales.

"¡Hágalos ver más contentos! Como clientes habituales pasándola muy bien juntos."

"También quiero un aire de temporada. Póngales bufandas y pajaritas, désles un aspecto invernal."

Con esa sola observación, los animales de la pantalla se envolvieron en cálidas bufandas rojas y verdes y se transformaron al instante en las estrellas de una "fiesta de invierno".

"Sí, ahora tiene esa sensación cálida de beber de día en un día frío."

Si se mira de cerca, algunos movimientos de las manos y la manera de sostener las jarras todavía son poco naturales. Pero ser exigente significa tardar más. Equilibrando el tiempo con lo bien que se transmite el mensaje, acepto un resultado razonablemente bueno.

#### Paso 4: Con el paso del tiempo, la información cambia

De aquí en adelante es donde la IA realmente demuestra su valor.

El banner original mostraba los horarios de diciembre y de enero como el "Horario de fin de año y Año Nuevo".

Pero una vez pasado el 31 de diciembre, la información de fin de año ya no hace falta.

Abrí el proyecto en el que había estado trabajando y pedí un cambio grande en el texto.

1.  Cambiar el título: de "Horario de fin de año y Año Nuevo" a "En Año Nuevo abrimos de día para tomar unas copas".

2.  Ordenar la información: borrar el horario de diciembre, que ya había pasado, y reducirlo solo al "horario de Año Nuevo (2/1–4/1)".

3.  Corregir los personajes del zodiaco: cambiar las serpientes del año que se va por caballos.

4.  Agregar un gancho: sumar una oferta atractiva, "highballs y pollo frito a discreción", como nuevo atractivo para la clientela.

![Paso 4: Con el paso del tiempo, la información cambia](images/fig-12.png)

Sin recrear la imagen desde cero, pude actualizar la información como quien reescribe las palabras de una pizarra. Esa es la fortaleza del diseño con IA.

#### Paso 5: De X a Instagram. Un formato que cambia a voluntad

Y ahora, el toque final.

"Ya lo anuncié en X. Ahora quiero publicarlo en las Stories de Instagram."

Pero las Stories usan el tamaño "vertical", que llena toda la pantalla del teléfono. Si se coloca tal cual una imagen horizontal, quedan franjas vacías arriba y abajo, y se ve mal.

Con una ilustración común, este es el tipo de cambio que obligaría a volver a dibujarla.

Pero lo único que hice fue decirle a la IA:

"Mantenga este diseño, pero reacomódelo en una distribución vertical para las Stories de Instagram."

La IA reacomodó en forma vertical a los animales, que estaban repartidos a lo ancho, ajustó el equilibrio del texto y generó al instante un diseño a la medida de los teléfonos inteligentes.

![La imagen vertical terminada para las Stories de Instagram](images/fig-13.png)

### 3-5. Caso 4: Hacer el logotipo del bar - Un diálogo que convierte el "significado" en "forma"

Más allá de las "imágenes" como banners y stickers, también asumí con la IA un desafío más abstracto: diseñar un nuevo logotipo.

Está pensado para incorporarse en banners y similares, de modo que se pueda reconocer a Tamuro de un vistazo.

El tema es Tamuro, el bar solo por recomendación que dirijo de noche. Este nombre lleva un deseo profundo: "ser un lugar donde todo tipo de personas se reúnan con libertad y alegría (tamuro-suru, pasar el rato) en el barrio de Higashi-Nakano".

¿Cómo condensar esta "historia" invisible en una pequeña marca de logotipo? Comenzó un paciente diálogo con la IA.

#### Paso 1: Elegir el tipo de letra y la dirección del diseño

Al principio le lancé ideas a la IA, como "un aspecto sobrio con el kanji 屯" y "algo pop en katakana", y le pedí unos cuantos borradores.

Pero ninguno me convencía. Dada la naturaleza del bar, quería algo más moderno, con un aire neutro que diera la bienvenida a la diversidad.

Así que cambié de rumbo.

"Basémonos en el alfabeto latino, que es muy versátil: 'TAMURO'. El estilo debe ser 'diseño plano', sin decoración complicada. Y debe verse con fuerza incluso a una sola tinta."

La IA propuso de inmediato un "TAMURO" sencillo y audaz, en letra sans-serif.

![El logotipo en letra sans-serif](images/fig-14.png)

#### Paso 2: Infundir "significado" a la forma

Aquí empieza la verdadera prueba. Unas letras simples, sin más, no significan nada. Y tener solo la "M" en el centro tampoco transmite mucho.

"Quiero expresar el origen del nombre, 'personas que se reúnen'. ¿Podría reunir todo en un 'círculo' cálido y cercano, dando forma a cada letra del alfabeto de modo que parezca una persona que se mueve con alegría?"

Es un pedido muy abstracto. Pero la imaginación de mi subgerente (la IA) superó mis expectativas.

Lo que ideó la IA fue un diseño en el que los esqueletos de las letras "T", "A", "M" y las demás se transformaban en siluetas de personas bailando con los brazos y las piernas extendidos.

![Un logotipo que traslada el alfabeto a figuras de personas](images/fig-15.png)

#### Paso 3: El tira y afloja entre el diseño y la legibilidad

"¡Interesante! Pero así no se puede leer 'TAMURO'..."

Si se le da demasiado peso al diseño, deja de reconocerse como letras, y si se pone el peso en las letras, pierde su encanto. Me topé con este dilema.

Desde ahí fue cuestión de afinar una y otra vez.

"La letra 'A' parece una persona, lo cual está bien, pero enfatice un poco más su estructura como 'A'. Ponga el travesaño con firmeza."

"El equilibrio general es bueno, pero las personas están demasiado amontonadas y se sienten agobiadas. Deje un poco más de espacio, para que se vea alegre."

"¡Combine las personas bailando de antes con las letras de TAMURO, y hágalo un círculo!"

![La marca circular "TAMURO", terminada tras ensayo y error](images/fig-16.png)

Aunque está hecha de animadas siluetas de personas, basta mirar la parte inferior para leer con claridad "TAMURO".

Lanzándonos ideas una y otra vez con la IA, obtuve un logotipo con el que quedé conforme, uno que fusiona la legibilidad, la calidad del diseño y, sobre todo, el "deseo" que puse en el bar.

Ahora se usa como ícono de las cuentas del bar en X (antes Twitter) y en Instagram.

### 3-6. El primer obstáculo: la división sencilla y la "trampa de la calidad de imagen"

El desafío creativo de hacer el logotipo había terminado.

Pero el trabajo aún no estaba hecho.

Volvamos a los stickers de LINE. Lo que tenía en las manos era una "hoja" con 25 ilustraciones dibujadas en una sola página.

Para presentarlos como stickers de LINE, tenía que recortar cada uno, hacer transparente el fondo y cambiarle el tamaño. Era una tarea tediosa que venía posponiendo.

"No hay manera de que recorte esto a mano..."

Consulté a Gemini y le pedí una solución. Gemini dijo, como si nada:

"Automaticémoslo con un lenguaje de programación llamado Python."

Con toda franqueza, casi me rindo ahí mismo.

"¿Python? He oído el nombre, pero instalar ese tipo de software en mi computadora me da miedo. Además, la configuración suena difícil. Por favor, no esperen tanto de alguien que atiende un bar..."

Pero esta es una de las partes más destacadas del libro. Como si intuyera lo que yo pensaba, Gemini hizo una sugerencia sorprendente.

Gemini:

"No necesita preparar ningún entorno. Use una herramienta gratuita de Google llamada 'Google Colab'. Funciona en su navegador, así que lo único que tiene que hacer es copiar y pegar en ella el código que yo escriba."

"¿Qué? ¿Existe algo así?"

No podía creer lo que oía. Nunca había imaginado que existiera un entorno donde la programación funciona solo con un navegador, sin instalar nada en mi propia computadora.

No era "después de estudiar Python", sino "hacer que la IA me enseñara hasta la existencia de la herramienta (Colab)".

En ese momento, se derrumbó mi suposición de que "programar requiere muchísima preparación".

### 3-7. No "lea" la pantalla de error: "haga una captura y envíela"

Tal como se me indicó, abrí Google Colab, pegué el código y presioné el botón de reproducir.

Pero la realidad no es tan sencilla. Lo que apareció en la pantalla fue una hilera de texto rojo brillante... un mensaje de error.

"Error: Image file not found..."

El yo de antes habría tenido una reacción alérgica con solo ver este error y habría cerrado el navegador en silencio.

Pero ahora tenía una aliada: la IA "multimodal", una IA con ojos.

Ni siquiera intenté leer el mensaje de error.

Simplemente tomé una captura de pantalla y la pegué, zas, en el cuadro de chat de Gemini.

Y añadí una sola línea: "Apareció algún tipo de error."

![Pegar en Gemini, tal cual, la pantalla de error de Google Colab](images/fig-17.png)

Gemini analizó la imagen de inmediato y devolvió una respuesta.

Gemini:

"Ah, el nombre del archivo de la imagen que se está cargando es incorrecto. Corregí el código para usar '.jpg'. Por favor, vuelva a ejecutarlo con esta versión."

"...¡Vaya, esto es divertido!"

Este intercambio se sentía menos como programar y más como un juego de "encuentre las diferencias" o de lanzarse la pelota de un lado a otro.

- Yo: (pegando una captura de pantalla) "Se detuvo otra vez."

- Gemini: "El tamaño de la imagen no coincide. Agregaré una función que lo ajuste automáticamente."

- Yo: (pegando una captura de pantalla) "Esta vez la imagen se ve pixelada."

- Gemini: "Olvidé agregar el proceso llamado 'LANCZOS', que conserva la calidad de la imagen. Lo corregiré."

No entiendo ni una sola línea del código. Cuando aparece un error, simplemente tomo una captura de pantalla y se la lanzo a la IA con un "¡Mire!"

Este "delegar por completo el análisis del error" fue el mayor secreto de cómo logré, con cero conocimientos, construir un sistema, y al mismo tiempo fue la experiencia más emocionante de todas.

### 3-8. El muro más grande: el "desalineamiento del dibujo a mano" y el "desborde"

Mientras seguía con esta "conversación llamada errores", el sistema se fue refinando cada vez más.

Y por fin entré en el mayor desafío: la "Fase 2: Recorte automático de distribuciones dibujadas a mano".

Me entró la ambición.

"Hagamos una hoja de 5×5, con 25 stickers. Y como quiero un toque más artesanal, quiero colocarlos libremente, sin quedar atado a las líneas de la cuadrícula."

Con un código que simplemente divide la hoja en partes iguales, la mano de un personaje o el texto se desborda a la celda siguiente y queda cortado de forma lamentable.

También probé un método de "recortar todo menos el fondo blanco", pero los márgenes salieron desiguales y fracasó.

Estaba a punto de rendirme. Entonces, recurriendo a mi instinto de mis tiempos en el área de sistemas, le dije a Gemini:

"Quiero que abandone la idea de recortar la imagen con tijeras. En cambio, mire en qué celda está el 'punto central' de cada dibujo. Si el centro está en esa celda, aunque se desborde un poco, trate el dibujo entero como 'perteneciente a esa celda' y échelo en la cubeta de esa celda."

Esta fue la solución que bauticé como "método de la cubeta por cuadrícula".

¿Por qué se me ocurrió "meterlo en una cubeta según el punto central" en lugar de "cortar con tijeras"?

La forma de pensar de quien no es del ramo (analógica): se imagina "recortar una sola imagen con tijeras". Así se corta justo por la línea y se les cercenan las manos y los pies a los personajes.

La forma de pensar de la persona de sistemas (digital): una computadora no tiene un sentido físico de "cortar". En cambio, tiene "coordenadas (posiciones)". Así lo vi yo: "Aunque se desborde un poco, mientras el 'ombligo (punto central)' del dibujo esté dentro de la celda, podemos considerar el dibujo entero como 'perteneciente a esta celda'."

![La idea analógica de "cortar por las líneas" y la idea digital de "elegir por un punto"](images/fig-18.png)

Esto es lo que significa "traducir un trabajo analógico vago a reglas digitales claras". Cuando da instrucciones a una IA, funciona bien idear una regla como esta, en la que la respuesta sale igual "sin importar quién mire (o calcule)".

Gemini convirtió este pedido abstracto en código de maravilla. El resultado fue perfecto.

El texto "¡Gracias!" y las colas que se habían desbordado a las celdas vecinas fueron reconocidos sin problemas y reunidos, cada uno, dentro de su propio sticker.

Hasta atendió mi pedido caprichoso: "El último (el 25) no hace falta, sáltelo." Por fin tenía una herramienta donde "basta soltar la imagen y presionar un botón, y se produce un conjunto completo de imágenes para la solicitud de stickers en LINE".

Todo lo que hice fue transmitir el "problema en el terreno (los dibujos se cortan)" y proponer una "solución lógica (decidir por el punto central)". La IA escribió todo el código difícil.

Esta es la esencia misma del "vibe coding": construir sistemas partiendo de cero conocimientos.

#### Resumen del Capítulo 3

1.  Dibujar con IA no es "de una sola vez". Puede rehacerse tantas veces como quiera según la situación: cambiar de personajes, agregar un aire de temporada, cambiar de medio.

2.  Incluso un "concepto" abstracto (personas que se reúnen) puede convertirse en una "forma" (un logotipo) mediante un diálogo repetido.

3.  Las tareas tediosas (recortar imágenes) son justamente lo que Gemini × Google Colab puede automatizar. Los errores se resuelven con capturas de pantalla.

#### Columna 1: Un curso intensivo de "Google Colab" para quien dirige un local y viene de letras

~Use una "cocina de alquiler" y deje su computadora como está~

Hablemos del "Google Colab" que apareció en el texto principal. Programar (Python) en su propia computadora es como "hacer un auténtico ramen desde cero, empezando por el caldo, en la cocina de su casa". La preparación es mucho trabajo.

Google Colab, en cambio, es "una cocina de alquiler gratuita, totalmente equipada con utensilios". Basta abrir el navegador y las mejores herramientas están listas. No necesita cambiar ninguna configuración de su computadora. Puede programar solo con un navegador y mantener limpio su entorno. Primero, busque "Google Colab" y eche un vistazo a esta cocina de alquiler.

#### Columna 2: No "leer" la pantalla de error es la respuesta correcta

~Domine el arma definitiva: la captura de pantalla~

Cuando aparece un error, ¿intenta descifrar con empeño el mensaje en inglés? Es una pérdida de tiempo.

Cuando algo sabe raro mientras cocina, le pide a un chef que lo pruebe. De la misma manera, muéstrele a la IA solo una "captura de pantalla (screen capture)".

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Presione estas teclas, dibuje un recuadro alrededor del error y péguelo en Gemini. Eso es todo. No "lea el error", "muestre el error". Solo con cambiar así la mentalidad, triplicará su velocidad de desarrollo.

He presentado varios ejemplos hasta ahora, y todo lo que hago se reduce a los siguientes tres puntos.

・No exija la forma final de una sola vez (está bien suponer un diálogo)\
・Diga "no, eso no es del todo lo que quiero" sin dudar\
・Suponga que el costo de las correcciones es cero y lance los pedidos sin pensarlo demasiado

No necesita talento para el diseño. Lo único que necesita es el valor de poner en palabras "algo no me convence".

## Capítulo 4: Práctica, parte 2 - Hacer más eficiente el trabajo diario (con IA multimodal)

~Termine el "tedioso ingreso de datos" con un solo teléfono~

### 4-1. El problema de actualizar la carta de vinos

Para quien dirige un bar o un restaurante, actualizar la carta es una carga poco vistosa pero pesada.

Lo que más me preocupaba era hacer la "carta de vinos".

Cada vez que llega un vino nuevo, hay que hacer las siguientes tareas:

1.  Mirar la etiqueta de la botella (letra cursiva en otro idioma, difícil de leer).

2.  Escribir en la computadora el nombre de la marca y la añada (el año) sin errores.

3.  Buscar en internet las características y el sabor del vino.

4.  Redactar una "presentación" que dé ganas de leer a la clientela.

5.  Pensar en platos que combinen bien con ese vino (maridajes).

Hacer todo esto con el diccionario en la mano, en los huecos de un servicio muy ocupado, es casi imposible. Lo dejaba para después con un "luego lo hago", y la lista de recomendados muchas veces se quedaba sin actualizar.

### 4-2. Basta con tomar una foto. La sorpresa de la "Gem de Carta de Vinos"

Así que decidí probar la "función multimodal (reconocimiento de imágenes)" de Gemini.

El método es tan sencillo que casi parece mentira.

1.  Tome una foto de la botella de vino con su smartphone.

2.  Envíe esa foto a Gemini.

3.  Añada una línea: "Haga una lista."

Eso es todo.

![Foto de la etiqueta de una botella de vino real tomada con un smartphone](images/fig-19.jpg)

Enseguida, Gemini lee la información de la etiqueta a partir de la foto.

No solo transcribe el nombre de la marca, como "Cave d'Occi Winery, Tsukimi de Ippai 2024", sino que además busca sus características en una enorme base de datos en línea y genera de forma automática una descripción atractiva.

Lo que más me sorprendió es que también entregaba "sugerencias de maridaje" en el mismo paquete.

En cuestión de segundos aparecían en la pantalla sugerencias como "El aroma intenso de este vino combina bien con ○○".

Las horas que antes pasaba peleándome con el diccionario se redujeron a un solo clic del obturador del teléfono.

### 4-3. Cómo crear su propia "Gem"

Para que todo esto fuera mucho más eficiente, pasé a usar una función llamada "Gems".

Es una "función de IA personalizada, solo suya", en la que se puede dejar memorizados de antemano un rol y unas reglas para la IA.

Explicarlo todo desde cero cada vez ("Usted es un sumiller. Mire esta foto y...") es un fastidio.

Por eso registré de antemano en Gemini las siguientes "instrucciones (prompt)". Este es el interior de la cabeza de la "IA sumiller" exclusiva de mi bar.

#### Las instrucciones que tengo registradas realmente

> Lea la imagen y cree una carta de vinos con el siguiente formato.
>
> Para los precios, no use precios de mercado. Calcúlelos suponiendo el precio de botella de un restaurante típico (aproximadamente 2,5 a 3 veces el costo).
>
> No use formato de tabla. Hágala de modo que quepa en una o dos hojas de papel A4.
>
> El formato es solo una referencia; cree la carta usando únicamente lo que se ha ingresado.
>
> El formato es el siguiente.
>
> Reino Unido 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (unos US$ 57)
>
>  Dorado pálido con burbujas agradables. Notas de melón y miel entre aromas cítricos... (el resto se omite)

En realidad, la mitad inferior de este prompt, la parte del "formato (muestra)",

no se me ocurrió de la nada.

Antes, cuando buscaba información de vinos en internet, pensaba: "Ah, la descripción de este local se entiende muy bien", o "Esta página lo escribe de una forma que abre el apetito", y simplemente copiaba y pegaba esos pasajes en un bloc de notas, una y otra vez.

Le arrojé esa "nota hecha de retazos" a Gemini tal cual.

"Estos son pasajes que copié y reuní hace un tiempo. Imite este tono y escriba también sobre el vino de la foto nueva."

Solo le dije eso.

Aun así, estas instrucciones contienen tres trucos que reducen la carga de trabajo en el local.

① "La lógica del cálculo de precios"

Es lo que más tiempo ahorra. Como pido "el precio que cobraría un restaurante" y no "el precio de mercado", la IA parte de los precios de compra habituales y calcula hacia atrás para darme una cifra como "¥8.500 (unos US$ 57)" que puede ir directo a la carta. (Por supuesto, la decisión final es de quien dirige el local, pero contar con una referencia lo hace todo más fácil.)

② "Sin formato de tabla, sino que quepa en una hoja A4"

Si el resultado llega en formato de tabla, como en Excel, el diseño se desarma al pegarlo en el menú. Al pedirle desde el principio que escriba en un "formato de menú A4", busco un resultado que se pueda imprimir y usar tal cual.

③ Usar texto copiado de internet como "muestra"

En lugar de pedir de forma vaga "Escriba una buena descripción", le muestro un ejemplo concreto (mi nota copiada y pegada): "bandera 🇬🇧 + nombre del vino + precio + descripción sensorial".

Cuando se le muestra un ejemplo a una IA, entiende: "Ah, este es el tono y la manera en que debo escribir", y la precisión del resultado se dispara. En términos técnicos esto se llama "few-shot prompting", pero en esencia es lo mismo que "enseñar con el ejemplo, dejando que miren cómo uno trabaja".

Y ese "ejemplo" puede ser perfectamente un texto encontrado, el equivalente escrito de una foto encontrada en la web.

![El texto terminado de la carta de vinos entregado por Gemini](images/fig-20.png)

### 4-4. Ni siquiera tiene que ser una imagen. La revolución de copiar y pegar desde LINE

Lo bueno de esta "Gem de Carta de Vinos" es que la entrada no se limita a las fotos.

De hecho, en un bar es frecuente hacer los pedidos al proveedor de bebidas por LINE, ¿verdad?

Cuando se cierra el pedido, el proveedor envía un mensaje como este.

> "Gracias, como siempre. Hemos recibido su pedido de la siguiente manera.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24, 3 botellas
>
> ・Ridgeview Bloomsbury, 6 botellas
>
> ・○○ (vino nuevo), 2 botellas
>
> Se lo entregamos mañana."

Un día se me ocurrió de pronto: "¿No podría usar este texto tal cual?"

Como prueba, copié este mensaje de LINE y lo pegué directamente en Gemini.

El resultado fue perfecto.

Gemini reconoció solo los "nombres de producto" del mensaje de LINE, buscó la información en internet y armó una lista en el formato de siempre (bandera + precio + descripción).

Es decir, ni siquiera tengo que esperar a que lleguen las botellas para tomarles fotos.

En el mismo momento en que hago el pedido, con solo copiar y pegar dentro del teléfono, la lista de la carta queda terminada antes de que los productos lleguen.

No hace falta abrir la computadora ni encender la cámara.

En un rincón de la cocina, o en el tren, el trabajo se hace solo con el teléfono.

¿No es esta la "eficiencia real" que merece quien atiende un local en solitario?

### 4-5. La sugerencia de la IA × el criterio sobre el terreno (la realidad)

Aun así, no me trago las sugerencias de la IA sin pensar. Lo que importa aquí es nuestro "criterio humano sobre el terreno".

Una vez, la IA hizo esta sugerencia para acompañar un vino:

IA: "Para este vino tinto, el pato asado con salsa de naranja es un maridaje perfecto."

Una sugerencia maravillosa, pero por desgracia ese día no había pato en el refrigerador del local.

No pienso: "La IA lo dice, así que tengo que comprar pato." Pienso así:

Yo (sobre el terreno): "No tenemos pato, pero hoy llegó un buen pollo de granja. Tiene una grasa comparable a la del pato, así que sellaré este pollo hasta que la piel quede crujiente y lo terminaré con una salsa con sabor a naranja, tal como dice la IA."

"El conocimiento de la IA (el pato y la naranja van juntos)" × "las existencias reales del local (tenemos pollo)" = "un plato nuevo para el menú, realista y sin complicaciones".

Esta combinación es el verdadero placer de desarrollar menús con IA.

La IA le da la respuesta de manual, pero no sabe qué hay hoy en el refrigerador. Llenar ese hueco es su trabajo como responsable del local.

### 4-6. La última milla: la IA no puede "catar"

Hay una cosa más que nunca debe dejar en manos de la IA.

Es la cata que usted hace antes de que algo salga hacia la clientela.

Las descripciones y los maridajes que escribe la IA se basan en "datos genéricos".

Pero el vino es algo vivo. Incluso con la misma etiqueta, el sabor cambia según la añada y la forma en que se haya almacenado.

Una vez, la IA escribió esta descripción para un vino blanco: "Un vino fresco, ligero y seco. Perfecto con carpaccio de mariscos."

Pero cuando abrí la botella y lo probé, estaba más evolucionado de lo que esperaba, con notas ricas, como de miel.

"Si lo sirvo como un 'vino ligero y seco', la clientela se va a decepcionar... Combinaría mejor con pollo en salsa de crema que con carpaccio."

Corregí enseguida el texto que había producido Gemini.

- Antes (IA): "Fresco y ligero. Bueno para entradas"

- Después (persona): "Cuerpo rico y pleno por la crianza. Con fuerza suficiente para acompañar un plato principal"

La IA hace el 90% del borrador, y la persona lo prueba y añade "el último 10% (el alma)".

Esta comprobación es responsabilidad de quien dirige un restaurante, y es algo que la IA jamás podrá imitar.

No "porque lo dijo la IA", sino "porque lo probé y estaba delicioso".

Para servirlo con esa seguridad, todavía hoy pruebo el vino recién abierto con una carta hecha por la IA en una mano.

#### Columna 3: Consejos para fotografiar las cosas de modo que la IA las vea "correctamente"

~ Como mostrarle una etiqueta a un sumiller ~

Cuando le envía una foto a Gemini, unos cuantos trucos pequeños pueden mejorar mucho lo bien que reconoce lo que ve.

1.  Evite los reflejos: las etiquetas de las botellas reflejan fácilmente la luz, así que cambie un poco el ángulo o proyecte una sombra con su cuerpo al tomar la foto.

2.  Tome varias fotos y envíelas juntas: para cosas como el contenido de un refrigerador, envíe una toma amplia y primeros planos a la vez, y la IA reconocerá incluso los artículos que quedan en los puntos ciegos.

3.  Señale con el dedo: también ayuda señalar con el dedo el punto que quiere que la IA mire mientras toma la foto. Ponga algo como "Estoy señalando con el dedo" en el prompt. Es lo mismo que señalar un plato en el menú de un restaurante en el extranjero.

## Capítulo 5: Aplicaciones - Análisis de negocio y mejora de la rentabilidad

~ Descubra la "mina de oro invisible". Una reunión de gestión con su consultor de IA ~

### 5-1. La noche en que me rompo la cabeza con la calculadora al final de cada mes

Para quienes tenemos pequeños restaurantes independientes, ningún momento pesa tanto como el trabajo de cierre mensual.

En la quietud de la madrugada, sumando los datos de la caja y pasándolos a Excel, lo único que se oye es el propio suspiro.

"La meta de ventas de este mes era de ○○0.000 yenes. ...No la alcancé."

"La cantidad de clientes no está mal. El fin de semana estuvimos llenos. Pero, por alguna razón, el gasto por cliente no crece."

¿Por qué no logro la meta? Sé que la comida es buena. Me esfuerzo en la atención.

"¿Será que los precios son demasiado altos?"

"No, si bajo más no tendré ganancias. Y los costos de los ingredientes también están subiendo."

Preguntas sin respuesta dan vueltas y vueltas en mi cabeza, y al final lo cierro apelando a la pura fuerza de voluntad: "El mes que viene le pondré más ánimo y empujaré más las recomendaciones." Este era mi mal hábito, y el de muchas personas que dirigen un local.

Pero ahora tengo un asesor sin emociones.

Me senté frente a Gemini con los datos de ventas de ese mes y los datos del menú del local.

### 5-2. Un experimento: hacer que la IA lea "lo visual" y "los números" al mismo tiempo

Esta vez, le di a Gemini tres datos.

Le arrojé, todo mezclado, el "diseño (cerebro derecho)" y los "números (cerebro izquierdo)" que siempre había manejado por separado.

1.  "La meta de ventas de este mes"

- Mi deseo sincero. La cifra que tengo que alcanzar sí o sí.

2.  "Todos los datos de los tickets de venta recientes (CSV/Excel)"

- El resultado en la realidad. Los datos concretos de quién pidió qué y a qué precio.

3.  "Un archivo PDF del menú actual"

- El mundo que ve la clientela. Información visual como la ubicación de las fotos y el tamaño y el color del texto.

Y entonces hice esta pregunta.

No fue una orden de trabajo como la anterior de "haga una imagen". Fue una pregunta, de las que hace quien dirige un local.

> "Compare los datos de ventas actuales (la realidad) con la distribución del menú (la apariencia).
>
> Señale el cuello de botella: ¿qué nos falta para llegar a la meta de ○○0.000 yenes?"

### 5-3. La "idea preconcebida de quien dirige el local" que la IA descubrió

Unos segundos después llegó la respuesta de Gemini, y dio justo en mi punto ciego.

Yo había supuesto que recibiría consejos generales como "Desarrollemos un plato nuevo" o "Hagamos promoción en redes sociales".

Pero lo que señaló la IA fue un hecho que yo intentaba esconder sin darme cuenta.

La respuesta de Gemini:

> "Al cruzar los datos con el menú, encontré una gran oportunidad perdida.
>
> El plan de barra libre, que tiene un margen de ganancia alto y puede elevar de forma segura el gasto por cliente, aparece hoy en el menú (Antes) solo como texto, discretamente, en la parte más baja de la esquina izquierda.
>
> Mientras tanto, el mejor lugar del menú, en lo más alto, lo ocupa el 'Menú ¥2.200 (unos US$ 15)', de precio bajo. Así, la clientela se inclina hacia el plan más barato y ni siquiera advierte la opción de barra libre, de mayor precio."

Al mirar la pantalla no pude evitar soltar un gruñido. Tenía toda la razón.

Sí tenemos un plan de barra libre. Pero en algún rincón de mi mente yo pensaba esto:

"No somos un izakaya de cadena *(un pub informal japonés que sirve comida y bebidas)*. Vender barra libre con letras grandes se ve barato."

"Quiero que la gente saboree el vino, así que solo debería pedirlo quien ya lo conoce."

Esa "idea preconcebida" mía se reflejaba en la distribución del menú, en el texto de la parte más baja.

![El menú Antes. El plan de barra libre está en la parte inferior izquierda y no llama la atención. Tampoco se distingue que la comida va aparte](images/fig-21.png)

La IA no lo pasó por alto.

"Usted quiere alcanzar su cifra de meta, ¿verdad? Entonces debería poner el menú que más desea vender, el de barra libre, justo arriba, con orgullo."

### 5-4. ¿No hay material de imagen? Que la IA también lo dibuje

Tomé una decisión. "Si verse elegante solo hace bajar las ventas, lo probaré, cueste lo que cueste."

Pero aquí surgió un problema.

"Aunque lo ponga grande arriba, solo con texto se queda corto..."

Y si saco de un sitio de fotos gratuitas una imagen de gente brindando con cerveza, de inmediato parece un restaurante de cadena. No encaja con el ambiente de mi local.

No tengo talento para dibujar, y contratar a una persona ilustradora cuesta dinero y tiempo.

Empecé a preocuparme: "¿Qué hago...?", pero enseguida me acordé.

"Es verdad, tengo un subgerente (la IA) que sabe dibujar."

En un sitio de material gratuito había encontrado algo cercano a la imagen que quería. Decía que se permitía modificarlo.

Escribí lo siguiente en el cuadro del chat:

> "Dibuje una ilustración para poner en la parte superior del menú. Use la imagen adjunta como base.
>
> Quiero la sensación de gente brindando con alegría, pero sin que se vea barato.
>
> Por favor, hágalo en un estilo sencillo de ilustración a base de líneas."

Unos segundos después aparecieron en la pantalla cuatro propuestas de ilustración.

De entre ellas elegí la ilustración "¡Salud!", sencilla y cálida, que mejor combinaba con el ambiente del local.

![La ilustración "¡Salud!" que la IA generó en solo 10 segundos](images/fig-22.png)

Tardó apenas 10 segundos.

No solo el análisis: el "material" necesario para la mejora se puede conseguir en el acto.

Esta es la verdadera fortaleza de incorporar la IA generativa a la gestión.

### 5-5. Solo cambiar la distribución elevó el gasto por cliente en un 40% aproximadamente

Así que rediseñé el menú.

#### Antes: el menú tal como estaba

- Mejor lugar (lo más alto): productos de precio bajo como el "Menú ¥2.200 (unos US$ 15)" y el "Menú Cerrado ¥3.300 (unos US$ 22)".

- Barra libre: indicada solo con texto, en la esquina inferior izquierda, como "Barra libre desde ¥3.000 (unos US$ 20)". Estaba completamente enterrada.

#### Después: el menú corregido

- Mejor lugar (lo más alto): planes de precio alto, de ¥4.500–¥5.700 (unos US$ 30–US$ 38), presentados como "¡Nuestra recomendación! Menú Disfrute Total (con barra libre)".

- Diseño: con la ilustración "¡Salud!" generada por la IA, se guía con fuerza la mirada, de forma visual, hacia "Mire aquí primero".

- Cambio de distribución: los menús baratos que antes eran las estrellas se pasaron más abajo.

![El menú Después. El menú con barra libre está colocado en lo más alto](images/fig-23.png)

La comida, los precios y la calidad de las bebidas casi no cambiaron, en realidad. Lo único que cambié fue "cómo se muestra" y "dónde".

¿Y el resultado?

Desde el día siguiente, el comportamiento de pedido de la clientela cambió de forma notable.

Las primeras palabras de quienes abrían el menú ya no eran "Una cerveza para empezar", sino "Entonces tomemos este 'Menú Recomendado (¥4.900 (unos US$ 33))', el de la ilustración".

Quienes antes terminaban con "el Menú (¥2.200 (unos US$ 15)) más dos bebidas" (un gasto de unos ¥3.500 (unos US$ 23) por cliente) ahora elegían desde el principio el menú de ¥4.900 (unos US$ 33).

Solo con esto, el gasto por cliente subió en ¥1.400 (unos US$ 9,3).

Además, la clientela ganó el beneficio de "poder beber sin preocuparse por la cuenta", así que la satisfacción subió en lugar de bajar.

### 5-6. Contrastar los resultados con el PDF de ventas de diciembre (PDCA)

Había pasado un mes desde que puse en marcha la medida.

No detenerse aquí es la esencia de usar IA.

Muchas personas que dirigen un local juzgan los resultados por intuición y lo dejan ahí: "Estuvimos ocupados, así que seguro funcionó", o "Subieron las ventas, así que está bien".

Pero volví a sentarme frente a Gemini.

Esta vez subí el "PDF de los datos de ventas de diciembre", donde ya estaban los resultados, y pregunté esto:

> "Ya están los resultados de la medida del mes pasado (el cambio del menú).
>
> Mire estos datos de ventas de diciembre y contraste y evalúe los resultados: ¿aumentó como se esperaba la cantidad de pedidos del 'Menú Recomendado' y cómo afectó al gasto por cliente?"

Gemini analizó los datos al instante y me devolvió un informe.

![La pantalla del informe de análisis de ventas de Gemini: hice un resumen para la publicación, así que el contenido difiere en parte del texto de abajo](images/fig-24.png)

El análisis de Gemini:

> "Son resultados excelentes. Según la tendencia de los datos, la cantidad de pedidos del 'Menú Disfrute Total' subió a aproximadamente 1,8 veces la del mes anterior.
>
> Como resultado, el gasto general por cliente subió en promedio ○○ yenes.
>
> El factor principal es que colocar el plan de barra libre en un lugar más alto elevó el valor de los pedidos, sobre todo en los grupos."

Al oír esas palabras, por primera vez sentí un verdadero alivio.

No un "de algún modo ganamos dinero", sino la seguridad de "alcancé las cifras de forma deliberada".

Esto se convierte en la fuerza para la siguiente medida.

1.  Plan (Planificar): mirar los datos de ventas y el menú, y encontrar el problema (el plan de barra libre estaba escondido).

2.  Do (Hacer): pedirle a la IA que dibuje una ilustración y cambiar la distribución del menú.

3.  Check (Verificar): pedirle que lea el PDF de ventas de diciembre y comprobar los resultados.

4.  Act (Actuar): pensar en revisar a continuación la distribución del menú de comidas.

El "ciclo PDCA" que las grandes empresas operan a un costo enorme puede operarlo una sola persona como yo, solo con un smartphone, si cuenta con la IA como compañera.

## Capítulo 6: Desafíos - Desarrollar un sistema solo para mi propio local

~ "Si no existe, se construye." Un proyecto de desarrollo de sistemas sin personas expertas ~

※Para que quede claro, no hace falta hacer todo lo de este libro.

・Enviar una imagen y pedirle a la IA que escriba texto\
・Convertir un mensaje largo de LINE en un diagrama

Con estas dos cosas basta para empezar. Solo con eso, ya le facilitarán el trabajo sin duda.\
También basta con leer esto como un relato y pensar: "Vaya, con la IA se puede hacer hasta esto."

### 6-1. Las aplicaciones listas para usar no llegan al lugar donde me "pica"

Hasta ahora he hablado de usar la IA sobre plataformas ya existentes, como la generación de imágenes y el análisis de menús.

Pero a medida que se sigue con el negocio, surgen preocupaciones que las "aplicaciones listas para usar" sencillamente no pueden resolver.

En particular, en un modelo de negocio poco convencional como el nuestro, "curry de día, bar de noche", el flujo de entradas y salidas de dinero también es complicado.

"Quiero cotejar el saldo de mi cuenta de PayPay Bank con los pagos que vienen y saber con qué monto llegaré a fin de mes."

"Las fechas de pago se dividen entre el 10 y el 25. Quiero simular eso."

El software de contabilidad que hay es muy capaz, pero ninguno apuntaba exactamente a "la preocupación que tenía en la cabeza en ese momento".

Así que tomé una decisión.

"Si no existe, lo construyo. Tengo a Gemini, el mejor ingeniero."

### 6-2. Fases 1 a 3: de las notas garabateadas a la "nube"

El desarrollo empezó mostrándole a Gemini mis notas de Google Keep.

![La nota de Keep que fue el punto de partida del desarrollo](images/fig-25.png)

#### Fase 1: construir la lógica

"Quiero automatizar los cálculos de esta nota."

Respondiendo a mi pedido, Gemini armó enseguida la lógica de cálculo.

- Cuando cambio el monto de un concepto, calcula al instante el saldo final.

- Si los fondos están a punto de quedarse cortos, muestra una "advertencia" en rojo.

- Simula el momento de los pagos, divididos entre "el 10" y "el 25 / fin de mes".

- Los datos se guardan en el navegador (caché).

Solo con esto ya era bastante cómodo, pero se me despertó la ambición. "Quiero que los datos se queden aunque cierre el navegador. Quiero poder consultarlos también desde el teléfono."

#### Fase 2: adoptar una herramienta desconocida, "Firebase"

Yo estaba pensando en enlazarlo con una hoja de cálculo, pero la sugerencia de Gemini fue inesperada.

"Si piensa en el tiempo real y en la eficiencia, usemos 'Firebase', de Google. El plan gratuito alcanza para hacerlo funcionar."

"¿Firebase...?" Nunca había oído esa palabra. Pero con el instinto de mis tiempos de coordinador de sistemas, decidí: "Si la IA lo recomienda con tanta fuerza, vamos con eso."

Como resultado, al usar una base de datos llamada Firestore, los datos pasaron a guardarse de forma segura en la nube.

#### Fase 3: inicio de sesión con Google y un sistema de aprobación

Se trata de dinero, así que no conviene que cualquiera pueda verlo.

Al principio pensé en algo como una "frase de contraseña", pero Gemini sugirió: "Si quiere más seguridad, usemos el inicio de sesión con Google."

Luego, cuando dije: "Quiero que solo el personal que yo apruebe pueda verlo", incluso construyó "un sistema en el que una persona administradora puede aprobar y quitar miembros desde la pantalla".

### 6-3. Fases 4 y 5: enfrentarse a la pantalla negra (la terminal)

A partir de aquí llegó el mayor desafío del vibe coding: publicar la aplicación en internet (desplegarla).

#### Advertencia: de aquí en adelante, es el curso de "cinturón negro"

Las próximas páginas son la parte "práctica" más difícil de este libro. Usted manejará una "pantalla negra (terminal)" como las que usan los hackers en las películas.

Hablaré con franqueza. Aquí seguro le saldrán errores. A mí también. Se topará con muros como un "error de permisos de PowerShell" que se lee como un conjuro. Pero no tenga miedo. Lo que hay que hacer aquí es lo mismo de siempre: solo "tomar una captura de pantalla del error y lanzársela a la IA".

La verdad que aprendí en mis días en el negocio de los sistemas es esta: "Hasta los profesionales reciben errores. La única diferencia es si uno se rinde cuando aparece uno o busca (pregunta) ayuda." Si le parece demasiado difícil, salte esta sección y quédese solo con la posibilidad: "Con la IA se puede hacer hasta esto."

Gemini dijo:

"Prepararemos el entorno de desarrollo en su computadora con Windows. Instale 'Node.js' y escriba los siguientes comandos en 'VS Code'."

Abrí la pantalla negra (terminal) como me indicó, y de inmediato apareció un error.

"No se puede ejecutar por las restricciones de seguridad de PowerShell."

Una persona común que dirige un local se desanimaría aquí.

Pero yo copié y pegué el mensaje de error y se lo envié a la IA.

La IA respondió al instante: "Levante la restricción con un comando llamado 'Set-ExecutionPolicy'."

Sin entender qué significaba, escribí el comando, luego npm run build, firebase deploy...

Cada vez que tecleaba esos caracteres que parecían conjuros, el texto corría por la pantalla y el proceso avanzaba.

Y por fin, mi aplicación apareció en la web.

#### Fase 5: convertirla en una aplicación para smartphone (PWA)

La aplicación publicada estaba al principio "sin estilos", con el diseño roto, pero esto también se resolvió agregando una herramienta llamada "Tailwind CSS".

Luego, cuando le pedí: "Quiero poner un ícono en la pantalla de inicio del teléfono y usarla como una aplicación", me enseñó los ajustes para convertirla en una "PWA (Progressive Web App)".

Así nació dentro de mi teléfono una aplicación exclusiva que hice yo (sin escribir ni una sola línea de código).

![La pantalla de la aplicación terminada para administrar el flujo de caja](images/fig-26.png)

### 6-4. Fase 6: el problema a los 30 días y su solución

Aproximadamente un mes después de empezar a usarla, surgió un problema.

"Funcionaba hasta ayer, ¡y de repente no puedo entrar!"

Entré en pánico y consulté a Gemini, y la causa estaba en un lugar inesperado.

"La configuración de la base de datos (Firestore) seguía en 'modo de prueba (limitado a 30 días)'. Ya venció."

Para ahorrar la molestia de configurar al comienzo del desarrollo, la IA había establecido a propósito una regla con fecha de vencimiento.

"Reescribamos las reglas de seguridad para que 'cualquier usuario que haya iniciado sesión pueda seguir usándola'."

Cuando reescribí unas pocas líneas del archivo de configuración como indicó la IA, la aplicación volvió a funcionar sin problemas.

Este problema también fue una buena experiencia para mí.

Aprendí que "un sistema es algo vivo y necesita mantenimiento".

Y gané la tranquilidad de que "aunque haya problemas, siempre hay una respuesta si le pregunto a la IA".

### 6-5. Caso de estudio 2: el "proyecto de reconocimiento facial" que empezó con un video de demostración en X (antes Twitter)

Aquí va otro desarrollo de sistema que emprendí, y el más grande.

Es "un sistema que reconoce con una cámara a la clientela que entra y me informa discretamente su nombre, sus datos y sus preferencias".

Empezó en la red social X, por la que yo navegaba sin ninguna intención.

En mi pantalla apareció un video de demostración publicado por una persona ingeniera: usaba la IA integrada en Google Chrome (Built-in AI) para explicar en tiempo real lo que veía una cámara web.

Se activó mi instinto de antiguo profesional de sistemas.

"Esto es 'multimodal'. Y si viene integrado en el navegador, ¿no podría funcionar por completo en mi propia computadora, sin pagar la nube?"

Si esto funcionaba, quizá podría construir un sistema de atención exclusivo para mi local, sin instalar un sistema costoso.

Copié la URL y se la lancé a Gemini.

"Quiero hacer lo mismo que esto. Dígame cómo implementarlo."

#### Fase 1: funcionó, pero no podía saber "quién"

Cambié los ajustes de Chrome (flags) como indicó Gemini y pegué el código, y el mismo sistema de la demostración funcionó sin problemas.

Cuando aparecí en la cámara, la pantalla mostró esto:

"Un hombre con lentes está sentado frente a una computadora."

Usa una IA integrada en el navegador llamada GeminiNano. Su ventaja es que funciona por completo dentro del navegador sin conectarse a la nube, pero solo puede reconocer cosas generales como "lentes" y "hombre". No llega a determinar quién es la persona.

Es una tecnología asombrosa. Pero, como responsable de un restaurante, me decepcioné de inmediato.

"Así no sirve."

Lo que quiero saber no es una característica general como "un hombre con lentes", sino la identificación de la persona: "¿Es A o es B?"

#### Fase 2: el muro de la integración con Google Fotos y la respuesta de la IA

Entonces le planteé a Gemini una idea ingenua.

"Conecte este sistema a mi Google Fotos. Ahí hay datos de agrupación de rostros de mis amistades y de la clientela habitual; si los compara con eso, se pueden obtener los nombres, ¿verdad?"

La respuesta de Gemini fue fría, pero correcta.

"Lo siento, pero eso no es posible. Los datos de reconocimiento facial de Google Fotos son información de privacidad muy sensible, y por motivos de seguridad no se permite que los usen programas externos."

Es comprensible. El camino parecía terminar aquí.

Pero desde aquí vino la verdadera esencia del "vibe coding (desarrollo mediante el diálogo)". La IA no se limitó a negarse.

#### Fase 3: una alternativa y un giro

Gemini siguió con esta sugerencia:

"No podemos usar Google Fotos, pero es posible construir su propio sistema de reconocimiento facial en un entorno local con bibliotecas de código abierto (como OpenCV o face_recognition). ¿Lo intentamos?"

Respondí "Sí" de inmediato.

Desde ahí, el plan de desarrollo cambió por completo. En lugar de usar las funciones de Chrome, construiría un sistema de reconocimiento facial desde cero con un lenguaje de programación llamado Python.

#### Fase 4: pelear con la pantalla negra y conectar con una hoja de cálculo

Lo que tenía que hacer no cambió. Le pregunté a Gemini "cómo instalar las bibliotecas necesarias" y pegué la respuesta en la pantalla negra (el símbolo del sistema).

Cuando aparecía un error, le devolvía a Gemini el texto rojo tal cual.

Unas horas después, el sistema por fin estuvo completo.

1.  La cámara web captura mi rostro.

2.  Lo compara con los "datos de fotos de rostros" de una carpeta de la computadora.

3.  Cuando encuentra una coincidencia, consulta la lista de clientes en una hoja de cálculo de Google.

4.  La pantalla muestra "Bonta: quedan ○○ g en la botella cuadrada".

![El sistema de reconocimiento facial en funcionamiento. Reconoce el rostro de quien dirige el local y muestra información. La imagen capturada fue pixelada con mosaico usando Gemini](images/fig-27.png)

Costo de subcontratación: ¥0 (unos US$ 0,00). Mi propio trabajo de programación: cero.

Fue el momento en que nació, en un rincón de Higashi-Nakano, un "sistema CRM de reconocimiento facial" único en su especie.

#### Fase 5: y entonces me doy cuenta de la "responsabilidad de proteger"

El sistema estaba completo. Pero junto con la alegría, sentí un escalofrío en la espalda.

"Un momento. Ahora mismo, esta computadora guarda datos faciales de la clientela (información biométrica), ¿no es así...?"

Hasta entonces yo había pensado: "Mientras funcione, está bien." Pero una vez en operación real, es otra cosa.

¿Y si esta computadora se infecta con un virus? Los datos faciales de la clientela y la información de sus preferencias (datos personales) podrían filtrarse juntos.

Una computadora aislada, sin conexión a internet, sería segura, pero mientras maneje reservas y redes sociales, la conexión a internet es indispensable.

"Poder construir una herramienta útil" y "poder administrarla con seguridad" son cosas distintas.

Fue aquí donde sentí de verdad por primera vez la importancia del "seguro de riesgo cibernético" del que me habló alguien de una aseguradora cuando vino a ofrecérmelo.

Yo me había reído: "A un local pequeño como el nuestro no le harán ciberataques", pero ahora que la IA nos permite construir sistemas avanzados, quienes dirigimos un local por cuenta propia también asumimos la responsabilidad de ser verdaderos "administradores de datos".

Con la IA se pueden conseguir herramientas mágicas.

Pero aprendí que cargar con el "bastón (el conocimiento)" y el "escudo (las medidas de seguridad)" para usar esa magia también será, de ahora en adelante, parte del trabajo de quien dirige un local.

### 6-6. La "responsabilidad" y el "seguro" que acompañan a la libertad

#### Importante: privacidad y datos personales

Este "sistema de reconocimiento facial" es un prototipo experimental que construí para comprobar qué es técnicamente posible. Si se usara en un local real, los datos faciales de la clientela contarían como "datos personales (datos biométricos)" y tendrían que protegerse estrictamente conforme a la ley (la Ley de Protección de la Información Personal).

Si piensa adoptar algo así, tenga presentes sin falta estos dos puntos.

Avisar a la clientela y obtener su consentimiento: hace falta un proceso, como colocar un cartel en la entrada que diga "Usamos reconocimiento facial con IA" y pedir el consentimiento cuando las personas se registran como miembros. Filmar en secreto no está permitido de ninguna manera.

Proteger los datos: hacen falta medidas que reduzcan a cero el riesgo de filtración, como administrar los datos en un entorno aislado de internet.

Poder construir algo no es lo mismo que tener permiso para hacerlo. Si usted tiene habilidades técnicas y dirige un local, recuerde que la responsabilidad de usar esa tecnología viene con ellas.

Hasta ahora he hablado de lo maravilloso que puede ser un sistema hecho a mano. Pero, como persona que dirige un negocio, también debo contarle una realidad dura.

Es esta: "Todo lo que usted construya por su cuenta es su propia responsabilidad."

Con un servicio de suscripción mensual (SaaS), si el servidor se cae, la empresa pide disculpas y lo pone otra vez en marcha.

Pero un sistema construido con vibe coding no tiene "atención al cliente".

Si su aplicación deja de funcionar de pronto en el pico del almuerzo, nadie vendrá a ayudar.

Cuando Google cambia una especificación, que un código que ayer funcionaba bien hoy dé errores es algo de todos los días.

Por eso hago dos preparativos.

Uno es un "respaldo analógico".

"Si el reconocimiento facial se detiene, mirar el libro de clientes en papel." "Si la aplicación de caja se cae, usar una calculadora y comprobantes escritos a mano."

Las herramientas digitales son solo "herramientas cómodas". No hay que depender tanto de ellas como para que, cuando se detengan, se detenga también el local.

El otro es el "seguro" que mencioné antes.

El seguro de responsabilidad cibernética no cubre solo el riesgo de una filtración de información, sino también la indemnización por el negocio perdido cuando un error propio detiene el sistema. Para quien dirige un local por cuenta propia y se arma con TI, es parte de ser una persona adulta responsable.

"A veces las cosas se detendrán. A veces nos equivocaremos."

Tómelo como un hecho, acepte el riesgo y tome medidas frente a él.

Solo cuando tenemos esta determinación podemos usar de verdad un "sistema libre" sin ataduras.

### 6-7. No hace falta una persona experta. Hace falta perseverancia

No pagué ni un solo yen en honorarios de subcontratación por el desarrollo de estos dos sistemas.

Lo único que usé fue una suscripción de IA de unos pocos miles de yenes al mes, y la perseverancia de alguien que dirige un local y pensaba: "Tengo que quitarme sí o sí esta preocupación (el flujo de caja)" y "Quiero hacer felices a mis clientes".

No es cuestión de "no puedo, porque no sé programar".

Si usted tiene algo que quiere construir (el Qué), la IA le enseñará cómo construirlo (el Cómo).

Aun cuando aparezcan palabras que no entiende (Node.js, PowerShell, Firestore...), no hay nada que temer.

Contamos con el mejor compañero que existe, "Gemini", para traducirlas y guiarnos.

#### Columna 4: ¿Cuál es la diferencia entre Excel y una base de datos (Firestore)?

~ ¿Es un "nota para que la lea usted" o un "libro de registro para que lo lea el sistema"? ~

En el desarrollo de la aplicación de flujo de caja apareció Firebase (Firestore). Quizá se preguntó: ¿por qué no Excel?

Una hoja de cálculo (Excel) es un "cuaderno que las personas miran y en el que escriben". Es muy flexible, pero para un sistema resulta ambigua en cuanto a "qué hay en cada lugar".

Una base de datos (Firestore), en cambio, es un "casillero bien ordenado hecho para el sistema". Como está fijado que "la fecha va en el casillero 1 y el monto en el casillero 2", un programa puede manejarlo al instante. Además, no se rompe cuando varias personas entran al mismo tiempo.

"Si va a crear una aplicación, use una base de datos, no Excel." Solo con saber esto, subirá el nivel de sus instrucciones a la IA.

## Epílogo: una "receta del futuro" que solo tiene su local

~ La IA no es una tecnología difícil. Es una nueva compañera de "conversación" ~

Gracias por leer este libro hasta el final.

Si prueba una sola cosa de este libro, pruebe esta: "Pegue ese engorroso mensaje de LINE directamente en la IA y pídale que lo 'convierta en un diagrama'."

No poseo conocimientos especiales de IA. Simplemente he repetido, todos los días, la práctica de "hablarle a la IA con las palabras del lugar de trabajo", \
en el campo de batalla de un restaurante.

Por eso creo que basta con que se lleve de este libro no una "colección de respuestas correctas", sino solo una "forma de pensar".

Cuando abrió la primera página, ¿qué imagen tenía de las palabras "usar IA"?

"Suena difícil." "Hacen falta conocimientos de programación, ¿verdad?" "No tiene nada que ver con un local pequeño como el mío."

Quizá pensó algo así.

Pero ahora que ha leído hasta aquí este registro de mi "prueba y error", tal vez esa imagen haya cambiado un poco.

Lo que hice no fue hacer un uso sofisticado de una tecnología de TI avanzada.

Me quejé: "Esto no puedo hacerlo a mano." Protesté: "Esto es difícil de usar." Y pedí a mi antojo: "Quiero que funcione más así."

Hoy en día, en el mundo de la ingeniería, el término "vibe coding" es tendencia.

Es un método para construir un sistema por intuición, conversando con la IA.

Así como quien juega al shogi conversa con la IA para leer las próximas jugadas, nosotros también podemos conversar con la IA y construir el "futuro de nuestros locales".

Como decirle al personal de cocina: "Póngale un poquito más de sal."

Como preguntarle a la persona que vende pescado en el mercado: "¿Hay buen pescado hoy?"

Hablarle a la IA y decirle: "Haga más fácil este trabajo." Ahí empieza todo.

Antes trabajé en el departamento de sistemas de una empresa, coordinando entre "el local" y las "personas desarrolladoras".

Ahora hago lo mismo entre "mi propio local" y la "IA".

Y estoy convencido de esto:

"Quien dirige un local y conoce los problemas del día a día del local puede convertirse en la persona más capaz al mando de la IA."

Empiece hoy, usted también.

Primero, saque su teléfono y hable con Gemini.

"Oye, ¿por dónde empiezo con la preparación de hoy?"

"¿Cómo puedo hacer que este plato del menú se venda mejor?"

"Este trámite es una lata. ¿Puedes hacer algo al respecto?"

No se preocupe si aparece un error. Es una señal de que la "conversación" ha comenzado.

Solo tome una captura de pantalla y devuélvasela con un "algo no cuadra".

Tras acumular esas conversaciones, le esperan un "tiempo" y un "respiro" que nunca habría imaginado, y "un futuro que pertenece solo a su local".

Ahora, contratemos también para su local a un "subgerente" confiable.

Porque la receta del futuro nacerá de la conversación entre usted y la IA.

### Los tres caminos que ofrece este libro

Este libro se puede leer gratis en PDF, en la plataforma note y en Google Play. (Solo en Kindle, las reglas de la tienda exigen un precio mínimo.) A cambio, he preparado tres lugares a los que puede ir cuando termine de leer. Si usa aunque sea uno de ellos, habrá valido la pena escribir este libro.

1. Pruébelo en su propio local. Puede empezar con un cuaderno gratuito de la serie Agenda. https://bontallc.com/agenda?via=b1-es-{{FMT}}
2. Siga lo que hago. Escribo sobre las próximas herramientas que construyo y sobre la vida cotidiana en el bar, en note y en X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Si alguna vez viene a Tokio, visite Tamuro. A un minuto de la salida este de la estación Higashi-Nakano. Puede entrar sin reserva. Cuando se escribió este libro por primera vez, Tamuro era solo por recomendación. Hoy cualquier persona puede entrar sin reserva. Sitio de reservas https://tamuroreservation.vercel.app/?src=b1-es-{{FMT}}

Si nos visita gracias a este libro: al hacer su reserva, introduzca el código de cupón "BOOK". Le serviremos una bebida en su primera visita. Si vino sin reserva, solo diga "Vi el libro" al hacer su primer pedido. También le serviremos una bebida. Es un pequeño recurso para que yo pueda contar cuántas personas vinieron por el libro.

### Sobre la autoría

Raku Bonta

Dirige en solitario un restaurante con 11 asientos en la barra y 8 en la sala de tatami, en Higashi-Nakano, Tokio.

De día es un local de curry con hanbāgu perfumado de especias. De noche es un bar-comedor solo por recomendación que sirve un menú del día que cambia cada jornada.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry](images/fig-28.png)

▼ Bar solo por recomendación "Tamuro"

https://www.instagram.com/tamuro.higashinakano/

![Bar solo por recomendación "Tamuro"](images/fig-29.png)

El local también se dedica a construir comunidad a través de la comida, con eventos de vino cada dos semanas, una clase de cocina mensual y cenas de varios tiempos.

Antes de abrir el local por su cuenta hace 12 años, la autoría trabajó en una empresa en "planificación de sistemas" y "arquitectura de soluciones".

Los cargos suenan difíciles, pero el trabajo real era el de "coordinación: transmitir con exactitud a los proveedores de TI los deseos de quienes trabajan en el local de 'queremos hacer esto' y lograr que lo construyan". Sin ser una persona ingeniera de programación avanzada, la autoría tiene una trayectoria como "traductora" que conecta a las personas con la tecnología.

Hoy, apoyándose en esa experiencia, la autoría usa IA generativa como Google Gemini para dirigir su propio local, y practica y comparte una "reforma del negocio que funciona incluso con cero conocimientos especializados".
