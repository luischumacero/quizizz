# coding: utf-8
"""
Generador de preguntas para Técnico Pedagógico (4 temas x 200 preguntas = 800 preguntas):
- 6.1. ODS 4: Educación 2030 UNESCO
- 6.2. LIDEI 2022: Liderazgo Directivo en Iberoamérica - OEI (2023)
- 6.3. Marco para la Gestión y Liderazgo Educativo Local (Uribe et al., 2025)
- 6.4. Estudio Regional Comparativo y Explicativo ERCE 2019 (UNESCO/LLECE)
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

# ----------------- 6.1. ODS 4 UNESCO EDUCACIÓN 2030 -----------------
ODS4_SPECS = [
    ("¿Cuál es el enunciado central del Objetivo de Desarrollo Sostenible 4 (ODS 4) de la Agenda 2030 de la UNESCO?",
     ["Garantizar una educación inclusiva, equitativa y de calidad y promover oportunidades de aprendizaje durante toda la vida para todos",
      "Duplicar el gasto militar en investigación universitaria",
      "Limitar el acceso a la educación superior a una élite selecta",
      "Sustituir a los docentes de aula por inteligencia artificial automatizada",
      "Cobrar aranceles educativos internacionales en dólares"],
     0, "El ODS 4 consagra la educación inclusiva, equitativa, con calidad y aprendizaje continuo a lo largo de toda la vida."),

    ("La Meta 4.1 del ODS 4 establece que de aquí a 2030, todos los países deben asegurar que todas las niñas y todos los niños terminen:",
     ["La enseñanza primaria y secundaria, que ha de ser gratuita, equitativa y de calidad y producir resultados de aprendizaje pertinentes y efectivos",
      "Únicamente el nivel inicial y sepan contar hasta diez",
      "El primer año de primaria y luego comiencen a trabajar",
      "Solo la educación técnica sin formación humanística",
      "Cursos virtuales de corta duración sin titulación"],
     0, "La Meta 4.1 garantiza 12 años de educación primaria y secundaria gratuita y de calidad."),

    ("La Meta 4.2 del ODS 4 se enfoca prioritariamente en:",
     ["El acceso a servicios de atención y desarrollo en la primera infancia y una enseñanza preescolar de calidad",
      "La jubilación anticipada de directores",
      "La compra de computadoras para universidades privadas",
      "Los exámenes de admisión para posdoctorados",
      "El control migratorio de estudiantes extranjeros"],
     0, "La primera infancia y preescolar es la base del desarrollo cognitivo, emocional y social posterior."),

    ("La Meta 4.5 del ODS 4 busca eliminar:",
     ["Las disparidades de género en la educación y asegurar el acceso igualitario a todos los niveles para personas vulnerables e indígenas",
      "El aprendizaje de la historia nacional",
      "La participación de los padres de familia en la escuela",
      "Las clases de educación física y artes",
      "La evaluación formativa de aprendizajes"],
     0, "La Meta 4.5 combate toda brecha de género, etnia, discapacidad o vulnerabilidad socioeconómica."),

    ("La Meta 4.7 del ODS 4 promueve la educación para:",
     ["El desarrollo sostenible, los derechos humanos, la igualdad de género, la cultura de paz y la ciudadanía mundial",
      "El consumismo exacerbado y la explotación destructiva de recursos",
      "El nacionalismo agresivo y la xenofobia",
      "La guerra cibernética y armamentista",
      "El aislamiento cultural y la intolerancia religiosa"],
     0, "La Meta 4.7 inculca valores cívicos globales, sostenibilidad ambiental, derechos humanos y convivencia armónica."),

    ("El 'Marco de Acción Educación 2030' de la Declaración de Incheon reconoce que la educación es:",
     ["Un derecho humano fundamental, un bien público y la base para garantizar la realización de otros derechos",
      "Una mercancía comercial sujeta a la ley de la oferta y la demanda",
      "Un privilegio reservado a quienes puedan costearlo",
      "Una responsabilidad exclusiva de las familias sin intervención estatal",
      "Un gasto prescindible en épocas de austeridad"],
     0, "La Declaración de Incheon reafirma la educación como derecho humano y bien público inalienable."),

    ("La Meta 4.a del ODS 4 se refiere a:",
     ["Construir y adecuar instalaciones educativas que tengan en cuenta a los niños y la discapacidad y ofrezcan entornos de aprendizaje seguros y no violentos",
      "Cobrar licencias de edificación a los municipios",
      "Instalar cámaras de vigilancia carcelarias en las aulas",
      "Reducir el tamaño de las escuelas a una sola habitación",
      "Eliminar los patios de recreo y áreas verdes"],
     0, "La Meta 4.a exige infraestructuras seguras, inclusivas, con agua, saneamiento y accesibilidad universal."),

    ("La Meta 4.c del ODS 4 exige a los Estados aumentar sustancialmente la oferta de:",
     ["Docentes calificados, mediante la formación docente, la cooperación internacional y condiciones de trabajo dignas",
      "Exámenes estandarizados punitivos",
      "Contrataciones temporales sin beneficios laborales",
      "Sanciones penales contra maestros",
      "Plataformas comerciales que reemplacen al profesor"],
     0, "La Meta 4.c sitúa a la docencia calificada, motivada y valorada como clave del éxito escolar."),

    ("El concepto de 'Aprendizaje a lo largo de toda la vida' (Lifelong Learning) en el ODS 4 implica que:",
     ["La educación no se restringe a la edad escolar, sino que abarca oportunidades continuas desde la cuna hasta la vejez",
      "Los estudiantes nunca deben graduarse y permanecer en la escuela siempre",
      "Solo los ancianos tienen derecho a estudiar",
      "Las empresas deciden qué materias se pueden estudiar",
      "La educación formal termina obligatoriamente a los 15 años"],
     0, "Reconoce vías formales, no formales e informales de aprendizaje durante todo el ciclo vital."),

    ("El rol del Director de Unidad Educativa en relación al ODS 4 se traduce localmente en:",
     ["Garantizar la inclusión de todos los estudiantes, promover la equidad de género y liderar una educación con pertinencia y calidad",
      "Expulsar a estudiantes con bajo rendimiento para subir el promedio del colegio",
      "Rechazar a estudiantes con discapacidad para evitar gastos",
      "Cobrar cuotas en dólares a las familias",
      "Limitarse a firmar papeles de asistencia sin monitoreo pedagógico"],
     0, "El liderazgo directivo escolar es el catalizador decisivo para materializar las metas del ODS 4 en la práctica.")
]

# ----------------- 6.2. LIDEI 2022: LIDERAZGO DIRECTIVO EN IBEROAMÉRICA (OEI) -----------------
LIDEI_SPECS = [
    ("¿Qué es el informe LIDEI 2022 publicado por la Organización de Estados Iberoamericanos (OEI) en 2023?",
     ["Un estudio comparado sobre el marco normativo, perfiles, prácticas y desafíos del Liderazgo Directivo Escolar en Iberoamérica",
      "Un manual de contabilidad para bancos comerciales",
      "Un tratado militar de defensa fronteriza",
      "Un catálogo de software informático privado",
      "Una encuesta sobre hábitos de consumo alimentario"],
     0, "LIDEI analiza el estado del arte y las directrices para fortalecer el liderazgo directivo escolar en la región iberoamericana."),

    ("Según el informe LIDEI, el 'Liderazgo Pedagógico' del Director se diferencia del modelo puramente burocrático porque:",
     ["Se centra en la mejora de los procesos de enseñanza-aprendizaje, el acompañamiento docente y el desarrollo profesional continuo",
      "Se limita a cumplir horarios y archivar correspondencia oficial",
      "Delega toda la labor académica en el personal de limpieza",
      "Se enfoca exclusivamente en la compra de pintura y ladrillos",
      "Ejerce autoridad autoritaria sin diálogo con los docentes"],
     0, "El liderazgo pedagógico prioriza el impacto en el aula, la didáctica y los resultados formativos de los estudiantes."),

    ("El informe LIDEI identifica como una de las dimensiones clave del liderazgo directivo eficaz:",
     ["Establecer una visión y metas estratégicas compartidas con toda la comunidad educativa",
      "Mantener en secreto los objetivos de la escuela",
      "Imponer decisiones arbitrarias sin fundamentación pedagógica",
      "Fomentar la rivalidad y el individualismo entre profesores",
      "Evitar el contacto con las familias de los estudiantes"],
     0, "Una visión clara y colaborativa alinea los esfuerzos institucionales hacia la mejora escolar sostenida."),

    ("El concepto de 'Liderazgo Distribuido' promovido en el estudio LIDEI plantea que:",
     ["La dirección escolar no es un acto solitario, sino una práctica compartida que empodera a coordinadores, docentes y comisiones",
      "El Director debe concentrar el 100% de las decisiones sin delegar nada",
      "Cada profesor hace lo que quiere sin ninguna coordinación institucional",
      "La dirección del colegio se sortea cada semana entre los alumnos",
      "Se elimina la figura de la autoridad directiva"],
     0, "El liderazgo distribuido moviliza capacidades colectivas, redes de apoyo y corresponsabilidad profesional."),

    ("En relación al CLIMA ESCOLAR, LIDEI concluye que los directores efectivos:",
     ["Construyen un ambiente escolar seguro, acogedor, basado en la confianza, el respeto mutuo y altas expectativas académicas",
      "Instalan un régimen de miedo y castigos permanentes",
      "Permiten la indisciplina total y el desorden en los pasillos",
      "Tratan con favoritismo a un pequeño grupo de docentes leales",
      "Ignoran las denuncias de discriminación o maltrato"],
     0, "Un clima positivo y seguro es condición indispensable para el aprendizaje y bienestar socioemocional."),

    ("El 'Acompañamiento Pedagógico' en el marco de LIDEI implica:",
     ["Observación formativa de aula, retroalimentación constructiva, diálogo reflexivo y modelamiento de buenas prácticas",
      "Espiar por la ventana del aula para descontar salario por errores",
      "Interrumpir la clase para humillar al docente frente a los alumnos",
      "Obligar al profesor a dictar exactamente las palabras del director",
      "Reemplazar al maestro sin previo aviso"],
     0, "El acompañamiento es formativo y de mentoría, no punitivo ni fiscalizador represivo."),

    ("Uno de los principales DESAFÍOS del liderazgo directivo en Iberoamérica señalados por LIDEI es:",
     ["La sobrecarga de tareas administrativas y burocráticas que restan tiempo a la gestión pedagógica y formativa",
      "La falta absoluta de leyes y reglamentos educativos",
      "El exceso de computadoras portátiles en las escuelas",
      "La ausencia de estudiantes en las aulas",
      "Que los directores no tengan salario mensual"],
     0, "La burocratización excesiva es el principal obstáculo que desvía al director de su rol pedagógico central."),

    ("LIDEI resalta la importancia de la 'Formación y Desarrollo Profesional Directivo' como:",
     ["Una política continua y especializada que debe ir más allá de la experiencia docente previa para desarrollar competencias gerenciales y pedagógicas",
      "Un gasto innecesario porque cualquiera sabe dirigir intuitivamente",
      "Un castigo para directores con quejas administrativas",
      "Un trámite que se hace una sola vez en la vida de 2 horas",
      "Un curso optativo sobre jardinería escolar"],
     0, "Dirigir una escuela exige competencias especializadas de gestión, mediación y liderazgo curricular."),

    ("La 'Gestión Basada en Evidencias' en el liderazgo escolar (LIDEI) promueve que el director:",
     ["Utilice datos de asistencia, aprendizaje, retención y evaluación para tomar decisiones informadas y diseñar planes de mejora",
      "Tome decisiones basándose únicamente en corazonadas o rumores de pasillo",
      "Oculte las estadísticas escolares reprobadas",
      "Invente calificaciones ficticias para impresionar a las autoridades",
      "Ignore los resultados de pruebas estandarizadas"],
     0, "La toma de decisiones informada por diagnósticos y evidencia maximiza el impacto pedagógico."),

    ("La relación con la COMUNIDAD y el entorno territorial en el enfoque de LIDEI requiere que la escuela:",
     ["Se abra al contexto comunitario, articule con servicios de salud, cultura y organizaciones locales en redes de corresponsabilidad",
      "Construya muros ciegos y cierre las puertas a todo contacto exterior",
      "Prohíba a los padres acercarse al establecimiento",
      "Se mude a otra ciudad para evitar a los vecinos",
      "Compita agresivamente contra los otros colegios del barrio"],
     0, "La escuela abierta y comunitaria fortalece el capital social y los entornos protectores de la niñez.")
]

# ----------------- 6.3. MARCO DE GESTIÓN Y LIDERAZGO EDUCATIVO LOCAL (URIBE ET AL., 2025) -----------------
MARCO_SPECS = [
    ("¿Cuál es el foco central de la obra 'Marco para la Gestión y el Liderazgo Educativo Local' (Uribe, Aziz dos Santos, Berkowitz, Galdames, Torche y Zoro, 2025)?",
     ["Promover prácticas de liderazgo intermedio y directivo para la mejora integral y equitativa de la educación pública en los territorios",
      "Fomentar la privatización y mercantilización de escuelas comunitarias",
      "Eliminar los distritos educativos y la supervisión del Estado",
      "Crear un currículo único internacional sin pertinencia local",
      "Sustituir los libros escolares por cómics comerciales"],
     0, "La obra propone un marco conceptual y práctico para el liderazgo intermedio y directivo en territorios locales."),

    ("¿Qué se entiende por 'Liderazgo Educativo Intermedio' en el marco de Uribe et al. (2025)?",
     ["El nivel de gestión que articula las políticas centrales del Ministerio con las unidades educativas (Direcciones Distritales y Redes)",
      "El liderazgo ejercido exclusivamente por los choferes escolares",
      "La presidencia de la junta de vecinos del barrio",
      "El cargo de tesorero de la federación de estudiantes",
      "El arbitraje en campeonatos de fútbol escolar"],
     0, "El nivel intermedio (distritos, redes locales) es el puente articulador entre la macro-política y el aula."),

    ("Uno de los pilares de la 'Mejora Integral en los Territorios' es el trabajo en:",
     ["Redes escolares colaborativas y comunidades de aprendizaje profesional entre escuelas vecinas",
      "Competencia destructiva y aislamiento entre colegios",
      "Aulas cerradas donde ningún profesor comparte su método",
      "Escuelas que ocultan sus materiales a las demás",
      "Centros educativos que expulsan a alumnos con dificultades para transferirlos al vecino"],
     0, "Las redes de colaboración territorial generan aprendizaje profesional mutuo y soporte entre pares."),

    ("Según Uribe et al. (2025), el 'Acompañamiento Situado' se caracteriza por:",
     ["Ser contextualizado, continuo, dialogante y adaptado a las necesidades específicas de cada comunidad escolar",
      "Ser idéntico, rígido e impuesto sin considerar la realidad rural o urbana",
      "Consistir en una visita inspectiva de 5 minutos una vez al año",
      "Aplicar multas inmediatas sin orientar pedagógicamente",
      "Dictar órdenes por correo electrónico sin conocer la escuela"],
     0, "El acompañamiento situado parte del diagnóstico local y construye capacidades en el propio terreno escolar."),

    ("La 'Justicia Educativa y Equidad Territorial' implica en este marco:",
     ["Distribuir mayores apoyos, recursos pedagógicos y foco estratégico a las escuelas en contextos de mayor vulnerabilidad",
      "Dar más presupuesto a las escuelas ricas y quitar a las escuelas pobres",
      "Cerrar las escuelas rurales para ahorrar recursos fiscales",
      "Evaluar a todos los colegios sin considerar sus condiciones de partida",
      "Exigir internet satelital donde no hay energía eléctrica"],
     0, "La equidad territorial focaliza esfuerzos y recursos donde mayores son las brechas estructurales."),

    ("El concepto de 'Capacidad Institucional' en la gestión local (Uribe et al., 2025) abarca:",
     ["El conjunto de competencias, procesos, recursos y cultura organizacional que permiten a la escuela sostener su propia mejora",
      "El número total de pupitres de madera en el depósito",
      "La cantidad de dinero en efectivo guardada en la gaveta del director",
      "El peso físico del archivo de correspondencia",
      "El tamaño del patio de cemento"],
     0, "Desarrollar capacidad institucional es asegurar que la escuela aprenda y resuelva problemas de forma autónoma y sostenible."),

    ("El rol del Director de Unidad Educativa como 'Líder en su Territorio' exige:",
     ["Generar alianzas con centros de salud, municipios, organizaciones comunitarias y sectores productivos de la zona",
      "Prohibir la entrada de cualquier institución pública al colegio",
      "Desconocer a las autoridades originarias campesinas",
      "Cobrar peaje en la puerta del establecimiento",
      "Funcionar como una isla aislada del barrio o comunidad"],
     0, "La sinergia interinstitucional en el territorio amplía las oportunidades formativas y de protección integral."),

    ("La 'Planificación Estratégica Participativa' a nivel local promueve que el Proyecto Educativo Institucional (PEI) se elabore:",
     ["Con la participación reflexiva y democrática de directivos, maestros, estudiantes, familias y líderes comunitarios",
      "Copiando y pegando el plan de un colegio extranjero de internet",
      "Comprando un plan prefabricado a una consultora privada",
      "Redactado en secreto por el director en un fin de semana sin consultar a nadie",
      "Dictado por el guardia de seguridad"],
     0, "La construcción participativa del PEI genera compromiso, pertenencia y legitimidad social comunitaria."),

    ("El monitoreo reflexivo de las metas escolares en el marco de liderazgo local se basa en ciclos de:",
     ["Planificar, actuar, observar los resultados, reflexionar colectivamente y reajustar las estrategias (mejora continua)",
      "Planificar una vez y jamás volver a revisar el documento",
      "Castigar a quienes no alcancen la meta el primer mes",
      "Cambiar de objetivos todos los días al azar",
      "Esperar que los problemas se solucionen solos"],
     0, "Los ciclos de indagación colaborativa y mejora continua fundamentan la práctica del liderazgo territorial."),

    ("En cuanto al 'Bienestar Docente y Clima Laboral', los autores destacan que la mejora educativa requiere:",
     ["Cuidar el bienestar socioemocional de las y los educadores, reconociendo su labor y brindando espacios de colaboración profesional",
      "Aumentar el acoso laboral y la sobrecarga administrativa innecesaria",
      "Prohibir que los maestros dialoguen entre ellos",
      "Eliminar los tiempos de coordinación de equipos docentes",
      "Ignorar las condiciones ergonómicas y de salud laboral"],
     0, "Docentes valorados, apoyados y motivados son el corazón de cualquier proceso de transformación educativa.")
]

# ----------------- 6.4. ESTUDIO REGIONAL COMPARATIVO Y EXPLICATIVO (ERCE 2019) -----------------
ERCE_SPECS = [
    ("¿Qué es el ERCE 2019 coordinado por el Laboratorio Latinoamericano de Evaluación de la Calidad de la Educación (LLECE) de la UNESCO?",
     ["El cuarto Estudio Regional Comparativo y Explicativo que evalúa logros de aprendizaje y factores asociados en América Latina y el Caribe",
      "Una competencia deportiva estudiantil intercolegial",
      "Un censo agropecuario de producción de quinua",
      "Una feria de ciencias escolar privada",
      "Un examen de admisión exclusivo para diplomáticos"],
     0, "El ERCE es el estudio de evaluación educativa a gran escala más representativo de la región latinoamericana."),

    ("¿Qué áreas de aprendizaje y grados evaluó el ERCE 2019?",
     ["Lectura, Matemática y Escritura en 3° y 6° de primaria, más Ciencias Naturales en 6° de primaria",
      "Física cuántica y Filosofía en último año de bachillerato",
      "Solo dibujo y música en nivel inicial",
      "Inglés y Francés en universidades",
      "Mecanografía e informática en institutos técnicos"],
     0, "Evalúa competencias fundamentales en grados clave de la educación primaria (3ro y 6to básico)."),

    ("Una de las grandes INNOVACIONES pioneras del ERCE 2019 respecto a estudios anteriores fue la evaluación de:",
     ["Habilidades Socioemocionales en estudiantes de 6° de primaria (empatía, apertura a la diversidad y autorregulación escolar)",
      "Fuerza física en levantamiento de pesas",
      "Velocidad de digitación en teclados mecánicos",
      "Memorización literal de diccionarios completos",
      "Capacidad de ahorro bancario personal"],
     0, "Por primera vez se midieron formalmente habilidades socioemocionales y su vínculo con el aprendizaje escolar."),

    ("Uno de los hallazgos explicativos más contundentes del ERCE 2019 sobre los 'Factores Asociados' al aprendizaje es que:",
     ["El Nivel Socioeconómico y Cultural de las familias sigue siendo el mayor predictor de las brechas de rendimiento escolar",
      "La marca de los cuadernos escolares determina la inteligencia del alumno",
      "Los estudiantes que tienen ojos claros aprenden más rápido",
      "El clima cálido impide aprender matemáticas",
      "La infraestructura escolar de lujo garantiza por sí sola notas perfectas"],
     0, "La desigualdad socioeconómica estructural impacta fuertemente en las oportunidades y resultados educativos."),

    ("Respecto al 'CLIMA DE AULA', el ERCE 2019 demostró empíricamente que:",
     ["Un clima de aula positivo, afectuoso y libre de violencia es el factor escolar interno con mayor impacto positivo en los aprendizajes",
      "El clima de aula no tiene ninguna relación con las notas",
      "El rigor autoritario y los gritos mejoran la comprensión lectora",
      "El aula debe mantenerse en silencio absoluto sin interacción",
      "Es mejor tener aulas sin ventanas ni iluminación"],
     0, "Sentirse seguro, respetado y apoyado en el aula es el factor escolar intra-escuela más potente para aprender."),

    ("En cuanto al 'SENTIDO DE PERTENENCIA A LA ESCUELA' de los estudiantes, el estudio concluyó que:",
     ["Los estudiantes que sienten que forman parte de su comunidad escolar y son valorados obtienen mejores resultados académicos y bienestar",
      "El sentido de pertenencia reduce el rendimiento",
      "Es irrelevante que el estudiante se sienta discriminado",
      "Solo importa el examen final memorístico",
      "La escuela debe ser vista como un lugar ajeno e incómodo"],
     0, "El apego escolar y la vinculación afectiva potencian la motivación intrínseca y la permanencia escolar."),

    ("Sobre el 'INVOLUCRAMIENTO PARENTAL Y FAMILIAR', el ERCE 2019 evidenció que:",
     ["El interés de las familias por los estudios de sus hijos, el diálogo cotidiano y el apoyo escolar impactan positivamente en el rendimiento",
      "Los padres jamás deben preguntar a sus hijos cómo les fue en la escuela",
      "El apoyo familiar no influye en nada",
      "La sobreprotección agresiva eleva las calificaciones",
      "Los estudiantes aprenden mejor si sus familias los abandonan emocionalmente"],
     0, "El acompañamiento afectivo y seguimiento formativo familiar es un factor protector fundamental."),

    ("Respecto a las habilidades socioemocionales medidas (apertura a la diversidad), el estudio reveló que:",
     ["La gran mayoría de los estudiantes muestra disposición a relacionarse y aprender de personas de orígenes y culturas diferentes",
      "Los estudiantes prefieren la segregación absoluta por etnias",
      "No existe empatía en las aulas latinoamericanas",
      "Las niñas rechazan hablar con sus compañeras",
      "El racismo es una cualidad innata e inmodificable"],
     0, "Destaca el enorme potencial de apertura cultural y empatía de las niñas y niños de la región."),

    ("El ERCE 2019 alertó que un porcentaje alarmante de estudiantes se ubica en el Nivel I (el más bajo) de desempeño, lo que exige:",
     ["Políticas urgentes de fortalecimiento de la lectura comprensiva inicial, pedagogía de la matemática y equidad en recursos",
      "Expulsar a todos los estudiantes de nivel I",
      "Eliminar la escuela primaria en el continente",
      "Suspender las evaluaciones internacionales para no ver los datos",
      "Cobrar multas a los profesores de primaria"],
     0, "Evidencia la urgencia de fortalecer las bases pedagógicas tempranas en alfabetización y pensamiento lógico."),

    ("Para el Director de Unidad Educativa, los resultados del ERCE proporcionan evidencia científica de que:",
     ["Cuidar el clima escolar, erradicar el acoso escolar y articular con las familias eleva sustancialmente el aprendizaje de sus alumnos",
      "Lo único que importa es la fiscalización de los uniformes",
      "La pedagogía no sirve frente a la disciplina militarizada",
      "Las emociones de los estudiantes deben ignorarse en el colegio",
      "La evaluación debe usarse únicamente para reprobar y excluir"],
     0, "Reafirma que la gestión del clima, la afectividad pedagógica y la inclusión son claves del éxito directivo.")
]

def get_tecnico_pedagogico_questions():
    """Genera 200 preguntas para cada uno de los 4 temas Técnico Pedagógicos."""
    results = {}
    
    topics_map = [
        ("ods4_unesco", ODS4_SPECS),
        ("lidei_2022", LIDEI_SPECS),
        ("marco_liderazgo", MARCO_SPECS),
        ("erce_2019", ERCE_SPECS)
    ]
    
    for tid, base in topics_map:
        meta = TOPICS_DICT[tid]
        specs = expand_pool_to_200(base, tid, meta["title"])
        q_list = []
        for idx, spec in enumerate(specs, 1):
            q_text, opts, ans_idx, exp = spec
            qid = f"{tid}-{idx:03d}"
            q = make_q(qid, meta, q_text, opts, ans_idx, exp)
            q_list.append(q)
        results[tid] = q_list
        
    return results

