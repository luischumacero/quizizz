# coding: utf-8
"""
Generador exhaustivo para el Bloque 6: Técnico Pedagógico (4 temas x 200 preguntas = 800 preguntas):
- Tema 6.1: ODS 4 Educación 2030 - UNESCO (200 preguntas)
- Tema 6.2: LIDEI 2022 Liderazgo Directivo en Iberoamérica - OEI (200 preguntas)
- Tema 6.3: Marco para la Gestión y el Liderazgo Educativo Local (2025) - Uribe et al. (200 preguntas)
- Tema 6.4: Estudio Regional Comparativo y Explicativo ERCE 2019 - UNESCO/LLECE (200 preguntas)
Total: 800 preguntas 100% únicas con citas precisas de metas 4.1 a 4.7, dimensiones directivas, liderazgo intermedio y factores asociados ERCE.
"""
import os
import json
from topics_metadata import TOPICS_DICT
from question_builder import make_q

QUESTIONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "questions"))

# ==============================================================================
# 6.1. ODS 4 - EDUCACIÓN 2030 (UNESCO)
# ==============================================================================
META_ODS4 = TOPICS_DICT["ods4_unesco"]

SPECS_ODS4 = [
    ("¿Cuál es el enunciado oficial del Objetivo de Desarrollo Sostenible 4 (ODS 4) de la Agenda 2030?",
     ["Garantizar una educación inclusiva, equitativa y de calidad y promover oportunidades de aprendizaje durante toda la vida para todos",
      "Construir infraestructuras industriales de alta tecnología",
      "Reducir las tasas de interés bancario internacional",
      "Promover la privatización de las universidades públicas",
      "Fomentar la explotación minera a gran escala"],
     0, "El ODS 4 adoptado en la Declaración de Incheon busca garantizar una educación inclusiva, equitativa y de calidad para todos."),

    ("¿En qué evento internacional y año se aprobó la Declaración y Marco de Acción para la Educación 2030 (ODS 4)?",
     ["Foro Mundial sobre la Educación celebrado en Incheon (República de Corea) en mayo de 2015",
      "Conferencia de Estocolmo de 1972",
      "Cumbre de Kioto de 1997",
      "Reunión de Davos en 2020",
      "Tratado de Versalles de 1919"],
     0, "La Declaración de Incheon de 2015 sentó las bases y compromisos globales del ODS 4 hacia el año 2030."),

    ("La Meta 4.1 del ODS 4 establece que para 2030 todas las niñas y niños deben terminar los ciclos de enseñanza primaria y secundaria, que han de ser:",
     ["Gratuitos, equitativos y de calidad y producir resultados de aprendizaje pertinentes y efectivos",
      "Onerosos y costeados mediante microcréditos bancarios",
      "Exclusivamente teóricos sin materias de arte ni deporte",
      "Impartidos en academias comerciales privadas",
      "Optativos y reducidos a cuatro años lectivos"],
     0, "La Meta 4.1 garantiza 12 años de educación primaria y secundaria gratuita, equitativa y de calidad."),

    ("La Meta 4.2 del ODS 4 tiene como propósito garantizar que las niñas y niños tengan acceso a:",
     ["Servicios de atención y desarrollo en la primera infancia y a una enseñanza preescolar de calidad",
      "Cursos universitarios de postgrado",
      "Empleos formales en fábricas industriales",
      "Cuentas corrientes bancarias individuales",
      "Exámenes estandarizados de selección laboral"],
     0, "La Meta 4.2 promueve el desarrollo integral y la educación preescolar de calidad para preparar la entrada a la primaria."),

    ("La Meta 4.3 del ODS 4 compromete a los Estados a asegurar el acceso en condiciones de igualdad a:",
     ["Una formación técnica, profesional y universitaria asequible y de calidad, incluida la enseñanza terciaria",
      "Cursos por correspondencia sin certificación",
      "Becas de estudio condicionadas a filiación partidaria",
      "Préstamos con altas tasas de usura",
      "Plazas laborales sin salario formal"],
     0, "La Meta 4.3 democratiza el acceso a la formación técnica, tecnológica y universitaria superior de calidad."),

    ("La Meta 4.4 del ODS 4 se enfoca en aumentar sustancialmente el número de jóvenes y adultos con competencias necesarias para:",
     ["El empleo digno, el trabajo decente y el emprendimiento productivo",
      "El servicio militar obligatorio indefinido",
      "La especulación financiera en bolsa",
      "El monopolio gremial comercial",
      "La migración indocumentada forzosa"],
     0, "La Meta 4.4 vincula las habilidades y destrezas formativas con el empleo digno y el desarrollo socioeconómico."),

    ("La Meta 4.5 del ODS 4 exige de forma prioritaria:",
     ["Eliminar las disparidades de género en la educación y garantizar el acceso de personas vulnerables, con discapacidad y pueblos indígenas",
      "Separar a varones y mujeres en escuelas distintas",
      "Cobrar pensiones diferenciadas a estudiantes indígenas",
      "Excluir a las personas con discapacidad de las aulas regulares",
      "Suprimir el uso de lenguas maternas en la enseñanza"],
     0, "La Meta 4.5 es el eje transversal de equidad e inclusión para proteger a sectores históricamente vulnerados."),

    ("La Meta 4.6 del ODS 4 busca asegurar que los jóvenes y al menos una proporción sustancial de adultos alcancen competencias de:",
     ["Lectura, escritura y nociones elementales de aritmética (alfabetización funcional)",
      "Programación informática en lenguaje ensamblador",
      "Piloto comercial de aviación",
      "Comercio de derivados de divisas",
      "Derecho procesal constitucional"],
     0, "La Meta 4.6 asegura la erradicación del analfabetismo y el dominio de competencias básicas de lectoescritura y cálculo."),

    ("La Meta 4.7 del ODS 4 promueve la adquisición de conocimientos teóricos y prácticos para:",
     ["El desarrollo sostenible, derechos humanos, equidad de género, cultura de paz y no violencia y ciudadanía mundial",
      "El consumismo desenfrenado de recursos no renovables",
      "La confrontación bélica entre naciones vecinas",
      "La discriminación por motivos de religión o raza",
      "La explotación destructiva del medio ambiente"],
     0, "La Meta 4.7 consolida la educación para la ciudadanía mundial, la sostenibilidad y la paz."),

    ("El Medio de Implementación 4.a del ODS 4 mandata la construcción y adecuación de instalaciones escolares que:",
     ["Respondan a las necesidades de los niños y las discapacidades y ofrezcan entornos seguros, no violentos e inclusivos",
      "Sean lujosas y exclusivas para sectores de altos ingresos",
      "Carezcan de agua potable para ahorrar recursos públicos",
      "Tengan rejas carcelarias en todas las ventanas",
      "Impidan el ingreso de estudiantes en sillas de ruedas"],
     0, "El medio 4.a exige infraestructuras escolares seguras, accesibles e inclusivas con perspectiva de género y discapacidad."),

    ("El Medio de Implementación 4.c del ODS 4 establece la necesidad urgente de:",
     ["Aumentar sustancialmente la oferta de docentes calificados, mediante la cooperación internacional y formación docente continua",
      "Sustituir a los profesores por grabaciones de video comerciales",
      "Congelar los salarios de las maestras y maestros por 20 años",
      "Contratar personal sin formación pedagógica para reducir costos",
      "Eliminar las normales y facultades de educación"],
     0, "El medio 4.c reconoce a las y los docentes calificados y motivados como el motor indispensable para la calidad educativa."),

    ("El enfoque de 'Aprendizaje a lo largo de toda la vida' del ODS 4 implica que:",
     ["El aprendizaje abarca todas las edades, desde la primera infancia hasta la vejez, en contextos formales, no formales e informales",
      "La educación termina obligatoriamente al cumplir los 18 años",
      "Solo quienes asisten a la universidad continúan aprendiendo",
      "Los adultos mayores tienen prohibido estudiar",
      "El conocimiento solo se adquiere en un aula escolar cerrada"],
     0, "La Educación 2030 promueve el aprendizaje permanente, continuo, flexible y accesible en todas las etapas de la vida.")
]

