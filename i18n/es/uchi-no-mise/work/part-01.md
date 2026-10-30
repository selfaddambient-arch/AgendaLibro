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
