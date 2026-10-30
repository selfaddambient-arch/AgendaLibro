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