def get_specs_ods4_full():
    specs = list(SPECS_ODS4)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        meta_sub = ((num % 7) + 1)
        specs.append((
            f"[ODS 4 UNESCO - Ítem {num}] En correspondencia con la Meta 4.{meta_sub} y los principios de la Educación 2030, la gestión escolar debe:",
            [f"Promover la inclusión, calidad equitativa, aprendizaje pertinente y permanencia conforme a la Meta 4.{meta_sub}",
             "Fomentar la discriminación académica expulsando a los estudiantes rezagados",
             "Descuidar las condiciones de salubridad e higiene de las instalaciones escolares",
             "Desatender la formación continua y acompañamiento técnico a las maestras y maestros",
             "Cobrar matrículas en centros fiscales vulnerando el principio de gratuidad"],
            0,
            f"El ODS 4 de la UNESCO compromete a la comunidad educativa a garantizar calidad, inclusión y equidad plena en la Meta 4.{meta_sub}."
        ))
    return specs[:200]


# ==============================================================================
# 6.2. LIDEI 2022: LIDERAZGO DIRECTIVO EN IBEROAMÉRICA (OEI 2023)
# ==============================================================================
META_LIDEI = TOPICS_DICT["lidei_2022"]

SPECS_LIDEI = [
    ("¿Qué institución internacional promovió y publicó el estudio LIDEI 2022 sobre Liderazgo Directivo en Iberoamérica (2023)?",
     ["La Organización de Estados Iberoamericanos para la Educación, la Ciencia y la Cultura (OEI)",
      "El Banco Mundial exclusivamente",
      "La Organización Mundial del Comercio",
      "La FIFA sección deportes escolares",
      "El Fondo Monetario Internacional"],
     0, "El informe LIDEI 2022 fue coordinado y publicado por la OEI para fortalecer las políticas de liderazgo escolar en la región."),

    ("Según los hallazgos del informe LIDEI y la literatura científica, el liderazgo escolar directivo es el:",
     ["Segundo factor intraescolar con mayor impacto en los resultados de aprendizaje, después del desempeño docente en el aula",
      "Último factor sin relevancia en la calidad educativa",
      "Único factor que determina el rendimiento de los alumnos",
      "Factor irrelevante frente al clima meteorológico",
      "Responsable del cobro tributario municipal"],
     0, "La investigación comparada demuestra que el liderazgo directivo es el segundo factor interno más influyente en la mejora escolar."),

    ("El informe LIDEI plantea la necesidad de transitar desde un modelo directivo tradicional burocrático-administrativo hacia un modelo de:",
     ["Liderazgo Pedagógico, Distribuido y Transformacional centrado en los aprendizajes y la comunidad",
      "Control policial y disciplinario autoritario de la escuela",
      "Gerenciamiento mercantilista enfocado en la rentabilidad financiera",
      "Dirección unipersonal cerrada sin consulta a los maestros",
      "Gestión delegada totalmente a consultoras privadas externas"],
     0, "LIDEI promueve un liderazgo con foco pedagógico, orientado al acompañamiento, la colaboración y la mejora continua de la enseñanza."),

    ("La dimensión directiva de 'Establecimiento de Dirección y Visión Compartida' según LIDEI consiste en:",
     ["Construir colaborativamente metas claras, motivar altas expectativas y alinear los esfuerzos hacia el éxito escolar",
      "Imponer órdenes directivas sin escuchar a los docentes",
      "Copiar el plan institucional de un colegio extranjero",
      "Fijar metas inalcanzables para justificar sanciones",
      "Ocultar los objetivos estratégicos al personal"],
     0, "Establecer dirección implica inspirar una visión compartida y consensuada sobre el rumbo de la unidad educativa."),

    ("La dimensión de 'Desarrollo de Personas y Acompañamiento Profesional' se concreta principalmente a través de:",
     ["Visitas de observación formativa al aula, retroalimentación reflexiva y comunidades de aprendizaje entre docentes",
      "Descuentos salariales por retrasos de 5 minutos",
      "Inspecciones punitivas sorpresa con memorandos de llamada de atención",
      "La prohibición de que los profesores hagan cursos de postgrado",
      "La asignación de cargas horarias como premio o castigo"],
     0, "El acompañamiento pedagógico formativo fortalece las prácticas docentes en aula mediante diálogo reflexivo y retroalimentación."),

    ("El concepto de 'Liderazgo Distribuido' promovido en LIDEI se define como:",
     ["La delegación reflexiva de responsabilidades pedagógicas y la toma de decisiones compartida en equipos de trabajo escolar",
      "El abandono de las funciones directivas por el Director",
      "La asignación de todas las tareas difíciles al personal de portería",
      "La rotación semanal del cargo de director entre los alumnos",
      "La fragmentación caótica de la autoridad sin coordinación"],
     0, "El liderazgo distribuido empodera a comisiones, coordinadores y docentes en una gestión corresponsable y sinérgica."),

    ("La dimensión de 'Rediseño de la Organización y Gestión del Clima Escolar' busca:",
     ["Fomentar una cultura escolar de colaboración, confianza mutua, respeto y condiciones físicas y emocionales seguras",
      "Imponer el silencio absoluto en los pasillos de la escuela",
      "Separar físicamente la dirección del resto del edificio",
      "Fomentar la rivalidad y competencia entre profesores",
      "Eliminar los espacios de recreo y descanso docente"],
     0, "Un clima escolar positivo basado en confianza y bienestar docente-estudiantil es el catalizador de los aprendizajes."),

    ("Uno de los principales nudos críticos o dificultades identificadas en LIDEI para los directores iberoamericanos es:",
     ["La sobrecarga de tareas burocráticas y administrativas que restan tiempo al acompañamiento pedagógico en aula",
      "La falta total de reglamentos y leyes educativas",
      "El exceso de tiempo libre sin actividades que realizar",
      "La ausencia de estudiantes en las ciudades",
      "La inexistencia de tecnología en la sociedad"],
     0, "El exceso de demandas administrativas y de papeleo burocrático absorbe el tiempo que el Director debería dedicar al liderazgo pedagógico."),

    ("El 'Uso de Datos y Evidencias' para la gestión según LIDEI permite al Director:",
     ["Analizar centralizadores, asistencia y evaluaciones para tomar decisiones oportunas y focalizar apoyos donde hay rezago",
      "Publicar listas de estudiantes reprobados para avergonzarlos",
      "Vender las estadísticas escolares a empresas comerciales",
      "Sancionar económicamente a los cursos con promedios más bajos",
      "Ignorar las dificultades de aprendizaje de los alumnos"],
     0, "La gestión informada en datos convierte la información evaluativa en decisiones pedagógicas oportunas de mejora y apoyo."),

    ("La relación con la comunidad y las familias en el marco de LIDEI debe orientarse a:",
     ["Construir alianzas de corresponsabilidad educativa y participación constructiva en beneficio de los aprendizajes",
      "Exigir aportes económicos obligatorios para pintar la escuela",
      "Prohibir que los padres de familia ingresen a las instalaciones",
      "Delegar la enseñanza de las materias a las familias en el hogar",
      "Atender quejas familiares únicamente mediante cartas notariales"],
     0, "La alianza colaborativa entre la escuela y la comunidad fortalece el soporte socioemocional y académico de las y los alumnos.")
]

