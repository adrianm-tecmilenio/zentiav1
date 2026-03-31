#Que la segunda misión de cada fase sea una recomendación de skilling

RUTAS_PROMPT = r"""
##Contexto inicial:

- Eres un agente de Inteligencia Artificial que forma parte de una plataforma para darle acompañamiento a personas adultas que trabajan y quieren descubrir o evolucionar su propósito de vida, la plataforma se llama Zentia.

- Actúa como especialista en diseño educativo, comportamiento humano y bienestar, con enfoque en hábitos y cambio sostenible. Quiero que generes un reto personalizado de 21 días para una persona usuaria de Zentia a partir de su perfil. El objetivo del reto es ayudarle a dar pasos pequeños pero significativos que la acerquen a una meta personal relacionada con su propósito de vida, de forma sostenible, humana y emocionalmente conectada. 

##Instrucciones:
- Recibirás la siguiente lista de inputs:
    * Propósito de vida (proposito): es el propósito de vida del usuario, que te ayudará a generar misiones más personalizadas.
    * Arquetipo (arquetipo): es el arquetipo del usuario, puede ser "planeador", "fantasioso", "generalista" o "autonomo". Más adelante verás la descripción de cada arquetipo.
    * Meta personal (meta): es la meta personal del usuario, que te ayudará a generar misiones más personalizadas.
    * Preguntas (preguntas): recibirás preguntas y respuestas del usuario, que te ayudará a generar misiones más personalizadas. Estas preguntas nos indican como está el usuario en diferentes aspectos de su vida. Más adelante verás cada pregunta y sus posibles respuestas.

- Tu tarea principal es generar 3 fases con misiones diarias, cada fase debe tener:
    * Un nombre para la fase.
    * Un objetivo para la fase.
    * 7 misiones diarias en una arreglo de strings.
    * Una reflexión corta (máximo 100 palabras) sobre la fase, normalmente es una pregunta que te ayudará a reflexionar sobre la fase.
    * Una pregunta clave para la fase, que te ayudará a reflexionar sobre la fase.

- Genera cada fase de 7 días bajo esta narrativa: 
    * Fase 1: días 1 al 6 y el día 7 un checkpoint reflexivo, una pregunta que le ayude al usuario a reflexionar sobre la fase.
    * Fase 2: días 8 al 13 y el día 14 un checkpoint reflexivo, una pregunta que le ayude al usuario a reflexionar sobre la fase.
    * Fase 3: días 15 al 20 y el día 21 un checkpont reflexivo, una pregunta que le ayude al usuario a reflexionar sobre la fase.

- Recibirás 3 cursos de la plataforma "Skilling Center" que se han encontrado para el usuario de acuerdo a su información.

- Cada segunda misión de cada fase debe ser una recomendación de skilling como la siguiente:

{
    "nombre": "Conoce acerca de [tema del curso]",
    "descripcion": "Te invitamos a explorar y profundizar en [tema aquí].\n\n1. Primero, explora lo que quieras: un libro, un podcast o un video sobre el tema.\n2. Después, profundiza al revisar este curso del Skilling Center copiando y pegando el enlace en tu navegador: <a href='[enlace al curso del Skilling aquí]'> [enlace al curso del Skilling aquí] </a>\n3. Escribe en breve qué fue lo más interesante o valioso que encontraste.",
    "tipo": "textField",
    "tiempo": "10 minutos",
    "complejidad": "low"
}

IMPORTANTE: Aplica este formato para cada una de las 3 fases. La descripción es la misma para todas las fases. Incluye los saltos de línea en la descripción.

- El mensaje incluirá una lista de 3 cursos recomendados para el usuario, que contendrá el nombre del curso, el enlace entre otra información sobre cada curso.

- Cada misión (día) incluye: 
        - Nombre de la misión (Una acción concreta (con lenguaje accesible, sin tecnicismos))
        - Descripción de la misión
        - Tipo de misión (como se debe realizar la imagen), puede ser "textField", "imagen"
        - Tiempo de la misión
        - Complejidad de la misión

    * Una breve explicación si lo necesita 
    * Ejemplos o sugerencias para evitar que la persona se bloquee 
    * Lenguaje emocional acorde a su arquetipo y estilo de avance 

## Formato de entrada:
    # Recibirás los siguientes elementos:
    # - arquetipo: Te llegará como una palabra que describe el tipo de persona que es el usuario, puede ser "explorador", "alma" o "corazon".
    # - meta: Te llegará como una frase donde el usuario explica cuál es su meta personal.
    # - proposito: Te llegará como una frase donde el usuario describe su propósito de vida.
    # - preguntas: Te llegará como una lista de preguntas y respuestas del usuario, que te ayudará a generar misiones más personalizadas. Estas preguntas nos indican como está el usuario en diferentes aspectos de su vida. Más adelante verás cada pregunta y sus posibles respuestas.

## Descripción de los arquetipos:
    - Planeador (planeador): Te gusta tener claridad antes de avanzar. Valoras la estabilidad, planificas con cuidado y cumples lo que te propones. Tu orden y constancia son grandes aliados, aunque a veces te limites por buscar demasiada estructura.
    - Fantasioso (fantasioso): Te mueve el propósito y la pasión. Tienes muchas ideas e inspiración, aunque a veces se quedan en el aire. Tu fuerza está en imaginar lo posible; tu reto es dar pasos concretos sin perder tu esencia.
    - Generalista (generalista): Te interesa todo y te gusta aprender de muchas cosas. Eres flexible, curioso/a y ves conexiones únicas. A veces te cuesta enfocarte, pero tu variedad es una fortaleza cuando logras integrarla.
    - Autónomo (autónomo): Buscas libertad y hacer las cosas a tu modo. Te motiva la independencia financiera y tomar decisiones propias. Actúas con rapidez y enfoque, aunque a veces rechaces estructuras que podrían ayudarte.

## Preguntas y posibles respuestas:
    - ¿Qué tan capaz te sientes de identificar cómo te sientes cuando enfrentas un conflicto interpersonal?
    A) No logro reconocer cómo me siento
    B) Difícilmente logro reconocer mis emociones
    C) Sí logro identificar mis emociones en la mayoría de ocasiones
    D) Siempre puedo reconocer mis emociones incluso en situaciones difíciles

    - ¿Te despiertas sintiéndote descansado/a la mayoría de los días?
    A) Sí
    B) No

    - ¿Tu situación financiera te permite hacer planes a mediano plazo (3 años o más)?
    A) Sí
    B) No

    - ¿Qué tan satisfecho/a estás hoy con tu situación financiera actual?
    A) Nada satisfecho
    B) Poco satisfecho
    C) Medianamente satisfecho
    D) Muy satisfecho

    - ¿Tienes claridad sobre a qué te quieres dedicar laboralmente?
    A) Sí
    B) No

    - ¿Crees que tu vida tiene una razón de ser más allá de lo cotidiano?
    A) Verdadero
    B) Falso

    - ¿Tus actividades y relaciones contribuyen al bienestar de otras personas?
    A) Totalmente en desacuerdo
    B) Parcialmente en desacuerdo
    C) En desacuerdo
    D) De acuerdo
    E) Totalmente de acuerdo

    - Si pudieras avanzar con constancia hacia algo que realmente te importa… ¿Hacia qué meta o propósito te gustaría empezar a caminar?
    A) Conseguir un mejor trabajo
    C) Subir de puesto o crecer dentro de mi empleo actual
    D) Encontrar mi vocación o un rumbo profesional claro
    E) Tener independencia financiera
    F) Explorar nuevas fuentes de ingreso
    G) Equilibrar mi vida personal y profesional
    H) Otro (especifica)
"""

RUTAS_USER_PROMPT = """
Información de usuario:
{user_info}

Cursos:
{cursos}
"""

MISION_PROMPT = """
##Contexto inicial:

- Eres un agente de Inteligencia Artificial que forma parte de una plataforma para darle acompañamiento a personas adultas que trabajan y quieren descubrir o evolucionar su propósito de vida, la plataforma se llama Zentia.

- Actúa como especialista en diseño educativo, comportamiento humano y bienestar, con enfoque en hábitos y cambio sostenible. Quiero que generes una misión personalizada para una persona usuaria de Zentia a partir de su perfil. El objetivo de la misión es ayudarle a dar pasos pequeños pero significativos que la acerquen a una meta personal relacionada con su propósito de vida, de forma sostenible, humana y emocionalmente conectada. 

##Instrucciones:
- Recibirás la siguiente lista de inputs:
    * Propósito de vida (proposito): es el propósito de vida del usuario, que te ayudará a generar misiones más personalizadas.
    * Arquetipo (arquetipo): es el arquetipo del usuario, puede ser "planeador", "fantasioso", "generalista" o "autonomo". Más adelante verás la descripción de cada arquetipo.
    * Meta personal (meta): es la meta personal del usuario, que te ayudará a generar misiones más personalizadas.
    * Preguntas (preguntas): recibirás preguntas y respuestas del usuario, que te ayudará a generar misiones más personalizadas. Estas preguntas nos indican como está el usuario en diferentes aspectos de su vida. Más adelante verás cada pregunta y sus posibles respuestas.

- Tu tarea principal es generar una misión personalizada para el usuario.

- La misión incluye: 
        - Nombre de la misión (Una acción concreta (con lenguaje accesible, sin tecnicismos))
        - Descripción de la misión
        - Tipo de misión (como se debe realizar la imagen), puede ser "textField", "imagen"
        - Tiempo de la misión
        - Complejidad de la misión

## Descripción de los arquetipos:
    - Planeador (planeador): Te gusta tener claridad antes de avanzar. Valoras la estabilidad, planificas con cuidado y cumples lo que te propones. Tu orden y constancia son grandes aliados, aunque a veces te limites por buscar demasiada estructura.
    - Fantasioso (fantasioso): Te mueve el propósito y la pasión. Tienes muchas ideas e inspiración, aunque a veces se quedan en el aire. Tu fuerza está en imaginar lo posible; tu reto es dar pasos concretos sin perder tu esencia.
    - Generalista (generalista): Te interesa todo y te gusta aprender de muchas cosas. Eres flexible, curioso/a y ves conexiones únicas. A veces te cuesta enfocarte, pero tu variedad es una fortaleza cuando logras integrarla.
    - Autónomo (autónomo): Buscas libertad y hacer las cosas a tu modo. Te motiva la independencia financiera y tomar decisiones propias. Actúas con rapidez y enfoque, aunque a veces rechaces estructuras que podrían ayudarte.



"""

NEW_RUTAS_PROMPT = """
Eres el Agente Planificador de Zentia.

Tu tarea es generar un plan de 8 semanas (2 meses) para ayudar a una persona a avanzar hacia el objetivo profesional que seleccionó en la app. El plan debe ser claro, práctico y ejecutable.

IMPORTANTE:
- En el mensaje del usuario recibirás un bloque llamado OBJECTIVE_SPECS_ACTIVO.
- Usa OBJECTIVE_SPECS_ACTIVO como guía principal para definir el enfoque del plan.
- Nunca menciones “OBJECTIVE_SPECS”, “PDF”, “diccionario” ni fuentes internas en tu respuesta final.

REGLAS DE ESTILO (obligatorias):
- Lenguaje claro y sencillo; evita palabras complicadas.
- Usa “habilidades y conocimientos” (no uses la palabra “competencias”).
- Instrucciones paso a paso, accionables y directas (“Haz esto”, “Escribe”, “Envía”, “Agenda”).
- Acciones pequeñas y realistas: 15-50 minutos por día.
- Continuidad explícita entre días (“Retoma…”, “Usa lo que hiciste ayer…”).
- Acciones visibles y activas (conversaciones, entregables, decisiones, exposición).
- La reflexión y el propósito de vida siempre conectados a una acción concreta el mismo día.
- Cuando haya retroalimentación, especifica a quién pedirla, qué preguntar y cuál es el entregable resultante.

REGLAS DE ESTRUCTURA (fijas):
- 2 meses (Mes 1 y Mes 2)
- 8 semanas (Semana 1 a Semana 8)
- 5 días por semana (Día 1 a Día 5)
- Cada día debe tener: tiempo (15-50 min), instrucciones (2-6 bullets), entregable (1 frase concreta)

FORMATO DE SALIDA (OBLIGATORIO):
Debes responder ÚNICAMENTE con un objeto JSON válido (sin markdown, sin explicaciones, sin texto extra).
El JSON debe seguir EXACTAMENTE este esquema:

{
  "titulo": "Plan de trabajo · ...",
  "subtitulo": "Adaptado al perfil de ...",
  "objetivo_seleccionado": "...",
  "meses": [
    {
      "numero": 1,
      "titulo": "...",
      "resultado_mes": "...",
      "semanas": [
        {
          "numero": 1,
          "titulo": "...",
          "resultado_semana": "...",
          "habilidades_conocimientos": ["...", "..."],
          "dias": [
            {
              "numero": 1,
              "tiempo_estimado_min": 20,
              "instrucciones": ["...", "..."],
              "entregable": "..."
            }
          ]
        }
      ]
    },
    {
      "numero": 2,
      "titulo": "...",
      "resultado_mes": "...",
      "semanas": [ ... semanas 5 a 8 ... ]
    }
  ]
}

REGLAS DE VALIDACIÓN (no las menciones, solo cúmplelas):
- meses debe tener exactamente 2 elementos.
- Mes 1 debe contener semanas 1 a 4.
- Mes 2 debe contener semanas 5 a 8.
- Cada semana debe contener exactamente 5 días (1 a 5).
- tiempo_estimado_min debe ser entero entre 15 y 50.
- habilidades_conocimientos debe tener 1 a 3 elementos.
- instrucciones debe tener 2 a 6 bullets, todos accionables.
- entregable debe ser concreto y verificable.

OUTPUT:
Devuelve solo JSON válido y nada más.
"""

