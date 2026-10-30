# Hecho a la medida de nuestro bar

Cómo quien dirige un bar de 19 asientos construyó con IA todo, desde las reservas hasta sus herramientas

Raku Bonta

La serie Agenda: https://bontallc.com/agenda?via=b2-es-{{FMT}}

Instagram de Tamuro: https://www.instagram.com/tamuro.higashinakano/

Sitio de reservas de Tamuro: https://tamuroreservation.vercel.app/?src=b2-es-{{FMT}}

## Introducción

Este libro es un registro sincero de cómo quien dirige un bar de 19 asientos en Higashi-Nakano *(un barrio residencial del oeste de Tokio, justo al oeste de Shinjuku)*, Tokio, maneja el local con la ayuda de la IA.

El bar se llama "Tamuro". El nombre significa un lugar donde la gente se reúne. Abrió en noviembre de 2018: un local pequeño con 11 asientos en la barra y 8 en el salón de tatami. Durante el día, en ese mismo espacio, una persona del personal atiende un restaurante de curry con hanbāgu *(bistec de carne picada a la plancha al estilo japonés, parecido al hamburg steak)* llamado "Quatre Épices".

En mi libro anterior, *El subgerente de IA*, escribí sobre la IA generativa en sí. En poco más de un año desde entonces, la IA pasó de ser una herramienta que responde preguntas a una que saca el trabajo adelante por usted. Usted le da una instrucción, y ella escribe el programa, lo prueba, corrige sus propios errores y termina la tarea. A este tipo de IA la llamamos IA agéntica.

Con esta IA agéntica construí yo mismo el sistema de reservas de Tamuro. Construí un sistema de descuentos para acompañar una subida de precios. Construí un sistema para cultivar la relación con la clientela habitual. Construí una IA que responde las preguntas de la clientela. Y al final llegué al punto en que una persona puede preguntarle a Tamuro desde su propia IA y seguir hasta hacer una reserva.

También tomé las herramientas prácticas que había hecho para mi propio local, las adapté para que otros locales pudieran usarlas y empecé a ofrecerlas por unos cientos de yenes al mes. Esa es la serie Agenda.

Este libro describe lo que construí en el camino, en qué fallé y qué tuve que volver a aprender. No son solo historias de éxito. Yo seguía construyendo cosas que funcionaban, guiado por la intuición, y las contradicciones se fueron acumulando. Más tarde descubrí que los datos personales de la clientela podían leerse desde fuera. La IA escribió cosas que el local nunca había afirmado. He incluido esos fallos tal como ocurrieron.

### Cómo leer este libro

Este libro tiene cinco capítulos.

| Capítulo | Contenido | Ideal para |
| --- | --- | --- |
| Capítulo 1 | Un local que recibe reservas desde la IA (el lado del negocio del sistema de reservas) | Todas las personas |
| Capítulo 2 | El sistema de reservas por dentro (técnico) | Quienes construyen y quienes sienten curiosidad por la tecnología |
| Capítulo 3 | Compartir las herramientas de nuestro local con otros locales (el lado del negocio de la serie Agenda) | Todas las personas |
| Capítulo 4 | Un sistema para crear productos en solitario (técnico) | Quienes construyen y quienes sienten curiosidad por la tecnología |
| Capítulo 5 | El futuro de los locales pequeños | Todas las personas |

Los capítulos 2 y 4 son técnicos y usan más términos especializados. Cada uno comienza con un resumen de tres líneas con los puntos clave; si la tecnología no le interesa, lea solo eso y pase al capítulo siguiente. Si lee los capítulos 1, 3 y 5 en orden, la historia mantiene un hilo claro.

Siempre que pude, añadí junto a cada término técnico una explicación en lenguaje sencillo. Aunque usted nunca haya escrito un programa, espero que se haga una idea de lo que significa llevar un local con IA.

### Sobre quien escribe

Trabajé unos 16 años en informática, sobre todo en planificación de sistemas y como enlace entre el área operativa del negocio y los proveedores de desarrollo, y luego entré en el negocio de la comida y la bebida. Así que esta no es la historia de alguien que nunca había escrito una línea de código y lo construyó todo solo con IA. Quiero ser transparente al respecto.

Aun así, hoy puedo construir y operar por mi cuenta, mientras atiendo el local, algo de una escala que antes exigía un equipo y financiamiento. Hace unos años habría sido impensable. Quiero describir la realidad de ese cambio de la forma más concreta posible.

### Cómo se hizo este libro

Este libro también lo hice con IA. A partir de los registros que he llevado en mi trabajo diario de desarrollo, la IA escribió los borradores, y yo leí, revisé y tomé las decisiones. También le pedí a la IA que tomara las capturas de pantalla usadas como ilustraciones.

Lo he revisado de principio a fin, pero un texto escrito por IA puede incluir afirmaciones inexactas. Como explico más adelante en el libro, la IA dice "ya está hecho", y comprobarlo es tarea humana. Puede haber errores en este libro que yo haya pasado por alto.

Además, las especificaciones de las herramientas y los servicios de IA cambian en pocos meses. Los pasos, los precios y las funciones que admite cada empresa que se describen en este libro corresponden a octubre de 2026. Cuando usted lo pruebe por su cuenta, consulte la información oficial de ese momento.

Si detecta un error, me alegraría que me lo dijera en note o en X. Lo iré corrigiendo a medida que me entere.

### Tres caminos para después de este libro

Este libro se puede leer gratis en PDF, en note y en Google Play. (Solo en Kindle, las reglas de la tienda exigen un precio mínimo.) A cambio, he preparado tres lugares a los que puede ir cuando termine de leer. Si aunque sea uno le resulta útil, habrá valido la pena escribir este libro.

1. Pruébelo en su propio local. Puede empezar con la serie Agenda con el cuaderno gratuito. https://bontallc.com/agenda?via=b2-es-{{FMT}}
2. Siga mis novedades. Escribo sobre las próximas herramientas que construyo y sobre la vida diaria del local en note y X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Si alguna vez viene a Tokio, visite Tamuro. A un minuto de la salida este de la estación de Higashi-Nakano. Puede entrar sin reserva. Sitio de reservas https://tamuroreservation.vercel.app/?src=b2-es-{{FMT}}

## Capítulo 1: Un local que recibe reservas desde la IA

### 1-1 "¿Hay algún lugar abierto esta noche?" Usted se lo pregunta a la IA

Un viernes por la tarde, alguien que acaba de salir del trabajo le habla a su teléfono.

"¿Hay algún lugar en Higashi-Nakano donde pueda tomar algo a solas esta noche? Algo que no sea muy ruidoso".

Quien responde no es un amigo. Es la IA que esa persona usa todos los días. La IA enumera los locales candidatos, describe el ambiente de cada uno y le informa los horarios disponibles y los precios de esta noche. Si algo le llama la atención, puede ir directo a la pantalla de reserva.

Esto no es una historia sobre el futuro.

El 10 de agosto de 2026, OpenAI añadió una función de reserva de restaurantes a ChatGPT. Según las notas de la versión oficial, se conecta con los servicios de reservas OpenTable, Resy y Yelp, y los horarios disponibles aparecen directamente dentro de las respuestas de ChatGPT. También se pueden hacer preguntas para acotar las opciones y, una vez que se elige un horario conveniente, se puede pasar directamente a reservar. Cubre OpenTable en todo el mundo, Resy en Estados Unidos y Yelp en Estados Unidos y Canadá.

En otras palabras, la puerta que la gente usa para buscar dónde comer está empezando a pasar de los buscadores y los sitios de reseñas de restaurantes a "mi propia IA".

Pero hay una condición. Los únicos locales que se pueden reservar a través de ChatGPT son los registrados en los grandes servicios de reservas. Los locales pequeños que no figuran allí son invisibles para la IA.

Entonces, ¿qué debe hacer un bar de 19 asientos en Higashi-Nakano que no usa los grandes servicios de reservas?

Tamuro eligió otro camino. Sin pasar por los grandes servicios, conectó su propio sistema de reservas directamente con la IA.

Cuando alguien le pregunta a su propio ChatGPT o Claude: "¿Hay sitio en Tamuro esta noche?", la IA consulta directamente el sistema de reservas de Tamuro, comprueba los horarios disponibles y los precios, y responde. Una vez fijadas las condiciones, lleva a la persona a la página de reservas de Tamuro con el número de personas y la fecha y la hora ya completados. El botón final de confirmación lo pulsa la propia persona.

Este "punto de conexión entre la IA y el sistema de un local" se llama servidor MCP. MCP significa Model Context Protocol, un conjunto común de acuerdos que permite a la IA usar herramientas y datos externos. Explico los detalles en el capítulo 2.

De hecho, los grandes servicios de reservas también acaban llevando a la clientela a sus propias pantallas. En las reservas que exigen tarjeta de crédito, el proceso se completa en la pantalla de OpenTable, y los cambios o cancelaciones posteriores se gestionan en cada servicio. La IA es la entrada, y la pantalla del servicio de reservas es donde se confirma. Lo que hace Tamuro tiene la misma estructura. La única diferencia es que no hay ninguna gran empresa en medio.

Y quien construyó este sistema no fue una empresa de desarrollo externa. Fui yo, quien dirige el local. Le di instrucciones a la IA, hice que la IA escribiera los programas e hice que la IA ejecutara las pruebas.

Por supuesto, no llegué hasta aquí desde el principio. Empezó con un formulario de reservas muy simple. Luego vino una subida de precios, después las ideas de descuentos, después un sistema para cultivar la relación con la clientela habitual, y luego los fallos y la reconstrucción.

Primero, describo en cinco líneas cómo es Tamuro. A un minuto a pie de la salida este de la estación de Higashi-Nakano. 19 asientos: 11 en la barra y 8 en el salón de tatami. Cerca de la mitad de la clientela viene sola, y la barra facilita empezar a conversar con la persona de al lado. La comida es una combinación de cuatro entradas y un plato fuerte, y el plato más popular es un tonteki (bistec de cerdo) dulce y con ajo. Los vinos son sobre todo de España e Italia, y hay unas 20 clases de ginebra artesanal japonesa. Puede entrar sin reserva.

Quiero también decir algo que buscaba. No quería limitarme a tomar reservas. Quería que incluso un local pequeño pudiera construir con sus propias manos todo el recorrido de darse a conocer, lograr que la gente venga y lograr que vuelva. Los descuentos, los correos y la ventana de chat que aparecen en este capítulo son todos piezas al servicio de ese único propósito.

En este capítulo, retrocedo en el tiempo y sigo cómo creció el sistema de reservas de Tamuro.

【Figura 1-1】La pantalla después de conectar desde ChatGPT al servidor MCP de Tamuro (10 de octubre de 2026). Lee la información del local y responde que puede informar sobre horarios disponibles, menús, precios y la guía hacia la página de reservas *(La pantalla está en japonés.)*

### 1-2 El punto de partida: solo tomar reservas