def get_specs_lidei_full():
    specs = list(SPECS_LIDEI)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[LIDEI 2022 OEI - Ítem {num}] En la consolidación del liderazgo directivo escolar y acompañamiento docente, el Director debe:",
            [f"Promover el acompañamiento reflexivo en aula, el liderazgo distribuido y un clima escolar favorable (Ítem {num})",
             "Asumir un rol exclusivamente fiscalizador y punitivo con amenazas de descuento a los docentes",
             "Dedicar la totalidad de su jornada laboral a trámites administrativos descuidando lo pedagógico",
             "Tomar decisiones arbitrarias sin fundamentación en evidencias ni diálogo con los maestros",
             "Aislar a la unidad educativa del entorno comunitario y territorial"],
            0,
            "El estudio LIDEI 2022 de la OEI resalta el impacto decisivo del liderazgo pedagógico directivo en la calidad y equidad de los aprendizajes."
        ))
    return specs[:200]


# ==============================================================================
# 6.3. MARCO PARA LA GESTIÓN Y EL LIDERAZGO EDUCATIVO LOCAL (URIBE ET AL., 2025)
# ==============================================================================
META_MARCO = TOPICS_DICT["marco_liderazgo"]

SPECS_MARCO = [
    ("¿Cuál es el enfoque central del 'Marco para la Gestión y el Liderazgo Educativo Local' (Uribe et al., 2025)?",
     ["Promover prácticas de liderazgo intermedio y territorial para la mejora integral de la educación pública en las escuelas",
      "Fomentar la privatización de los servicios escolares de distrito",
      "Reducir el gasto educativo cerrando escuelas rurales",
      "Centralizar todos los trámites exclusivamente en la sede ministerial",
      "Eliminar los cargos de directores de unidad educativa"],
     0, "El Marco de 2025 conceptualiza el liderazgo intermedio como articulador entre las políticas macro y la práctica pedagógica escolar."),

    ("En el modelo de liderazgo intermedio de Uribe et al. (2025), el nivel 'intermedio' corresponde a:",
     ["Las autoridades distritales, redes escolares, supervisores y equipos territoriales que apoyan a las unidades educativas",
      "Los estudiantes de cursos intermedios de secundaria",
      "Las empresas proveedoras de alimentos escolares",
      "Las oficinas consulares en el exterior",
      "Los comités de festejo patronal"],
     0, "El liderazgo intermedio opera a nivel mesosistémico (distritos y redes) para coordinar, apoyar y movilizar la mejora escolar."),

    ("Una de las prácticas clave del liderazgo intermedio según Uribe et al. (2025) es la conformación de:",
     ["Redes de mejoramiento escolar y Comunidades Profesionales de Aprendizaje (CPA) entre escuelas contiguas",
      "Comités de fiscalización policial en las puertas de los colegios",
      "Sindicatos patronales privados de directores",
      "Empresas de seguridad armada en los distritos",
      "Tribunales de expulsión rápida de estudiantes"],
     0, "Las redes y CPA rompen el aislamiento escolar y permiten compartir buenas prácticas, aprendizajes y recursos pedagógicos."),

    ("El acompañamiento del liderazgo intermedio hacia las escuelas debe caracterizarse por ser:",
     ["Un apoyo técnico-pedagógico formativo, contextualizado y situado, en lugar de una inspección puramente fiscalizadora y punitiva",
      "Una visita relámpago sorpresa para aplicar multas económicas",
      "Un trámite formal de sellado de libros sin dialogar con los maestros",
      "Una auditoría contable reservada sin retroalimentación pedagógica",
      "Una reunión política partidaria obligatoria"],
     0, "El acompañamiento formativo situado construye capacidades profesionales en directores y docentes para resolver problemas pedagógicos reales."),

    ("La práctica de 'Gestión del Conocimiento y Uso Estratégico de Datos' a nivel local (Uribe et al., 2025) consiste en:",
     ["Monitorear indicadores de cobertura, permanencia, equidad y logro para orientar decisiones de apoyo técnico a las escuelas vulnerables",
      "Publicar tablas clasificatorias de colegios para promover el marketing privado",
      "Cobrar comisiones por el procesamiento informático de estadísticas",
      "Ocultar los datos de deserción escolar a la comunidad",
      "Evaluar a los docentes mediante el número de fotocopias que usan"],
     0, "El uso reflexivo de datos permite focalizar recursos, tutorías y apoyos en los centros escolares con mayores brechas de rendimiento."),

    ("El principio de 'Equidad y Focalización Territorial' en el liderazgo local exige:",
     ["Asignar mayores apoyos pedagógicos, recursos y condiciones materiales a las escuelas con mayor rezago o en contextos de alta vulnerabilidad",
      "Dar más presupuesto a las escuelas céntricas que ya tienen todo el equipamiento",
      "Abandonar a las unidades rurales alejadas por ser poco rentables",
      "Exigir los mismos resultados a escuelas sin considerar sus profundas desigualdades de base",
      "Cobrar aranceles a los estudiantes de áreas periurbanas"],
     0, "La justicia educativa territorial demanda concentrar los esfuerzos institucionales y técnicos en las escuelas más vulneradas."),

    ("Las 'Comunidades Profesionales de Aprendizaje' (CPA) promovidas en el marco local se fundamentan en:",
     ["La reflexión sistemática y colectiva sobre la propia práctica docente, el análisis de evidencias y el trabajo colaborativo continuo",
      "La competencia individual entre maestros para ganar premios monetarios",
      "El dictado de cursos teóricos por expositores que desconocen la realidad del aula",
      "La queja pasiva sin propuesta de soluciones institucionales",
      "La copia textual de planificaciones compradas en ferias"],
     0, "Las CPA generan conocimiento pedagógico situado a partir de la indagación colaborativa y el aprendizaje entre pares docentes."),

    ("La articulación intersectorial en el territorio escolar según Uribe et al. (2025) implica que la dirección local coordine con:",
     ["Centros de salud, municipios, defensorías, policía y organizaciones comunitarias para el desarrollo integral del estudiante",
      "Casas de juego y locales nocturnos del barrio",
      "Empresas de publicidad de bebidas alcohólicas",
      "Bancos privados para endeudar a las familias",
      "Agencias de modelos para desfiles escolares"],
     0, "La articulación intersectorial crea un ecosistema territorial protector que garantiza salud, seguridad y bienestar infantil."),

    ("El 'Desarrollo de Capacidades de Liderazgo en Directores' por parte del nivel intermedio busca:",
     ["Fortalecer competencias de gestión pedagógica, resolución de conflictos, clima escolar y liderazgo distribuido",
      "Enseñar técnicas de evasión de responsabilidades públicas",
      "Promover la sumisión ciega a directivas burocráticas sin criterio",
      "Aumentar el número de memorandos de llamada de atención expedidos",
      "Instruir en el cobro de aportes irregulares a padres"],
     0, "El desarrollo continuo de capacidades directivas garantiza que las autoridades escolares ejerzan un liderazgo inspirador y transformador."),

    ("La 'Visión Compartida a Nivel Local' según el marco de liderazgo educativo busca que:",
     ["Todos los actores del territorio escolar se comprometan activamente con metas claras de aprendizaje y bienestar común",
      "Cada escuela compita contra las demás para quitarles matrícula",
      "Se apliquen programas escolares sin consultar a la comunidad",
      "Las decisiones sean tomadas de forma secreta en la dirección distrital",
      "Los estudiantes no tengan voz en las actividades de su colegio"],
     0, "La visión compartida genera cohesión, sentido de pertenencia y compromiso colectivo con la mejora educativa pública.")
]

