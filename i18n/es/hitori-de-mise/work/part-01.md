## Introducción

Este libro es un registro a enero de 2026. Algunas de mis formas de llevar el local, y algunos nombres y especificaciones de las herramientas de IA, han cambiado desde entonces. La historia continúa en el segundo libro, *Hecho a la medida de nuestro bar*.

### Por qué alguien que venía del mundo de los sistemas conversa con la IA en un restaurante subterráneo

Gracias por elegir este libro.

*Una sola persona atiende el local, y la IA apareció a mi lado.*

Al ver ese título, tal vez algunos de ustedes piensen: "Ese soy yo." Otros quizá se pregunten: "¿Qué significa que la IA aparezca a su lado?"

Este no es un libro técnico sobre programación difícil. Es un libro para personas como ustedes, quienes dirigen un restaurante, están cada día en la cocina, hacen la preparación y no dan abasto atendiendo a la clientela.

Permítanme contarles un poco sobre mí.

Ahora dirijo un pequeño restaurante en el sótano de un edificio en Higashi-Nakano *(un barrio residencial del oeste de Tokio, justo al oeste de Shinjuku)*, en Tokio.

Tiene dos caras. De día, es un local especializado en curry con hanbāgu *(bistec de carne picada a la plancha al estilo japonés, parecido al hamburg steak)*, con un aroma intenso a especias. De noche, es un bar-restaurante, que ofrece un menú del día y bebidas.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Bar "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar "Tamuro" (Instagram)](images/fig-02.png)

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
