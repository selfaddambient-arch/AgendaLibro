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