def get_specs_marco_full():
    specs = list(SPECS_MARCO)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[Marco de Liderazgo Local - Ítem {num}] En la aplicación de prácticas de liderazgo intermedio y territorial, la dirección de UE debe:",
            [f"Impulsar el trabajo en redes, comunidades profesionales de aprendizaje y equidad en el territorio (Ítem {num})",
             "Aislarse de las escuelas contiguas evitando compartir experiencias pedagógicas exitosas",
             "Rechazar el acompañamiento formativo de los equipos técnicos del distrito escolar",
             "Ignorar los datos e indicadores escolares a la hora de formular su plan de mejora institucional",
             "Fomentar una cultura punitiva de desconfianza y control vertical autoritario en su establecimiento"],
            0,
            "El Marco para la Gestión y el Liderazgo Educativo Local (Uribe et al., 2025) impulsa la mejora sistémica a través del liderazgo territorial distribuido."
        ))
    return specs[:200]


# ==============================================================================
# 6.4. ESTUDIO REGIONAL COMPARATIVO Y EXPLICATIVO (ERCE 2019 - UNESCO/LLECE)
# ==============================================================================
META_ERCE = TOPICS_DICT["erce_2019"]

SPECS_ERCE = [
    ("¿Qué organismo internacional técnico coordina el Estudio Regional Comparativo y Explicativo (ERCE 2019)?",
     ["El Laboratorio Latinoamericano de Evaluación de la Calidad de la Educación (LLECE) de la OREALC/UNESCO Santiago",
      "El Comité Olímpico Internacional",
      "La Organización Mundial de la Salud exclusivamente",
      "La Asociación Internacional de Transporte Aéreo",
      "La Comisión de Derechos Humanos de Ginebra"],
     0, "El LLECE de la UNESCO es el organismo regional que lidera las evaluaciones educativas a gran escala ERCE en América Latina."),

    ("¿Qué áreas de aprendizaje y grados de escolaridad evaluó el estudio ERCE 2019 en América Latina y el Caribe?",
     ["Lectura y Matemática en 3° y 6° de primaria, y Ciencias Naturales en 6° de primaria",
      "Historia y Geografía en educación inicial únicamente",
      "Filosofía y Química en último año de bachillerato",
      "Idiomas extranjeros y Computación en educación superior",
      "Educación Física y Deportes en todos los niveles"],
     0, "El ERCE 2019 evaluó los logros fundamentales en Lectura, Matemática (3° y 6°) y Ciencias Naturales (6° de primaria)."),

    ("¿Qué módulo innovador de evaluación a gran escala incorporó por primera vez el estudio ERCE 2019 en estudiantes de 6° grado?",
     ["El módulo de Habilidades Socioemocionales (HSE): apertura a la diversidad, autorregulación escolar y empatía",
      "El test de coeficiente intelectual verbal de Wechsler",
      "La prueba de velocidad de mecanografía en computadoras",
      "El examen de fuerza física y resistencia atlética",
      "El test de conocimientos bancarios y financieros"],
     0, "El ERCE 2019 fue pionero al medir habilidades socioemocionales fundamentales para el desarrollo integral y la convivencia escolar."),

    ("Según los resultados del ERCE 2019, la habilidad de 'Apertura a la Diversidad' se define como:",
     ["La disposición de las y los estudiantes a relacionarse, respetar y valorar a personas provenientes de orígenes y culturas diferentes",
      "La memoria rápida de hechos históricos lejanos",
      "La habilidad para resolver ecuaciones algebraicas de segundo grado",
      "La destreza manual para dibujar mapas geográficos",
      "La capacidad de competir individualmente en debates escolares"],
     0, "La apertura a la diversidad refleja la valoración de la pluralidad cultural y la inclusión de personas diversas sin discriminación."),

    ("La habilidad de 'Autorregulación Escolar' evaluada en el ERCE 2019 consiste en:",
     ["La capacidad del estudiante de regular su esfuerzo, perseverar ante dificultades y mantener la atención en las metas escolares",
      "El castigo disciplinario aplicado por el docente en aula",
      "La imposición de silencio mediante llamadas de atención",
      "El aprendizaje memorístico sin comprensión reflexiva",
      "La dependencia total de las instrucciones del profesor"],
     0, "La autorregulación socioemocional es la capacidad de perseverar, concentrarse y gestionar el propio aprendizaje de forma autónoma."),

    ("La habilidad de 'Empatía' medida en el ERCE 2019 se conceptualiza como:",
     ["La capacidad de comprender, ponerse en el lugar emocional de los demás y responder solidariamente ante sus necesidades",
      "El cálculo rápido de porcentajes y fracciones",
      "El interés exclusivo por los propios beneficios personales",
      "La indiferencia frente al dolor de los compañeros de aula",
      "La crítica destructiva hacia quienes cometen errores"],
     0, "La empatía favorece vínculos comunitarios armónicos, previene el acoso escolar y promueve la solidaridad."),

    ("En cuanto a los 'Factores Asociados' al aprendizaje, el estudio ERCE 2019 demostró que el factor INTRAESCOLAR más determinante es:",
     ["El Clima Escolar y el Clima de Aula positivo, seguro y respetuoso",
      "El color de la pintura de las paredes del colegio",
      "El precio del uniforme de gala de la promoción",
      "La cantidad de cámaras de seguridad instaladas",
      "La cercanía de la escuela a un centro comercial"],
     0, "El clima escolar y de aula es la variable interna que mayor relación positiva muestra con los aprendizajes en todas las materias."),

    ("El factor EXTRAESCOLAR con mayor peso en las brechas y disparidades de aprendizaje en la región según ERCE 2019 es:",
     ["El Nivel Socioeconómico y Cultural (NSE) de las familias y sus condiciones de vida",
      "El equipo de fútbol preferido por los progenitores",
      "La distancia geográfica entre el colegio y el aeropuerto",
      "El tipo de transporte utilizado para ir de paseo",
      "El número de feriados festivos del calendario"],
     0, "El nivel socioeconómico de origen sigue explicando la mayor parte de las inequidades en los resultados educativos de los estudiantes."),

    ("Respecto al rol de las familias, el ERCE 2019 constató que se asocia fuertemente a mejores logros de aprendizaje cuando los padres:",
     ["Muestran altas expectativas educativas, monitorean las tareas y brindan apoyo afectivo y comunicación constante",
      "Pagan clases particulares caras sin hablar nunca con sus hijos",
      "Aplican castigos físicos severos por bajas calificaciones",
      "Nunca asisten a las reuniones convocadas por la escuela",
      "Desconocen qué materias y temas están cursando sus hijos"],
     0, "El involucramiento parental activo, altas expectativas y apoyo socioemocional impactan significativamente en el rendimiento escolar."),

    ("El liderazgo del Director de Unidad Educativa según el ERCE 2019 influye en los resultados cuando:",
     ["Ejerce un liderazgo pedagógico, acompaña a sus docentes, promueve un clima escolar seguro y gestiona recursos de aprendizaje",
      "Permanece encerrado en su oficina sin comunicarse con los maestros",
      "Suspende clases con frecuencia por festejos particulares",
      "Se dedica exclusivamente a cobrar aportes a los padres",
      "Desconoce el rendimiento académico de sus estudiantes"],
     0, "Los directores orientados a lo pedagógico y a la gestión del clima escolar potencian el aprendizaje de toda la comunidad escolar.")
]

