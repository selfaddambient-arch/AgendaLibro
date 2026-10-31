El tema es Tamuro, el bar que dirijo de noche. Este nombre lleva un deseo profundo: "ser un lugar donde todo tipo de personas se reúnan con libertad y alegría (tamuro-suru, pasar el rato) en el barrio de Higashi-Nakano".

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
