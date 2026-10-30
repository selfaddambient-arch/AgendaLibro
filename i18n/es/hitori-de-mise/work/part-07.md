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