OBJECTIVE_SPECS = {
    "cambiar de trabajo por uno más alineado conmigo": {
        "objective_id": 1,
        "entry_profile": {
            "estado_general": "Insatisfacción con el trabajo actual, con motivación mezclada con bloqueo; quiere algo distinto pero le cuesta convertirlo en acciones concretas.",
            "como_se_percibe": [
                "Se siente desconectada entre lo que hace y lo que le importa.",
                "Duda de sus fortalezas reales y del rol donde podría aportar más valor.",
                "Ve el cambio laboral como deseable pero abrumador o lejano."
            ],
            "comportamientos_habituales": [
                "Piensa en cambiar, pero posterga decisiones.",
                "Consume información (vacantes, contenido, consejos) sin convertirlo en plan.",
                "Reacciona desde urgencia o cansancio más que desde una visión clara."
            ]
        },
        "exit_profile": {
            "estado_general": "Gana claridad, confianza y dirección; entiende qué busca y tiene un plan de acción realista para avanzar.",
            "como_se_percibe": [
                "Se reconoce como protagonista activa de su cambio profesional.",
                "Identifica qué tipo de trabajo se alinea con propósito/valores/habilidades.",
                "Se siente más segura al decidir incluso con incertidumbre."
            ],
            "comportamientos_observables": [
                "Convierte reflexión en hábitos semanales concretos.",
                "Evalúa oportunidades con criterios propios.",
                "Da pasos consistentes: networking intencional, actualizar CV, explorar roles alineados."
            ]
        },
        "skills_knowledge_outcomes": [
            "Definir un objetivo profesional claro y con sentido personal (qué busca, por qué y para qué).",
            "Tener claridad estratégica sobre su transición (qué cambiar y qué conservar: rol/industria/cultura/forma de trabajo).",
            "Diseñar hábitos profesionales pequeños y sostenibles conectados a una intención clara.",
            "Gestionar activamente el cambio laboral con acciones concretas (explorar, preparar, conectar oportunidades)."
        ]
    },

    "crecer y subir de nivel en mi rol actual": {
        "objective_id": 2,
        "entry_profile": {
            "estado_general": "Se siente competente pero estancada; quiere crecer dentro de la organización, sin claridad total de qué significa subir de nivel ni cómo hacerlo visible.",
            "como_se_percibe": [
                "Responsable y comprometida, pero poco estratégica.",
                "Duda si su esfuerzo está siendo visto/valorado.",
                "Insegura sobre si tiene las habilidades para el siguiente nivel."
            ],
            "comportamientos_habituales": [
                "Cumple tareas bien, pero opera en modo ejecución.",
                "Espera feedback/reconocimiento para validar si va bien.",
                "Aprende de forma reactiva (cuando surge un problema)."
            ]
        },
        "exit_profile": {
            "estado_general": "Entiende qué significa subir de nivel en su contexto y construye un plan concreto para desarrollar habilidades y hacer visible su valor.",
            "como_se_percibe": [
                "Agente activo de su crecimiento.",
                "Identifica fortalezas, áreas de oportunidad e impacto.",
                "Más seguridad al asumir retos y conversaciones profesionales."
            ],
            "comportamientos_observables": [
                "Convierte intención de crecer en hábitos semanales.",
                "Actúa con intención estratégica, no solo operativa.",
                "Busca y usa retroalimentación; toma iniciativa en proyectos/conversaciones/aprendizajes."
            ]
        },
        "skills_knowledge_outcomes": [
            "Definir qué significa crecer en su rol, alineado a propósito/valores/etapa y expectativas de su organización.",
            "Leer estratégicamente su rol y el contexto organizacional (qué se valora para el siguiente nivel).",
            "Diseñar hábitos de crecimiento (acción + reflexión + aprendizaje continuo) conectados al propósito.",
            "Gestionar su desarrollo de forma visible: pedir feedback, comunicar avances, tomar iniciativa progresiva."
        ]
    },

    "empezar o fortalecer un proyecto propio": {
        "objective_id": 3,
        "entry_profile": {
            "estado_general": "Tiene idea/proyecto temprano pero se siente dispersa o insegura; le cuesta sostener avances y decidir con claridad.",
            "como_se_percibe": [
                "Creativa y con iniciativa, pero duda del rumbo.",
                "Entusiasmo intermitente + miedo al error/fracaso.",
                "Dificultad para priorizar entre ideas/responsabilidades."
            ],
            "comportamientos_habituales": [
                "Avanza irregularmente (rachas + pausas).",
                "Planea más de lo que ejecuta.",
                "Cambia enfoque sin validar aprendizajes.",
                "Depende de la motivación emocional para avanzar."
            ]
        },
        "exit_profile": {
            "estado_general": "Gana claridad, foco y confianza; define prioridades y avanza sostenidamente con hábitos alineados al propósito y a la etapa del proyecto.",
            "como_se_percibe": [
                "Creadora activa de su camino profesional.",
                "Confía más en su criterio; aprende del error.",
                "Ve el proyecto como proceso, no como prueba de valor personal."
            ],
            "comportamientos_observables": [
                "Traduce visión en acciones semanales concretas.",
                "Prioriza decisiones clave sobre tareas accesorias.",
                "Ejecuta, evalúa y ajusta con intención.",
                "Sostiene avances aunque la motivación fluctúe."
            ]
        },
        "skills_knowledge_outcomes": [
            "Definir el sentido del proyecto alineado a propósito/valores/habilidades/etapa vital.",
            "Definir foco y prioridades realistas según etapa (idea/validación/fortalecimiento).",
            "Diseñar hábitos emprendedores sostenibles (ejecución, aprendizaje, visibilidad) conectados a intención.",
            "Tomar decisiones con autonomía, experimentar y ajustar sin paralizarse."
        ]
    },

    "mejorar mi estabilidad y organización financiera": {
        "objective_id": 4,
        "entry_profile": {
            "estado_general": "Estrés o desorden financiero; cubre lo inmediato pero sin visión clara ni sistema; tema financiero desconectado del propósito y metas.",
            "como_se_percibe": [
                "Reactiva frente al dinero más que intencional.",
                "Ve finanzas como problema aislado.",
                "Duda de su capacidad para sostener hábitos financieros."
            ],
            "comportamientos_habituales": [
                "Control parcial o inexistente de ingresos/gastos.",
                "Decisiones desde urgencia, emoción o evitación.",
                "Buenas intenciones sin acciones sostenibles."
            ]
        },
        "exit_profile": {
            "estado_general": "Más claridad, calma y dirección; entiende dinero como herramienta para lo que quiere construir y tiene un plan de acción realista.",
            "como_se_percibe": [
                "Protagonista de su estabilidad financiera.",
                "Dinero al servicio de su bienestar/valores.",
                "Capaz de decidir alineado a propósito."
            ],
            "comportamientos_observables": [
                "Convierte reflexión en acciones financieras concretas.",
                "Ejecuta hábitos financieros con intención clara.",
                "Da seguimiento y ajusta su plan."
            ]
        },
        "skills_knowledge_outcomes": [
            "Describir su situación financiera con claridad y conectarla con valores/prioridades.",
            "Identificar emociones/creencias sobre el dinero y gestionarlas para actuar mejor.",
            "Diseñar hábitos financieros pequeños conectados a un plan (no hábitos aislados).",
            "Construir un plan de acción financiero a corto/mediano plazo y sostenerlo."
        ]
    },

    "lograr un mejor equilibrio entre trabajo y vida personal": {
        "objective_id": 5,
        "entry_profile": {
            "estado_general": "Siente que el trabajo ocupa demasiado; cansancio/saturación; se siente siempre disponible; no sabe qué ajustar ni cómo sostener cambios.",
            "como_se_percibe": [
                "Sobrepasada por demandas laborales.",
                "Poco control del tiempo/energía.",
                "Equilibrio como ideal difícil."
            ],
            "comportamientos_habituales": [
                "Extiende horarios laborales.",
                "Prioriza trabajo sobre bienestar.",
                "Confunde disponibilidad con compromiso."
            ]
        },
        "exit_profile": {
            "estado_general": "Define cómo quiere vivir su tiempo/energía; entiende que equilibrio es decidir mejor; sostiene límites, hábitos y decisiones alineadas a propósito.",
            "como_se_percibe": [
                "Más agencia sobre su tiempo.",
                "Prioriza bienestar sin culpa.",
                "Ve el equilibrio como construcción consciente."
            ],
            "comportamientos_observables": [
                "Límites claros entre trabajo y vida personal.",
                "Hábitos de descanso/conexión/recuperación.",
                "Plan de acción personal que ajusta según su realidad."
            ]
        },
        "skills_knowledge_outcomes": [
            "Definir qué es equilibrio para su etapa, conectado a propósito (recuperación = sostenibilidad).",
            "Gestionar tiempo/energía con intención e identificar señales de saturación.",
            "Diseñar hábitos de recuperación en 3 niveles: mini (día), medio (semanal), macro (periódico).",
            "Construir un plan sostenible de equilibrio que prioriza energía, no solo tiempo."
        ]
    },

    "aún no lo tengo claro": {
        "objective_id": 6,
        "alias": "clarificar mi siguiente paso profesional",
        "entry_profile": {
            "estado_general": "Pausa/confusión/transición; siente que algo no encaja; cansancio mental o emocional; presión por tener claridad.",
            "como_se_percibe": [
                "Capaz, pero desorientada.",
                "Duda de su criterio para decidir.",
                "Percibe presión externa por 'tener claridad'."
            ],
            "comportamientos_habituales": [
                "Da vueltas a las mismas preguntas sin concluir.",
                "Evita decidir por miedo a equivocarse.",
                "Consume contenido inspiracional sin acción.",
                "Se compara con otros y aumenta confusión."
            ]
        },
        "exit_profile": {
            "estado_general": "Recupera claridad/calma/dirección; aunque no tenga respuesta definitiva, tiene hipótesis claras y criterio para explorar sin bloqueo.",
            "como_se_percibe": [
                "Se ve en proceso (no 'perdida').",
                "Confía más en explorar y decidir.",
                "Normaliza la incertidumbre como parte del desarrollo."
            ],
            "comportamientos_observables": [
                "Explora opciones con intención y criterio.",
                "Convierte reflexión en acciones pequeñas constantes.",
                "Toma microdecisiones y ajusta rumbo con lo aprendido."
            ]
        },
        "skills_knowledge_outcomes": [
            "Autoconciencia profesional y emocional aplicada (identificar energía, motivación, desgaste).",
            "Explorar propósito como brújula (marco orientador, no restrictivo) para decisiones.",
            "Diseñar un proceso estructurado de exploración con experimentos pequeños.",
            "Tomar decisiones progresivas con menor bloqueo (microdecisiones sin esperar certeza absoluta)."
        ]
    }
}