[El sitio de reservas de Tamuro](https://tamuroreservation.vercel.app/?src=b2-es-{{FMT}}) era muy simple al principio. Se elige una fecha, una hora y el número de personas, se ingresa un nombre y los datos de contacto, y se envía. Le llega un aviso al local. Eso es todo.

Construí la primera base con la herramienta de desarrollo con IA de Google (Antigravity). Le contaba a la IA cada función que se me ocurría y, cuando funcionaba, pasaba a la siguiente. Es lo que se llama vibe coding (decirle a la IA lo que a uno se le ocurra y hacer que construya a ojo).

Para mí, en aquel momento, fue una sorpresa tras otra. Uno describe con palabras la disposición de una pantalla y toma forma en minutos. Uno dice que quiere un calendario, y aparece un calendario. En los huecos que dejaba atender el local, fue surgiendo un sitio de reservas.

A Tamuro se puede entrar sin reserva. De hecho, la mayoría de las reservas se hacen el mismo día, y mucha gente simplemente llega. Aun así, construí un sistema de reservas porque quería una forma de conectar con la clientela antes de su visita. Cuando alguien reserva, quedan su nombre y sus datos de contacto. Y cuando quedan sus datos de contacto, puedo invitarle a volver.

Un sistema de reservas no es solo una recepción. Se convierte en la puerta de entrada a una relación con la clientela. Esta idea llevó más adelante al sistema de descuentos y al sistema para cultivar la relación con la clientela habitual.

Pero por haber levantado una base guiado por la intuición, terminé pagando un precio alto más tarde. Lo cuento en el capítulo 2.

### 1-3 Construir a la vez una subida de precios y descuentos

Para un restaurante o un bar, subir los precios es una decisión inevitable. Los ingredientes, los servicios y la mano de obra se encarecen sin parar. Tamuro también subió los precios. Subí cada menú unos ¥400–¥500 (unos US$ 2,7–US$ 3,3).

El aumento era grande, así que era evidente que, si lo anunciaba tal cual, la clientela habitual se iría alejando. Por eso, a la vez que la subida de precios, decidí incorporar un sistema de descuentos al sistema de reservas. No se trata solo de abaratar. Recompensa con descuentos a quienes actúan de maneras buenas para el local.

El primero es el descuento por grupo. Cuantas más personas haya en el grupo, menor es el precio por persona. Cerca de la mitad de la clientela de Tamuro viene sola, pero si viene en grupo, las ventas del local crecen muchísimo. Incluso después de restar el descuento, el local sale ganando. Para la clientela, además, es un motivo para invitar a sus amistades. De hecho, ha aumentado la cantidad de gente que viene en grupo usando el descuento por número de personas del sitio de reservas.

El segundo es el descuento por reserva anticipada. Si se reserva con al menos una semana de anticipación, se obtiene un 2% de descuento; con al menos dos semanas, un 4%. La mayoría de las reservas de Tamuro se hacen el mismo día, así que no puedo prever lo que viene. El descuento por reserva anticipada es un mecanismo para asegurar ventas futuras. En los días de lluvia y de frío, si ya hay reservas, el local puede prepararse con tranquilidad.

En tercer lugar, construí también un mecanismo de compra grupal. Si se reunía un número determinado de personas en una fecha y hora determinadas, se ofrecía un menú fijo a precio rebajado. Se suponía que sería un mecanismo con el espíritu de Tamuro, donde personas desconocidas se reúnen a la misma hora.

Pero el plan de compra grupal no se usó nunca. Cero resultados. En agosto de 2026 detuve este plan y decidí no volver a usarlo.

Tirar algo que uno hizo da pena. Pero si se construye con IA, el costo y el tiempo de construir son pequeños. Se construye en pequeño, se prueba y, si no funciona, se tira. Creo que esta velocidad es la mayor ventaja de llevar un local con IA.

Hay un truco más en los precios. Entre los planes, coloco a propósito un plan premium caro. No importa que casi nadie elija el plan premium. Con un plan costoso al lado, el estándar parece asequible. Cumple el papel de lo que se llama un ancla (un punto de referencia para comparar).

【Figura 1-7】A más personas, menor precio por persona (comparación de 1, 4 y 6 personas)

### 1-4 Un sistema para cultivar la clientela habitual

Una vez que los nombres y los datos de contacto quedan en el sistema de reservas, lo siguiente que uno quiere es cultivar la relación con la clientela. Un sistema que gestiona la información de la clientela y profundiza las relaciones se llama CRM (gestión de la relación con el cliente). Poco a poco fui añadiendo funciones de CRM al sistema de reservas de Tamuro.

Cuando la clientela se registra como miembro, puede ver su historial de reservas en una página personal. Si registra su cumpleaños, recibe un obsequio de cumpleaños. A quienes llevan un tiempo sin venir les llega un mensaje para invitarles a volver. También hay una tarjeta de sellos. Con tres visitas se gana una bebida, con cinco un bistec y otros beneficios, y al llegar a cinco la cuenta vuelve a empezar. También hay una función para recomendar a amistades.

Diseñé con especial cuidado el mecanismo para invitar a una segunda visita. En restaurantes y bares se dice que lo que decide si alguien se vuelve habitual es que regrese una segunda vez. En Tamuro envío dos correos de invitación, a los siete días y a los 21 días de la primera visita. El primero no lleva cupón; solo el segundo lo lleva. En lugar de atraer con un descuento desde el principio, primero ayudo a recordar. Si aun así no vienen, les doy un empujoncito.

También cuidé que los correos no se acumularan. La clientela recibe como máximo un mensaje al día. Cuando coinciden, la prioridad va en este orden: cumpleaños, invitación a la segunda visita, invitación a volver para quienes llevan tiempo sin venir, otros avisos. Quienes ya tienen su próxima reserva no reciben correos que les inviten a venir.

El consentimiento para recibir correos está desactivado de forma predeterminada. Dejarlo activado aumentaría el número de destinatarios, pero un diseño en el que la gente consiente sin saberlo podría ser un problema según la ley de protección al consumidor. Ganarse la confianza, no sumar cifras. Ese fue mi criterio.

Hay otro pequeño detalle en los correos. En el correo de confirmación de la reserva va un "Tema de hoy". Algo sobre la temporada, el vino o la comida. La IA escribe automáticamente un tema breve cada día.

El objetivo es ofrecerle a la persona un tema de conversación antes de su visita. Tamuro es un local con mucha conversación entre la clientela. Un tema leído en el correo se convierte en lo primero que le dice a quien tiene al lado en la barra. Por eso no dejé que el correo de confirmación terminara en "Hemos recibido su reserva", sino que hice que transmitiera de antemano un poco del ambiente del local.

Una vez cambié la IA que escribe los temas. La cambié por una que produce temas más naturales y más cercanos al tono del local. Sin embargo, este no es un mecanismo para aumentar la clientela. Es un mecanismo para mejorar un poco la experiencia de quienes vienen. Volveré a escribir sobre esa distinción en la segunda mitad de este capítulo.

Entre estos mecanismos, los que fueron mostrando resultados poco a poco son los planes "Mucho gusto" y "Bienvenido de nuevo". Son planes fáciles de contratar y de precio razonable que solo pueden elegir quienes vienen por primera vez y quienes llevan más de un año sin venir. Les dan un motivo para venir tanto a la clientela nueva como a la que se está alejando.

Por otro lado, también hubo un problema. Mucha gente reserva como invitada sin registrarse como miembro. Si exigiera el registro como miembro en cada reserva, podrían desistir de reservar por completo. Así que, una vez terminada la reserva, muestro un aviso: "¿Desea vincular esta reserva a una cuenta de miembro?", y construí una forma de hacerse miembro después. No pone ningún obstáculo a la reserva y enlaza la relación más tarde.

【Figura 1-8】Planes que solo pueden elegir quienes vienen por primera vez y quienes llevan más de un año sin venir *(La pantalla está en japonés.)*

【Figura 1-9】La tarjeta de sellos en la página personal (datos sintéticos) *(La pantalla está en japonés.)*

【Figura 1-5】Correo de confirmación de la reserva. Incluye un "Tema de hoy" (datos sintéticos) *(La pantalla está en japonés.)*

### 1-5 En números: cerca del 88% de las reservas son del mismo día

Mientras seguía añadiendo mecanismos, me di cuenta de algo. No podía saber cuáles de ellos funcionaban.

Así que conté los datos de las reservas. De las 244 reservas de los últimos 90 días, 215 fueron reservas del mismo día. Es decir, el 88,1%. El promedio es de 2,71 reservas por día.

Tamuro no era un lugar para el que se reserva, sino un lugar al que se viene por impulso. Solo quedó claro cuando lo puse en números.

Estas cifras dejaron ver dos cosas.

Una es cómo armar el formulario de reserva. Si la mayoría de las reservas son para el mismo día, resulta más cómodo que, al abrirse la pantalla de reserva, ya esté seleccionado el horario disponible más cercano de hoy. En cambio, algunas personas que quieren reservar para una fecha posterior lo enviarán por descuido con la fecha de hoy. Por eso hice que hoy destaque en el calendario y, en la pantalla de confirmación, muestro la fecha y la hora en grande con "Hoy". Conservé la comodidad de elegir el mismo día y facilité que se noten los errores.

La otra es el sentido del descuento por reserva anticipada. Que haya muchas reservas del mismo día significa que no podemos prever las ventas futuras. Basta el mal tiempo para que baje el flujo de gente. Para aumentar aunque sea un poco las reservas con anticipación, hace falta que más personas usen el descuento por reserva anticipada. Esta inquietud llevó más adelante a la historia de construir una IA que publica en nombre de quien dirige el local.

Para mirar números, hace falta un sistema que cuente. El sitio de reservas no tenía ningún análisis de accesos. No podía saber cuántas personas llegaban a la página de reservas, cuántas abandonaban a mitad de camino y cuántas terminaban. Así que añadí un sistema que cuenta tres etapas: llegó a la página, decidió los detalles, terminó la reserva. No registra quién vino, solo la etapa y la hora.

Más adelante, construí también un sistema que envía por correo un informe semanal que resume las cifras de reservas. Cuento cómo surgió en 1-7.

【Figura 1-3a】Hoy destaca en el calendario *(La pantalla está en japonés.)*

【Figura 1-3b】En la pantalla de confirmación, la fecha y la hora aparecen en grande como "Hoy" *(La pantalla está en japonés.)*

### 1-6 Demasiados planes entre los que elegir

Una vez instalado el sistema de descuentos, quise a continuación aumentar los horarios y los planes que se venden.

La franja de las 6 p. m. no se llenaba, así que creé una hora feliz hasta las 7 p. m. Para quienes llegan después de haber comido, creé un plan solo de bebidas, sin comida. El menú degustación y la clase de cocina, que antes se hacían una vez al mes, los convertí en eventos a pedido que se abren cuando alguien se inscribe, y los recibo a través del sitio de reservas. Para vender el tiempo previo a la apertura los fines de semana, desde las 3:30 p. m., creé un plan de fiesta para grupos de seis o más.

Cada uno tiene su razón. En el plan de fiesta, por ejemplo: si lo hacía parecer una ganga por el precio, solo atraería a clientela que había estado eligiendo el plan estándar, y las ventas caerían. Por eso puse la diferenciación no en el precio, sino en las horas previas a la apertura, que nunca habían traído ventas. El descuento de la hora feliz no deja ganancia si se combina con otros descuentos, así que decidí que no se puede combinar.

Y así los planes se multiplicaron. Estándar, Premium, Mucho gusto, Bienvenido de nuevo, Hora feliz, Solo bebidas, Menú degustación, Clase de cocina, Fiesta. Cada uno tiene condiciones sobre el número de personas, algunos aceptan descuentos y otros no, y hay restricciones de horario.

Un día abrí el formulario de reserva y me di cuenta: con esto, la clientela no puede elegir.

Yo, que lo construí, entiendo cada diferencia. Pero ¿podría alguien que abre el sitio de reservas por primera vez comparar nueve planes y sus condiciones de descuento y elegir el que le conviene? Si no puede, abandona a mitad de la reserva. Los planes que me esforcé por añadir podrían terminar reduciendo las reservas.

Podría haber simplificado los planes. Pero cada plan tiene una hora que quiero vender y una clientela a la que quiero recibir. No quise recortar ninguno.

Así que pensé en un sistema en el que la clientela consulta con la IA y decide un plan. Usted le dice el número de personas, la fecha y la hora a las que le gustaría venir y cómo quiere disfrutar su visita, y la IA le da el plan y el precio adecuados y lo lleva directo a reservar. El local carga con la complejidad de los planes. A la clientela solo le queda una conversación.

Este sistema es el "T-AI-MURO" del que escribo en 1-8. Antes de eso, hay una cosa más que noté en esta etapa.

【Figura 1-2】Selección de plan en el formulario de reserva. Hay esta cantidad de pestañas alineadas *(La pantalla está en japonés.)*

### 1-7 "¿Esto realmente atrae clientela?"

El día en que añadí el plan de fiesta, pasé todo el día haciendo una mejora tras otra en el sitio de reservas. Ajusté el encabezado, igualé el diseño de los correos y cambié la IA que crea los temas de conversación para la clientela dentro del local.

Por la tarde, de pronto me vino una pregunta.

"¿Esto realmente ayuda a atraer más clientela?"

Cuando se lo pregunté a la IA, ordenó con honestidad las mejoras de ese día.

| Categoría | Mejoras de ese día |
| --- | --- |
| Cosas que pueden crear reservas nuevas | Plan de fiesta, la franja de las 3:30 p. m. en fines de semana y festivos |
| Cosas que aumentan la tasa de reservas completadas entre quienes visitan la página | Ajuste del encabezado, alineación de las pestañas |
| Cosas que fomentan las visitas de regreso | Unificación del diseño de los correos |
| Cosas que no ayudan a atraer clientela | Cambio de la IA que crea los temas de conversación, el enlace a la siguiente parada, el aviso de Agenda |

De las mejoras de ese día, solo el plan de fiesta y la franja de las 3:30 p. m. llevaban directamente a atraer clientela. El resto eran mejoras para no perder a quienes ya habían llegado a la página de reservas. También importan, pero no aumentan la clientela.

Había un problema mayor. Para ninguna de las mejoras tenía una forma de medir si había funcionado. No había ninguna cifra que conectara "lo mejoré" con "aumentó la clientela".

Mi respuesta fue una sola frase: "Construyamos una".

Así que me puse a crear un informe semanal de captación de clientela. El número de reservas, el número de comensales, el monto total, las cancelaciones. Desgloses por día de la semana y por franja horaria. La proporción de primeras visitas frente a las de quienes regresan. Los conteos de las franjas de fiesta y de las 3:30 p. m. De dónde vinieron las reservas (el formulario de reserva, la ventana de chat, reservas desde la IA, registros manuales del local). La cantidad de clics en los correos y el número de reservas dentro de los siete días posteriores a esos clics.

Donde hay números, aparece también el tiempo. Ese mismo día había encontrado otro hueco. Había fijado la clase de cocina y la franja de las 3:30 p. m. del plan de fiesta como "fines de semana", pero cuando me pregunté "¿qué pasa en los festivos?" y lo investigué, el sistema de reservas no tenía ningún concepto de días festivos. En un lunes festivo el local abre, y sin embargo la franja de las 3:30 p. m. no aparecía. Le di una lista de festivos y lo corregí para que los tratara como fines de semana. Era un hueco que nadie notaría hasta que lo notara la persona que lo construyó.

Antes de construir el informe, primero tapé los huecos relacionados con el tiempo.

Incluso la clientela habitual que venía desde antes de que yo empezara a usar el sistema de reservas aparece como "primera visita" en los registros. Por eso, en el informe escribo "primera visita registrada" y siempre añado la fecha en que empezaron los registros. Para juzgar si una mejora funcionó, hace falta la imagen de antes. Para el primer informe, hice el conteo retrospectivo de las últimas ocho semanas y lo usé como punto de partida. En una semana en que el local cerró temporalmente, por viaje u otras razones, las reservas bajan de forma natural. Por eso también indico el número de días de apertura, para que se pueda comparar por día de apertura.

La sección "Cambios destacados" no se la pedí a la IA; la hice seguir cálculos fijos y frases fijas. Es para mantener en cero el costo semanal. Los nombres y los datos de contacto de la clientela no aparecen en el informe; solo se muestran conteos y proporciones.

Una vez que construí una forma de medir, cambió la manera misma en que construyo las mejoras. Empecé a decidir desde el principio, a la vez, la mejora y el método para medir su efecto. La medición no es algo en lo que se piensa después de una mejora; va en el mismo documento de instrucciones que la mejora. Eso fue lo que aprendí ese día.

【Figura 1-6】El informe semanal de captación de clientela que llega cada semana (datos sintéticos) *(La pantalla está en japonés.)*

### 1-8 Una ventana para conversar con el local: "T-AI-MURO"

Como escribí en 1-6, los planes se habían multiplicado y en el formulario de reserva se había vuelto difícil elegir un plan para quien viene por primera vez. Y la clientela nueva quiere saber más que los planes y las fechas. ¿Qué ambiente tiene el lugar? ¿Me sentiré fuera de lugar yendo solo? ¿Cómo es quien dirige el local? ¿Se puede ir con niños? Si uno alinea botones de reserva sin responder preguntas como estas, no puede darle a quien duda el empujón que necesita.

Así que decidí poner en el sitio de reservas una "ventana para conversar con el local". Cuando alguien escribe una pregunta, la IA responde en nombre del local. Si durante la conversación se definen el número de personas, la fecha y la hora, la persona puede ir directo a la pantalla de confirmación de la reserva. Se llama "T-AI-MURO" y, en la conversación, se presenta como "Tamuro". T-AI-MURO habla como el propio local y se refiere a quien dirige el local en tercera persona.

La clientela casi no escribe. Solo toca las opciones que ofrece T-AI-MURO, y la conversación avanza. Eso significa que las opciones que ofrece a continuación deciden la calidad de la conversación. Siempre mezclo tres clases de movimientos en las opciones: movimientos hacia una reserva (número de personas, precio, horarios disponibles, fecha y hora), movimientos hacia conocer el local (el ambiente, quien dirige, quién es la clientela, si se puede conversar con la persona de al lado) y movimientos que surgen del curso de la conversación. Llevar a la gente a una reserva no es la única meta. Dejar que conozcan el ambiente del local y a quien lo dirige también es el corazón de esta ventana.

Solo los precios, decidí, no los calcularía la IA. No hay garantía de que la IA calcule correctamente, cada vez, cómo se acumulan los descuentos o cómo se aplican los escalones por número de personas. El programa produce los precios y los horarios disponibles con cálculos fijos, y la IA se atiene a la tarea de ponerlos en palabras.

#### El primer conocimiento vino de mis propias publicaciones pasadas

Para que T-AI-MURO responda preguntas sobre el local, necesita conocimiento del local. Como material, exporté todas las publicaciones que había escrito hasta entonces en Instagram y en X (antes Twitter) y las usé. A partir de ellas armé las preguntas que probablemente haría la clientela y las respuestas.

Al probarlo de verdad, resultó que las publicaciones de X servían más como material que las de Instagram. Instagram es sobre todo fotos, con pocas palabras. En X había dejado registros escritos, con mis propias palabras, sobre la comida, el local y lo que pensaba.

#### Solo 9 de 36 aprobaron

Antes de poner T-AI-MURO en producción, probé con qué corrección podía responder. Las pruebas también las hice con IA. A una IA que hacía de cliente le di un personaje y un propósito, y la hice conversar con T-AI-MURO. Preparé 36 escenarios: "solo esta noche", "4 personas dentro de dos semanas", "con un niño", "alergias", "reserva privada", "aviso de retraso", "el origen del nombre del local", "cómo es quien dirige el local", y así sucesivamente.

El resultado de la primera ronda: 9 aprobados de 36.

La respuesta más frecuente era "Lo siento, no pude responder bien a eso". Esta respuesta aparecía incluso ante preguntas sobre el ambiente del local y sobre quien lo dirige. Cada vez que aparecían palabras como "reserva", "hoy", "reserva privada" o "responsable", salía una lista de horarios disponibles sin importar de qué se tratara realmente la pregunta. En algunas conversaciones, un mensaje sobre un retraso se tomaba como una reserva nueva. A una persona vegetariana le dio como ejemplos platos salteados con copos de bonito y sopa de miso. Incluso dio información en inglés sobre una compra grupal que ya habíamos detenido.

#### Respondí 11 preguntas con una línea cada una

Parte de la causa estaba en cómo se había construido el programa. Esa historia la dejo para el capítulo 2. La otra causa era simple: faltaban datos del local. Una IA no puede responder lo que no sabe.

Así que reuní las preguntas que la IA no podía responder y decidí responderlas yo mismo, una línea cada una.

Se puede entrar sin reserva. Con menores que aún no van a la escuela primaria es difícil. Cancelaciones y cambios hasta el día anterior, por correo, teléfono o mensaje en redes sociales. Para avisar de un retraso, por favor llame por teléfono. Hay una zona de fumadores fuera del local. Se permite traer bebidas propias con un cargo por descorche. Se puede reservar en privado según el rango de precios y el horario, con un máximo de 19 personas. Las restricciones alimentarias y los aniversarios los atendemos en lo que podamos, así que consúltenos antes. Quien dirige el local está en el local casi todos los días de apertura. Se planea un festival de yukata más o menos una vez al año.

Eso es todo. Con solo responder 11 preguntas con una línea cada una, en la segunda prueba aprobaron 24 de 36.

| Pregunta | Primera respuesta | Segunda respuesta |
| --- | --- | --- |
| ¿Se puede ir con niños? | Lo siento, no pude responder bien a eso | Se puede atender desde la edad de la escuela primaria si nos consulta. Con menores que aún no van a la escuela primaria es difícil |
| ¿Se puede entrar sin reserva? | (lista de horarios disponibles) | Se puede entrar sin reserva |
| ¿Está hoy el responsable de la barra? | (lista de horarios disponibles) | Quien dirige el local está en el local casi todos los días de apertura. Hoy el local abre, así que tiene previsto estar |
| ¿Es un lugar tranquilo? ¿Todos son habituales? | Lo siento, no pude responder bien a eso | Es un lugar para relajarse. La conversación entre la clientela surge con facilidad y no es un lugar bullicioso |

Aquí empezó a asomar un patrón. La IA crea las preguntas que esperamos, T-AI-MURO las responde y yo corrijo los errores. Luego, solo las preguntas que no se pueden responder porque faltan datos del local se pasan a quien dirige el local. El esfuerzo de esa persona es solo una línea por cada pregunta sin respuesta. Todo lo demás lo maneja la IA.

#### La escena donde fracasó el "presupuesto de ¥5.000 (unos US$ 33)"

También le puse un veredicto de IA a las pruebas con IA. Otra IA lee el registro de la conversación y decide si aprueba o no.

Entre ellos había un escenario con una persona cuyo "presupuesto es de ¥5.000 (unos US$ 33)". El veredicto de la IA fue aprobado. T-AI-MURO había presentado con cortesía planes dentro del presupuesto.

Pero al leerlo, era un fracaso. No había preguntado el número de personas. Tamuro tiene un descuento por grupo. Según el tamaño del grupo, cambian los planes que se pueden elegir con el mismo presupuesto.

En ese momento, volví a formular el propósito.

"Apunta al grupo más grande posible, para que el monto total sea lo más alto posible. Confirma el número de personas. La meta final es que la clientela venga. Cuantas más, mejor. Para aumentar las ventas".

Con esa sola declaración, cambió todo el diseño de la conversación. Confirmar siempre el número de personas antes de responder sobre precios, y responder con el monto total. Justo antes de un escalón del descuento por grupo, añadir "con una persona más obtienen tanto por ciento de descuento". Cuando se da un presupuesto, mostrar primero el mejor plan dentro del presupuesto. Sin embargo, la clientela que viene sola representa la mitad del total, así que, para una persona sola, no sugerir aumentar el tamaño del grupo.

Cuando uno hace que la IA ejecute las pruebas de IA, estas corren rápido. Pero quien decide el criterio de aprobación es una persona. Si el propósito se puede enunciar en una frase, de eso dependía la calidad de las conversaciones de la IA.

#### Los deseos de la clientela tienen prioridad sobre las recomendaciones del local

Hubo una escena más donde tracé una línea importante.

Durante las pruebas, encontré un problema: todas las reservas se estaban derivando al plan más barato. Cuando lo corregí, esta vez casi todas pasaron a ser el plan Estándar, y el monto total promedio se disparó a casi el doble. Casi me alegré, pero, al mirar de cerca, la IA que hacía de cliente simplemente había estado pulsando la primera opción cada vez. Incluso a quienes decían "lo más barato está bien" se les recomendaba el Estándar.

Aquí fijé un principio. Lo que la clientela declara con claridad como deseo (la opción más barata, un presupuesto, el nombre de un plan) siempre tiene prioridad sobre la recomendación del local. La recomendación del local es solo para cuando la clientela no ha dicho nada.

El objetivo del local de aumentar las ventas y la confianza de la clientela pueden chocar según la forma de recomendar. Si se pierde la confianza, las visitas mismas disminuyen. Quien podía trazar esta línea era quien dirige el local, no la IA.

Más tarde, cuando reentrené a T-AI-MURO con una gran cantidad de preguntas, la causa más común de errores era "reaccionar a palabras y hacer un movimiento fijo antes de responder la pregunta". En cuanto oía palabras como "número de personas", "cuánto cuesta" o "solo", se saltaba la pregunta y pasaba al flujo de reserva o a las recomendaciones. En términos de servicio, es un empleado que empuja una venta sin escuchar a la clientela. Responder primero la pregunta de la clientela. Este fundamento de la hospitalidad fue el mayor desafío incluso para la IA.

En la noche del 6 de octubre de 2026, T-AI-MURO apareció en la parte superior del sitio de reservas como la entrada oficial, ya en producción. Como algunas personas no quieren reservar por conversación, he mantenido al lado el formulario de reserva anterior.

> Pruébelo: abra el sitio de reservas de Tamuro (https://tamuroreservation.vercel.app/?src=b2-es-{{FMT}}) y pregúntele a T-AI-MURO "solo esta noche". La conversación lo lleva hasta la disponibilidad y los precios de hoy.

【Figura 1-4】La pantalla de conversación de T-AI-MURO. La conversación avanza con solo tocar las opciones *(La pantalla está en japonés.)*

【Figura 1-10】Las preguntas que no pudo responder se acumulan en la pantalla de administración (datos sintéticos) *(La pantalla está en japonés.)*

### 1-9 Y luego, desde la IA de la clientela

Al construir T-AI-MURO, el sitio de reservas de Tamuro ganó la capacidad de "responder en conversación preguntas sobre el local, mostrar precios y horarios disponibles, y guiar a las personas hasta una reserva".

Lo siguiente que pensé fue hacer posible lo mismo desde la propia IA de la clientela.

T-AI-MURO solo puede conversar con quienes llegan al sitio de reservas de Tamuro. Pero mucha gente consulta primero a la IA que usa todos los días. Si esa IA no conoce Tamuro, Tamuro ni siquiera entra en la lista de candidatos. En vez de esperar a que la clientela llegue al sitio de Tamuro, abrir la ventana de Tamuro del lado de la IA de la clientela. Eso es el servidor MCP.

Para ser sincero, al principio dudé en construirlo. En este momento, no mucha gente reserva restaurantes desde su propia IA. Al juzgar que no podía esperar un aumento directo de reservas, en su momento le bajé la prioridad y lo dejé en pausa.

Decidí construirlo de todos modos porque pensé que era cuestión de tiempo que cambiara la entrada. Como escribí al principio, en agosto de 2026 se hizo posible reservar desde ChatGPT a través de un gran servicio de reservas. Tarde o temprano, hacer que una IA le encuentre un restaurante será lo normal. Cuando eso ocurra, los locales pequeños que no figuran en los grandes servicios quedarán fuera del radar de la IA. Así que hay que abrir la ventana antes de que cambie la entrada.

Lo que decidí para la primera versión fue muy acotado. Solo tenía que hacer lo mismo que la ventana de conversación del sitio de reservas (T-AI-MURO). Lo único que puede hacer es leer la información del local, los horarios disponibles y los precios, y entregar la URL de una página de reserva con las condiciones ya completadas. La confirmación de la reserva la hace la propia persona en la página de Tamuro. La IA de la clientela no confirma una reserva por su cuenta. El empujón final lo da una persona.

Volvamos a la escena de apertura.

Un viernes por la tarde, alguien le pregunta a su propia IA: "¿Hay algún lugar en Higashi-Nakano donde pueda tomar algo a solas esta noche?". La IA consulta la ventana de Tamuro. El sistema de reservas de Tamuro devuelve los horarios disponibles de esta noche, además del plan y el precio adecuados para una persona sola. La IA se lo comunica a la persona y le ofrece una página de reserva de Tamuro con la fecha, la hora y el número de personas ya completados.

Todo lo que he escrito en este capítulo sostiene esta serie de pasos. El sistema de descuentos construido junto con la subida de precios. El sistema para fidelizar a la clientela habitual. Los datos que mostraron que la mayoría de las reservas se hacen el mismo día. El conocimiento del local que creció al responder 11 preguntas con una línea cada una. El principio de poner los deseos de la clientela por delante de las recomendaciones del local.

Un local que se reserva a través de la IA no se construyó de la noche a la mañana. Se apoya en la acumulación de pequeños sistemas añadidos uno por uno, probados, descartados y corregidos.

> Pruébelo: registre el servidor MCP de Tamuro (https://tamuroreservation.vercel.app/api/mcp) en su propia IA y pregunte: "¿Hay sitio en Tamuro esta noche?". La forma de registrarlo está escrita en el Epílogo.

### 1-10 Lo que construí y lo que funcionó

En este capítulo he hablado de construir muchos sistemas. Pero "pude construirlo" y "el negocio cambió" son cosas distintas. Al final del capítulo, separaré las dos.

Lo que se pudo confirmar con números. Que el 88,1% de las reservas son para el mismo día. Que la tasa de aprobación de la ventana de conversación subió de 9 a 24 pruebas superadas solo con añadir 11 datos del local. Que la tasa de aprobación de las respuestas sobre precios y planes subió del 29,4% al 42,7% tras las correcciones. Son hechos registrados.

Lo que parece que funciona, pero cuya causalidad no puedo demostrar. Que más gente viene en grupo usando el descuento por grupo. Que se están eligiendo los planes para quienes vienen por primera vez o regresan. Que el tema del correo de confirmación se ha vuelto parte de la conversación en la barra. Lo percibo en el día a día del local, pero no puedo decir "no habrían venido sin ese sistema".

Lo que se ha construido, pero cuyo efecto todavía no conozco. Cuántas reservas anticipadas más traerá el descuento por reserva anticipada. Cuántas reservas llegarán realmente desde MCP. Acabo de empezar a medir con el informe semanal, y las cifras llegarán más adelante.

Mire por separado el asombro de "pude construir tanto con IA" y el resultado de "cómo cambió eso el negocio". Sin esta distinción, el mero hecho de construir se convierte en la meta. Yo estuve a punto de caer en eso una vez (como escribí en 1-7).

La historia de lo que hay detrás de este sistema de reservas, la tecnología, continúa en el capítulo 2. Si no le interesa la tecnología, salte al capítulo 3. Allí cuento cómo las pequeñas herramientas nacidas alrededor de este sistema de reservas se están compartiendo también con otros locales.

## Capítulo 2: Tecnología - El sistema de reservas por dentro

Puntos clave de este capítulo

- La calidad de las conversaciones de la IA dependió menos de la inteligencia de la IA que de "los datos del local que le entregué" y de "si un programa sustituye por su cuenta las respuestas de la IA"
- El sistema de reservas que construí por intuición todavía tenía un hueco que permitía leer desde fuera los datos personales de la clientela, y cero pruebas automáticas. Hice que una IA lo auditara para encontrarlos e hice que una IA los corrigiera
- De esa reflexión cambié mi manera de construir: definir los requisitos en detalle antes de construir y entregarle a la IA la especificación misma para que la implemente

(Este capítulo tiene muchos términos técnicos. Si no le interesa la tecnología, puede saltar al capítulo 3 sin perder el hilo de la historia.)

### 2-1 Cómo funciona el servidor MCP

MCP (Model Context Protocol) es un conjunto común de convenciones para que la IA use herramientas y datos externos. Propuesto por Anthropic, hoy lo admiten muchas IA, entre ellas ChatGPT y Claude.

Para ponerlo en una analogía, MCP es un estándar de tomacorrientes, para la IA. Como la forma del tomacorriente está fijada, los aparatos de cualquier fabricante funcionan al enchufarlos. De la misma manera, si uno construye un punto de acceso que se ajuste al formato de MCP, cualquier IA puede usar ese punto de acceso.

Un servidor MCP le dice a la IA "qué puede hacer a través de este punto de acceso". El servidor MCP de Tamuro, por ejemplo, ofrece herramientas como las siguientes.

- Leer la información del local (horario de atención, número de asientos, normas de la casa, ambiente)
- Leer los planes y los precios (el resultado de calcular los descuentos según el número de personas y la fecha)
- Leer los horarios disponibles (las horas en que se puede reservar en un día especificado)
- Crear la URL de una página de reserva con las condiciones ya completadas

Cuando alguien le pregunta a su propia IA: "¿Hay sitio en Tamuro esta noche?", la IA se conecta al servidor MCP de Tamuro, elige "leer horarios disponibles" entre las herramientas disponibles y la llama. El servidor de Tamuro devuelve el resultado, y la IA lo pone en palabras para la persona.

Lo importante es que la IA no confirme reservas por su cuenta. En la primera versión, dejé deliberadamente fuera de las herramientas la confirmación de la reserva. Todo lo que la IA puede hacer es leer y guiar a las personas a una página de reserva con las condiciones ya completadas. El botón de confirmar lo pulsa la propia persona en la página de Tamuro. El peligro de que la IA cree grandes cantidades de reservas equivocadas o de broma se evita por diseño desde el principio.

El cálculo de precios usa el mismo mecanismo de cálculo que el sitio de reservas. Los precios que se muestran en el formulario de reserva, en la ventana de conversación y a través de MCP salen todos del mismo programa. Este es el otro sentido de la tarea sobre la que escribiré más adelante, "reunir el cálculo de descuentos en un solo lugar".

【Figura 2-1】De la IA de la clientela a la página de reservas de Tamuro. La persona pulsa el botón de confirmar

### 2-2 Cómo funciona la ventana de conversación "T-AI-MURO"

#### Los precios los pone el programa, las palabras las pone la IA

T-AI-MURO divide los papeles en dos. El programa produce los precios y los horarios disponibles con cálculos fijos, y la IA los pone en palabras para la clientela.

La IA es buena para producir texto, pero no hay garantía de que calcule correctamente cada vez. Cómo se acumulan los descuentos, los escalones por número de personas, el número de días del descuento por reserva anticipada, si se puede combinar con la hora feliz. Si se dejan todas estas reglas a la IA, seguramente se equivocará en alguna parte. Y un error en el precio daña más que nada la confianza de la clientela.

Así que las partes que no deben fallar van al programa, y las partes que se transmiten con calidez y naturalidad van a la IA. Esta división es el primer principio al construir la ventana de conversación.

#### Para un local pequeño, no hace falta RAG

Para que la IA responda sobre el local, hay que entregarle el conocimiento del local. Un método de uso común es RAG (generación aumentada por recuperación). Se corta el conocimiento en trozos pequeños y se almacenan y, cada vez que llega una pregunta, se buscan solo las partes que parecen relevantes y se le entregan a la IA. Cuando el conocimiento es vasto, este método es indispensable.

Pero el conocimiento de Tamuro no es tan grande. La historia del local, la comida, las normas, el ambiente, el pensamiento de quien dirige el local. Todo junto cabe con holgura en lo que la IA puede leer de una vez.

Así que en Tamuro elegí hacer que la IA lea cada vez el texto completo del conocimiento del local. No hace falta construir el mecanismo de búsqueda que exige RAG, y no se pierde nada en la búsqueda. Al principio pensaba reutilizar un mecanismo de RAG, pero a mitad de camino cambié al enfoque del texto completo.

Hacer que lo lea completo cada vez cuesta más en tarifas de IA. Por eso uso un mecanismo que reutiliza el mismo texto para reducir los costos de entrada (caché de prompts: en lugar de hacer que la IA vuelva a leer cada vez el mismo preámbulo, recuerda lo que ya ha leído). Basta con incorporar RAG cuando el conocimiento crezca mucho.

#### Un programa que sustituye respuestas por su cuenta

En el capítulo 1 escribí que en la primera prueba aprobaron solo 9 de 36. Parte de la causa estaba en cómo se había construido el programa.

Al investigar, encontré un mecanismo que había quedado en su lugar en el que el programa juzgaba por palabras clave la respuesta que había dado la IA y la cambiaba por una frase fija. Cuando aparecían palabras como "reserva" u "hoy", descartaba la respuesta de la IA y ponía en su lugar una lista de horarios disponibles. Incluso cuando la IA respondía correctamente, la respuesta nunca llegaba a la clientela.

Además, descubrí que el cuerpo principal del conocimiento del local (33 secciones) no estaba incluido en las instrucciones a la IA. La IA había estado respondiendo sin conocer el local.

La calidad de las conversaciones de la IA dependió menos de la inteligencia de la propia IA que de los datos del local entregados y de que un programa sustituyera por su cuenta las respuestas de la IA.

#### Completar las preguntas y respuestas esperadas contando

Aumenté los escenarios de prueba de los 36 iniciales a 110, y luego a 355. Pero si uno añade escenarios según se le van ocurriendo, no hay forma de saber si falta algo. A la pregunta "¿Es exhaustivo?", la respuesta honesta era "No, no lo es".

Así que, en lugar de ampliar la cobertura con imaginación, hice que fuera cuestión de contar con una máquina los lugares por los que todavía no se había pasado, y completarlos. Para cuatro cosas: las 33 secciones del conocimiento del local, las transiciones entre opciones, los escalones de los descuentos y las combinaciones de franjas horarias y días de la semana. Cuento cuántas veces se pasó por cada una en las pruebas y añado automáticamente escenarios donde la cuenta es cero.

También usé un método de cruzar seis ejes (número de personas, propósito, tipo de consumición, fecha y hora, redacción, menú) y crear escenarios de modo que cada combinación de dos factores se recorra al menos una vez.

También encontré un hueco en torno al tiempo. "Hoy" y "a partir de ahora" los determina la hora real en que se ejecuta la prueba, así que los resultados de ejecutarla al mediodía y de noche difieren. Por eso fijé el reloj durante las pruebas e hice que corrieran en cinco momentos: antes de abrir, durante el horario de atención, justo antes de cerrar, en un día de descanso habitual y en un festivo.

Las respuestas de la IA varían ligeramente cada vez, incluso ante la misma pregunta. Para los escenarios directamente ligados a las ventas, fijé la condición de que deben aprobar las tres veces al ejecutarse tres veces.

#### Cuando sale una cifra mala, sospeche primero de la prueba

En la prueba que ejecutó 355 escenarios en 5 momentos, de 1.775 conversaciones, aprobó el 28,5%.

En lugar de ponerme a corregir de inmediato, primero me pregunté: "¿Esta cifra es de verdad una debilidad de T-AI-MURO, o la prueba está equivocada?" Si uno corrige mientras la prueba está equivocada, termina "corrigiendo" incluso las respuestas correctas.

| Causa del error | Cantidad |
| --- | --- |
| Una frase fija secuestra la pregunta | 276 |
| No responde la pregunta, pasa al flujo de reserva o a las recomendaciones | 266 |
| Fallo del entorno de pruebas (T-AI-MURO no pudo producir una respuesta por el tope de costos) | 211 |
| Errores en fechas, días de la semana, festivos, días de descanso | 142 |
| Inventar o afirmar datos que el local no tiene, prometer transmitir mensajes | 119 |

Los dos primeros compartían la misma raíz: "reaccionar a palabras y hacer un movimiento fijo antes de responder la pregunta de la clientela". Los 211 del tercer lugar no eran errores de T-AI-MURO. Se alcanzó el tope de costos a mitad de la prueba, y T-AI-MURO simplemente no pudo producir respuestas. Si se excluyen estos, la tasa de aprobación pasa a ser del 32,4%.

La IA que juzga también puede equivocarse. Cuando saqué 20 casos y los revisé, 2 eran errores del lado de la prueba. En uno de ellos, quien juzgaba no sabía que "este sitio de reservas tiene registro de miembros". La IA que juzga tampoco sabe nada más allá de los materiales que se le dieron. La precisión de la prueba la decide lo completas que sean las reglas del local entregadas a quien juzga.

En la nueva prueba tras las correcciones, la tasa de aprobación de las respuestas sobre precios y planes subió del 29,4% al 42,7%. Todavía no he ejecutado la prueba final que vuelve a pasar todos los casos. Para mantener bajos los costos, he decidido que la prueba de todos los casos se ejecute una sola vez, antes de poner un cambio importante en producción. La tasa de aprobación se sigue elevando incluso mientras escribo este libro.

#### La prueba detuvo la producción

Las pruebas con IA cuestan dinero. La primera prueba de 36 escenarios costó unos ¥426 (unos US$ 2,8). La mayor parte se fue en el "esfuerzo de razonamiento" de la IA que hacía de cliente, y cuando lo desactivé, 3 escenarios costaron unos ¥6 (unos US$ 0,04).

Pero entonces, un día, a mitad de una prueba, se agotó el saldo de uso de la IA y todo se detuvo. En un solo día había usado unos 35 millones de tokens (la unidad de texto que una IA lee y escribe). La causa fue ejecutar una y otra vez la prueba de 221 escenarios y ejecutar cuatro veces cada uno los escenarios ligados directamente a las ventas.

Lo que daba miedo era que la prueba y la producción usaban la misma billetera. Cuando se agota el saldo, se detiene incluso la ventana de conversación de producción. Otro día, esta vez alcancé un tope mensual que yo mismo había fijado, y la ventana de conversación de producción y la IA que crea los temas de conversación para la clientela dentro del local se detuvieron al mismo tiempo.

El peligro real de un presupuesto de pruebas no era la factura, sino que la producción usaba la misma billetera.

A partir de ahí cambiaron las reglas. Hacer primero las comprobaciones que no cuestan nada (pruebas del programa y revisiones automáticas de pantalla). Limitar las pruebas que llaman a la IA a las relacionadas con lo corregido. Ejecutar la prueba de todos los casos una sola vez, antes de pasar a producción. Escribir el costo estimado y un tope en las instrucciones, y detenerse si parece probable alcanzarlo. Para conservar fondos para la producción, detener las pruebas cuando el uso de toda la organización se acerque al tope.

También hubo una lección sobre cómo se inflan los costos. Una vez, el costo de la IA que juzga llegó a 2,6 veces la estimación. La causa fue que el largo preámbulo entregado a quien juzga cada vez (el conocimiento y las reglas del local) no se reutilizaba, así que se cobraba la tarifa de escritura en caché completa cada vez. Cuando lo corregí para escribir el preámbulo una vez y reutilizarlo, el costo por conversación bajó a cerca de un tercio. El costo de la IA no se infla por cuántas veces se la llama, sino por cuántas veces se escribe desde cero en la caché el mismo preámbulo.

La misma prueba completa de 221 escenarios bajó de unos ¥1.040 (unos US$ 6,9) a unos ¥400 (unos US$ 2,7) mediante mejoras repetidas. Reemplacé a la IA que hacía de cliente por un guion fijo, y dividí la información entregada a la IA en un "núcleo enviado cada vez" y "secciones que se leen solo cuando hacen falta".

Por las restricciones de presupuesto, el diseño cambió hacia aumentar las partes que se pueden comprobar sin costo, es decir, las partes decididas por el programa. Como resultado, la precisión también subió. El dinero cambia el diseño.

【Figura 2-2】Resultados de las pruebas con IA. La tasa de aprobación y un desglose de las causas de los errores

### 2-3 Hacer que una IA audite lo que construí

#### Los nombres de la clientela podían leerse desde fuera

En agosto de 2026, mientras revisaba cómo funcionaba el sistema de reservas, hice un descubrimiento que me dio escalofríos.

Los datos de reservas de la clientela podían ser leídos por cualquiera desde fuera. Nombres, números de teléfono, direcciones de correo, el campo de peticiones. Todo lo ingresado en una reserva se podía extraer completo, sin autenticación.

Hay algo que debo decir con honestidad. Es cierto que los datos podían leerse desde fuera. En ese momento, el sitio de reservas tenía muy poco tráfico, y creo que es poco probable que alguien los haya leído de verdad. Pero no tengo ningún registro que pueda demostrar que no se leyeron. "Podrían haberse obtenido" y "se obtuvieron de verdad" son dos cosas distintas, pero solo lo primero ya era un fallo grave para un local.

Al rastrear la causa, se reducía a cómo estaba construido el formulario de reserva. Para calcular los asientos disponibles, el formulario cargaba 35 días de datos de reservas directamente desde la pantalla. Si los datos se pueden leer directamente desde la pantalla, cualquiera que sepa cómo se construyen pantallas así puede leer los mismos datos. Era el resultado de una primera base construida por intuición, una que alcanzó la meta de "mostrar los asientos disponibles" por el camino más corto.

También descubrí que la dirección de correo para avisar a quien administra el local era pública, y que cualquiera podía escribir en el lugar donde se guardaban las traducciones, lo que significaba que los datos podían vandalizarse o los costos inflarse.

El orden de la corrección importó. Si prohibía de golpe la lectura, el formulario de reserva ya no podría mostrar los asientos disponibles y dejaría de funcionar. Así que primero moví el cálculo de asientos disponibles a un punto de acceso del lado del servidor. Luego cambié la pantalla de reserva completada para que también obtuviera del servidor solo la información que necesita. Por último, cerré la lectura desde fuera. Hice la corrección en cuatro etapas en este orden y la apliqué a producción.

Después de la corrección, comprobé de forma automática que de verdad estuviera cerrado. Preparé una prueba que intenta leer datos de reservas sin autenticación, y la ejecuto automáticamente después de cada cambio para confirmar que siempre es rechazada. No lo corregí una vez y lo di por terminado. Lo dispuse de modo que una comprobación vigile que nunca vuelva a abrirse.

#### Había datos reales de la clientela en el historial de desarrollo

Luego hice que la IA auditara todo el repositorio (el lugar de almacenamiento del programa), y apareció un problema más grave.

Durante el desarrollo, un archivo con datos de clientela real (direcciones de correo y números de teléfono de 55 reservas) se había enviado al repositorio y seguía incluido en el historial de cambios del programa. El repositorio era privado, pero como permanecía en el registro, no podía dejarlo así.

Eliminé el archivo de todo el historial de cambios, reescribí el historial y lo almacené de nuevo. Aun así, los registros antiguos de antes de la reescritura podrían seguir existiendo del lado de GitHub, que aloja el repositorio. Por eso pedí al soporte de GitHub que los eliminara, y confirmé que se hizo.

La auditoría encontró también otros problemas: el punto de acceso de traducción podía usarse sin autenticación, el inicio de sesión de administración podía ser atacado por fuerza bruta, y había una ventana de tiempo en la que, si se volvía a activar el pago, una reserva podía confirmarse aún sin pagar. Los corregí uno por uno, empezando por el más grave.

#### Ni una sola prueba automática

La auditoría reveló un hecho más. El sistema de reservas no tenía ni una sola prueba automática.

Las pruebas automáticas son un mecanismo en el que una máquina comprueba automáticamente si el programa funciona correctamente. Sin pruebas, cuando uno corrige algo, no tiene forma de comprobar si se ha roto otra cosa. Cada vez que se añade una función, en algún lugar algo se rompe en silencio. Ese era exactamente el estado de las cosas durante el período en que construía por intuición.

Así que reconstruí desde cero la base de pruebas. Introduje un sistema (CI) que ejecuta automáticamente cuatro comprobaciones después de cada cambio: verificación de tipos, verificación de estilo, pruebas y la compilación. Las decisiones importantes, como el cálculo de precios, la validación de las reservas, la vinculación de miembros y la emisión de cupones, se separaron de los programas de pantalla para que puedan verificarse por sí solas. Las reglas de lectura y escritura de la base de datos también se comprueban en un entorno de pruebas que imita una base de datos real. Las pruebas unitarias empezaron en 275 y más tarde pasaron de 500.

Hay una condición que siempre impongo a las pruebas: "rómpalo y confirme que falla". Aunque una prueba se ponga en verde (apruebe), no se sabe si esa prueba puede detectar de verdad un problema. Solo después de romper deliberadamente el programa y confirmar que la prueba se pone en rojo (falla) confío en la prueba. Eso se debe a que las pruebas escritas por IA a veces no comprueban nada en absoluto.

#### Ocho huecos en el formulario de reserva

Una vez instalada la base de pruebas, hice que la IA examinara de nuevo todo el flujo de reserva. Encontró ocho problemas que causaban daño real.

El más grave era que pulsar repetidamente el botón de enviar creaba una reserva doble. Esto ocurría de verdad en producción. Lo corregí con un mecanismo que procesa una misma acción una sola vez aunque llegue dos veces (idempotencia). Los demás problemas eran estos: no se podía confirmar una reserva si quedaba información de un elemento del menú eliminado; había una brecha en el control de aforo completo que dejaba margen para superar la capacidad; nadie se enteraba cuando fallaba el envío de un correo de confirmación; la entrada no se validaba del lado del servidor; aparecían en pantalla mensajes técnicos internos cuando ocurría un error; el texto de los campos de entrada era tan pequeño que la pantalla hacía zoom automáticamente en el iPhone; y el autocompletado de la entrada no funcionaba.

Para los fallos de correo, hice posible detectarlos en la pantalla de administración y reenviarlos. Durante esa investigación, descubrí también que el registro de auditoría que anota las confirmaciones de reserva había estado fallando todas las veces, desde mucho antes de la corrección, y no había registrado nada.

Los corregí uno por uno y los apliqué a producción.

#### No omitir la verificación del código que escribió la IA

Lo que aprendí de esta experiencia es que, precisamente porque un programa lo escribió la IA, no se debe omitir la verificación.

La IA da forma rápidamente a lo que se le dice. Pero los cuidados sobre lo que no se le dice, como "evite que se pueda leer desde fuera" o "trate un envío doble como uno solo", no se incorporan a menos que se le indiquen. Y huecos como estos yacen en silencio dentro de programas que parecen funcionar.

Las personas no necesitan leer todo el código. La corrección del programa la vigilan las comprobaciones automáticas y la auditoría de otra IA. Comprobar si el resultado se ajusta al propósito del local corresponde a quien lo dirige. No hace falta leerlo, pero no se debe omitir la verificación. Eso es lo que creo que significa construir con una IA agéntica.

【Figura 2-3】Las reglas de cuando se podía leer desde fuera y las reglas después de la corrección (extracto) *(La pantalla está en japonés.)*

### 2-4 Construir por intuición multiplica las contradicciones

Cuantas más funciones añadía, más partes había que chocaban con lo que había decidido antes.

El caso típico fue el cálculo de descuentos. En el formulario de reserva, la pantalla de confirmación, el correo y la pantalla de administración, el cálculo de descuentos estaba escrito por separado en cada lugar. Si cambiaba una regla de descuento en un lugar, otro lugar seguía calculando con la regla antigua. Para la misma reserva, la pantalla y el correo podían mostrar montos distintos.

Más tarde, reuní el cálculo de precios en un solo archivo. El formulario de reserva, la ventana de chat y el servidor MCP obtienen los precios a partir de ese archivo.

Las reglas para acumular descuentos también cambiaron en el camino. Como escribí en el capítulo 1, la hora feliz iba a ser originalmente combinable con otros descuentos, pero descubrí que no dejaría ganancia y la cambié a no combinable. Cada vez que cambiaba una regla, una persona tenía que recordar dónde corregir. Esa era la debilidad de un sistema construido por intuición.

También hubo una discrepancia entre el entorno de pruebas y la producción. Mientras probaba la ventana de chat, una pregunta, "¿No había algo como un 10% de descuento?", reveló que las reglas de descuento del entorno de pruebas se habían desviado de la producción. Si los valores del entorno de pruebas difieren de los de producción, se pueden superar las pruebas y aun así fallar en producción. Lo que decidí entonces fue el principio de que "la producción es la correcta". Desde entonces, antes de cada ejecución de pruebas, copio la configuración de producción al entorno de pruebas y confirmo que la discrepancia sea cero antes de ejecutar.

La IA construye lo que se le dice. Pero no se da cuenta de las contradicciones con decisiones anteriores. Lo que previene las contradicciones no es la IA. Es decidir las cosas de antemano.

### 2-5 Volver a aprender la definición de requisitos

Tras reflexionar sobre el sistema de reservas que construí por intuición, volví a aprender la definición de requisitos. Definir los requisitos significa decidir, antes de construir, qué se va a construir, qué no se va a construir y quién lo usará y cómo, y dejarlo escrito en un documento.

Era algo que hacía como cosa natural cuando era ingeniero de sistemas. Pero una vez que pude construir con IA, lo había omitido sin darme cuenta. Uno le cuenta una idea y en minutos aparece algo que funciona. En esa velocidad, había recortado el esfuerzo de decidir.

Mi manera de construir ahora tiene tres etapas.

1. Primero, definir los requisitos con detalle. Qué se construye, qué no se construye, quién lo usará. El comportamiento de cada pantalla. Cómo se tratan las excepciones (errores, doble pulsación, vencimientos). Las reglas que fácilmente terminan contradiciéndose más adelante, como los precios y los descuentos, las defino con especial detalle. También este trabajo lo hago conversando con la IA de chat. Le pido a la IA que encuentre de antemano los huecos y las contradicciones, y quien dirige el local decide.
2. Escribir lo decidido en un "documento de requisitos". No mediante instrucciones habladas o improvisadas, sino reuniéndolas en un solo documento. Ese documento pasa a ser el único criterio para comprobar después qué es lo correcto.
3. Entregar el documento completo a la IA y pedirle que lo implemente. Le doy el documento entero a la IA que escribe el programa (Claude Code), junto con las condiciones para aprobar (que pasen todas las pruebas, que se revise en el entorno de pruebas antes de producción, y así sucesivamente). La IA construye por sí sola hasta cumplir las condiciones, y se revisa a sí misma. Quien dirige el local solo mira cuando se detiene a mitad de camino y en la revisión final.

Por ejemplo, el documento de requisitos de la ventana de chat "T-AI-MURO" se reescribió desde la primera versión hasta la tercera. En la segunda versión decidí "que la IA no calcule los precios", "reunir en una sola ventana el conocimiento del bar y el cálculo de precios" y "conservar también el formulario, para quienes no quieren reservar por chat". En la tercera versión decidí "dónde guardar la copia maestra del conocimiento del bar", "que solo esta ventana muestre los horarios libres", "que el primer intercambio sea una pregunta de cuatro opciones" y "no guardar los registros de conversación; almacenar solo las preguntas que no se pudieron responder". Como las decisiones quedan en un documento, después puedo rastrear por qué las cosas son como son.

Con esta forma de construir, incluso cuando agrego funciones puedo detectar de inmediato las contradicciones al cotejar con el documento. Justamente en una época en que construye la IA, hace falta el "poder de decidir" antes de construir. Esa fue la mayor lección que aprendí del sistema de reservas.

También armé un mecanismo que convierte el procedimiento mismo en un documento y se lo entrega a la IA, para que esta forma de construir pueda ejecutarse igual cada vez que lance un producto nuevo. Escribiré sobre eso en el Capítulo 4.

【Figura 2-4】Índice del documento de requisitos de T-AI-MURO (versión 3) *(La pantalla está en japonés.)*

### 2-6 Aprender el lenguaje de la interfaz

Hay algo más que volví a aprender: los nombres de los componentes de la pantalla.

Aun cuando le decía a la IA "haga esto aquí", la pantalla muchas veces no salía como yo esperaba. Al pensar en la causa, descubrí que no conocía los nombres de los componentes de pantalla. Aunque describiera "una ventanita que aparece encima" o "un aviso que desaparece en unos segundos", a la IA le costaba entender a qué me refería.

Así que leí un libro de referencia sobre UI (user interface, el aspecto y el manejo de una pantalla) y aprendí los nombres de los componentes y los términos técnicos del diseño.

| Componente | Qué es |
| --- | --- |
| Modal | Una ventana pequeña que aparece sobre la pantalla. No se puede operar la pantalla de atrás hasta cerrarla |
| Toast | Un aviso que aparece en el borde de la pantalla durante unos segundos y desaparece solo |
| Pestaña | Un mecanismo en el que al pulsar un título cambia el contenido |
| Acordeón | Un mecanismo en el que al pulsar un título se abre y se cierra el contenido |
| Drawer | Un menú que se desliza desde el costado de la pantalla como un cajón |
| Otros | Breadcrumbs (un rastro que muestra dónde está usted ahora), carruseles (elementos que se desplazan hacia el costado), bottom sheets (un panel que sube desde la parte inferior de la pantalla), etcétera. Cada nombre que aprenda le permite dar instrucciones a la IA en una sola frase |

Al usar los nombres precisos de los componentes, las pantallas que produce la IA se acercan a lo buscado al primer intento. Si usted dice: "Muestre la pantalla de confirmación de la reserva como un modal", la IA no duda.

#### La IA oscila entre extremos al agregar y recortar

Aun después de aprender las palabras, construir pantallas con la IA tenía otro tipo de dificultad. La IA oscila mucho.

Cuando pedí un encabezado "con estilo" para el sitio de reservas, obtuve un encabezado grueso e impresionante. Pero lo esencial de un sitio de reservas son las reservas. Para la clientela habitual que reserva cada vez, un encabezado grueso con largas explicaciones es solo una molestia. Le pedí que recortara la altura a más o menos la mitad, manteniendo la misma cantidad de información.

Cuando unifiqué el pie de los correos y agregué un enlace a la Guía de la Siguiente Parada, el texto del cuerpo me pareció, en comparación, simple y pobre. Así que agregué al cuerpo también un título, una tabla de puntos clave y un botón para pulsar. Cuando agregué en el pie una entrada a la ventana de chat, se veía recargado. Cuando lo comprimí en dos líneas de enlaces separadas por filetes, quedó ordenado pero poco visible. Al final se asentó en dos tarjetas que presentan la función de cada enlace según "cuándo usarlo". La de la izquierda es "para su próxima reserva", la de la derecha, "después de la comida".

Demasiado grueso, demasiado recortado, demasiado llamativo. Lo que decidió el punto justo fue, cada vez, la palabra de quien dirige el local.

#### Una propuesta de diseño sin imágenes

Esto también ocurrió. Le pedí a la IA que escribe programas que creara propuestas de mejora para la ventana de chat usando una IA de diseño (Claude Design), y volvió un informe que decía: "Hice propuestas para ocho pantallas". Pero al abrirlo, solo había descripciones en texto. La IA no había logrado dibujar imágenes, y sin embargo solo quedó el informe de "hecho".

Al final, la IA del lado del chat dibujó cuatro propuestas directamente en la pantalla de diseño. Tomó los colores de la pantalla actual a partir de una captura, puso la historia del bar en una línea de tiempo, dividió la sazón en dos apartados, "método de cocción" y "sabor", convirtió los planes en tarjetas explicativas y unificó los precios en un resumen de reserva.

Cuando uno le hace correr una prueba a la IA, dice "aprobada". Cuando uno le pide un diseño, dice "listo". Comprobar lo que hay dentro es trabajo de una persona. El criterio para juzgar es algo que solo las personas pueden seguir sosteniendo.

#### Lo que usted puede llevarse de este capítulo

- Construir algo que funciona y poder operarlo con seguridad son cosas distintas.
- Compruebe lo que produce la IA no por las palabras de la IA, sino con pruebas. Una prueba solo es confiable una vez que se ha comprobado que falla cuando uno rompe las cosas.
- Los cálculos que no pueden fallar, como los precios, no deben dejarse a la generación de texto de la IA. Que los calcule el programa.

La continuación de este capítulo (los huecos recién encontrados y los pasos que di para repararlos) está en note y X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Capítulo 3: Repartir las herramientas de mi local a otros locales

### 3-1 El pequeño letrero verde de la página de reservas

Abra la página de reservas de Tamuro y verá, cerca de la parte superior, un pequeño letrero verde. Mientras el local está abierto dice "OPEN", y cuando cierra dice "CLOSED". Cuando quien dirige el local pulsa el botón de extensión, la hora de cierre se extiende 30 minutos y aparece un toque de bermellón en el letrero.

Los restaurantes independientes comparten un rasgo. Abren casi exactamente a la hora, pero el cierre suele alargarse. Si la conversación con la clientela está animada, las luces del local siguen encendidas pasada la última orden de las 10:30 p. m.

Pero desde el lado de la clientela, eso no se ve. El estado "Abierto" de Google Maps se determina solo a partir del horario registrado, así que no refleja ni extensiones, ni cierres anticipados, ni cierres temporales. Nadie se acerca a un local pasada su hora de cierre pensando: "Quizás todavía esté abierto". Llamar para preguntar también resulta incómodo.

Este letrero es una herramienta que responde a esa pregunta: "¿Todavía está abierto?". Se llama "AgendaLuce (Cuaderno de Luces)". Luce significa "luz" en italiano.

El Cuaderno de Luces está hecho para funcionar casi sin atención de quien dirige el local. Registre una vez los horarios de apertura y cierre de cada día de la semana, y el letrero se enciende y se apaga automáticamente. Quien dirige el local solo lo toca para extender, cerrar antes o tomar un día libre. Para extender, basta con pulsar una sola vez un botón en el smartphone. El personal también puede operarlo desde un enlace exclusivo que funciona sin iniciar sesión.

La clientela no necesita iniciar sesión ni registrarse. Al abrir la página pública, puede ver el estado actual de la luz. Si la agrega a la pantalla de inicio del smartphone, funciona como una aplicación. El pequeño componente del letrero también se puede incrustar en otros sitios web. Lo que aparece en la página de reservas de Tamuro es ese componente.

El Cuaderno de Luces es gratuito. Si solo incrusta el componente del letrero en su sitio web, la configuración toma unos 10 minutos.

Y aquí viene lo importante. Este Cuaderno de Luces no es solo para Tamuro. Cualquier local puede usarlo.

Dejé deliberadamente el nombre del local fuera del diseño del letrero. Si le pusiera el nombre del local, se convertiría en un letrero de Tamuro. También se puede elegir el idioma de visualización. Hice el componente pequeño para que se pueda incrustar en el sitio web de cualquier local.

Una herramienta nacida del problema de Tamuro, "el cierre se alarga", hecha desde el principio en una forma que cualquiera puede usar. Eso es el Cuaderno de Luces. Y el conjunto de herramientas como esta es la "serie Agenda".

【Figura 3-1a】El letrero del Cuaderno de Luces en la parte superior de la página de reservas (abierto) *(La pantalla está en japonés.)*

【Figura 3-1b】Aparece un toque de bermellón durante una extensión *(La pantalla está en japonés.)*

【Figura 3-6a】La pantalla de quien dirige el local. Para extender, se pulsa el botón una vez *(La pantalla está en japonés.)*

【Figura 3-6b】Justo después de pulsar extender. La hora de cierre se extiende 30 minutos *(La pantalla está en japonés.)*

【Figura 3-6c】La página pública que ve la clientela (durante una extensión) *(La pantalla está en japonés.)*

### 3-2 Todo empezó con el cuaderno de cuero negro

La serie Agenda no fue planeada como una serie. Empezó con un solo sistema, uno que ni siquiera se ha lanzado todavía.

Lo primero que me propuse construir fue un mecanismo que reconoce los rostros de la clientela y da la bienvenida a los habituales. Una cámara en la entrada del local distingue a las personas que llegan por el rostro y le avisa a quien dirige el local: "Esa es la persona que comió el tonteki la última vez, la que no veíamos desde hace tres meses". Quería que una máquina ayudara con el trabajo que quien dirige un local pequeño hace de memoria: recordar rostros, nombres y preferencias.

Pero poco después de empezar a construir, me di cuenta de que este era un sistema al que se le confiaba algo muy pesado. Rostros. Atributos. Historial de visitas. La forma de ser de cada persona de la clientela. Todo es información cuya filtración causaría un daño irreparable.

Lo que me vino a la mente entonces fue "El cuaderno de cuero negro" de Seicho Matsumoto. Un registro que no se muestra a nadie, pero que ciertamente existe. Un libro de apuntes que, una vez abierto, pone en juego la vida y la muerte de las personas. ¿No es exactamente eso lo que estoy tratando de construir?

En italiano, "cuaderno" es Agenda, y "negro" es Nera. Juntos: AgendaNera. El cuaderno de cuero negro. Así quedó decidido primero el nombre.

AgendaNera todavía se está construyendo. Es el que estoy construyendo con más cuidado de toda la serie.

Y este nombre fue el detonante. Si hay un cuaderno negro, puede haber cuadernos de otros colores. Reconstruiría los mecanismos que usaba todos los días en mi propio local en formas que cualquier local pueda usar, y los lanzaría un cuaderno a la vez. Esa es la [serie Agenda](https://bontallc.com/agenda?via=b2-es-{{FMT}}).

### 3-3 Agregar cuadernos, de uno en uno

La serie Agenda es un conjunto de pequeñas aplicaciones web, cada una de las cuales responde con una herramienta a un problema de un restaurante. Cada una tiene un nombre italiano y un apodo japonés que termina en "techō" (cuaderno). Cada nombre tiene su propio origen.

| Nombre | Apodo | Origen del nombre | Qué hace |
| --- | --- | --- | --- |
| AgendaTimbro | Fichajes | Timbro significa "sello". Es el fichaje mismo | Registra la entrada y la salida del personal |
| AgendaOro | Rentabilidad | Oro significa "oro". El cuaderno del dinero | Estima la rentabilidad de abrir un local o de un nuevo plato del menú (gratis) |
| AgendaBis | Guía de la Siguiente Parada | Bis significa "otra vez". El "¡Bis!" que se grita desde el público en un concierto | Guía a la clientela hacia una siguiente parada cercana (gratis) |
| AgendaQA | Guía de Soporte | Qua significa "aquí". Cuando hay un apuro, aquí | El servicio de ayuda compartido de la serie (gratis) |
| AgendaLuce | Cuaderno de Luces | Luce significa "luz" | Muestra si el local está abierto (gratis) |
| AgendaRicetta | Cuaderno de Costos de Receta | Ricetta significa "receta" | Calcula el costo de una receta y su porcentaje de costo (gratis) |
| AgendaNera | Cuaderno de Clientes Habituales | Nera significa "negra". El cuaderno de cuero negro | Da la bienvenida a los habituales con reconocimiento facial (en construcción) |
| AgendaTurno | Cuaderno de Turnos | Turno es en italiano "turno" o "turno de servicio" | Reúne las solicitudes de turnos del personal y entrega el horario que arma la propia IA de quien dirige el local (próximamente) |

¿Qué cuaderno le conviene a qué tipo de local? Fichajes es para locales con dos o más integrantes de personal que manejan la asistencia en papel o en LINE *(la aplicación de mensajería más usada de Japón)*. Rentabilidad es para quienes están por abrir un local y para quienes quieren revisar sus números porque cambió el alquiler o los costos. La Guía de la Siguiente Parada es para locales centrados en las comidas que quieren enviar pronto a la clientela al siguiente lugar. El Cuaderno de Luces es para locales independientes cuyo cierre se retrasa o se adelanta respecto de lo previsto. El Cuaderno de Costos de Receta es para locales donde las recetas están en la cabeza pero nunca se ha calculado el porcentaje de costo.

#### Fichajes no calcula los sueldos

Fichajes convierte la tableta del local o los smartphones del personal en una máquina de fichaje tal como están. Basta tocar su nombre. La hoja de asistencia se totaliza automáticamente y se puede exportar como CSV (un formato que se abre en programas de hoja de cálculo). La jornada comercial empieza a las 5 a. m., así que aun con horarios de madrugada la fecha no cambia a mitad del servicio.

Pero Fichajes, deliberadamente, no calcula los sueldos.

Los salarios por hora, los complementos y las fechas de corte difieren demasiado de un local a otro. Madrugada con 25% adicional, feriados como categoría aparte, transporte por monto diario. Se construyera como se construyera, siempre habría algún local al que no le sirviera.

Así que, en lugar de calcular, preparé "una plantilla de instrucciones para entregar a una IA". Quien dirige el local pega el CSV de asistencia descargado y esta plantilla, tal cual, en la IA que use normalmente, sea ChatGPT, Claude o Gemini. Entonces la IA calcula los recargos nocturnos, el pago de feriados y el transporte, y los presenta en una lista. Las reglas de cada local, como "la fecha de corte es a fin de mes, la madrugada lleva 25% adicional y los domingos son una categoría aparte", se pueden agregar a la plantilla y se reflejan tal cual. El CSV incluye columnas con el día de la semana y el nombre del feriado para que la IA pueda calcular correctamente.

Yo no guardo el mecanismo de cálculo; cada local conserva sus reglas en sus propias manos. Pensé que esa es la forma más difícil de romper.

#### Guíelos a una siguiente parada y deje su local en su memoria

La Guía de la Siguiente Parada es una herramienta para hacer una "página guía de la siguiente parada" que se entrega a la clientela. A quienes han terminado su comida, los guía a un bar cercano o a un lugar para un último bocado, junto con cuántos minutos se tarda a pie.

Parece una herramienta para enviar a la clientela a otra parte, pero tiene un pequeño truco. Guiar a alguien a una segunda parada implica que la primera parada fue su local. Mientras parece enviar a la clientela a otro local, en realidad está grabando en su memoria que "la primera parada fue este local". Así está diseñada.

#### Tres principios de diseño: automático, fuerza prestada, una sola función

Todos los cuadernos de la serie Agenda comparten tres principios.

El primero es "automático". Debe funcionar sin que quien dirige el local lo toque todos los días. Con el Cuaderno de Luces, una vez que se registra el horario, la luz se enciende y se apaga sola. Quien dirige un restaurante no tiene tiempo de tocar una pantalla durante el servicio. Una herramienta que no funciona si no se la toca terminará por dejar de usarse.

El segundo es "fuerza prestada". No construir todo uno mismo, sino dejar las cosas en manos de las herramientas y la IA que quien dirige el local ya usa. El cálculo de sueldos de Fichajes es el caso modelo. El cuaderno de turnos es igual: se ocupa solo de reunir las preferencias del personal y deja el trabajo de armar los turnos a la propia IA de quien dirige el local. No carga con un mecanismo complicado propio ni con el costo de llamar a una IA. Por eso el precio se puede mantener bajo.

El tercero es "una sola función". Cada cuaderno hace una sola cosa, y la hace de manera confiable. Un sistema multifunción es demasiado pesado para un local independiente. Si se siguen agregando funciones, se vuelve más difícil de usar y se multiplican las contradicciones del lado de quien construye. Eso lo aprendí en carne propia con el sistema de reservas del Capítulo 2. Por eso agrego los cuadernos de uno en uno, cada uno haciendo "solo esta cosa, bien hecha".

#### Por qué el sistema de reservas no está en la serie

A esta altura, imagino una pregunta obvia. Lo que más trabajo le costó a Tamuro es el sistema de reservas. ¿Por qué no ponerlo en la serie Agenda?

De hecho, alguna vez tuve la intención. El plan era convertir el sistema de reservas en una forma que otros restaurantes pudieran usar y lanzarlo como un cuaderno más de la serie. Pero en agosto de 2026 cancelé ese plan.

La razón es justamente lo que escribí en el Capítulo 1. El sistema de reservas de Tamuro está repleto de la manera de hacer negocio de Tamuro. Que las personas que vienen solas son la mitad de la clientela. Que casi el 90% de las reservas se hacen el mismo día. Que quiero vender el tiempo previo a la apertura. Que quiero que vengan en grupo. Que quiero hacer crecer a los habituales. Construí las combinaciones de descuentos, el orden de los correos y la manera de recomendar en la conversación, todo para ajustarse a esto.

Si lo diluyera hasta convertirlo en algo que cualquiera pudiera usar, se volvería un sistema de reservas corriente que le queda más o menos bien a todos los locales. Entonces la fuerza de Tamuro desaparecería. El sistema de reservas y el CRM son la manera en que el local se vende a sí mismo. En lugar de ajustar el local a un sistema genérico, hay que ajustar el sistema del local al local. Nuestro local, con nuestras propias especificaciones. Así que decidí mantener el sistema de reservas de Tamuro solo para Tamuro.

Entonces, ¿no hay nada que repartir fuera del local? Sí lo hay. Alrededor del sistema de reservas hay muchos problemas pequeños comunes a todos los locales. El núcleo del local se mantiene con especificaciones propias. Las herramientas que resuelven los problemas de alrededor se construyen desde el principio en una forma que todos puedan usar, y se reparten. La página de reservas de Tamuro es una muestra con ambas cosas alineadas en una sola pantalla. Sobre un sistema de reservas solo para Tamuro está el letrero del Cuaderno de Luces que cualquiera puede usar.

【Figura 3-2】La página de presentación de la serie Agenda *(La pantalla está en japonés.)*

【Figura 3-3a】Presentación de Fichajes *(La pantalla está en japonés.)*

【Figura 3-3b】Presentación de Rentabilidad *(La pantalla está en japonés.)*

【Figura 3-3c】Presentación de la Guía de la Siguiente Parada *(La pantalla está en japonés.)*

【Figura 3-4】La pantalla de fichaje de Fichajes. Basta tocar su nombre (datos sintéticos) *(La pantalla está en japonés.)*

### 3-4 Construir para todos desde el principio

Hago una herramienta para mi propio local y luego la reparto también a otros locales. Dicho así suena sencillo, pero para hacerlo debe cambiar la manera de decidir las cosas antes de empezar a construir.

Si construyera solo para Tamuro, lo más rápido sería escribir directamente en el programa el horario de Tamuro y el nombre de Tamuro. Pero entonces ningún otro local podría usarlo. Si después se intenta volverlo de uso general, se termina buscando cada lugar con datos fijos y corrigiéndolos uno por uno.

Por eso las herramientas de la serie Agenda se especifican desde el principio con la premisa de que todos pueden usarlas. Parto de un problema de Tamuro, pero en la etapa de requisitos separo dos preguntas: "¿Esto es cierto solo de Tamuro, o es cierto de todos los locales?". No poner el nombre del local en el letrero. Dejar que se elija el idioma. Hacerlo fácil de incrustar en cualquier sitio web. Decisiones como estas las fijé mientras escribía el documento de requisitos del Cuaderno de Luces.

Este es otro uso de la definición de requisitos que volví a aprender en el Capítulo 2. Si se deciden estas cosas primero, la herramienta se puede usar en Tamuro y repartir tal cual a otros locales.

Los problemas de mi local también son los problemas de otros locales. No soy la única persona al frente de un local que quiere avisar a la clientela que la hora de cierre se está alargando. Quien dirige un local independiente construye una herramienta a partir de su propio problema y luego la reparte a otros locales. Esa es la idea detrás de la serie Agenda.

### 3-5 La democratización de la tecnología

La serie Agenda ya tiene más de 10 productos. Los construyo y los opero yo solo, mientras estoy detrás de la barra.

Hace unos años, esto habría sido impensable. Para construir un producto hacía falta alguien que lo planificara, alguien que diseñara las pantallas, alguien que escribiera el código, alguien que lo probara y alguien que lo operara. Sin un equipo y sin fondos, no era posible sacar un producto al mundo.

Eso ya no es así. Quien dirige el local le cuenta los requisitos a la IA, la IA escribe el código, la IA lo prueba y otra IA lo audita. Lo que hace quien dirige el local es decidir qué construir, juzgar si los resultados de la IA se ajustan al propósito del local y hacer solo las operaciones que únicamente las personas pueden hacer.

A este tipo de cambio se le suele llamar la "democratización de la tecnología". El poder de construir ya no es propiedad de unas pocas personas o empresas.

Pero seamos honestos aquí. Como escribí en la Introducción, trabajé en TI durante unos 16 años, sobre todo en planificación de sistemas y en la coordinación entre las personas en el terreno y los proveedores de desarrollo. Conocía por experiencia la definición de requisitos, la manera de pensar las bases de datos y cómo ejecutar pruebas. Por eso no afirmaré que alguien que nunca ha escrito una línea de código podría hacer lo mismo a partir de mañana.

Aun así, ha cambiado muchísimo. Ahora puedo construir por mi cuenta, en los huecos de mi trabajo principal, cosas de una escala que antes requería un equipo. Y para quienes no tienen experiencia, la barrera de entrada ha bajado sin duda. La IA le enseñará si le pregunta sobre algo que no entiende. Le dará forma a lo que usted le diga con palabras. Lo que falta no es técnica, sino la capacidad de decidir qué construir y las palabras para decírselo a la IA. Esas son capacidades que las personas que dirigen locales usan todos los días de todos modos.

### 3-6 El debate sobre la "muerte del SaaS"

El software que las personas usan por internet a cambio de una cuota mensual, como la serie Agenda, se llama SaaS (Software as a Service, software como servicio). Software de contabilidad, de control de horarios y asistencia, de gestión de reservas. Hoy los restaurantes funcionan con muchas herramientas SaaS.

¿Pondrá la IA fin al SaaS? En 2026, ese debate se encendió con fuerza.

Un detonante fue una declaración del director ejecutivo de Microsoft, Satya Nadella. En un pódcast de diciembre de 2024, Nadella dijo que las aplicaciones SaaS se derrumbarían en la era de los agentes de IA. El razonamiento: una vez que los agentes de IA se encarguen de la parte de toma de decisiones del trabajo empresarial, ya no hará falta el software hecho para que las personas lo operen a través de pantallas.

Luego, en febrero de 2026, Anthropic anunció Claude Cowork (una herramienta de IA que realiza tareas empresariales de forma autónoma), y las acciones de las empresas estadounidenses de software se vendieron con fuerza. En Wall Street, la caída pasó a llamarse la "SaaSpocalypse". Lo que temían los inversionistas era que, si los agentes de IA hacen el trabajo, el modelo SaaS de cobrar una cuota por persona (precio por puesto) se vendría abajo.

También hay contraargumentos. El director ejecutivo de Nvidia, Jensen Huang, dijo que los agentes de IA no reemplazarán al software sino que usarán el software en lugar de las personas, y calificó la venta masiva de reacción exagerada. Tampoco faltan quienes consideran que el SaaS que incorpora la IA se verá fortalecido.

¿Morirá realmente el SaaS? Esto es lo que pienso.

Lo que muere es la capa intermedia del SaaS: la que cobra una cuota mensual alta por puesto y supone que las personas lo operan a través de pantallas. Si la IA hace el trabajo en lugar de las personas, no hace falta un puesto por cada persona. Si nadie está operando una pantalla, no hace falta una pantalla elaborada.

Lo que queda son herramientas baratas que hacen una sola cosa de manera confiable. Y herramientas que a la IA le resulta fácil usar.

Esto es exactamente lo que dicen los tres principios de la serie Agenda. Funciona de forma automática, se deja en manos de la IA de quien dirige el local (apoyarse en otros) y hace una sola cosa (una sola función). AgendaTurno deja el trabajo de armar el horario de turnos a la IA de quien dirige el local, que es justo la forma de "la IA usa el software" que describe Huang. El sistema de reservas de Tamuro abre una ventana a las IA de la clientela mediante MCP, y esa es la misma idea.

Por supuesto, aquí puede parecer que hay una contradicción. Hablo de la muerte del SaaS y, sin embargo, la serie Agenda es en sí misma SaaS. Pero la serie Agenda es un conjunto de herramientas que quien dirige un local construyó para su propio local y luego hizo públicas a un precio bajo. No es un modelo que cobre una cuota mensual alta por puesto, ni supone que las personas se pasen pegadas a una pantalla todos los días. Está construida desde el principio con la premisa de que la IA la usará.

#### La "muerte del SaaS" para los restaurantes

Este debate puede sonar a un asunto de inversionistas y de la industria de TI. Pero para los restaurantes, lo mismo está a punto de ocurrir de una forma mucho más cercana.

Muchos locales independientes pagan una cuota mensual a sitios gastronómicos y de reservas y, además, pagan una comisión por cada reserva que el sitio les trae. A cambio de traer clientela, el sitio retiene el vínculo con la clientela, y no es raro que el local ni siquiera tenga los datos de contacto de las personas. Si el sitio sube sus tarifas, el local no tiene más remedio que aceptarlas, y si cambia el sistema de clasificación, cambia el flujo de clientela.

Como escribí en el Capítulo 1, en 2026 comenzó la época en que la clientela hace que su propia IA busque locales. Si el punto de entrada se traslada a la IA, todo el esquema de pagar a un sitio cuotas mensuales y comisiones para aparecer bien ubicado en sus listados empieza a tambalear. Si un local abre por su cuenta una ventana a la IA, la clientela puede llegar a él sin pasar por los grandes sitios. Los registros de reservas y la relación con la clientela quedan en manos del local.

Si pusiera "la muerte del SaaS" en palabras de un local independiente, sería "el fin de la época en que pagar bastaba para aparecer en la lista". Tamuro abrió su ventana mediante MCP y mantiene sus reservas y su CRM con especificaciones propias como preparación para eso.

Si el SaaS morirá o no, todavía nadie lo sabe. Pero la forma de las herramientas que quedarán en la era de la IA se va dejando ver poco a poco. Eso es lo que pienso.

### 3-7 Monetización: en pequeño, en cantidad y a bajo precio

Construyo la serie Agenda con el objetivo de que se sostenga como negocio. El objetivo es convertirla en un segundo pilar de ingresos, aparte del restaurante.

Fijé precios modestos y bajos. Las cuotas mensuales parten de unos cientos de yenes. Fichajes, por ejemplo, cuesta ¥500 (unos US$ 3,3) por mes. También mezclo herramientas gratuitas, como Rentabilidad, el Cuaderno de Luces y el Cuaderno de Costos de Receta. Las herramientas gratuitas sirven como la entrada por la que las personas conocen la serie Agenda. El Cuaderno de Luces no usa ni una API de mapas ni IA generativa, así que casi no cuesta nada operarlo. Por eso puedo regalarlo.

Hay una sola cuenta. Con una cuenta común llamada AgendaID, puede usar todas las herramientas de la serie. No necesita registrarse de nuevo para cada herramienta. Las herramientas de pago vienen con un período gratuito de tres meses y se pueden empezar sin registrar una tarjeta. El período gratuito está disponible una sola vez por cada combinación de local y producto. Si usted recomienda a otro local, recibe una bonificación.

La razón por la que puedo mantener los precios bajos está en cómo construyo. Construyo solo, dejo que la IA escriba el código y reutilizo una base compartida. El costo de la base de datos se mantiene en unos US$ 35 por mes para toda la serie. Si el costo de construir y el costo de operar son ambos pequeños, un negocio puede sostenerse incluso con ventas pequeñas.

Seamos honestos. Mientras escribo este libro, algunos locales han probado las herramientas, pero casi no hay suscripciones de pago. La forma de construir está lista, pero la forma de darla a conocer todavía está pendiente. Este libro también está pensado como un volumen con ese propósito: darla a conocer.

#### Construir algo y lograr que se siga usando son cosas distintas

Seamos honestos en una cosa más. Poder construir una herramienta y que alguien siga usándola son asuntos distintos.

Construir se ha vuelto más rápido gracias a la IA. Pero lograr que la gente siga usándola exige otro trabajo. Responder las preguntas sobre cómo usarla (para eso existe la Guía de Soporte). Enviar un aviso antes de que termine el período gratuito. Explicar el motivo cuando se sube un precio. Borrar correctamente los datos cuando alguien pide darse de baja. Y, sobre todo, mantenerla funcionando sin que quien dirige el local la toque.

De los tres principios de la serie Agenda, "automático" es el principio pensado para lograr que "se siga usando". Una herramienta que no funciona si quien dirige el local no la toca todos los días terminará siendo cancelada. El trabajo no termina cuando se construye. Se convierte en un negocio solo cuando se sigue usando. Sumar, de uno en uno, locales que la sigan usando: ese es mi trabajo después de publicar este libro.

#### Si quiere empezar en su propio local

Para quienes lean este libro y quieran probarlo en su propio local, hay tres pasos.

1. Abra https://bontallc.com/agenda?via=b2-es-{{FMT}} e inicie sesión con una cuenta de Google (se creará su AgendaID. No hace falta registrar una tarjeta)
2. Primero, agregue un cuaderno gratuito. Recomiendo el Cuaderno de Luces. Basta con pegar el componente del letrero en su sitio web y funciona en 10 minutos. Si todavía no ha abierto, pruebe Rentabilidad
3. Si le parece que le conviene, pruebe Fichajes gratis durante tres meses. Llega un aviso cuando se acerca el plazo, así que no se le cobrará aunque lo deje así

Si tiene preguntas, consulte a través de la Guía de Soporte (AgendaQA). La IA responde al instante las dudas sobre el uso, y las preguntas sobre especificaciones y errores las leo personalmente.

Las ventas de un restaurante dependen del clima y de la estación. La cantidad de asientos y el horario de atención tienen límites. Las ventas de herramientas, en cambio, no tienen límite de asientos. Dirigir un local mientras se reparten herramientas nacidas de los problemas del propio local, y que eso se convierta poco a poco en ingresos: creo que esto puede ser otra manera de ganarse la vida para un local independiente.

#### Seguir siendo una empresa pequeña, y salir al mundo

Hay otra cosa que decidí desde el principio sobre la serie Agenda. No la construiría solo en japonés.

Fichajes, Rentabilidad y la Guía de Soporte se pueden usar los tres en 20 idiomas. Los textos de la pantalla y las preguntas frecuentes, todo. Una herramienta hecha para un bar de 19 asientos en Tokio funciona igual en inglés, en coreano, en vietnamita.

Hay dos razones. Una es que los problemas de los restaurantes no cambian cuando cambia el país. Se quiere registrar las entradas y salidas del personal. Se quiere conocer la rentabilidad antes de abrir. Se quiere avisar a la clientela que se extendió el horario de cierre. Todos son problemas que comparten los locales independientes de todo el mundo. La otra es que la cantidad de locales independientes en Japón sigue bajando. Si atendiera solo al mercado de habla japonesa, las ventas de herramientas tendrían un techo.

En el pasado, para que una empresa pequeña vendiera productos en el extranjero, necesitaba agentes locales, empresas de traducción y entidades legales. Ahora la IA ayuda con la traducción y la corrección. Los sistemas de pago compartidos funcionan en todo el mundo. Para distribuir el software solo hace falta un servidor, y no hacen falta existencias ni almacén en cada país. Una herramienta hecha por una sola persona puede estar en los estantes del mundo, en 20 idiomas, al día siguiente de hacerse. En el pasado, solo las grandes empresas podían hacer eso.

Una empresa muy pequeña que hace negocios con varios países desde el principio: a esas empresas a veces se las llama micromultinacionales (empresas multinacionales diminutas). Bonta LLC apunta exactamente a eso, con un local en Higashi-Nakano y una sola persona al frente.

Por supuesto, traducir a 20 idiomas no significa que quienes dirigen locales en el extranjero vayan a empezar a usarlas de inmediato. Algunas de las traducciones todavía esperan la revisión de hablantes nativos para sonar naturales. Aun así, al quitar la barrera del idioma desde el principio, desaparece el techo sobre hasta dónde pueden llegar las herramientas, igual que el techo de asientos.

Cómo estoy construyendo esa base es el tema del Capítulo 4.

【Figura 3-5】Cambio de idioma en la Guía de Soporte. Se enumeran 20 idiomas *(La pantalla está en japonés.)*

## Capítulo 4: Tecnología - Un sistema para construir productos en solitario, de forma continua

Puntos clave de este capítulo

- Convertí el procedimiento para lanzar un producto nuevo en un documento, en una forma (una skill) que una IA puede leer y ejecutar. Lo que hacen las personas es solo juzgar y realizar las operaciones que solo las personas pueden hacer
- Las partes compartidas, como el inicio de sesión, el cobro, las páginas de presentación y las guías hacia otros productos, se construyen una vez y se reutilizan en todos los productos. El costo de base de datos de esa base es de unos US$ 35 por mes
- El sistema todavía está creciendo. Sigo agregando al documento de procedimiento los fracasos, como un diseño rechazado cinco veces seguidas

(Este es un capítulo con muchos términos técnicos. Si no le interesa la tecnología, puede saltar al Capítulo 5 y la historia sigue conectada.)

### 4-1 ProductBootstrap: entregar a la IA el procedimiento de lanzamiento mismo

Cada vez que construía un producto, repetía la misma preparación y los mismos errores. Crear un repositorio (un almacén para programas). Conectar el inicio de sesión. Decidir los colores del diseño. Montar el sistema de pruebas. Preparar el entorno de producción. Seguramente había hecho todo eso para el producto anterior, pero había olvidado los detalles y tropezaba en los mismos lugares.

Así que convertí el procedimiento para lanzar un producto nuevo en un documento. Una forma de ese documento que la IA que escribe el código (Claude Code) puede leer y ejecutar es lo que llamo una "skill". El nombre de esta skill es ProductBootstrap. "Bootstrap" es un término común en el mundo de la computación para arrancar por sí mismo a partir de un mecanismo mínimo, y lo apliqué al lanzamiento de productos.

No guardo ningún programa de plantilla. Copio el producto terminado más recientemente y empiezo el producto nuevo a partir de él. Así, las lecciones más nuevas pasan automáticamente al siguiente producto. Tampoco hace falta seguir manteniendo una plantilla vieja.

#### El flujo del procedimiento

1. Entregar el documento de requisitos. Si los campos obligatorios (nombre del producto, qué hace, quién lo usa, precio, unidad de precio, color identificador, ubicación del diseño maestro, etcétera) se dejan en blanco, la IA no empieza. La regla es que no le hace preguntas a quien dirige el local en el camino. Si no está todo listo al principio, no comienza
2. Decidir el color del producto. Cada producto de la serie Agenda tiene un color identificador. La IA mide los colores de los productos existentes, propone unos cuatro candidatos que no se superponen, y quien dirige el local elige
3. Fijar el diseño. Hago que una IA de diseño (Claude Design) cree propuestas para las pantallas. La IA ejecuta su autocomprobación hasta tres rondas, y solo las propuestas que pasan la comprobación se muestran a quien dirige el local
4. Dejar la implementación a la IA hasta el final. La IA construye y corrige por sí sola hasta cumplir las condiciones de aceptación fijadas (verificaciones de tipos, verificaciones de estilo, todas las pruebas en verde, aprobar cada verificación de pantalla y que los cambios en la base de datos pasen sin problemas en el entorno de pruebas)
5. Quien dirige el local aprueba solo al pasar a producción. Todo hasta el entorno de pruebas avanza sin supervisión, y quien dirige el local juzga solo la operación de producción

Construí la etapa de implementación para que no se detenga a mitad de camino a esperar la aprobación de quien dirige el local. Al principio avanzaba pidiendo aprobación en cada etapa, pero así nada avanzaba. Cuando hay varias ventanas de trabajo de IA, cada una se detiene esperando aprobación, y quien dirige el local tiene que ir ventana por ventana emitiendo juicios. Así que lo cambié: entrego de antemano el rango que ya está aprobado y las condiciones de aceptación que una máquina puede juzgar, y solo se detiene ante un fallo.

También se fijan las condiciones de detención. Cuando el documento de procedimiento y la decisión de quien dirige el local entran en conflicto. Cuando se vuelve necesaria una operación que solo una persona puede hacer. Cuando no logra avanzar con el mismo error tres veces seguidas. Cuando la autenticación caduca, los permisos son insuficientes o hace falta una operación irreversible. Fuera de eso, la IA avanza por su cuenta. El estado del trabajo se registra en un archivo pequeño, de modo que, aunque se caiga a mitad de camino, puede reanudar desde ahí.

#### Las personas hacen solo dos cosas

Escribí esto en el documento de procedimiento: la IA ejecuta todos los pasos. A quien dirige el local solo se le pueden pedir las dos cosas siguientes.

- El juicio mismo. Aprobar, dictaminar, decidir cuál de dos opciones tomar
- Las operaciones que solo una persona puede hacer. Claves que solo se pueden emitir desde la pantalla de administración de un servicio externo, trámites que implican verificación de identidad, operaciones en un dispositivo real y juicios visuales

Si la IA le deriva cualquier otra tarea a quien dirige el local, eso es una violación del documento de procedimiento. En la tabla de procedimiento agregué una columna de "ejecutor" a cada fila, y toda fila en cuya columna de quien dirige el local no se pueda indicar un motivo se pasa al lado de la IA.

Tuve una razón para hacer esta regla. Cuando ordené el trabajo restante de un producto, la IA enumeró "crear el proyecto del servidor", "registrar el destino del inicio de sesión", "ingresar las variables de entorno" y "montar el entorno de pruebas", todo como tareas de quien dirige el local. Cada una era una operación que la IA podía ejecutar por sí misma. "¿Por qué lo hago yo?" fue mi reacción sincera en ese momento. La IA lo hace por sí misma si uno se lo pide. Pero si no se lo pide, se lo pasa a una persona. Por eso tuve que escribirlo en el documento de procedimiento.

Puse todos los fracasos del sistema de reservas que describí en el Capítulo 2 en la lista de verificación de este documento de procedimiento. Poner primero las pruebas. No conservar datos de producción en el entorno de desarrollo. Construir primero el entorno de pruebas. El siguiente producto evita el mismo dolor desde el principio.

#### Todavía en crecimiento

Este documento de procedimiento no es un producto terminado. Es algo a lo que sigo agregando cada vez que algo falla.

Por ejemplo, hubo una vez en que le pedí a la IA de diseño la pantalla de un producto cinco veces seguidas, y las cinco fueron rechazadas. Eso incluye las rondas en las que le entregué las reglas de diseño de toda la serie (DESIGN.md).

Al principio, la IA diagnosticó la causa como "el esquema de colores mismo". Yo lo negué. Las causas reales eran dos. Una era que se usaban libremente colores sin definición en las reglas. La otra era que tres secciones con funciones distintas estaban apiladas verticalmente con el mismo color de fondo y los mismos márgenes, sin ningún límite entre ellas. No se había violado ninguna regla, y sin embargo sus funciones habían desaparecido del aspecto.

Así que agregué cláusulas a las reglas de diseño. No dar el mismo aspecto a cosas con funciones distintas. No separarlas solo por el color. Lo más importante va primero en la línea de visión. Solo las cosas verdaderamente iguales pueden alinearse con el mismo peso. No hacer un diseño que simplemente apile cosas verticalmente.

Hubo otra lección del fracaso. Si uno transmite el "aspecto por defecto que hay que evitar" solo como una lista de prohibiciones, la IA oscila por completo hacia otro aspecto por defecto que no figura en la lista. Cuando prohibí a la vez las tarjetas, las sombras y las esquinas redondeadas, lo que volvió fue una pantalla como de periódico hecha solo de filetes y márgenes. Desde entonces, hago escribir los materiales de la solicitud en tres columnas: "el patrón que hay que evitar", "lo que quería prohibir" y "qué hacer en su lugar".

También cambié a mitad de camino cómo decido los colores identificadores. Cuando los productos superaron los ocho, la banda de colores oscuros quedó ocupada por los productos existentes, y del noveno producto en adelante ya no se podía conseguir un color oscuro para líneas y botones sin chocar con los existentes. Así que revisé la regla: el color identificador de un producto se usa solo para colores de superficie claros, y las líneas, los filetes, los íconos y los botones principales se unifican todos en el negro carbón compartido de la serie. Fue una restricción que solo se hizo evidente cuando los productos se multiplicaron.

Cada vez que algo falla, corrijo el documento de procedimiento. El siguiente producto se vuelve más fácil en esa medida. Creo que hacer crecer el documento de procedimiento es la mejor inversión para seguir construyendo productos en solitario.

【Figura 4-2】Las etapas del procedimiento de lanzamiento y quién las ejecuta (la IA o quien dirige el local) *(La pantalla está en japonés.)*

【Figura 4-3】Los colores identificadores de la serie Agenda. Un color por producto, usado solo en superficies *(La pantalla está en japonés.)*

### 4-2 AgendaHub: la puerta de entrada

A medida que los productos se multiplican, uno termina construyendo las mismas cosas una y otra vez. Inicio de sesión, cobro, páginas de presentación, guías hacia otros productos. Para operar esto en solitario, hay que construir las partes compartidas una vez y reutilizarlas en todos los productos.

AgendaHub es el lugar donde se reúnen esas partes compartidas. Lo llamo la "puerta de entrada".

Primero, es la entrada que enruta desde una sola dirección a todos los productos. Bajo un único dominio, bontallc.com, se alinea una entrada para cada producto: /agendatimbro, /agendaoro, /agendaluce. A la clientela le parece que los productos están dentro de un mismo sitio, pero en realidad detrás de cada uno corre un programa distinto.

Luego, es el lugar donde se ubican las páginas de presentación de los productos. Hay una página de presentación de la serie y, dentro de ella, una sección para cada producto. Cada sección contiene el nombre del producto y su apodo, el precio, un problema expresado con las palabras de quien dirige el local que empieza con "Cuando usted...", una descripción de lo que puede hacer y un enlace a la página de detalle. Cuando lanzo un producto nuevo, agregar esta sección forma parte del procedimiento de lanzamiento.

Y es el hogar de las reglas de diseño y de los procedimientos de lanzamiento. El maestro de los colores identificadores, las reglas de pantalla (DESIGN.md), la skill ProductBootstrap que describí en 4-1, la skill que revisa las pantallas y la skill que hace cambios en la base de datos de forma segura. Para todas las reglas que abarcan la serie, el contenido real vive aquí, y cada producto lo lee por referencia.

【Figura 4-1】La estructura de la serie Agenda. Desde la puerta de entrada (AgendaHub) hasta cada cuaderno, y cada cuaderno se conecta a una cuenta (AgendaID) *(La pantalla está en japonés.)*

### 4-3 AgendaID: cuentas y cobro compartidos

AgendaID es el sistema compartido de la serie para las cuentas y el cobro.

A quien dirige un local le basta con iniciar sesión una vez con una cuenta de Google para usar todos los productos. No hace falta crear una cuenta para cada producto. También planeo que, con el tiempo, la configuración de idioma pase de un producto a otro.

El cobro también es un solo sistema. En lugar de construir para cada producto la conexión con el servicio de pagos (Stripe), AgendaID se encarga de todo. Hay cuatro categorías de precios: un producto ligero de ¥300 (unos US$ 2) por mes, un producto de pago por uso, un producto de compra única de ¥600 (unos US$ 4) y un producto gratuito. Los productos de pago tienen un período gratuito de tres meses sin registro de tarjeta, que se puede usar una vez por cada combinación de local y producto. También hay un mecanismo que suma tres meses de período gratuito a quien recomienda y a la persona recomendada.

Antes de que termine el período gratuito, llegan correos de aviso con siete días y con un día de anticipación. Primero construí estos correos también dentro de Fichajes, pero al multiplicarse los productos me di cuenta de que era un desperdicio darle el mismo mecanismo a cada producto, así que lo consolidé del lado de AgendaID.

#### La baja y la eliminación también bajo reglas compartidas

Hay una parte poco llamativa pero importante: la baja y la eliminación de datos.

Cuando alguien se da de baja, ¿qué datos se eliminan y cuándo? Si se construye por separado para cada producto, seguramente se omitirá algo en alguna parte. Además, la serie Agenda incluye productos que manejan datos especialmente sensibles, como el que identifica a la clientela habitual por reconocimiento facial.

Así que dividí la granularidad de la eliminación en cuatro niveles y la convertí en una regla compartida por toda la serie. Son: dar de baja un producto, eliminar un local, retirar una cuenta (salir de toda la serie) y una solicitud de eliminación de una persona del personal. Los niveles superiores se propagan en cascada a los inferiores, y cada producto registra su propio procedimiento de eliminación de datos en el sistema compartido. El plazo de gracia para la eliminación es de 30 días, y durante ese tiempo se puede deshacer.

A esto se suma un eje de tiempo. Los registros de asistencia, por ejemplo, deben conservarse por ley durante cinco años. Aunque un exintegrante del personal solicite la eliminación, dentro del período de conservación el registro debe mantenerse, con los nombres y similares anonimizados, en lugar de borrarse físicamente. Necesité decidir la línea entre "eliminar" y "conservar" cotejándola con la ley.

#### Un inicio de sesión de prueba para que la IA no contamine producción

Agregué a AgendaID un mecanismo más, para la IA: una entrada de inicio de sesión de prueba.

Para que la IA compruebe que las cosas funcionan, la IA tiene que iniciar sesión y operar las pantallas. Pero el inicio de sesión se hace con una cuenta de Google, así que la IA no puede iniciar sesión por sí sola. Y tampoco puedo entregarle a la IA la cuenta de quien dirige el local. Existe el peligro de que las pruebas de la IA contaminen los datos de producción.

Así que construí una entrada que emite cuentas sintéticas (perfiles ficticios de prueba) utilizables solo en el entorno de pruebas. No funciona en producción. La base de datos del entorno de pruebas es un proyecto separado de producción y contiene solo datos sintéticos. La IA inicia sesión por esta entrada, opera las pantallas y confirma que las cosas funcionan. Las cuentas de prueba se reconstruyen todos los días y las antiguas se eliminan.

Con esto, la IA puede hacer por sí sola incluso la comprobación final, en un entorno construido exactamente como producción, sin tocar producción.

### 4-4 La navegación común y el fracaso de la palabra "puerta de entrada"

Para que las personas usuarias puedan pasar desde cualquier producto a los demás, di a todos los productos un menú de navegación compartido. Es el camino que permite que quien dirige un bar y usa Fichajes haga una pregunta en la Guía de Soporte, o vaya a ver los otros cuadernos.

Detrás de esta navegación compartida hay una pequeña historia de fracaso.

En la primera versión, había puesto un enlace que decía "Volver a la puerta de entrada". Eso fue porque, internamente, yo llamaba a AgendaHub la "puerta de entrada". Pero al comprobarlo en un dispositivo real, algo no estaba bien. Dos enlaces, "Volver a la puerta de entrada" y "Ver la serie Agenda", saltaban al mismo lugar. Además, el enlace de soporte estaba por encima del menú del trabajo diario, así que el orden de importancia estaba al revés. Y, sobre todo, las palabras "puerta de entrada" no significan nada para quien usa el producto por primera vez. Era el lenguaje interno de quien lo hace.

Así que restablecí los principios. Ordenar los elementos según su cercanía al propósito de la persona usuaria: el trabajo diario en lo más alto, los enlaces que llevan hacia afuera en lo más bajo. Ni siquiera un enlace pensado para ganar nuevas personas usuarias va por encima del trabajo. El límite debe poder explicarse en una sola línea. Escribir los textos con las palabras de la persona usuaria, no con lenguaje interno. No poner nunca más de un enlace que salte al mismo lugar. Descarté "Volver a la puerta de entrada" y lo fusioné todo en un único enlace, "Ver los otros cuadernos Agenda".

En el Capítulo 2 escribí sobre aprender el lenguaje de la interfaz. Ese era el lenguaje que quien dirige el local usa para hablar con la IA. Este es lo opuesto: el lenguaje que quien hace el producto usa para hablar con la persona usuaria. En ambos casos se trataba de ajustar las palabras a la persona a quien uno le habla.

【Figura 4-4】La navegación compartida después de la corrección. El trabajo está arriba, y los enlaces que llevan hacia afuera están en lo más bajo *(La pantalla está en japonés.)*

### 4-5 La base cuesta US$ 35 por mes

El costo de base de datos de toda la base descrita en este capítulo es de unos US$ 35 por mes. El plan de pago que incluye el proyecto de producción cuesta US$ 25, y el proyecto del entorno de pruebas, US$ 10.

Tampoco esta era la cifra desde el principio. En un momento estaba pagando US$ 45 por mes. La base de datos de desarrollo de un producto de reconocimiento facial seguía cobrándose aunque no la estaba usando. La pasé al nivel gratuito y la detuve, eliminé otro proyecto que no usaba, y así llegué a la cifra actual.

También vigilo el costo de la IA. El trabajo de la IA que escribe programas se factura por la cantidad de tokens (la unidad de texto que la IA lee y escribe). Evito concentrar costos haciendo que la ventana de trabajo se limite al papel de coordinación y dejando la implementación misma a otra IA con un cupo de costo aparte. Para el modelo generativo de la ventana de chat también miro el precio y elijo lo necesario y suficiente. Aunque un modelo de nivel superior cueste solo US$ 1 más por mes, elijo preguntándome "¿es suficiente?"

Si se construye en pequeño, incluso unas ventas pequeñas bastan para sostenerse. La historia de monetización del Capítulo 3 se apoya en lo poco que cuesta esta base.

### 4-6 La IA coordinadora y la persona que decide

Por último, quiero describir la forma de mi jornada de trabajo.

Mantengo abiertas varias ventanas de trabajo de IA al mismo tiempo. Hay una ventana para el sistema de reservas, una ventana para cada producto y una ventana coordinadora que les envía instrucciones y reúne los resultados. A la ventana coordinadora la llamé AgendaRegia (el cuaderno de coordinación).

Quienes dictaminan, es decir, deciden "por qué camino ir", somos la IA del lado del chat y yo. La IA del chat encuentra de antemano los huecos y las contradicciones de las especificaciones, adjunta a cada una una decisión por defecto y las propone todas a la vez. Yo las leo y decido. Lo decidido se reúne en una hoja de instrucciones llamada Goal y se pega en la ventana de trabajo. Incluye aprobaciones por adelantado y condiciones de aceptación que una máquina puede juzgar. La ventana de trabajo la lee y sigue hasta el final, deteniéndose solo cuando algo falla.

También hago que la hoja de instrucciones incluya una estimación de cuándo estará terminado el trabajo. Encajo este trabajo entre los horarios de apertura del bar, así que si no sé cuánto tardará algo, no puedo planificar mi día.

El papel de quien dirige el local no es leer, sino decidir. No necesito leer los 1.775 registros de conversación. Respondo las preguntas sobre los hechos del bar. Dictamino sobre lo que solo puede decidir la política del bar. Después de que algo entra en servicio, lo toco personalmente cinco o seis veces para comprobar si algo se siente raro. Eso es todo.

Antes de llegar a esta forma, rehice el trabajo muchas veces. La IA agregaba funciones por su cuenta y las pantallas se volvían inestables. El trabajo crecía sin límite a partir de una sola instrucción. Esperar la aprobación en cada etapa hacía que nada avanzara. Cada vez agregué una regla, y así se llegó a la forma actual. Esto también sigue creciendo.

#### Lo que usted puede llevarse de este capítulo

- Para el trabajo repetido, convierta el procedimiento mismo en un documento y entréguelo a la IA. Si corrige el documento de procedimiento cada vez que falla, la próxima vez será más fácil
- Construya las partes comunes (inicio de sesión, cobro, navegación) una sola vez y reutilícelas en todos los productos. Si la base es pequeña, incluso unas ventas pequeñas bastan para sostenerse
- Las personas hacen solo el juicio y las operaciones que solo las personas pueden hacer. Si la IA le deriva cualquier otra tarea, agréguela al documento de procedimiento

La continuación de este capítulo (los próximos cuadernos que construiré y las lecciones que agregué al documento de procedimiento) está en note y X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Capítulo 5: El futuro de un bar pequeño

### 5-1 De Zatta Gohan a Tamuro

Entré en el mundo de la gastronomía a los 39 años.

El detonante fue un bar de barrio llamado Zatta. Una vez al mes, a veces cada dos semanas, me dejaban servir comidas allí. Durante mucho tiempo había aprendido a cocinar por mi cuenta, pero ahora tenía un lugar donde las personas comían mi comida y se alegraban. Esa fue mi experiencia fundacional.

En 2014, abrí en Arai-Yakushi un restaurante llamado Zatta Gohan. Era un local pequeño que servía comidas en menú fijo. Lo dirigí durante siete años.

Sin embargo, en Arai-Yakushi sentí un límite en la cantidad de clientela. Entonces encontré un local en Higashi-Nakano. Se llega caminando en menos de un minuto desde la salida este de la estación. Incluso en un día de lluvia, se llega sin mojarse mucho.

En noviembre de 2018, abrí allí Tamuro. "Tamuro" significa un lugar donde la gente se reúne. Tiene 11 asientos en la barra y 8 asientos de tatami, 19 en total. Durante tres años dirigí dos locales en paralelo, Arai-Yakushi y Higashi-Nakano. Durante la época de la COVID, mantener ambos se volvió difícil, así que cerré el local de Arai-Yakushi y me quedé solo con Tamuro.

#### El bar de curaduría

Tamuro se presenta como un "bar de curaduría".

Curaduría significa tener un ojo selectivo. Más que cocinar, quiero ejercer la curaduría. La comida, las bebidas, el ambiente del bar: lo hago todo seleccionando con ojo exigente. Eso es Tamuro.

Viajo a menudo para comer, tanto al extranjero como dentro de Japón. Vietnam, Camboya, Italia, Shanghái, Pekín, México. Recorrer lugares para comer es un placer y, al mismo tiempo, una manera de encontrar qué servir en Tamuro. Recreo ingredientes caros con ingredientes al alcance de la mano. Por ejemplo, si se seca yema de huevo y se ralla, se obtiene un sabor cercano a la bottarga. Pienso que este tipo de sustitución (localización) es mi papel.

Volví a estudiar cocina durante la época de la COVID. Tomé un curso de cocina francesa de ocho sesiones en total, y también asistí a un curso de cocina japonesa. Cómo manejar el umami y cómo controlar el fuego. Lo que aprendí allí es la base de mi cocina de hoy.

El menú de Tamuro se arma con cuatro entradas y un plato principal. Le doy una variedad de ingredientes para que la clientela que vive sola pueda comer muchas verduras. Lo armo de modo que los métodos de cocción (frito, en vinagre, estofado, a la parrilla) y los sabores (dulce, picante, ácido) no se superpongan. El plato más popular es el tonteki, el bistec de cerdo. Tiene una salsa ligeramente dulce hecha con salsa de soja de Kyushu, con mucho ajo.

#### Un lugar donde la gente se reúne

Cerca de la mitad de la clientela de Tamuro viene sola. Son principalmente personas de entre 30 y 50 años, y muchas son vecinas de Higashi-Nakano, pero también llegan personas de los alrededores de Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo y Eifukucho.

Lo que distingue al bar es cuánto conversa la clientela entre sí. Construí la barra para que sea fácil hablar con la persona de al lado, y yo o el personal decidimos los asientos juzgando quiénes se llevarán bien. Quienes vinieron solos a veces vuelven juntos más tarde. Como dice el nombre, se ha convertido en un lugar donde la gente se reúne. Publico el día a día del bar en [Instagram](https://www.instagram.com/tamuro.higashinakano/).

En el menú degustación que ofrezco más o menos una vez al mes, sirvo de siete a ocho platos a lo largo de dos o tres horas, junto con maridajes de vino. Cada mes cambia el tema: italiano, francés, japonés. Las clases de cocina son talleres de tres horas, y después de cocinar, todos brindan, comen y se van a casa. Está el aperitivo, que sirve vino y platos pequeños a primera hora de la tarde antes de abrir. Hay una barbacoa dos veces al año, más o menos. Hay una fiesta de fin de año una vez al año. Y está la fiesta del yukata de la que escribí en el Capítulo 1.

El sistema de reservas del que escribí en el Capítulo 1, la ventana de chat y MCP son todas herramientas para traer personas a este bar. La IA es un medio para reunir a la gente, no el objetivo.

### 5-2 El curry con hanbāgu de Quatre Épices

Tamuro es un bar nocturno. Durante el día, el local queda libre.

Aprovechando ese tiempo, empecé Quatre Épices en enero de 2024. Es un local de curry con hanbāgu que funciona solo a la hora del almuerzo en el mismo lugar, y lo atiende el personal.

Quatre Épices significa "cuatro especias" en francés. Fiel al nombre, en lugar de superponer muchas especias, las seleccionamos y las limitamos para que el perfil del sabor quede claro. El curry no lleva harina; se termina con la consistencia natural de las propias verduras y la carne. Satisfacción al terminar de comer, y ninguna pesadez en el estómago. Y armonía con el hanbāgu. Lo diseñé sobre esas tres premisas.

Somos exigentes con la cocción del hanbāgu. Fijamos la mezcla para que salga crujiente por fuera y esponjoso por dentro, y cocinamos de acuerdo con esa mezcla. El control del fuego que aprendí de noche en Tamuro sirve también al plato del mediodía.

Los precios, los días y los horarios pueden cambiar, así que consulte el Instagram de Tamuro (https://www.instagram.com/tamuro.higashinakano/) para ver la información más reciente.

Quatre Épices también tiene un comedor infantil en el mismo lugar. Es una actividad que aprovecha las instalaciones y las compras del bar existente para servir comidas a las niñas y los niños del barrio. A través de ese vínculo, también construimos una relación con el centro comunitario local. A veces servimos curry y sándwiches en eventos deportivos locales, eventos del centro comunitario y festivales de baile Bon (Bon Odori).

Con franqueza: aprovechar las horas del día no ha salido del todo bien. Organicé jornadas para tomar algo durante el día y alquilé el espacio a otras personas, pero la clientela no vino como yo esperaba. El atractivo del bar se percibe de manera distinta cuando está de noche quien lo dirige y cuando de día solo está el personal. Hacer crecer el local diurno con un atractivo diferente al del local nocturno sigue siendo una tarea inconclusa.

### 5-3 Bonta LLC: dos pilares

La pequeña empresa que dirige Tamuro y Quatre Épices es Bonta LLC. Yo ocupo su gerencia.

La empresa tiene dos pilares. Uno es la gastronomía: Tamuro y Quatre Épices. El otro es TI: el desarrollo de la serie Agenda y la consultoría.

La gastronomía y las herramientas difieren en cómo generan dinero. Sostener la empresa con dos pilares de naturaleza distinta es la forma que tengo en mente.

Y los dos pilares se suministran materiales entre sí. Los problemas del bar se convierten en semilla de una herramienta. Lo que aprendo construyendo herramientas vuelve a la gestión del bar. El Cuaderno de Luces nació de los cierres que se alargaban, y los registros de horario extendido del Cuaderno de Luces pasan a ser la base de las estimaciones de rentabilidad y de los turnos. Las "preguntas que no pudimos responder" que se acumulan en la ventana de chat mejoran la guía del bar. Este ciclo es la razón por la que puedo manejar yo solo tanto el bar como el desarrollo.

No pienso hacer la empresa más grande. En pequeño, en cantidad y a bajo precio. Esa es la forma de esta empresa.

### 5-4 Escribir como Raku Bonta

Cuando escribo y publico, uso el seudónimo "Raku Bonta". Este libro también lo escribí con ese nombre.

Mi libro anterior, *El subgerente de IA*, fue un libro sobre IA generativa. Ocupó el primer lugar en la categoría de gestión del tiempo de Amazon y lo leyeron muchas personas. Este libro es su continuación.

Además de libros, también escribo en note, una plataforma japonesa de publicación. Escribo sobre los esfuerzos del bar con la IA, lo que encontré en un viaje de aprendizaje, el avance de la publicación de mis libros y la serie Agenda. Puede seguir en note (https://note.com/bontallc) la continuación que no pude incluir en este libro.

Para mí, escribir es también una manera de poner en palabras tanto el bar como el desarrollo, y de comprobarlos. Como escribí en el Capítulo 1, la base de conocimiento inicial de la ventana de chat "T-AI-MURO" se construyó a partir de palabras que yo venía dejando en X. Lo que había escrito pasó a ser material para la IA. De ahora en adelante también, lo que escriba volverá tanto al bar como a la IA.

Hay una cosa más que he decidido sobre la escritura. No anuncio cosas inconclusas con un "próximamente". Lo termino, hago una página de presentación y solo entonces lo publico. Creo que mantener ese orden es lo que le gana la confianza a una empresa pequeña.

### 5-5 El futuro del local independiente

Por último, reuniré lo que escribí en este libro en una sola imagen.

【Figura 5-1】El panorama de lo que describe este libro. Un bar pequeño abre su propia ventana (la primera historia) y convierte sus problemas en herramientas para entregar a otros bares (la segunda historia) *(La pantalla está en japonés.)*

La clientela hará que su propia IA encuentre un bar y haga la reserva. En agosto de 2026 se hizo posible reservar restaurantes desde ChatGPT a través de un gran servicio de reservas. El punto de entrada se está trasladando de los buscadores y los sitios de reseñas gastronómicas a la IA de cada persona.

En ese momento, un bar que no figura en los grandes servicios de reservas es invisible para la IA. Pero aunque no se esté en los grandes servicios, hay un camino para que un bar se conecte directamente con la IA. Tamuro eligió ese camino abriendo una ventana llamada MCP. Un bar pequeño que abre por sí solo su propia ventana. Esa es la primera historia de este libro.

Quienes dirigen un bar podrán convertir sus propios problemas en herramientas y repartirlas a otros bares. El Cuaderno de Luces nació del problema de Tamuro, el de querer avisar que la hora de cierre se alargaría, y se puede usar en cualquier bar. El poder de construir está dejando de ser algo solo de ciertas personas o empresas. Quien dirige un bar pequeño pasa del lado que usa herramientas al lado que las construye y las distribuye. Esa es la segunda historia de este libro.

Lo que tienen en común las dos es que cuanto más pequeño es el bar, más definida puede ser su identidad.

Las grandes cadenas estandarizan sus sistemas para que cada sucursal ofrezca la misma calidad. Tamuro es lo opuesto. La clientela que viene sola es la mitad, casi el 90% de las reservas se hacen el mismo día y la clientela conversa entre sí. Para ajustarme a ese carácter de Tamuro, he construido con detalle el sistema de reservas, los descuentos y la ventana de chat. Precisamente porque no estandariza, destaca. Y porque destaca, se convierte en una razón para que la clientela lo elija.

Y cuanto más definida es la identidad del bar, más semillas de herramientas encuentra. Cuanto más se ahonda en el carácter del bar, más específicos se vuelven los problemas. Los problemas específicos se convierten en herramientas específicas. Las herramientas específicas ayudan a otros bares que tienen el mismo problema.

La IA ha hecho posible que una sola persona haga ambas cosas. Definir la identidad del bar y repartir herramientas. Antes había que elegir una u otra. Ahora se pueden hacer las dos.

Por supuesto, todavía es un trabajo en curso. La tasa de aprobación de la ventana de chat todavía se está elevando. El documento de procedimiento se amplía con cada fracaso. Cómo hacer crecer el local diurno sigue siendo un desafío. Las personas que reservan mediante la IA todavía no son muchas.

Aun así, creo que el futuro del bar pequeño es brillante. Ser pequeño no es una debilidad. Como somos pequeños, podemos probar rápido, descartar rápido y corregir rápido. Como somos pequeños, podemos tener una identidad definida. Y los problemas de un bar con identidad definida se convierten en herramientas y pasan a otros bares pequeños.

Escribí este libro desde un bar de 19 asientos en Higashi-Nakano.

## Epílogo

Gracias por leer hasta aquí.

Lo que escribí en este libro es un registro a octubre de 2026. Las herramientas de IA cambian de forma en cuestión de meses. Es posible que algunos de los mecanismos que describí ya hayan tomado otra forma para cuando se publique esto. Aun así, lo dejé por escrito, creyendo que un registro de qué construyó un bar pequeño con la IA y cómo, en qué fracasó y qué aprendió, debería seguir siendo útil por un tiempo.

La serie Agenda: https://bontallc.com/agenda?via=b2-es-{{FMT}}

Siga mis actividades: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Si alguna vez pasa por Higashi-Nakano, en Tokio, visite Tamuro. Puede reservar desde el sitio de reservas, mediante la ventana de chat "T-AI-MURO" del sitio o, por supuesto, a través de su propia IA.

Sitio de reservas de Tamuro: https://tamuroreservation.vercel.app/?src=b2-es-{{FMT}}

Instagram de Tamuro: https://www.instagram.com/tamuro.higashinakano/

Para quienes quieran intentar reservar desde la IA. La dirección de conexión del servidor MCP de Tamuro es la siguiente URL.

https://tamuroreservation.vercel.app/api/mcp

En los ajustes de su IA (como Claude o ChatGPT), abra la pantalla para agregar herramientas externas (conectores, servidores MCP) y registre esta URL. La forma de registrarla varía según la IA y con el tiempo, así que lo más seguro es buscar "MCP" o "conector" en la ayuda de cada IA. Según el plan que tenga, es posible que no pueda conectar un servidor MCP de su elección. Una vez registrada, pregúntele a su IA: "¿Hay lugar esta noche en Tamuro?". Revisará los horarios libres y los precios y lo guiará a la página de reservas. El botón de confirmar lo pulsa usted.

Para quienes lleguen después de leer el libro. Al reservar, ingrese el código de cupón "BOOK". Le serviremos una bebida de cortesía en su primera ronda. Si viene sin reserva, basta con decir "vi el libro" al hacer su primer pedido. Le serviremos igualmente una bebida de cortesía. Es un pequeño recurso que me permite contar cuántas personas vinieron por el libro.

Puede entrar sin reserva. Aun si viene a solas, no se sentirá fuera de lugar. Incluso puede terminar conversando animadamente con la persona de al lado.

Lo espero en Tamuro, un lugar donde la gente se reúne.

Raku Bonta

### Referencias

- OpenAI Help Center, "ChatGPT — Release Notes", 10 de agosto de 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (un ejemplo de servidor MCP en Estados Unidos que permite a la IA colocar órdenes de acciones y otros valores) https://docs.alpaca.markets/docs/alpaca-mcp-server
- El debate sobre la "muerte del SaaS": las declaraciones de Satya Nadella en el pódcast BG2 (diciembre de 2024), la fuerte caída de las acciones de software en febrero de 2026 y el nombre que recibió, y la refutación de Jensen Huang se tomaron de los siguientes reportajes y comentarios. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