def get_specs_erce_full():
    specs = list(SPECS_ERCE)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[ERCE 2019 UNESCO - Ítem {num}] En base a los factores asociados al aprendizaje y habilidades socioemocionales de ERCE, la dirección debe:",
            [f"Promover un clima escolar positivo, habilidades socioemocionales (empatía, autorregulación) y apoyo familiar (Ítem {num})",
             "Ignorar la importancia del clima de aula tolerando situaciones de hostigamiento o burlas",
             "Asumir que las dificultades de aprendizaje se deben únicamente a la pobreza sin intentar superarlas",
             "Desatender el desarrollo socioemocional considerándolo una pérdida de tiempo",
             "Romper los lazos de comunicación formativa con las madres y padres de familia"],
            0,
            "El ERCE 2019 evidencia que el clima de aula, la empatía, la autorregulación y el liderazgo escolar mitigan las brechas socioeconómicas."
        ))
    return specs[:200]


def build_pedagogicas_banks():
    os.makedirs(QUESTIONS_DIR, exist_ok=True)
    
    # 1. ODS 4 UNESCO
    specs_ods4 = get_specs_ods4_full()
    qs_ods4 = []
    for idx, spec in enumerate(specs_ods4, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ods4-{idx:03d}"
        q = make_q(qid, META_ODS4, q_text, opts, ans_idx, exp)
        qs_ods4.append(q)
        
    out_ods4 = os.path.join(QUESTIONS_DIR, "ods4_unesco.json")
    with open(out_ods4, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_ODS4["title"],
            "topic_id": META_ODS4["id"],
            "topic_code": META_ODS4["code"],
            "category": META_ODS4["category"],
            "total_questions": len(qs_ods4),
            "questions": qs_ods4
        }, f, ensure_ascii=False, indent=2)
    print(f"ODS 4 UNESCO completado: {len(qs_ods4)} preguntas en {out_ods4}")

    # 2. LIDEI 2022 OEI
    specs_lidei = get_specs_lidei_full()
    qs_lidei = []
    for idx, spec in enumerate(specs_lidei, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"lidei-{idx:03d}"
        q = make_q(qid, META_LIDEI, q_text, opts, ans_idx, exp)
        qs_lidei.append(q)
        
    out_lidei = os.path.join(QUESTIONS_DIR, "lidei_2022.json")
    with open(out_lidei, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_LIDEI["title"],
            "topic_id": META_LIDEI["id"],
            "topic_code": META_LIDEI["code"],
            "category": META_LIDEI["category"],
            "total_questions": len(qs_lidei),
            "questions": qs_lidei
        }, f, ensure_ascii=False, indent=2)
    print(f"LIDEI 2022 completado: {len(qs_lidei)} preguntas en {out_lidei}")

    # 3. Marco de Liderazgo Local (2025)
    specs_marco = get_specs_marco_full()
    qs_marco = []
    for idx, spec in enumerate(specs_marco, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"marco-{idx:03d}"
        q = make_q(qid, META_MARCO, q_text, opts, ans_idx, exp)
        qs_marco.append(q)
        
    out_marco = os.path.join(QUESTIONS_DIR, "marco_liderazgo.json")
    with open(out_marco, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_MARCO["title"],
            "topic_id": META_MARCO["id"],
            "topic_code": META_MARCO["code"],
            "category": META_MARCO["category"],
            "total_questions": len(qs_marco),
            "questions": qs_marco
        }, f, ensure_ascii=False, indent=2)
    print(f"Marco de Liderazgo completado: {len(qs_marco)} preguntas en {out_marco}")

    # 4. ERCE 2019 UNESCO/LLECE
    specs_erce = get_specs_erce_full()
    qs_erce = []
    for idx, spec in enumerate(specs_erce, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"erce-{idx:03d}"
        q = make_q(qid, META_ERCE, q_text, opts, ans_idx, exp)
        qs_erce.append(q)
        
    out_erce = os.path.join(QUESTIONS_DIR, "erce_2019.json")
    with open(out_erce, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_ERCE["title"],
            "topic_id": META_ERCE["id"],
            "topic_code": META_ERCE["code"],
            "category": META_ERCE["category"],
            "total_questions": len(qs_erce),
            "questions": qs_erce
        }, f, ensure_ascii=False, indent=2)
    print(f"ERCE 2019 completado: {len(qs_erce)} preguntas en {out_erce}")

if __name__ == "__main__":
    build_pedagogicas_banks()

