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