#Ejemplos de planes sobre objetivos
'''
OBJECTIVE_EXAMPLES = {
    "cambiar de trabajo por uno más alineado conmigo": {
    "titulo": "Plan de acción · Cambiar de trabajo por uno más alineado conmigo",
    "subtitulo": "Ruta estratégica personalizada para cambiar de trabajo por uno más alineado conmigo",
    "objetivo_seleccionado": "Cambiar de trabajo por uno más alineado conmigo",
    "meses": [
        {
            "numero": 1,
            "titulo": "Fase de Análisis y Definición",
            "resultado_mes": "Lograr los objetivos de la fase inicial para Cambiar de trabajo por uno más alineado conmigo.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Entender tu situación actual",
                    "resultado_semana": "Entender tu situación actual",
                    "habilidades_conocimientos": [
                        "Autoconocimiento laboral y capacidad de tomar decisiones conscientes."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi día bajo la lupa",
                                "Escribe:",
                                "- Qué haces actualmente.",
                                "- En qué se va la mayor parte de tu energía.",
                                "👉 Agrega:",
                                "Marca con ⚡ lo que te da energía.",
                                "Marca con 🪫 lo que te la quita."
                            ],
                            "entregable": "Registro de: Mi día bajo la lupa"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Lo que quiero conservar vs lo que ya no",
                                "Lee lo que escribiste antes o agrega al menos una idea nueva basada en lo que has vivido recientemente.",
                                "Haz dos listas:",
                                "- Lo que quiero conservar.",
                                "- Lo que no quiero repetir.",
                                "👉 Agrega:",
                                "Elige SOLO 1 cosa que esta semana puedes empezar a hacer diferente.",
                                "Ejemplo:",
                                "- Delegar algo pequeño.",
                                "- Decir no a una reunión innecesaria.",
                                "- Organizar tu día distinto."
                            ],
                            "entregable": "Registro de: Lo que quiero conservar vs lo que ya no"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Micro-valentía en acción",
                                "Haz ese pequeño cambio que seleccionaste anteriormente.",
                                "Si no lo hiciste, elige uno más simple y ejecútalo hoy."
                            ],
                            "entregable": "Registro de: Micro-valentía en acción"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Aprender del movimiento",
                                "Escribe:",
                                "¿Qué pasó cuando hice ese cambio?",
                                "¿Qué aprendí sobre mí?",
                                "Si no hiciste el cambio, responde:",
                                "¿Qué me detuvo? ¿Qué haré distinto esta vez?"
                            ],
                            "entregable": "Registro de: Aprender del movimiento"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Si no cambio...",
                                "Completa:",
                                "“Si sigo exactamente en este trabajo un año más, mi vida se vería ___”.",
                                "Responde pensando en tu situación actual."
                            ],
                            "entregable": "Registro de: Si no cambio..."
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Diseñar tu siguiente versión profesional",
                    "resultado_semana": "Diseñar tu siguiente versión profesional",
                    "habilidades_conocimientos": [
                        "Capacidad de visualizar y definir escenarios profesionales deseados."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi día ideal, con detalles",
                                "Describe tu día laboral ideal:",
                                "- Horario",
                                "- Tipo de tareas",
                                "- Nivel de autonomía",
                                "- Ambiente",
                                "- Nivel de presión",
                                "Hazlo concreto.",
                                "Realiza esta actividad sin revisar lo anterior, luego compáralo con tu versión pasada."
                            ],
                            "entregable": "Registro de: Mi día ideal, con detalles"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Los dos cambios clave",
                                "Elige máximo 2 cambios principales:",
                                "- Puesto",
                                "- Industria",
                                "- Modalidad",
                                "- Cultura",
                                "Justifica por qué."
                            ],
                            "entregable": "Registro de: Los dos cambios clave"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Personas que ya están donde yo quiero",
                                "Busca 3 perfiles reales en LinkedIn de personas que tengan algo parecido a lo que quieres.",
                                "Analiza:",
                                "- Qué hacen",
                                "- Qué habilidades mencionan",
                                "- Cómo describen su trabajo"
                            ],
                            "entregable": "Registro de: Personas que ya están donde yo quiero"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Camino visible",
                                "Retoma los perfiles de LinkedIn que elegiste.",
                                "Escribe:",
                                "¿Qué pasos dieron que tú podrías dar?",
                                "Nota: Puedes elegir solo un paso concreto y pequeño."
                            ],
                            "entregable": "Registro de: Camino visible"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Primer acercamiento profesional",
                                "Envía una solicitud de conexión breve y clara.",
                                "No tiene que ser perfecto."
                            ],
                            "entregable": "Registro de: Primer acercamiento profesional"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Alinear el cambio con tu propósito de vida",
                    "resultado_semana": "Alinear el cambio con tu propósito de vida",
                    "habilidades_conocimientos": [
                        "Capacidad de tomar decisiones profesionales alineadas a valores y propósito."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "El impacto que quiero generar",
                                "Escribe:",
                                "¿Qué impacto quiero generar con mi trabajo en los próximos 5 años?",
                                "No en el mundo. En tu entorno real.",
                                "Escríbelo como si empezaras desde cero."
                            ],
                            "entregable": "Registro de: El impacto que quiero generar"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mis valores no negociables",
                                "Haz una lista de 5 valores importantes para ti.",
                                "Marca los que no estás viviendo hoy."
                            ],
                            "entregable": "Registro de: Mis valores no negociables"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Coherencia o contradicción",
                                "Responde:",
                                "¿Mi trabajo actual honra mis valores?",
                                "Explica por qué sí o por qué no."
                            ],
                            "entregable": "Registro de: Coherencia o contradicción"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Cambio con sentido",
                                "Completa esta frase:",
                                "“Quiero cambiar de trabajo para poder ___”."
                            ],
                            "entregable": "Registro de: Cambio con sentido"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Mi filtro profesional",
                                "Escribe tu “Filtro de decisión profesional”:",
                                "Ejemplo:",
                                "No acepto trabajos donde:",
                                "- No pueda aprender.",
                                "- El ambiente sea tóxico.",
                                "- No haya autonomía.",
                                "Esto será tu brújula."
                            ],
                            "entregable": "Registro de: Mi filtro profesional"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Definir tu objetivo claro y medible",
                    "resultado_semana": "Definir tu objetivo claro y medible",
                    "habilidades_conocimientos": [
                        "Capacidad de definir y explicar un objetivo claro."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Tres versiones de mi meta",
                                "Escribe 3 versiones distintas de tu objetivo.",
                                "Ejemplo:",
                                "- En 3 meses quiero haber aplicado a 10 vacantes.",
                                "- En 4 meses quiero tener entrevistas activas.",
                                "- En 6 meses quiero estar en un rol X."
                            ],
                            "entregable": "Registro de: Tres versiones de mi meta"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Elijo y afino",
                                "Revisa las versiones de tu objetivo de la actividad anterior.",
                                "Elige una y hazla medible (con fecha o cantidad)."
                            ],
                            "entregable": "Registro de: Elijo y afino"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Emoción como indicador",
                                "Retoma el objetivo elegido.",
                                "Escribe qué emoción te genera y si esa emoción te da energía o te frena.",
                                "Si no te mueve, ajústala."
                            ],
                            "entregable": "Registro de: Emoción como indicador"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Señales de avance",
                                "Define:",
                                "¿Qué tendría que pasar en los próximos 30 días para saber que estoy avanzando?"
                            ],
                            "entregable": "Registro de: Señales de avance"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Compromiso conmigo",
                                "Escribe un compromiso contigo:",
                                "“Durante los próximos 30 días me comprometo a ___”.",
                                "Vuelve a leer tu objetivo y propósito de vida, si es necesario actualízalo para que estén alineados antes de continuar."
                            ],
                            "entregable": "Registro de: Compromiso conmigo"
                        }
                    ]
                }
            ]
        },
        {
            "numero": 2,
            "titulo": "Fase de Implementación y Crecimiento",
            "resultado_mes": "Lograr los objetivos de la fase avanzada para Cambiar de trabajo por uno más alineado conmigo.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Explorar trabajos reales",
                    "resultado_semana": "Explorar trabajos reales",
                    "habilidades_conocimientos": [
                        "Interpretar el mercado laboral y detectar oportunidades reales."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "El mercado habla",
                                "Busca cinco ofertas de trabajo que se parezcan a lo que quieres.",
                                "Revisa tus actividades anteriores, objetivo y propósito de vida si lo necesitas."
                            ],
                            "entregable": "Registro de: El mercado habla"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Patrones que se repiten",
                                "Retoma las ofertas encontradas.",
                                "Anota habilidades y requisitos que se repitan."
                            ],
                            "entregable": "Registro de: Patrones que se repiten"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "La habilidad estratégica",
                                "Identifica una habilidad que te ayudaría a acercarte a esos trabajos.",
                                "Reflexiona: ¿Es una habilidad que tengo o que debo desarrollar?"
                            ],
                            "entregable": "Registro de: La habilidad estratégica"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Plan de mejora:",
                                "Decide una forma concreta de empezar a practicar esa habilidad esta semana.",
                                "Busca cursos, artículos, apoyo con un amigo o colega."
                            ],
                            "entregable": "Registro de: Plan de mejora:"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Haciendo visible mi nueva dirección",
                                "Publica en LinkedIn una reflexión profesional alineada con tu nuevo rumbo.",
                                "Revisa tus actividades anteriores, objetivo y propósito de vida si lo necesitas."
                            ],
                            "entregable": "Registro de: Haciendo visible mi nueva dirección"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Retroalimentación estratégica",
                    "resultado_semana": "Retroalimentación estratégica",
                    "habilidades_conocimientos": [
                        "Capacidad de recibir retroalimentación y usarla para mejorar."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Eligiendo mi espejo profesional",
                                "Elige:",
                                "- Un jefe actual o anterior.",
                                "- Un compañero o compañera de trabajo de confianza."
                            ],
                            "entregable": "Registro de: Eligiendo mi espejo profesional"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Preguntando con intención",
                                "Revisa nuevamente a las personas seleccionadas en la actividad anterior.",
                                "Pídeles retroalimentación sobre ti:",
                                "Por ejemplo:",
                                "-“Estoy reflexionando sobre cómo seguir creciendo profesionalmente y quiero entender mejor mis fortalezas y roles donde pueda aportar más valor.”",
                                "- \"Desde lo que has visto de mí, ¿en qué tipo de entornos o responsabilidades crees que brillo más?\"",
                                "Revisa tus actividades anteriores, objetivo y propósito de vida si lo necesitas antes de contactar a alguien."
                            ],
                            "entregable": "Registro de: Preguntando con intención"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Escucha sin edición",
                                "Después de tu retroalimentación, escribe lo que te dijeron tal como lo expresaron.",
                                "Si no has podido llevar a cabo esta acción, puedes:",
                                "1. Pedir micro-feedback (una sesión breve con 2 preguntas específicas)",
                                "2. Ofrecer la opción asincrónica (un espacio en línea de 10 a 15 minutos)"
                            ],
                            "entregable": "Registro de: Escucha sin edición"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Detectando patrones",
                                "Revisa las notas que tomaste de la sesión de retroalimentación.",
                                "Busca ideas que se repitan en lo que te dijeron en la retroalimentación."
                            ],
                            "entregable": "Registro de: Detectando patrones"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Ajuste estratégico",
                                "Ajusta tu plan y objetivos con base en la información recabada en la retroalimentación."
                            ],
                            "entregable": "Registro de: Ajuste estratégico"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Exposición real",
                    "resultado_semana": "Exposición real",
                    "habilidades_conocimientos": [
                        "Acción, visibilidad y avance real hacia el cambio."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Actualización de mi narrativa profesional",
                                "Actualiza tu CV y/o perfil profesional para que refleje el trabajo que buscas.",
                                "Puedes empezar por actualizar el encabezado y resumen profesional, recuerda: pequeño avance > perfección."
                            ],
                            "entregable": "Registro de: Actualización de mi narrativa profesional"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Declaro hacia dónde voy",
                                "Escribe en tu perfil profesional un mensaje corto donde expliques:",
                                "- Qué tipo de trabajo buscas.",
                                "- Por qué te interesa."
                            ],
                            "entregable": "Registro de: Declaro hacia dónde voy"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Activando mi red",
                                "Envía ese mensaje a dos o tres contactos profesionales que te puedan acercar al trabajo que te gustaría conseguir."
                            ],
                            "entregable": "Registro de: Activando mi red"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Postulación consciente",
                                "Postúlate a una oferta de trabajo alineada con tu objetivo."
                            ],
                            "entregable": "Registro de: Postulación consciente"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Ensayo de entrevista",
                                "Practica una simulación de entrevista para tus posulaciones.",
                                "Graba tus respuestas en video 10 min."
                            ],
                            "entregable": "Registro de: Ensayo de entrevista"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Cerrar y decidir el siguiente paso",
                    "resultado_semana": "Cerrar y decidir el siguiente paso",
                    "habilidades_conocimientos": [
                        "Autonomía para seguir avanzando en tu transición laboral."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Mis cinco aprendizajes clave",
                                "Escribe cinco aprendizajes importantes que has vivido durante esta experiencia."
                            ],
                            "entregable": "Registro de: Mis cinco aprendizajes clave"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Antes y después",
                                "Describe cómo veías tu cambio laboral al inicio de la experiencia y cómo lo ves ahora."
                            ],
                            "entregable": "Registro de: Antes y después"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "El siguiente movimiento",
                                "Define el siguiente paso concreto que vas a dar.",
                                "Revisa tus actividades, objetivo y propósito de vida si lo necesitas."
                            ],
                            "entregable": "Registro de: El siguiente movimiento"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Plan de acción a corto plazo:",
                                "Agenda en tu calendario 3 acciones específicas para los próximos 30 días.",
                                "Especifica:",
                                "Fecha",
                                "Hora",
                                "Acción concreta",
                                "Revisa tus actividades anteriores, objetivo y propósito de vida si lo necesitas antes de escribir el plan."
                            ],
                            "entregable": "Registro de: Plan de acción a corto plazo:"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Nivel de alineación",
                                "Escribe qué tan alineado o alineada te sientes hoy con el camino que estás tomando."
                            ],
                            "entregable": "Registro de: Nivel de alineación"
                        }
                    ]
                }
            ]
        }
    ]
},
"crecer y subir de nivel en mi rol actual": {
    "titulo": "Plan de acción · Crecer y subir de nivel en mi rol actual",
    "subtitulo": "Ruta estratégica personalizada para crecer y subir de nivel en mi rol actual",
    "objetivo_seleccionado": "Crecer y subir de nivel en mi rol actual",
    "meses": [
        {
            "numero": 1,
            "titulo": "Fase de Análisis y Definición",
            "resultado_mes": "Lograr los objetivos de la fase inicial para Crecer y subir de nivel en mi rol actual.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Definir qué significa \"subir de nivel\" en tu rol actual",
                    "resultado_semana": "Definir qué significa \"subir de nivel\" en tu rol actual",
                    "habilidades_conocimientos": [
                        "Autoconocimiento profesional y lectura del contexto organizacional."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "¿Qué significa subir de nivel para mí?",
                                "Escribe:",
                                "- ¿Qué entiendo por crecer en mi rol?",
                                "- ¿Más responsabilidad? ¿Más sueldo? ¿Más impacto? ¿Más liderazgo?",
                                "Ejemplo:",
                                "\"Subir de nivel para mí significa liderar/atender proyectos y no solo ejecutarlos\".",
                                "\"Subir de nivel para mí significa tomar decisiones\"."
                            ],
                            "entregable": "Registro de: ¿Qué significa subir de nivel para mí?"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Cómo se crece aquí",
                                "Escribe:",
                                "- ¿Cómo han crecido otras personas en mi área o profesión?",
                                "- ¿Qué hicieron diferente?",
                                "- ¿Qué habilidades desarrollaron?",
                                "Si no tienes referentes directos:",
                                "- Observa perfiles en tu sector.",
                                "- Piensa en colegas que admires.",
                                "- Recuerda casos dentro de tu entorno profesional.",
                                "No dependas solo de LinkedIn. Puedes usar:",
                                "- Conversaciones informales.",
                                "- Experiencias pasadas.",
                                "- Referentes públicos del sector."
                            ],
                            "entregable": "Registro de: Cómo se crece aquí"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Expectativas reales",
                                "Escribe:",
                                "- ¿Qué se espera de alguien que está un nivel arriba en mi área?",
                                "- ¿Qué resultados entrega?",
                                "- ¿Qué problemas resuelve?",
                                "Si no lo tienes claro:",
                                "Anota lo que supones hoy."
                            ],
                            "entregable": "Registro de: Expectativas reales"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Mi rol actual bajo análisis",
                                "Haz 2 listas:",
                                "- Lo que hago bien hoy.",
                                "- Lo que todavía no hago pero debería dominar.",
                                "Usa ejemplos concretos.",
                                "Ejemplos:",
                                "Gestión del tiempo",
                                "Comunicación clara",
                                "Manejo de clientes/pacientes",
                                "Documentación técnica",
                                "Seguimiento de procesos"
                            ],
                            "entregable": "Registro de: Mi rol actual bajo análisis"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi definición de crecimiento",
                                "Redacta una frase clara:",
                                "\"Subir de nivel para mí significa _ y lo quiero lograr porque _\".",
                                "Conecta esta frase con tu objetivo y propósito de vida declarado. Si no se alinean, ajústalos."
                            ],
                            "entregable": "Registro de: Mi definición de crecimiento"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Reconocer tu impacto real en tu rol",
                    "resultado_semana": "Reconocer tu impacto real en tu rol",
                    "habilidades_conocimientos": [
                        "Identificación de fortalezas y comunicación de valor."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Mi impacto visible",
                                "Escribe 5 resultados concretos que hayas generado.",
                                "Ejemplo:",
                                "Casos resueltos",
                                "Procesos mejorados",
                                "Clientes satisfechos",
                                "Pacientes atendidos con calidad",
                                "Proyectos entregados",
                                "Conflictos solucionados",
                                "TIP: Si no tienes números exactos, describe el impacto cualitativo."
                            ],
                            "entregable": "Registro de: Mi impacto visible"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Historias de logro",
                                "Elige 2 logros, ya sea que los hayas descrito en la actividad anterior o que quieras seleccionar nuevos, y descríbelos usando la metodología STAR:",
                                "- Situación",
                                "- Tarea",
                                "- Acción",
                                "- Resultado",
                                "Revisa la metodología STAR si no la conoces."
                            ],
                            "entregable": "Registro de: Historias de logro"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Fortalezas clave",
                                "Retoma tus logros.",
                                "Identifica 3 fortalezas que se repiten.",
                                "Ejemplos:",
                                "Organización",
                                "Resolución de problemas",
                                "Empatía",
                                "Liderazgo"
                            ],
                            "entregable": "Registro de: Fortalezas clave"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Lo que otros ven en mí",
                                "Pregunta a:",
                                "- Colega",
                                "- Cliente",
                                "- Socio",
                                "- Compañero/a",
                                "- Líder",
                                "Pregunta:",
                                "“¿En qué consideras que aporto más valor?”",
                                "Si no puedes hablar con alguien, escribe:",
                                "“Lo que creo que otros valoran de mí es ___.”"
                            ],
                            "entregable": "Registro de: Lo que otros ven en mí"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi propuesta de valor interna",
                                "Escribe un párrafo:",
                                "\"Mi valor dentro del equipo / organización / área es _ porque _\".",
                                "Integra tu percepción y lo que otros mencionaron (si hubo conversación)."
                            ],
                            "entregable": "Registro de: Mi propuesta de valor interna"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Definir qué habilidades necesitas desarrollar",
                    "resultado_semana": "Definir qué habilidades necesitas desarrollar",
                    "habilidades_conocimientos": [
                        "Planeación estratégica de desarrollo profesional, priorización, traducción de expectativas a acciones."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Mapa del siguiente nivel",
                                "- Piensa en alguien (real o ideal) que esté más avanzado en tu profesión.",
                                "- Escribe 5 cosas que esa persona hace diferente (acciones, no cualidades).",
                                "- Para cada punto, anota un ejemplo concreto.",
                                "Ejemplo",
                                "Presenta avances con datos",
                                "Lleva un reporte semanal de métricas",
                                "Organiza su día con herramientas como planner",
                                "Se comunica con mayor precisión",
                                "[Herramienta sugerida: lista Hace/Entrega/Decide (3 columnas)]"
                            ],
                            "entregable": "Registro de: Mapa del siguiente nivel"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Comparación honesta",
                                "Retoma tu \"Mapa del siguiente nivel\".",
                                "Haz una tabla con 3 columnas:",
                                "- Lo que hago hoy (sí/no)",
                                "- Evidencia (ejemplo real)",
                                "- Qué mejorar (una idea)",
                                "Marca solo 3 cosas como \"faltantes importantes\"."
                            ],
                            "entregable": "Registro de: Comparación honesta"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Una prioridad estratégica",
                                "- Elige 1 habilidad/área que, si la mejoras, te acercaría más al siguiente nivel.",
                                "- Escríbela: \"Quiero mejorar _ para lograr _\".",
                                "- Define cómo se ve en la práctica (2 comportamientos observables).",
                                "Ejemplo:",
                                "\"Mejorar comunicación\" -> \"Enviar avances semanales + pedir decisiones claras\".",
                                "[Herramienta sugerida: regla 80/20 (elige lo que más mueve resultados)."
                            ],
                            "entregable": "Registro de: Una prioridad estratégica"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Plan de desarrollo en micro-acciones",
                                "Retoma tu \"definición de crecimiento\".",
                                "Genera un plan de 30 días con lo siguiente:",
                                "Define 4 micro-acciones (1 por semana) que puedas hacer en tu trabajo real.",
                                "Pon fecha tentativa en tu calendario.",
                                "Ejemplo:",
                                "Mejorar documentación técnica.",
                                "Solicitar retroalimentación mensual.",
                                "Liderar un pequeño proyecto.",
                                "Organizar mejor mis tiempos.",
                                "[Herramienta sugerida: WOOP (Deseo, Obstáculo, Plan) para anticipar frenos.]"
                            ],
                            "entregable": "Registro de: Plan de desarrollo en micro-acciones"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Compromiso visible",
                                "Elige 1 opción:",
                                "A. Escribe una nota para ti: \"Mi foco a 30 días es _ y hoy empiezo con _\".",
                                "B. Manda un mensaje breve a alguien de confianza: \"Estoy trabajando en _ este mes. Si ves oportunidades para practicarlo juntos, avísame\".",
                                "A quién pedirlo:",
                                "Un compañero/a, mentor, líder (puede ser lateral, no necesariamente superior).",
                                "El objetivo es crear compromiso, no conseguir respuesta"
                            ],
                            "entregable": "Registro de: Compromiso visible"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Preparar y practicar una conversación de crecimiento",
                    "resultado_semana": "Preparar y practicar una conversación de crecimiento",
                    "habilidades_conocimientos": [
                        "Comunicación profesional, autogestión de carrera y negociación de expectativas."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Guión de crecimiento",
                                "Escribe 6 líneas, una por punto:",
                                "1. Quiero crecer hacia: _",
                                "2. Porque para mí significa: _",
                                "3. Mi valor hoy es: _",
                                "4. Estoy trabajando en: _ (tu plan a corto plazo)",
                                "5. Me gustaría más oportunidades en: _",
                                "6. Una forma concreta de demostrarlo sería: _",
                                "[Herramienta sugerida: estructura \"Situación > Acción > Petición\"]"
                            ],
                            "entregable": "Registro de: Guión de crecimiento"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Simulación express",
                                "- Practica tu guión en voz alta (3 min).",
                                "- Grábate (audio o video) y escúchate una vez.",
                                "- Ajusta 2 frases para que suenen más claras.",
                                "TIP: si no quieres grabarte, practica frente al espejo 2 veces."
                            ],
                            "entregable": "Registro de: Simulación express"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Pregunta clave",
                                "Elige una persona:",
                                "Líder",
                                "Colega senior",
                                "Mentor",
                                "\"¿Qué tendría que mejorar para asumir mayor responsabilidad en esta área?\"",
                                "TIP: Redacta la pregunta y guárdala lista para compartirla cuando surja el momento."
                            ],
                            "entregable": "Registro de: Pregunta clave"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Captura de aprendizajes",
                                "- Escribe lo que escuchaste (literal o aproximado).",
                                "- Marca 1 señal clara: \"Esto esperan\".",
                                "- Marca 1 decisión: \"Esto voy a hacer\".",
                                "Si no pudiste hablar con nadie, escribe: \"Lo que creo que esperan + mi decisión\".",
                                "[Herramienta sugerida: \"Hechos / Interpretación / Próximo paso\".]"
                            ],
                            "entregable": "Registro de: Captura de aprendizajes"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Ajuste de ruta",
                                "- Retoma tu plan de 30 días.",
                                "- Ajusta solo 1 cosa: micro-acción, fecha, evidencia.",
                                "- Define tu \"siguiente acción\" en 10 palabras.",
                                "Ejemplo: \"Enviaré un update semanal con métricas cada viernes\"."
                            ],
                            "entregable": "Registro de: Ajuste de ruta"
                        }
                    ]
                }
            ]
        },
        {
            "numero": 2,
            "titulo": "Fase de Implementación y Crecimiento",
            "resultado_mes": "Lograr los objetivos de la fase avanzada para Crecer y subir de nivel en mi rol actual.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Convertir tu plan de crecimiento en acciones visibles dentro de tu trabajo real",
                    "resultado_semana": "Convertir tu plan de crecimiento en acciones visibles dentro de tu trabajo real",
                    "habilidades_conocimientos": [
                        "Disciplina profesional, ejecución estratégica y generación de evidencia."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Primera evidencia real",
                                "- Retoma tu plan de 30 días.",
                                "- Elige la primera micro-acción.",
                                "- Ejecútala hoy o deja programado el primer paso concreto si lo no has hecho.",
                                "Ejemplo: \"Enviar un correo con propuesta de mejora\", \"Llevar métricas a la reunión semanal\"."
                            ],
                            "entregable": "Registro de: Primera evidencia real"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Documento mi avance",
                                "- Escribe qué hiciste.",
                                "- Qué resultado tuvo.",
                                "- Qué aprendiste",
                                "TIP: Usa una nota fija tipo \"Registro de crecimiento\"."
                            ],
                            "entregable": "Registro de: Documento mi avance"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Un 1% mejor",
                                "- Identifica una mejora pequeña sobre lo que hiciste.",
                                "- Ajusta algo para hacerlo mejor la próxima vez.",
                                "Ejemplo: \"Mejorar claridad en mi entregable\", \"Llegar con datos más concretos\"."
                            ],
                            "entregable": "Registro de: Un 1% mejor"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Señal de liderazgo",
                                "- Detecta un problema pequeño en tu área.",
                                "- Escribe una propuesta breve (máximo media página).",
                                "- Compártela con el equipo o con quien corresponda.",
                                "No se necesita una reunión formal, puede ser un correo."
                            ],
                            "entregable": "Registro de: Señal de liderazgo"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi semana en 5 líneas",
                                "Escribe:",
                                "- Qué hice diferente esta semana.",
                                "- Qué impacto generé.",
                                "- Qué quiero mejorar la siguiente."
                            ],
                            "entregable": "Registro de: Mi semana en 5 líneas"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Hacer visible tu valor",
                    "resultado_semana": "Hacer visible tu valor",
                    "habilidades_conocimientos": [
                        "Comunicación estratégica y posicionamiento interno."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Haciendo visible mi avance",
                                "Elige una forma natural de mostrar resultados:",
                                "- Un correo de seguimiento.",
                                "- Un mensaje en canal de equipo/clientes/socios.",
                                "- Un breve update en reunión.",
                                "Enfócate en hechos, no en elogios.",
                                "Ejemplo: \"Esta semana implementé _ y logramos _\"."
                            ],
                            "entregable": "Registro de: Haciendo visible mi avance"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Evidencia con datos",
                                "Revisa tus acciones de semana anteriores.",
                                "Agrega números o indicadores simples.",
                                "Ejemplo:",
                                "- Tiempo reducido.",
                                "- Errores disminuidos.",
                                "- Respuesta más rápida."
                            ],
                            "entregable": "Registro de: Evidencia con datos"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Retroalimentación específica",
                                "Pregunta a un colega directo: \"¿Qué podría hacer diferente para aportar más al equipo?\""
                            ],
                            "entregable": "Registro de: Retroalimentación específica"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Decisión de ajuste",
                                "De la retroalimentación recibida anteriormente, elige 1 cosa concreta para mejorar esta semana."
                            ],
                            "entregable": "Registro de: Decisión de ajuste"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Actuar como el siguiente nivel",
                                "Pregúntate:",
                                "\"Si ya estuviera en el siguiente nivel, ¿cómo actuaría hoy?",
                                "Haz una acción alineada a esa respuesta."
                            ],
                            "entregable": "Registro de: Actuar como el siguiente nivel"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Consolidar hábitos que te posicionen en el siguiente nivel",
                    "resultado_semana": "Consolidar hábitos que te posicionen en el siguiente nivel",
                    "habilidades_conocimientos": [
                        "Autogestión profesional y liderazgo personal."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Anticipación estratégica",
                                "Detecta algo que pueda salir mal en tu área.",
                                "Propon una solución antes de que ocurra."
                            ],
                            "entregable": "Registro de: Anticipación estratégica"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mejor decisión autónoma",
                                "Toma una decisión que normalmente esperarías que otro tome.",
                                "Hazlo con responsabilidad."
                            ],
                            "entregable": "Registro de: Mejor decisión autónoma"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Delegar o facilitar",
                                "Identifica una tarea que puedes:",
                                "- Delegar mejor.",
                                "- Explicar con mayor claridad.",
                                "- Estandarizar.",
                                "Trabaja en ello hoy."
                            ],
                            "entregable": "Registro de: Delegar o facilitar"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Revisión de impacto",
                                "Escribe:",
                                "- ¿Estoy actuando distinto que hace un mes?",
                                "- ¿Qué cambios son visibles?"
                            ],
                            "entregable": "Registro de: Revisión de impacto"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi narrativa interna",
                                "Escribe:",
                                "\"Hoy me veo como alguien que _\".",
                                "Esto fortalece tu identidad profesional."
                            ],
                            "entregable": "Registro de: Mi narrativa interna"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Cerrar el ciclo con claridad y dejar un plan sostenible",
                    "resultado_semana": "Cerrar el ciclo con claridad y dejar un plan sostenible",
                    "habilidades_conocimientos": [
                        "Autonomía profesional y visión estratégica."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Evidencia acumulada",
                                "Revisa tus notas de las últimas semanas.",
                                "Haz una lista de:",
                                "- Acciones ejecutadas.",
                                "- Resultados visibles.",
                                "- Conversaciones importantes."
                            ],
                            "entregable": "Registro de: Evidencia acumulada"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Antes vs ahora",
                                "Escribe:",
                                "- Cómo veías tu crecimiento al inicio de la experiencia.",
                                "- Cómo lo ves ahora."
                            ],
                            "entregable": "Registro de: Antes vs ahora"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Meta a 90 días",
                                "Define:",
                                "- Qué quieres haber logrado en 3 meses.",
                                "- Qué acciones seguirás haciendo."
                            ],
                            "entregable": "Registro de: Meta a 90 días"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Calendario estratégico",
                                "Agenda en tu calendario:",
                                "- 3 acciones concretas.",
                                "- Incluye la fecha y la hora.",
                                "TIP: No más de 3 para que sea alcanzable y realista."
                            ],
                            "entregable": "Registro de: Calendario estratégico"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Nivel de alineación",
                                "Evalúa del 1 al 10:",
                                "- Qué tan alineado/a estás con tu crecimiento.",
                                "- Que tan alineado/a estás con tu propósito de vida actual.",
                                "- Qué necesitas ajustar.",
                                "Escribe en una frase final:",
                                "\"Mi siguiente paso concreto es _\".",
                                "Revisa tu objetivo, propósito declarados, tu plan de acción y ajústalos si es necesario."
                            ],
                            "entregable": "Registro de: Nivel de alineación"
                        }
                    ]
                }
            ]
        }
    ]
},
"empezar o fortalecer un proyecto propio": {
    "titulo": "Plan de acción · Empezar o fortalecer un proyecto propio",
    "subtitulo": "Ruta estratégica personalizada para empezar o fortalecer un proyecto propio",
    "objetivo_seleccionado": "Empezar o fortalecer un proyecto propio",
    "meses": [
        {
            "numero": 1,
            "titulo": "Fase de Análisis y Definición",
            "resultado_mes": "Lograr los objetivos de la fase inicial para Empezar o fortalecer un proyecto propio.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Definir o redefinir con claridad qué estás construyendo y por qué",
                    "resultado_semana": "Definir o redefinir con claridad qué estás construyendo y por qué",
                    "habilidades_conocimientos": [
                        "Pensamiento estratégico, claridad de propuesta de valor y enfoque emprendedor."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi proyecto en una frase",
                                "Escribe tu 'Value Proposition Statement':",
                                "\"Mi proyecto consiste en _ para ayudar a _ a lograr _\".",
                                "Ejemplo:",
                                "\"Mi proyecto consiste en asesoría legal para pequeñas empresas que necesitan contratos claros\".",
                                "[Herramientas sugeridas: Propuesta de valor (Value Proposition Canvas), investiga cómo definir claramente problema, solución y beneficio]"
                            ],
                            "entregable": "Registro de: Mi proyecto en una frase"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "El problema real y urgente",
                                "Pensando en tu proyecto. Escribe:",
                                "- ¿Qué problema específico resuelve?",
                                "- ¿Qué tan urgente es?",
                                "- ¿Qué pasa si no lo resuelven?",
                                "Ejemplo:",
                                "\"No tener asesoría fiscal clara puede generar multas o pérdidas económicas\".",
                                "[Herramienta sugerida: Job To Be Done (JTBD), investiga cómo identificar qué trabajo contrata el cliente]"
                            ],
                            "entregable": "Registro de: El problema real y urgente"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Mi ventaja diferencial",
                                "Pensando en tu proyecto. Responde:",
                                "- ¿Por qué alguien elegiría mi propuesta?",
                                "- ¿Qué hago diferente?",
                                "Si tu proyecto ya está activo, identifica qué dicen tus clientes cuando te recomiendan.",
                                "[Herramienta sugerida: Análisis FODA (fortalezas, oportunidades, debilidades, amenazas)"
                            ],
                            "entregable": "Registro de: Mi ventaja diferencial"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Mi motivación real",
                                "Responde:",
                                "- Este proyecto ¿me acerca a la vida profesional que quiero?",
                                "- ¿Es coherente con mis valores y propósito de vida?",
                                "Si no está alineado, ajusta el enfoque o tu propósito."
                            ],
                            "entregable": "Registro de: Mi motivación real"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Versión mínima viable o mejora clave",
                                "Define:",
                                "- Si vas iniciando: ¿Cuál es la versión más simple con la que puedo empezar?",
                                "- Si ya tienes proyecto: ¿Qué mejora pequeña generaría mayor impacto?",
                                "[Herramienta sugerida: Lean Startup - MVP (Producto Mínimo Viable]"
                            ],
                            "entregable": "Registro de: Versión mínima viable o mejora clave"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Confirmar que el mercado necesita lo que ofreces",
                    "resultado_semana": "Confirmar que el mercado necesita lo que ofreces",
                    "habilidades_conocimientos": [
                        "Escucha activa, validación de mercado y ajuste de propuesta."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Perfil del cliente",
                                "Define:",
                                "- Tipo de persona",
                                "- Problema principal",
                                "- Capacidad de pago",
                                "- Motivación",
                                "[Herramienta sugerida: Buyer persona]"
                            ],
                            "entregable": "Registro de: Perfil del cliente"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Análisis simple de competencia",
                                "Busca:",
                                "- ¿Quién ofrece algo similar?",
                                "- ¿Qué hacen bien?",
                                "- ¿Qué podría hacer mejor?",
                                "[Herramienta sugerida: Análisis comparativo simple en tabla]"
                            ],
                            "entregable": "Registro de: Análisis simple de competencia"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Conversación exploratoria",
                                "Habla con 1 persona real.",
                                "Preguntas para presentarle:",
                                "1. ¿Qué problema enfrentas en _?",
                                "2. ¿Cómo lo solucionas hoy?",
                                "No vendas, solo escucha.",
                                "Si ya tienes clientes, habla con uno actual.",
                                "[Herramienta sugerida: Técnica de entrevista abierta (preguntas abiertas, no dirigir respuestas)]"
                            ],
                            "entregable": "Registro de: Conversación exploratoria"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Aprendizajes clave",
                                "Después de tu conversación exploratoria. Escribe:",
                                "- Lo que confirmé",
                                "- Lo que debo ajustar",
                                "- Lo que no sabía"
                            ],
                            "entregable": "Registro de: Aprendizajes clave"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Ajuste estratégico",
                                "Reescribe tu propuesta inicial incorporando lo aprendido."
                            ],
                            "entregable": "Registro de: Ajuste estratégico"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Organizar tu proyecto para que no dependa solo de motivación",
                    "resultado_semana": "Organizar tu proyecto para que no dependa solo de motivación",
                    "habilidades_conocimientos": [
                        "Organización, gestión básica de negocio y planeación."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Modelo de ingresos claro",
                                "Como primer acercamiento, responde:",
                                "- ¿Cómo gano dinero?",
                                "- ¿Precio por servicio?",
                                "- ¿Suscipción?",
                                "- ¿Proyecto?",
                                "[Herramienta sugerida: Business Model Canvas (bloque de ingresos y clientes)]"
                            ],
                            "entregable": "Registro de: Modelo de ingresos claro"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Estructura básica de costos",
                                "Revisa tus respuestas anteriores sobre el modelo de ingresos claro y, a continuación, enlista:",
                                "- Herramientas",
                                "- Tiempo invertido",
                                "- Gastos operativos",
                                "[Herramienta sugerida: Business Model Canvas (bloque de ingresos y clientes)]"
                            ],
                            "entregable": "Registro de: Estructura básica de costos"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Bloques de trabajo fijos",
                                "Agenda, por lo menos, 2 espacios semanales dedicados al proyecto.",
                                "[Herramienta sugerida: Time Blocking (bloques de tiempo en calendario)]"
                            ],
                            "entregable": "Registro de: Bloques de trabajo fijos"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Plan a corto plazo en micro-acciones",
                                "Define 4 acciones estratégicas para llevarlas a cabo en los siguientes 30 días.",
                                "Ejemplo:",
                                "- Conseguir 2 clientes",
                                "- Mejorar la propuesta comercial",
                                "- Ajustar precio",
                                "- Crear material base",
                                "[Herramienta sugerida: WOOP (deseo, obstáculo, plan)]"
                            ],
                            "entregable": "Registro de: Plan a corto plazo en micro-acciones"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Compromiso visible",
                                "Escribe o comparte tu foco del mes."
                            ],
                            "entregable": "Registro de: Compromiso visible"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Hacer visible tu proyecto",
                    "resultado_semana": "Hacer visible tu proyecto",
                    "habilidades_conocimientos": [
                        "Comunicación, marca personal y confianza profesional."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Mensaje claro y breve",
                                "Redacta de forma breve en un borrador:",
                                "- Qué haces",
                                "- Para quién",
                                "- Qué problema resuelves",
                                "- Cómo te contactan"
                            ],
                            "entregable": "Registro de: Mensaje claro y breve"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Perfil profesional actualizado",
                                "Actualiza tu bio, LinkedIn o presentación profesional con lo que escribiste anteriormente.",
                                "Puedes revisar otros perfiles profesionales para encontrar inspiración."
                            ],
                            "entregable": "Registro de: Perfil profesional actualizado"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Primera publicación o contacto",
                                "Comparte tu proyecto o escribe a 1 posible cliente."
                            ],
                            "entregable": "Registro de: Primera publicación o contacto"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Registro de resultados",
                                "Después de compartir tu proyecto, anota:",
                                "- ¿Qué dijieron exactamente?",
                                "- ¿Que emoción noté?",
                                "- ¿Qué me pidieron?",
                                "- ¿Qué duda surgió?",
                                "Después responde: ¿Qué puedo mejorar en mi mensaje y oferta?",
                                "Si no obtuviste respuesta en 48-72 horas:",
                                "No lo tomes como fracaso, es información.",
                                "Responde:",
                                "- ¿Mi mensaje fue claro?",
                                "- ¿Hice una pregunta concreta o solo informé?",
                                "- ¿Facilité una acción sencilla? (ej. agendar llamada)",
                                "- ¿Esta persona realmente es mi cliente ideal?",
                                "Después define una acción:",
                                "Ajustar el mensaje, Simplificar la propuesta, Contactar a otra persona, Cambiar el canal (WhatsApp, llamada, correo)",
                                "[Herramienta sugerida: Ciclo Buil-Measure-Learn (Lean Startup) -> Construyo, Mido, Aprendo, Ajusto]"
                            ],
                            "entregable": "Registro de: Registro de resultados"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Iteración estratégica",
                                "Retoma lo que escribiste en la actividad anterior y define una mejora concreta:",
                                "- Cambiar mensaje",
                                "- Ajustar público",
                                "- Simplificar oferta",
                                "- Modificar precio",
                                "Escríbelo así:",
                                "\"Voy a probar _ durante los próximos 7 días.\"",
                                "Ejemplo: Voy a hacer el mensaje más específico y añadir una pregunta directa.",
                                "[Herramienta sugerida: Ciclo Buil-Measure-Learn (Lean Startup) -> Construyo, Mido, Aprendo, Ajusto]"
                            ],
                            "entregable": "Registro de: Iteración estratégica"
                        }
                    ]
                }
            ]
        },
        {
            "numero": 2,
            "titulo": "Fase de Implementación y Crecimiento",
            "resultado_mes": "Lograr los objetivos de la fase avanzada para Empezar o fortalecer un proyecto propio.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Instalar estructura mínima para que el proyecto no dependa solo de motivación",
                    "resultado_semana": "Instalar estructura mínima para que el proyecto no dependa solo de motivación",
                    "habilidades_conocimientos": [
                        "Gestión del tiempo, prioridad estratégica y disciplina sostenida."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Bloques de construcción",
                                "Agenda, al menos, 2 bloques semanales dedicados al proyecto (mínimo 45 min cada uno).",
                                "Si ya los tenías agendados por las actividades anteriores, refuerza los tiempos dedicados para comenzar a construir.",
                                "Ejemplo:",
                                "Martes 7:00 - 7:45 am",
                                "Sábado 10:00 - 10:45 am",
                                "[Herramienta sugerida: Time Blocking, Google calendar, agenda física]"
                            ],
                            "entregable": "Registro de: Bloques de construcción"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Lista estratégica de prioridades",
                                "Escribe 10 tareas pendientes del proyecto.",
                                "Luego:",
                                "- Marca solo 3 importantes.",
                                "- Elige 1 prioritaria.",
                                "[Herramienta sugerida: Matriz Eisenhower (Urgente/Importante)]"
                            ],
                            "entregable": "Registro de: Lista estratégica de prioridades"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Entrega mínima semanal",
                                "Produce algo concreto:",
                                "- Documento base",
                                "- Guía",
                                "- Presentación",
                                "- Ajuste de oferta",
                                "No buscamos perfección, es una entrega mínima visible.",
                                "[Herramienta sugerida: Concepto MVP continuo]"
                            ],
                            "entregable": "Registro de: Entrega mínima semanal"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Revisión de frenos",
                                "Para volverte consciente de tus bloqueos y evitar repetir patrones de procastinación, escribe:",
                                "- ¿Qué me detuvo esta semana?",
                                "- Es miedo, falta de tiempo o falta de claridad?",
                                "Define 1 ajuste."
                            ],
                            "entregable": "Registro de: Revisión de frenos"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Ritual de cierre semanal",
                                "Para mantener una mentalidad de mejora continua. Escribe:",
                                "- ¿Qué avancé?",
                                "- ¿Qué aprendí?",
                                "- ¿Qué haré primero la próxima semana?"
                            ],
                            "entregable": "Registro de: Ritual de cierre semanal"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Revisar si el proyecto es viable y sostenible",
                    "resultado_semana": "Revisar si el proyecto es viable y sostenible",
                    "habilidades_conocimientos": [
                        "Pensamiento financiero básico, Evaluación estratégica y toma de decisiones racional."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Ingreso real o proyectado",
                                "Responde lo siguiente:",
                                "- ¿Cuánto quiero generar?",
                                "- ¿Cuántos clientes necesito?",
                                "- ¿Es realista?",
                                "[Herramienta sugerida: Cálculo simple: Ingreso deseado / Precio por servicio]"
                            ],
                            "entregable": "Registro de: Ingreso real o proyectado"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Costo invisible",
                                "Enlista los costos que implica tu proyecto:",
                                "- Tiempo invertido",
                                "- Energía",
                                "- Recursos",
                                "¿Está compensado?"
                            ],
                            "entregable": "Registro de: Costo invisible"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Ajuste de precio o propuesta",
                                "Evalúa si tu precio y propuesta reflejan valor:",
                                "- ¿Mi precio refleja valor?",
                                "- ¿Estoy cobrando demasiado bajo?",
                                "Haz una pequeña mejora.",
                                "[Herramienta sugerida: Comparación simple con mercado]"
                            ],
                            "entregable": "Registro de: Ajuste de precio o propuesta"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Sistema simple de seguimiento",
                                "Es importante instalar un hábito de gestión.",
                                "Para ello, crea una tabla sencilla con los siguientes elementos para dar seguimiento:",
                                "Cliente | Estado | Próximo paso",
                                "[Herramienta sugerida: Excel o Notion básico]"
                            ],
                            "entregable": "Registro de: Sistema simple de seguimiento"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Decisión de sostenibilidad",
                                "Responde lo siguiente basado en tu proyecto y lo que sabes hasta ahora:",
                                "- ¿Quiero crecer?",
                                "- ¿Quiero mantener?",
                                "- ¿Quiero ajustar el modelo?",
                                "Escribe una decisión clara."
                            ],
                            "entregable": "Registro de: Decisión de sostenibilidad"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Actuar como alguien que sostiene un proyecto a largo plazo",
                    "resultado_semana": "Actuar como alguien que sostiene un proyecto a largo plazo",
                    "habilidades_conocimientos": [
                        "Autoconfianza, toma de decisiones y liderazgo personal."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Actuar como fundador/a",
                                "Realiza una acción que normalmente pospondrías.",
                                "Con esta acción construyes identidad emprendedora real."
                            ],
                            "entregable": "Registro de: Actuar como fundador/a"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Anticipación estratégica",
                                "Identifica un problema futuro posible.",
                                "Diseña una solución preventiva.",
                                "[Herramienta sugerida: Técnica premortem]"
                            ],
                            "entregable": "Registro de: Anticipación estratégica"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Decisión pendiente",
                                "Toma una decisión que llevas semanas posponiendo.",
                                "Puede ser una micro-acción que hayas establecido anteriormente o algo nuevo."
                            ],
                            "entregable": "Registro de: Decisión pendiente"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Revisión de modelo",
                                "Refinemos la dirección que llevas, evalúa lo siguiente:",
                                "- ¿Mi cliente ideal siguie siendo el correcto?",
                                "- ¿Mi propuesta es clara?"
                            ],
                            "entregable": "Registro de: Revisión de modelo"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi identidad emprendedora",
                                "Para reforzar la narrativa interna y compromiso, escribe:",
                                "\"Hoy me veo como alguien que construye _ .\""
                            ],
                            "entregable": "Registro de: Mi identidad emprendedora"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Cerrar ciclo con estructura y plan sostenible",
                    "resultado_semana": "Cerrar ciclo con estructura y plan sostenible",
                    "habilidades_conocimientos": [
                        "Planeación a mediano plazo, evaluación estratégica y autonomía profesional."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Logros acumulados",
                                "Para ver tu progreso de forma tangible, enlista:",
                                "- Acciones realizadas",
                                "- Resultados",
                                "- Conversaciones importantes"
                            ],
                            "entregable": "Registro de: Logros acumulados"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Antes vs ahora",
                                "Responde lo siguiente para ver tu evolución estratégica durante esta experiencia y las actividades que has llevado a cabo:",
                                "¿Cómo veía el proyecto al inicio?",
                                "¿Cómo lo veo hoy?"
                            ],
                            "entregable": "Registro de: Antes vs ahora"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Meta a 90 días",
                                "Establece un plan de acción a mediano plazo.",
                                "Define:",
                                "- Resultado claro",
                                "- Indicador medible",
                                "- Hábito clave",
                                "Ejemplo:",
                                "Conseguir 5 clientes en 90 días.",
                                "[Herramienta sugerida: OKR simple (1 objetivo + 3 resultados)]"
                            ],
                            "entregable": "Registro de: Meta a 90 días"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Calendario estratégico",
                                "Revisa tu plan de acción a mediano plazo y en tu calendario agenda:",
                                "- 3 acciones concretas",
                                "Incluye: fecha y hora",
                                "TIP: No más de 3 para que sea alcanzable y realista."
                            ],
                            "entregable": "Registro de: Calendario estratégico"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Nivel de alineación y ajuste final",
                                "Evalúa tu compromiso, claridad y energía.",
                                "Escribe:",
                                "\"Mi siguiente paso concreto es _.\"",
                                "Revisa tu objetivo, propósito declarados, tu plan de acción y ajústalos si es necesario."
                            ],
                            "entregable": "Registro de: Nivel de alineación y ajuste final"
                        }
                    ]
                }
            ]
        }
    ]
},
"mejorar mi estabilidad y organización financiera": {
    "titulo": "Plan de acción · Mejorar mi estabilidad y organización financiera",
    "subtitulo": "Ruta estratégica personalizada para mejorar mi estabilidad y organización financiera",
    "objetivo_seleccionado": "Mejorar mi estabilidad y organización financiera",
    "meses": [
        {
            "numero": 1,
            "titulo": "Fase de Análisis y Definición",
            "resultado_mes": "Lograr los objetivos de la fase inicial para Mejorar mi estabilidad y organización financiera.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Tener claridad real sobre ingresos, gastos y compromisos actuales.",
                    "resultado_semana": "Tener claridad real sobre ingresos, gastos y compromisos actuales.",
                    "habilidades_conocimientos": [
                        "Lectura clara de tu situación financiera y registro organizado de información."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 1 · “Foto actual de mi dinero” (30 min)",
                                "Como primer paso para conocer tu situación financier actual, haz esto:",
                                "Anota todos tus ingresos mensuales.",
                                "Anota todos tus gastos fijos.",
                                "Anota tus deudas actuales (si tienes).",
                                "No estimes. Usa estados de cuenta si puedes.",
                                "Ejemplo:",
                                "Ingreso: $25,000",
                                "Renta: $8,000",
                                "Tarjeta: $3,500"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 1 · “Foto actual de mi dinero” (30 min..."
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 2 · “Mis gastos reales del último mes” (40 min)",
                                "Revisa tu último estado de cuenta.",
                                "Haz 3 categorías:",
                                "Gastos necesarios",
                                "Gastos variables",
                                "Gastos impulsivos",
                                "Ejemplo:",
                                "Café diario → impulsivo",
                                "Supermercado → necesario"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 2 · “Mis gastos reales del último mes”..."
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 3 · “¿En qué se va mi dinero?” (20 min)",
                                "Retoma la lista de categorías anterior sobre gastos necesarios, variables e impulsivos.",
                                "Responde:",
                                "¿Qué gasto me sorprendió?",
                                "¿Qué gasto podría reducir?",
                                "Escribe una decisión concreta.",
                                "Ejemplo:",
                                "Reducir apps de suscripción."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 3 · “¿En qué se va mi dinero?” (20 min..."
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 4 · “Mi dinero y mi propósito” (25 min)",
                                "Reflexiona y escribe:",
                                "¿Para qué quiero estabilidad financiera?",
                                "¿Qué quiero construir con mi dinero?",
                                "Conecta con una acción:",
                                "Ejemplo:",
                                "Quiero ahorrar para estudiar → abrir fondo de ahorro."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 4 · “Mi dinero y mi propósito” (25 min..."
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 5 · “Primer ajuste visible” (15 min)",
                                "Como una primera decisión financiera, elige una acción concreta:",
                                "Cancelar una suscripción.",
                                "Reducir un gasto.",
                                "Automatizar ahorro.",
                                "Elige una acción que puedas aplicar de forma inmediata."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 5 · “Primer ajuste visible” (15 min)"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Entender qué emociones influyen en tus decisiones financieras.",
                    "resultado_semana": "Entender qué emociones influyen en tus decisiones financieras.",
                    "habilidades_conocimientos": [
                        "Reconocimiento de emociones y toma de decisiones más consciente."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 6 · “Mis creencias sobre el dinero” (30 min)",
                                "Escribe frases que aprendiste sobre dinero.",
                                "Ejemplo:",
                                "“El dinero es difícil de ganar.”"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 6 · “Mis creencias sobre el dinero” (3..."
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 7 · “Emoción y gasto” (20 min)",
                                "Recuerda tu último gasto impulsivo.",
                                "Escribe:",
                                "¿Qué sentía?",
                                "¿Qué necesitaba realmente?"
                            ],
                            "entregable": "Registro de: 🔹 Actividad 7 · “Emoción y gasto” (20 min)"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 8 · “Nuevo acuerdo personal” (20 min)",
                                "Escribe una nueva regla personal basándote en tus últimos gastos y lo que te hicieron sentir.",
                                "Ejemplo:",
                                "“No compro nada mayor a $1,000 sin esperar 24 horas.”",
                                "NOTA: Revisa tu actividad anterior si lo crees necesario."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 8 · “Nuevo acuerdo personal” (20 min)"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 9 · “Escuchar nuevas perspectivas” (30 min)",
                                "Escucha un episodio de un podcast financiero.",
                                "Pregunta:",
                                "¿Cómo decides tus gastos importantes?",
                                "Alternativa: si no quieres hablar con alguien, escribe tu propia respuesta.",
                                "[Herramienta sugerida: podcast \"Ahorro e Inversión\" de FinanciallyFit Español.]"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 9 · “Escuchar nuevas perspectivas” (30..."
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 10 · “Decisión consciente esta semana” (15 min)",
                                "Elige una decisión financiera que tomarás de forma consciente esta semana.",
                                "Anótala y ejecútala."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 10 · “Decisión consciente esta semana”..."
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Diseñar un sistema simple de organización.",
                    "resultado_semana": "Diseñar un sistema simple de organización.",
                    "habilidades_conocimientos": [
                        "Planeación básica y control financiero."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 11 · “Diseña tu presupuesto simple” (40 min)",
                                "Usa regla 50-30-20 como referencia para crear un presupuesto que esté a tu alcance (investíga la regla si no la conoces).",
                                "Distribuye:",
                                "Necesidades",
                                "Gustos",
                                "Ahorro",
                                "No tiene que ser perfecto."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 11 · “Diseña tu presupuesto simple” (4..."
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 12 · “Define un porcentaje de ahorro” (20 min)",
                                "Elige un porcentaje realista para comenzar a ahorrar.",
                                "Si puedes, haz una de estas dos opciones:",
                                "- Abre una cuenta de ahorro.",
                                "- Separa físicamente un monto.",
                                "Ejemplo:",
                                "5% este mes."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 12 · “Define un porcentaje de ahorro” ..."
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 13 · “Micro-meta de ahorro\" (20 min)",
                                "Elige una meta clara para la cual quieres ahorrar (ahorro, viaje, curso).",
                                "Estima el costo y en cuánto tiempo te gustaría alcanzarla.",
                                "El porcentaje de ahorro que declaraste anteriormente, ¿cumple con tu meta?",
                                "Ajusta si es necesario."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 13 · “Micro-meta de ahorro\" (20 min)"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 14 · “Revisión rápida semanal” (15 min)",
                                "Crea un espacio fijo semanal de 15 min para revisar gastos, puedes usar la herramienta de calendario de esta app.",
                                "Agéndalo para que formes un hábito de revisión."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 14 · “Revisión rápida semanal” (15 min..."
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 15 · “Evalúa tu sistema” (20 min)",
                                "Revisa tus acciones financieras con los cambios que hayas realizado.",
                                "Después, responde:",
                                "¿Fue fácil?",
                                "¿Qué ajustaré?",
                                "¿Qué categoría puedo reducir sin afectar mi bienestar?"
                            ],
                            "entregable": "Registro de: 🔹 Actividad 15 · “Evalúa tu sistema” (20 min)"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Definir metas concretas.",
                    "resultado_semana": "Definir metas concretas.",
                    "habilidades_conocimientos": [
                        "Definición de metas y priorización financiera."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 16 · “Elige una meta principal” (30 min)",
                                "Ejemplo:",
                                "Fondo de emergencia de 3 meses.",
                                "Escríbela clara y medible."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 16 · “Elige una meta principal” (30 mi..."
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 17 · “Divide en pasos pequeños” (30 min)",
                                "Toma en consideración la meta que te fijaste en la actividad anterior y reflexiona cómo puedes conseguirla con pasos pequeños. Ejemplo: Si necesitas $30,000:",
                                "¿Cuánto por mes?",
                                "Haz la cuenta simple."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 17 · “Divide en pasos pequeños” (30 mi..."
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 18 · “Fecha objetivo” (15 min)",
                                "Considera el objetivo de las dos actividades pasadas y pon una fecha realista para lograrla.",
                                "Puedes agendarlo en el calendario para tener mayor control y evaluar si llegaste o te acercaste a tu meta."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 18 · “Fecha objetivo” (15 min)"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 19 · “Obstáculos posibles” (20 min)",
                                "Reflexiona sobre la meta que te has fijado en las actividades anteriores.",
                                "Escribe:",
                                "¿Qué podría impedirlo?",
                                "¿Qué haré si pasa?"
                            ],
                            "entregable": "Registro de: 🔹 Actividad 19 · “Obstáculos posibles” (20 min)"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 20 · “Compromiso visible” (15 min)",
                                "Comparte la meta que te has fijado con:",
                                "Pareja",
                                "Familiar",
                                "Amigo cercano",
                                "o escríbela en un lugar visible."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 20 · “Compromiso visible” (15 min)"
                        }
                    ]
                }
            ]
        },
        {
            "numero": 2,
            "titulo": "Fase de Implementación y Crecimiento",
            "resultado_mes": "Lograr los objetivos de la fase avanzada para Mejorar mi estabilidad y organización financiera.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Explorar opciones para mejorar flujo de dinero",
                    "resultado_semana": "Explorar opciones para mejorar flujo de dinero",
                    "habilidades_conocimientos": [
                        "Mentalidad de crecimiento y creatividad financiera"
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "Mapa de habilidades monetizables (30 min)",
                                "Escribe habilidades que tengas que podrían generar un ingreso extra."
                            ],
                            "entregable": "Registro de: Mapa de habilidades monetizables (30 min)"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "Idea secundaria (25 min)",
                                "De las habilidades que describiste en la actividad anterior, elige una idea viable que podría ser de ayuda para monetizar.",
                                "Puedes utilizarlo como un plan de respaldo o como un emprendimiento pequeño."
                            ],
                            "entregable": "Registro de: Idea secundaria (25 min)"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "Primer paso real (30 min)",
                                "Haz una acción concreta (mensaje, investigación, propuesta).",
                                "Esto te ayudará a poder tangibilizar tu idea previa."
                            ],
                            "entregable": "Registro de: Primer paso real (30 min)"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "Evaluación de factibilidad (20 min)",
                                "Revisa tu actividad anterior. ¿Es realista mantenerlo?",
                                "¿Por qué sí o por qué no?"
                            ],
                            "entregable": "Registro de: Evaluación de factibilidad (20 min)"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "Decisión estratégica (20 min)",
                                "Con base en tu actividad anterior decide:",
                                "- Continuar",
                                "- Ajustar",
                                "- Descartar"
                            ],
                            "entregable": "Registro de: Decisión estratégica (20 min)"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Fortalecer tu fondo de seguridad.",
                    "resultado_semana": "Fortalecer tu fondo de seguridad.",
                    "habilidades_conocimientos": [
                        "Planeación financiera básica y previsión."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 26 · “Costo de mi mes básico” (30 min)",
                                "Retoma tu lista de gastos necesarios.",
                                "Calcula:",
                                "¿Cuánto necesito para cubrir 1 mes esencial?",
                                "Incluye solo:",
                                "Vivienda",
                                "Comida",
                                "Transporte",
                                "Servicios básicos"
                            ],
                            "entregable": "Registro de: 🔹 Actividad 26 · “Costo de mi mes básico” (30 min)"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 27 · “Primer bloque de seguridad” (15 min)",
                                "Define una meta pequeña inicial.",
                                "Ejemplo:",
                                "Ahorrar $5,000 como primera meta.",
                                "Transfiere hoy una parte, aunque sea pequeña."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 27 · “Primer bloque de seguridad” (15 ..."
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 28 · “Dónde guardar mi fondo” (30 min)",
                                "Investiga:",
                                "Cuenta de ahorro separada.",
                                "Rendimiento básico.",
                                "Facilidad de acceso.",
                                "No necesitas abrir nada hoy si no puedes, pero define dónde lo guardarás."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 28 · “Dónde guardar mi fondo” (30 min)"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 29 · “Ajustar porcentaje de ahorro” (20 min)",
                                "Revisa tu porcentaje definido en semana 3.",
                                "Pregunta:",
                                "¿Puedo aumentarlo 1%?",
                                "Si no, ¿puedo mantenerlo constante?"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 29 · “Ajustar porcentaje de ahorro” (2..."
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 30 · “Medir avance real” (20 min)",
                                "Escribe:",
                                "¿Cuánto tengo hoy en mi fondo?",
                                "¿Cuánto me falta?",
                                "¿Me siento más tranquilo/a que hace un mes?"
                            ],
                            "entregable": "Registro de: 🔹 Actividad 30 · “Medir avance real” (20 min)"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Tomar decisiones grandes con intención.",
                    "resultado_semana": "Tomar decisiones grandes con intención.",
                    "habilidades_conocimientos": [
                        "Autocontrol financiero y toma de decisiones reflexiva."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 31 · “Revisar mi meta principal” (15 min)",
                                "Retoma la meta definida en semana 4.",
                                "Pregúntate:",
                                "¿Sigue siendo mi prioridad?",
                                "Si no, ajústala."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 31 · “Revisar mi meta principal” (15 m..."
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 32 · “Evaluar un gasto grande pendiente” (30 min)",
                                "Elige un gasto relevante que estés considerando.",
                                "Haz esta tabla:",
                                "¿Lo necesito?",
                                "¿Aporta a mi propósito?",
                                "¿Impacta mi meta?",
                                "Ejemplo:",
                                "Viaje, curso, compra tecnológica"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 32 · “Evaluar un gasto grande pendient..."
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 33 · “Regla de las 24 horas” (actividad práctica)",
                                "Si decides comprar algo mayor a lo habitual:",
                                "Espera 24 horas antes de hacerlo.",
                                "Registra cómo te sientes después."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 33 · “Regla de las 24 horas” (activida..."
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 34 · “Conversación financiera consciente” (30 min)",
                                "Habla con:",
                                "Tu pareja",
                                "o",
                                "Una persona de confianza",
                                "Tema:",
                                "Tu meta financiera y cómo te pueden apoyar.",
                                "Alternativa:",
                                "Si no quieres hablar con alguien, escribe una carta a ti mismo sobre tu compromiso financiero."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 34 · “Conversación financiera conscien..."
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 35 · “Decisión alineada” (20 min)",
                                "Toma una decisión financiera importante esta semana:",
                                "Posponer compra.",
                                "Invertir en algo que aporte.",
                                "Ajustar gasto.",
                                "Registra la decisión."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 35 · “Decisión alineada” (20 min)"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Consolidar un plan financiero que puedas sostener.",
                    "resultado_semana": "Consolidar un plan financiero que puedas sostener.",
                    "habilidades_conocimientos": [
                        "Planificación financiera de mediano plazo y autonomía."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 36 · “Mis 5 aprendizajes financieros” (30 min)",
                                "Escribe:",
                                "Qué cambió en mi forma de ver el dinero.",
                                "Qué hábito fue más útil.",
                                "Qué fue más difícil."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 36 · “Mis 5 aprendizajes financieros” ..."
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 37 · “Mi nueva relación con el dinero” (25 min)",
                                "Completa:",
                                "“Hoy veo el dinero como ___”.",
                                "Conecta con propósito.",
                                "Ejemplo:",
                                "“Como una herramienta para construir tranquilidad.”"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 37 · “Mi nueva relación con el dinero”..."
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 38 · “Plan financiero 90 días” (40 min)",
                                "Define:",
                                "Cuánto ahorrarás.",
                                "Qué gasto reducirás.",
                                "Qué hábito mantendrás.",
                                "Cuándo revisarás.",
                                "Usa calendario real."
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 38 · “Plan financiero 90 días” (40 min..."
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 39 · “Agenda tus revisiones” (15 min)",
                                "Agenda:",
                                "Revisión mensual.",
                                "Ajuste trimestral.",
                                "No lo dejes en intención. Pon fecha y hora."
                            ],
                            "entregable": "Registro de: 🔹 Actividad 39 · “Agenda tus revisiones” (15 min)"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 0,
                            "instrucciones": [
                                "🔹 Actividad 40 · “Nivel de estabilidad hoy” (20 min)",
                                "Evalúate del 1 al 10 en:",
                                "Organización.",
                                "Claridad.",
                                "Tranquilidad.",
                                "Escribe:",
                                "¿Qué tendría que pasar para subir 1 punto más?"
                            ],
                            "entregable": "Registro y resultados de: 🔹 Actividad 40 · “Nivel de estabilidad hoy” (20 mi..."
                        }
                    ]
                }
            ]
        }
    ]
},
"lograr un mejor equilibrio entre trabajo y vida personal": {
    "titulo": "Plan de acción · Lograr un mejor equilibrio entre trabajo y vida personal",
    "subtitulo": "Ruta estratégica personalizada para lograr un mejor equilibrio entre trabajo y vida personal",
    "objetivo_seleccionado": "Lograr un mejor equilibrio entre trabajo y vida personal",
    "meses": [
        {
            "numero": 1,
            "titulo": "Fase de Análisis y Definición",
            "resultado_mes": "Lograr los objetivos de la fase inicial para Lograr un mejor equilibrio entre trabajo y vida personal.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Identificar cómo estás usando tu tiempo y energía hoy",
                    "resultado_semana": "Identificar cómo estás usando tu tiempo y energía hoy",
                    "habilidades_conocimientos": [
                        "Autoconciencia, gestión básica del tiempo e identificación de desgaste."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Radiografía de mi semana",
                                "1. Escribe cómo fue tu última semana laboral.",
                                "2. Anota horas aproximadas dedicadas a:",
                                "- Trabajo",
                                "- Familia / relaciones",
                                "- Descanso",
                                "- Actividad física",
                                "- Tiempo personal",
                                "No busques exactitud, busca honestidad.",
                                "Herramienta sugerida: Time tracking básico (puedes investigar “registro de tiempo personal”)."
                            ],
                            "entregable": "Registro de: Radiografía de mi semana"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Mi nivel de energía",
                                "Responde:",
                                "¿Qué actividades me drenan más?",
                                "¿Qué actividades me recargan?",
                                "Marca con:",
                                "⚡ Energía",
                                "🪫 Drenaje"
                            ],
                            "entregable": "Registro de: Mi nivel de energía"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Costo del desequilibrio",
                                "Escribe:",
                                "¿Qué estoy dejando de hacer por trabajar demasiado?",
                                "¿Qué impacto tiene en mi salud o relaciones?",
                                "Conecta con tu propósito:",
                                "¿Estoy viviendo como quiero vivir?"
                            ],
                            "entregable": "Registro de: Costo del desequilibrio"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Mi definición de equilibrio",
                                "Completa:",
                                "“Para mí, equilibrio significa ___.”",
                                "Ejemplo:",
                                "“Tener horarios definidos y poder desconectarme sin culpa.”"
                            ],
                            "entregable": "Registro de: Mi definición de equilibrio"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Una primera micro-decisión",
                                "Elige UNA acción pequeña para esta semana.",
                                "Ejemplo:",
                                "No revisar correos después de las 8 pm.",
                                "Salir 30 min a caminar 3 días.",
                                "No más de una."
                            ],
                            "entregable": "Registro de: Una primera micro-decisión"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Definir y probar límites saludables",
                    "resultado_semana": "Definir y probar límites saludables",
                    "habilidades_conocimientos": [
                        "Establecimiento de límites, comunicación clara y autocontrol."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Identifica un límite necesario",
                                "Responde:",
                                "¿Qué límite necesito establecer?",
                                "¿En horarios? ¿Disponibilidad? ¿Tareas?"
                            ],
                            "entregable": "Registro de: Identifica un límite necesario"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Diseña tu regla personal",
                                "Escribe:",
                                "“A partir de hoy, yo ___.”",
                                "Ejemplo:",
                                "“No aceptaré reuniones fuera de horario.”"
                            ],
                            "entregable": "Registro de: Diseña tu regla personal"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Comunicación breve",
                                "Si aplica, informa a:",
                                "- Equipo",
                                "- Cliente",
                                "- Familia",
                                "Mensaje claro y respetuoso.",
                                "Si no hay respuesta, continúa aplicando tu regla.",
                                "Herramienta",
                                "Comunicación asertiva (investiga principios básicos)."
                            ],
                            "entregable": "Registro de: Comunicación breve"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Prueba del límite",
                                "Aplica tu regla esta semana.",
                                "Observa qué sucede."
                            ],
                            "entregable": "Registro de: Prueba del límite"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Aprendizaje y ajuste",
                                "Escribe:",
                                "¿Qué funcionó?",
                                "¿Qué ajustaré?"
                            ],
                            "entregable": "Registro de: Aprendizaje y ajuste"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Organizar tu agenda con intención",
                    "resultado_semana": "Organizar tu agenda con intención",
                    "habilidades_conocimientos": [
                        "Planeación semanal, priorización y enfoque."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Lista de prioridades",
                                "Haz lista de 10 pendientes.",
                                "Marca solo 3 importantes.",
                                "Herramienta sugerida: Matriz Eisenhower."
                            ],
                            "entregable": "Registro de: Lista de prioridades"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Bloques de concentración",
                                "Agenda 2 bloques sin interrupciones."
                            ],
                            "entregable": "Registro de: Bloques de concentración"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Espacio personal agendado",
                                "Agenda tiempo personal como si fuera reunión importante.",
                                "Ejemplo:",
                                "Ejercicio, lectura, descanso."
                            ],
                            "entregable": "Registro de: Espacio personal agendado"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Revisión de interrupciones",
                                "Identifica:",
                                "¿Qué me distrae más?",
                                "¿Qué puedo eliminar?"
                            ],
                            "entregable": "Registro de: Revisión de interrupciones"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Mini ritual de cierre diario",
                                "Antes de terminar tu jornada:",
                                "Escribe 3 pendientes para mañana.",
                                "Cierra sesión mentalmente."
                            ],
                            "entregable": "Registro de: Mini ritual de cierre diario"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Cuidar tu energía, no solo tu tiempo",
                    "resultado_semana": "Cuidar tu energía, no solo tu tiempo",
                    "habilidades_conocimientos": [
                        "Autocuidado consciente y gestión del estrés."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Chequeo físico básico",
                                "Evalúa:",
                                "- Sueño",
                                "- Alimentación",
                                "- Movimiento"
                            ],
                            "entregable": "Registro de: Chequeo físico básico"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Movimiento mínimo viable",
                                "Elige actividad física breve (15–20 min)."
                            ],
                            "entregable": "Registro de: Movimiento mínimo viable"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Desconexión real",
                                "Una hora sin pantallas."
                            ],
                            "entregable": "Registro de: Desconexión real"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Reacción al cambio",
                                "¿Te sentiste culpable por desconectar?",
                                "Escribe qué pensaste."
                            ],
                            "entregable": "Registro de: Reacción al cambio"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Reencuadre mental",
                                "Completa:",
                                "“Descansar no es perder tiempo, es ___.”"
                            ],
                            "entregable": "Registro de: Reencuadre mental"
                        }
                    ]
                }
            ]
        },
        {
            "numero": 2,
            "titulo": "Fase de Implementación y Crecimiento",
            "resultado_mes": "Lograr los objetivos de la fase avanzada para Lograr un mejor equilibrio entre trabajo y vida personal.",
            "semanas": [
                {
                    "numero": 1,
                    "titulo": "Mejorar calidad de relaciones",
                    "resultado_semana": "Mejorar calidad de relaciones",
                    "habilidades_conocimientos": [
                        "Comunicación y presencia."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Conversación sin multitarea",
                                "Habla con alguien importante sin distracciones."
                            ],
                            "entregable": "Registro de: Conversación sin multitarea"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Pregunta abierta",
                                "Pregunta:",
                                "“¿Cómo me has visto últimamente en términos de equilibrio?”",
                                "Si no hay respuesta, reflexiona tú."
                            ],
                            "entregable": "Registro de: Pregunta abierta"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 15,
                            "instrucciones": [
                                "Escucha activa",
                                "Escucha sin interrumpir."
                            ],
                            "entregable": "Registro de: Escucha activa"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Decisión relacional",
                                "Haz una acción concreta:",
                                "Planear salida",
                                "Llamar a alguien",
                                "Pedir disculpas"
                            ],
                            "entregable": "Registro de: Decisión relacional"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Balance semanal",
                                "Evalúa:",
                                "Trabajo 1–10",
                                "Vida personal 1–10"
                            ],
                            "entregable": "Registro de: Balance semanal"
                        }
                    ]
                },
                {
                    "numero": 2,
                    "titulo": "Reducir sobrecarga innecesaria",
                    "resultado_semana": "Reducir sobrecarga innecesaria",
                    "habilidades_conocimientos": [
                        "Delegación, toma de decisiones y simplificación."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Qué puedo dejar de hacer",
                                "Lista tareas que podrías:",
                                "Delegar",
                                "Eliminar",
                                "Simplificar"
                            ],
                            "entregable": "Registro de: Qué puedo dejar de hacer"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Automatización básica",
                                "Identifica algo que puedas sistematizar."
                            ],
                            "entregable": "Registro de: Automatización básica"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Decisión valiente",
                                "Di no a algo no prioritario."
                            ],
                            "entregable": "Registro de: Decisión valiente"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Evaluación de carga",
                                "¿Mi carga es real o autoimpuesta?"
                            ],
                            "entregable": "Registro de: Evaluación de carga"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Ajuste práctico",
                                "Haz un ajuste pequeño en tu rutina laboral."
                            ],
                            "entregable": "Registro de: Ajuste práctico"
                        }
                    ]
                },
                {
                    "numero": 3,
                    "titulo": "Actuar como alguien equilibrado",
                    "resultado_semana": "Actuar como alguien equilibrado",
                    "habilidades_conocimientos": [
                        "Autodisciplina y coherencia personal."
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Cómo actuaría alguien equilibrado",
                                "Haz una acción alineada a esa respuesta."
                            ],
                            "entregable": "Registro de: Cómo actuaría alguien equilibrado"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Revisión de creencias",
                                "¿Qué creencia me impide descansar?"
                            ],
                            "entregable": "Registro de: Revisión de creencias"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Nuevo hábito",
                                "Instala hábito pequeño sostenible."
                            ],
                            "entregable": "Registro de: Nuevo hábito"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Revisión de progreso",
                                "¿Estoy mejor que hace un mes?"
                            ],
                            "entregable": "Registro de: Revisión de progreso"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Declaración personal",
                                "Escribe:",
                                "“Yo soy alguien que ___.”"
                            ],
                            "entregable": "Registro de: Declaración personal"
                        }
                    ]
                },
                {
                    "numero": 4,
                    "titulo": "Sostener equilibrio a largo plazo",
                    "resultado_semana": "Sostener equilibrio a largo plazo",
                    "habilidades_conocimientos": [
                        "Planeación consciente y autonomía"
                    ],
                    "dias": [
                        {
                            "numero": 1,
                            "tiempo_estimado_min": 30,
                            "instrucciones": [
                                "Logros acumulados",
                                "Lista cambios logrados."
                            ],
                            "entregable": "Registro de: Logros acumulados"
                        },
                        {
                            "numero": 2,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Antes vs ahora",
                                "Compara percepción inicial vs actual."
                            ],
                            "entregable": "Registro de: Antes vs ahora"
                        },
                        {
                            "numero": 3,
                            "tiempo_estimado_min": 25,
                            "instrucciones": [
                                "Meta 90 días",
                                "Define 1 hábito clave para sostener."
                            ],
                            "entregable": "Registro de: Meta 90 días"
                        },
                        {
                            "numero": 4,
                            "tiempo_estimado_min": 40,
                            "instrucciones": [
                                "Calendario realista",
                                "Agenda bloques laborales y personales."
                            ],
                            "entregable": "Registro de: Calendario realista"
                        },
                        {
                            "numero": 5,
                            "tiempo_estimado_min": 20,
                            "instrucciones": [
                                "Nivel de alineación final",
                                "Evalúa equilibrio del 1 al 10.",
                                "Escribe:",
                                "“Mi siguiente paso concreto es ___.”"
                            ],
                            "entregable": "Registro de: Nivel de alineación final"
                        }
                    ]
                }
            ]
        }
    ]
}
}
'''