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