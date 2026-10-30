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
