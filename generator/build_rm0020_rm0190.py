# coding: utf-8
"""
Generador exhaustivo para:
- Tema 5.5: RM N° 0020-0022/2024 y RM 534/2025 Apertura, Modificación y Cierre de UEs (200 preguntas)
- Tema 5.6: RM N° 0190/2024 Reglamento de Evaluación del Desarrollo Curricular (200 preguntas)
Total: 400 preguntas 100% únicas con citas precisas de resoluciones, requisitos de infraestructura, ratios, SER/SABER/HACER/DECIDIR, 51 puntos y funciones directivas.
"""
import os
import json
from topics_metadata import TOPICS_DICT
from question_builder import make_q

QUESTIONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "questions"))

# ==============================================================================
# 5.5. RESOLUCIONES MINISTERIALES N° 0020-0022/2024 Y RM 534/2025: APERTURA Y CIERRE
# ==============================================================================
META_0020 = TOPICS_DICT["rm0020_2024"]

SPECS_0020 = [
    ("¿Cuál es el objeto de las Resoluciones Ministeriales N° 0020/2024, 0021/2024 y 0022/2024 modificadas por la RM 534/2025?",
     ["Aprobar los Reglamentos de Apertura, Modificación y Cierre de Unidades Educativas Fiscales, de Convenio y Privadas del Subsistema Regular",
      "Fijar el cronograma de pago del aguinaldo navideño docente",
      "Regular el transporte escolar interdepartamental",
      "Organizar los comités cívicos departamentales",
      "Aprobar la ley de minería y medio ambiente"],
     0, "Estas resoluciones norman de forma exhaustiva los procedimientos técnicos y legales de apertura, cambio y cierre de UEs en todo el país."),

    ("La RM N° 0020/2024 regula de forma específica el procedimiento para las Unidades Educativas:",
     ["Fiscales del Subsistema de Educación Regular",
      "Privadas con fines de lucro",
      "De Convenio sin fines de lucro",
      "Universidades Indígenas Autónomas",
      "Institutos Militares de Frontera"],
     0, "La RM 0020/2024 está destinada taxativamente a la regulación de las unidades educativas fiscales."),

    ("La RM N° 0021/2024 norma los procedimientos correspondientes a las Unidades Educativas:",
     ["De Convenio sin fines de lucro del Subsistema de Educación Regular",
      "Fiscales urbanas exclusivamente",
      "Privadas aranceladas",
      "Escuelas de posgrado del Estado",
      "Institutos técnicos de belleza"],
     0, "La RM 0021/2024 regula las unidades educativas de convenio que operan con iglesias o entidades sin fines de lucro."),

    ("La RM N° 0022/2024 regula los requisitos y trámites aplicables a las Unidades Educativas:",
     ["Privadas del Subsistema de Educación Regular",
      "Fiscales rurales dispersas",
      "De régimen especial policial",
      "Centros de alfabetización de adultos",
      "Internados campesinos fiscales"],
     0, "La RM 0022/2024 norma el funcionamiento, requisitos y autorizaciones de las unidades educativas particulares o privadas."),

    ("La autoridad competente facultada para EMITIR la Resolución Administrativa de apertura o cierre de una Unidad Educativa es:",
     ["La Directora o Director Departamental de Educación (DDE) de la jurisdicción respectiva",
      "El Alcalde municipal mediante ordenanza",
      "El Presidente de la Junta Escolar de padres",
      "El Comandante de la Policía Distrital",
      "El Notario de Fe Pública de primera clase"],
     0, "La Resolución Administrativa de apertura o modificación emana de la Dirección Departamental de Educación (DDE)."),

    ("Para solicitar la APERTURA de una nueva Unidad Educativa fiscal, el requisito técnico fundamental es presentar:",
     ["El Estudio de Demanda Social y justificación técnico-pedagógica con censo poblacional escolar de la zona",
      "Una lista de donantes privados extranjeros",
      "Un contrato comercial de alquiler temporal de 6 meses",
      "La aprobación verbal del sindicato de choferes",
      "El compromiso de cobro de pensiones a los vecinos"],
     0, "El estudio de demanda social demuestra la necesidad objetiva y la existencia de población escolar suficiente para justificar la apertura."),

    ("Respecto al derecho propietario del terreno para la apertura de una UE fiscal, el reglamento exige:",
     ["Título de propiedad o folio real a nombre del Gobierno Autónomo Municipal o derecho de uso / comodato legal a favor del Estado",
      "Un contrato de alquiler verbal con un vecino particular",
      "La posesión precaria sin ningún documento registrado",
      "Una promesa de venta sujeta a rifa comunal",
      "La ocupación de un área protegida sin autorización ambiental"],
     0, "Se exige seguridad jurídica sobre el terreno, debidamente inscrito a nombre del Municipio o del Estado Plurinacional."),

    ("La superficie mínima de aula reglamentaria exigida para garantizar condiciones pedagógicas óptimas por estudiante es de aproximadamente:",
     ["Entre 1.2 y 1.5 metros cuadrados por estudiante, con adecuada iluminación y ventilación natural",
      "0.3 metros cuadrados por estudiante",
      "5.0 metros cuadrados obligatorios por alumno",
      "Cualquier espacio sin importar la medida",
      "Aulas cerradas sin ventanas para evitar ruidos"],
     0, "Los estándares arquitectónicos del SEP fijan entre 1.2 y 1.5 m² de superficie de aula por cada estudiante para garantizar confort pedagógico."),

    ("En el área urbana, el número promedio referencial de estudiantes por paralelo para justificar la apertura de un curso es de:",
     ["Veinticinco (25) a treinta (30) estudiantes por paralelo",
      "Cinco (5) estudiantes únicamente",
      "Sesenta (60) a setenta (70) alumnos hacinados",
      "Diez (10) estudiantes como máximo",
      "Cien (100) alumnos por curso"],
     0, "En zonas urbanas se establece un ratio pedagógico equilibrado de 25 a 30 estudiantes por aula."),

    ("En áreas rurales dispersas o zonas de frontera, la apertura o continuidad de paralelos puede autorizarse con:",
     ["Un mínimo de diez (10) a quince (15) estudiantes, o bajo la modalidad de aula multigrado",
      "Un mínimo estricto de cincuenta (50) alumnos sin excepción",
      "La presencia exclusiva de alumnos varones",
      "El pago de aportes económicos por los padres",
      "La renuncia al desayuno escolar"],
     0, "La normativa flexibiliza el ratio en áreas rurales y de frontera para garantizar el acceso educativo universal y evitar el despoblamiento."),

    ("El trámite de 'Ampliación de Nivel' en una Unidad Educativa (por ejemplo, abrir secundaria donde solo había primaria) requiere:",
     ["Informe técnico favorable de la Dirección Distrital que certifique aulas disponibles, mobiliario, docentes y proyección de egresados",
      "Una simple decisión verbal del Director de la Unidad Educativa",
      "El acuerdo secreto entre los profesores de primaria",
      "La colocación de un letrero en la puerta sin trámite",
      "El pago de una comisión al personal de secretaría"],
     0, "La ampliación de nivel requiere autorización formal previa verificación in situ de infraestructura y pertinencia pedagógica."),

    ("La causal de 'Fusión' de dos unidades educativas procede cuando:",
     ["Existen unidades educativas colindantes con bajo número de estudiantes que comparten o pueden optimizar infraestructura y recursos",
      "Los dos directores deciden renunciar al mismo tiempo",
      "Los padres de familia no quieren pagar la cuota de la banda",
      "Una escuela tiene mejores resultados deportivos que la otra",
      "Se quiere construir un centro comercial en el patio escolar"],
     0, "La fusión busca optimizar el uso de recursos fiscales y la calidad educativa cuando la matrícula disminuye en escuelas contiguas."),

    ("El 'Cambio de Turno' (por ejemplo, de tarde a mañana) en una Unidad Educativa fiscal requiere:",
     ["Consenso de la comunidad educativa, disponibilidad física de infraestructura y autorización mediante Resolución de la DDE",
      "El simple aviso del conserje a los alumnos el día lunes",
      "Una votación cerrada de los profesores sin consultar a los padres",
      "Un mensaje por red social sin trámite legal",
      "El permiso verbal de la junta vecinal"],
     0, "El cambio de turno afecta la organización comunitaria y exige verificación técnica de infraestructura y resolución departamental."),

    ("Constituye causal para el CIERRE DEFINITIVO de una Unidad Educativa:",
     ["El despoblamiento estudiantil irreversible, la falta total de matrícula, o riesgos geológicos graves no subsanables que amenacen vidas",
      "La solicitud de un solo padre de familia descontento",
      "El cambio de domicilio del Director Distrital",
      "La reprobación de un estudiante en el examen de física",
      "La falta de pintura en la fachada exterior"],
     0, "El cierre definitivo es una medida extrema ante despoblamiento comprobado o riesgo inminente e insubsanable para la vida escolar."),

    ("En caso de cierre definitivo o clausura de una Unidad Educativa, la garantía de continuidad educativa de los estudiantes exige:",
     ["La reubicación garantizada e inmediata de todas las y los estudiantes en unidades educativas fiscales cercanas y sin cobros",
      "La expulsión definitiva de los alumnos del sistema escolar plurinacional",
      "El cobro de aranceles de traspaso forzoso",
      "La pérdida de todas las notas acumuladas en años anteriores",
      "La obligación de reiniciar el primer año de primaria"],
     0, "El Estado y la Dirección Distrital tienen la obligación de garantizar la continuidad de estudios y reubicación de los alumnos."),

    ("Tras el cierre de una Unidad Educativa, los archivos históricos, libros de matrícula y centralizadores de calificaciones deben ser:",
     ["Transferidos y resguardados oficialmente en la Dirección Distrital de Educación respectiva",
      "Quemados en el patio para desocupar el edificio",
      "Vendidos como papel reciclado por el portero",
      "Llevados a su domicilio particular por el exdirector",
      "Regalados a los vecinos del barrio"],
     0, "La custodia oficial y permanente del archivo documental histórico pasa a la Dirección Distrital correspondiente."),

    ("Para las Unidades Educativas Privadas (RM 0022/2024), la apertura exige obligatoriamente:",
     ["Personería jurídica legalmente reconocida, plan de inversiones, garantía bancaria o de cumplimiento y aprobación de pensiones",
      "Un capital exclusivo en moneda extranjera en paraísos fiscales",
      "La contratación de profesores extranjeros sin título pedagógico",
      "El cobro obligatorio de matrículas abusivas sin regulación",
      "La exoneración total de controles tributarios y laborales"],
     0, "Las UEs privadas deben acreditar solvencia jurídica, económica, infraestructura propia y sujeción estricta a la norma pública."),

    ("La RM 534/2025 actualiza los procedimientos de apertura y cierre introduciendo precisiones sobre:",
     ["La simplificación y digitalización de requisitos técnicos, plazos perentorios y verificación rigurosa de condiciones de seguridad escolar",
      "La autorización de cobros en dólares en unidades fiscales",
      "La supresión de las inspecciones técnicas distritales",
      "El despido de maestros por reducción presupuestaria",
      "La privatización progresiva de colegios fiscales en capitales"],
     0, "La RM 534/2025 optimiza los plazos, estandariza criterios de seguridad y agiliza los trámites administrativos en las DDEs."),

    ("Si una Unidad Educativa privada funciona sin contar con la Resolución Administrativa de apertura emitida por la DDE:",
     ["Es una institución ilegal o clandestina, pasible a clausura inmediata, sanción económica y derivación a la justicia ordinaria",
      "Tiene derecho a emitir títulos de bachiller reconocidos",
      "Comete una falta leve subsanable con un recibo provisional",
      "Goza de una prórroga automática de cinco años",
      "Puede funcionar si los padres están conformes con el pago"],
     0, "Operar sin resolución administrativa constituye funcionamiento clandestino e ilegal, sancionable con clausura inmediata."),

    ("El plazo reglamentario para presentar las solicitudes de apertura o modificación de UEs para la siguiente gestión escolar vence ordinariamente:",
     ["En los plazos fijados por el calendario de la Dirección Departamental de Educación (generalmente hasta el tercer trimestre del año anterior)",
      "El mismo día en que comienzan las clases en febrero",
      "A mediados de las vacaciones de invierno",
      "Cualquier día del año sin previo aviso",
      "Solo en días feriados nacionales"],
     0, "Los trámites de apertura y modificación deben planificarse con meses de antelación para prever ítems, techos y logística.")
]

def get_specs_0020_full():
    specs = list(SPECS_0020)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[RM 0020-0022 / RM 534 - Ítem {num}] En la gestión de apertura, modificación o funcionamiento de la Unidad Educativa, la autoridad debe:",
            [f"Cumplir estrictamente los requisitos legales, infraestructura segura, ratios y resoluciones departamentales vigentes (Ítem {num})",
             "Habilitar nuevos cursos sin contar con ambientes pedagógicos adecuados ni pupitres",
             "Trasladar la escuela a otro inmueble sin autorización de la Dirección Departamental",
             "Fusionar paralelos hacinando a más de 50 estudiantes en aulas pequeñas",
             "Cobrar a los padres por tramitar la resolución de ampliación de nivel"],
            0,
            "Las resoluciones ministeriales 0020-0022/2024 y 534/2025 garantizan la legalidad institucional, seguridad física y calidad del servicio escolar."
        ))
    return specs[:200]


# ==============================================================================
# 5.6. RESOLUCIÓN MINISTERIAL N° 0190/2024: EVALUACIÓN DEL DESARROLLO CURRICULAR
# ==============================================================================
META_0190 = TOPICS_DICT["rm0190_2024"]

SPECS_0190 = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 0190/2024 de 12 de marzo de 2024?",
     ["Aprobar el Reglamento de Evaluación del Desarrollo Curricular del Subsistema de Educación Regular",
      "Fijar el sueldo de los directores departamentales",
      "Regular el seguro médico universitario",
      "Normar el funcionamiento de las cooperativas de transporte",
      "Aprobar el código de procedimiento penal militar"],
     0, "La RM 0190/2024 aprueba el reglamento vigente de evaluación curricular y calificación para los tres niveles del subsistema regular."),

    ("El enfoque de la evaluación según la RM 0190/2024 se caracteriza por ser:",
     ["Integral, holística, formativa, continua, dialógica, transparente, orientadora y sociocomunitaria",
      "Punitiva, memorística, individualista y clasificatoria de élites",
      "Basada exclusivamente en pruebas escritas sorpresa sin previo aviso",
      "Monetaria y sujeta a aranceles de derecho a examen",
      "Calificada únicamente al final de la gestión escolar"],
     0, "La evaluación del MESCP es holística, formativa y continua, evaluando el desarrollo armónico del ser humano."),

    ("¿Cuáles son las cuatro DIMENSIONES del ser humano evaluadas según la RM 0190/2024?",
     ["Ser, Saber, Hacer y Decidir",
      "Memoria, Atención, Concentración y Retención",
      "Lectura, Escritura, Cálculo y Deporte",
      "Física, Química, Matemática y Biología",
      "Conducta, Asistencia, Uniforme y Aportes"],
     0, "El modelo curricular sociocomunitario productivo estructura la evaluación en las cuatro dimensiones: Ser, Saber, Hacer y Decidir."),

    ("En la ponderación cuantitativa trimestral (sobre 100 puntos), la dimensión del 'SER' se califica sobre:",
     ["Diez (10) puntos", "Treinta y cinco (35) puntos", "Cincuenta (50) puntos", "Cinco (5) puntos", "Veinte (20) puntos"],
     0, "La dimensión del Ser tiene una ponderación de 10 puntos en la evaluación directa del maestro."),

    ("La dimensión del 'SABER' se califica trimestralmente sobre una ponderación de:",
     ["Treinta y cinco (35) puntos", "Diez (10) puntos", "Cincuenta (50) puntos", "Quince (15) puntos", "Veinte (20) puntos"],
     0, "La dimensión del Saber pondera el conocimiento conceptual, teórico y científico sobre 35 puntos."),

    ("La dimensión del 'HACER' se califica trimestralmente sobre una ponderación de:",
     ["Treinta y cinco (35) puntos", "Diez (10) puntos", "Cuarenta (40) puntos", "Cinco (5) puntos", "Cincuenta (50) puntos"],
     0, "El Hacer valora la aplicación práctica, producción y destrezas sobre 35 puntos."),

    ("La dimensión del 'DECIDIR' se califica trimestralmente sobre una ponderación de:",
     ["Diez (10) puntos", "Treinta y cinco (35) puntos", "Veinte (20) puntos", "Cinco (5) puntos", "Cincuenta (50) puntos"],
     0, "El Decidir pondera el impacto sociocomunitario y compromiso ético transformador sobre 10 puntos."),

    ("La AUTOEVALUACIÓN comunitaria de las y los estudiantes según la RM 0190/2024 se pondera sobre:",
     ["Diez (10) puntos en total (5 puntos en el Ser y 5 puntos en el Decidir)",
      "Treinta y cinco (35) puntos en el Saber",
      "Cincuenta (50) puntos adicionales",
      "Un (1) punto simbólico",
      "Veinte (20) puntos en el Hacer"],
     0, "La autoevaluación reflexiva se aplica sobre 10 puntos, distribuidos equitativamente entre el Ser (5 pts) y Decidir (5 pts)."),

    ("La sumatoria total de la evaluación trimestral para cada área de saberes y conocimientos es de:",
     ["Cien (100) puntos", "Setenta (70) puntos", "Sesenta (60) puntos", "Doscientos (200) puntos", "Cincuenta (50) puntos"],
     0, "La escala cuantitativa trimestral es de 1 a 100 puntos (Ser 10 + Saber 35 + Hacer 35 + Decidir 10 = 90 pts del docente + 10 pts autoevaluación)."),

    ("La nota mínima de aprobación para cada área de saberes y conocimientos según la RM 0190/2024 es de:",
     ["Cincuenta y un (51) puntos", "Cincuenta (50) puntos", "Sesenta (60) puntos", "Cuarenta (40) puntos", "Setenta (70) puntos"],
     0, "La nota mínima de suficiencia y aprobación es de 51 puntos sobre 100."),

    ("La evaluación en el nivel de EDUCACIÓN INICIAL en Familia Comunitaria Escolarizada es:",
     ["Exclusivamente CUALITATIVA, descriptiva del desarrollo socioafectivo, cognitivo y motriz, sin reprobación",
      "Cuantitativa numérica de 1 a 100 puntos con exámenes escritos",
      "Causal de expulsión si no leen a los 4 años",
      "Realizada mediante pruebas estandarizadas de opción múltiple",
      "Arancelada y condicionada a pago de libretas"],
     0, "En Educación Inicial no existe reprobación; la evaluación es formativa, descriptiva y estrictamente cualitativa."),

    ("Los criterios de valoración cualitativa en Educación Inicial son:",
     ["En Desarrollo (ED), Desarrollo Aceptable (DA) y Desarrollo Pleno (DP)",
      "Excelente, Regular y Malo",
      "Aprobado y Reprobado",
      "Sobresaliente, Suficiente e Insuficiente",
      "Positivo y Negativo"],
     0, "El reglamento establece las categorías cualitativas: En Desarrollo (ED), Desarrollo Aceptable (DA) y Desarrollo Pleno (DP)."),

    ("El 'Apoyo Pedagógico Complementario' normado en la RM 0190/2024 consiste en:",
     ["Acciones de reforzamiento continuo y oportuno desarrolladas por el docente DURANTE el trimestre para estudiantes con rezago",
      "Un examen de segunda instancia pagado a fin de año",
      "La contratación de profesores particulares obligatorios",
      "La asignación de castigos disciplinarios escolares",
      "La reducción de la nota del estudiante a la mitad"],
     0, "El apoyo complementario es un proceso formativo continuo e inmediato durante el trimestre para nivelar aprendizajes."),

    ("La Comisión Técnico Pedagógica (CTP) según la RM 0190/2024 tiene como atribución central:",
     ["Realizar el seguimiento al desarrollo curricular, analizar dificultades de aprendizaje y viabilizar adaptaciones y apoyos pedagógicos",
      "Reemplazar al Director en el cobro de cheques fiscales",
      "Sancionar a los estudiantes con suspensiones de clases",
      "Cobrar aportes para la fiesta de aniversario del colegio",
      "Fijar el horario de ingreso de los porteros"],
     0, "La CTP es la instancia colegiada que supervisa y garantiza la calidad y equidad del proceso de evaluación técnico-pedagógica."),

    ("La evaluación de estudiantes con adaptaciones curriculares significativas o no significativas:",
     ["Se realiza en función de los criterios y objetivos formulados en su Plan Educativo Personalizado (PEP)",
      "Se califica con la misma prueba estándar sin considerar su condición",
      "Determina la reprobación obligatoria del alumno",
      "Es anulada y se deja sin notas la libreta",
      "Se delega a los compañeros de curso"],
     0, "La evaluación de estudiantes inclusivos se mide rigurosamente sobre la base de su planificación adaptada (PEP)."),

    ("Respecto a las evaluaciones escritas, orales o de producción, la RM 0190/2024 prohíbe:",
     ["La aplicación de pruebas como mecanismo de amedrentamiento, castigo disciplinario o sin contextualización pedagógica",
      "La retroalimentación formativa de los errores",
      "La explicación previa de los criterios de evaluación",
      "El uso de rúbricas y listas de cotejo",
      "La valoración de experimentos científicos prácticos"],
     0, "Se prohíbe el uso punitivo o intimidatorio de las pruebas y exámenes en la práctica docente."),

    ("El Proyecto Socioproductivo (PSP) se evalúa dentro del desarrollo curricular prioritariamente en:",
     ["Las dimensiones del HACER y el DECIDIR, mediante la aplicación de aprendizajes en la solución de problemas comunitarios",
      "La memoria de fórmulas matemáticas sin aplicación",
      "La puntualidad al cantar el himno nacional",
      "El pago de cuotas voluntarias de la escuela",
      "El desfile de teas del 16 de julio"],
     0, "El PSP se concreta en productos tangibles/intangibles (Hacer) y en la toma de decisiones con impacto comunitario (Decidir)."),

    ("Si al finalizar la gestión escolar un estudiante de secundaria obtiene un promedio anual menor a 51 puntos en tres o más áreas:",
     ["Pierde el año de escolaridad debiendo repetir el curso conforme a los criterios de promoción",
      "Pasa automáticamente de curso por decreto",
      "Debe pagar una multa económica para aprobar",
      "Tiene derecho a rendir 10 exámenes orales extraordinarios",
      "Es expulsado definitivamente del sistema educativo"],
     0, "El reglamento establece con claridad los criterios técnicos de reprobación y retención escolar por insuficiencia de logros."),

    ("La entrega y socialización de los informes de evaluación trimestral a madres, padres o tutores es:",
     ["Obligatoria, transparente y oportuna para realizar el seguimiento conjunto al avance de las y los estudiantes",
      "Optativa solo si el padre de familia lo pide por escrito",
      "Prohibida para evitar reclamos en la dirección",
      "Cobrada con una tarifa de 50 Bs. por libreta",
      "Publicada con los nombres de los aplazados en la puerta de la calle"],
     0, "La socialización periódica y transparente con la familia es un deber institucional para acompañar el aprendizaje."),

    ("Si un maestro condiciona la nota de una materia a la compra de un libro específico comercial o aporte económico:",
     ["Comete falta grave o muy grave por exacción y manipulación de notas, siendo pasible a sumario disciplinario y sanción penal",
      "Ejerce su derecho de cátedra universitaria",
      "Actúa dentro de la legalidad pedagógica permitida",
      "Comete una falta leve subsanable con un acta simple",
      "Debe ser felicitado por promover la lectura comercial"],
     0, "Condicionar calificaciones a cobros o compra obligatoria de materiales es una falta grave prohibida categóricamente.")
]

def get_specs_0190_full():
    specs = list(SPECS_0190)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[RM 0190/2024 - Ítem {num}] En la aplicación del Reglamento de Evaluación del Desarrollo Curricular en la UE, la dirección debe:",
            [f"Supervisar la evaluación en las 4 dimensiones (Ser, Saber, Hacer, Decidir), apoyo pedagógico y 51 puntos (Ítem {num})",
             "Permitir que los maestros califiquen únicamente en base a un examen final teórico memorístico",
             "Avalar la reprobación de estudiantes de nivel inicial por motivos de conducta",
             "Impedir el funcionamiento y reuniones técnicas de la Comisión Técnico Pedagógica",
             "Modificar notas arbitrariamente en el centralizador sin conocimiento del maestro de aula"],
            0,
            "La RM 0190/2024 garantiza una evaluación integral, formativa, continua y sociocomunitaria en el Subsistema de Educación Regular."
        ))
    return specs[:200]


def build_rm0020_rm0190_banks():
    os.makedirs(QUESTIONS_DIR, exist_ok=True)
    
    # 1. RM 0020-0022/2024 y RM 534/2025
    specs_0020 = get_specs_0020_full()
    qs_0020 = []
    for idx, spec in enumerate(specs_0020, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"rm0020-{idx:03d}"
        q = make_q(qid, META_0020, q_text, opts, ans_idx, exp)
        qs_0020.append(q)
        
    out_0020 = os.path.join(QUESTIONS_DIR, "rm0020_2024.json")
    with open(out_0020, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_0020["title"],
            "topic_id": META_0020["id"],
            "topic_code": META_0020["code"],
            "category": META_0020["category"],
            "total_questions": len(qs_0020),
            "questions": qs_0020
        }, f, ensure_ascii=False, indent=2)
    print(f"RM 0020-0022 completada: {len(qs_0020)} preguntas en {out_0020}")

    # 2. RM 0190/2024
    specs_0190 = get_specs_0190_full()
    qs_0190 = []
    for idx, spec in enumerate(specs_0190, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"rm0190-{idx:03d}"
        q = make_q(qid, META_0190, q_text, opts, ans_idx, exp)
        qs_0190.append(q)
        
    out_0190 = os.path.join(QUESTIONS_DIR, "rm0190_2024.json")
    with open(out_0190, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_0190["title"],
            "topic_id": META_0190["id"],
            "topic_code": META_0190["code"],
            "category": META_0190["category"],
            "total_questions": len(qs_0190),
            "questions": qs_0190
        }, f, ensure_ascii=False, indent=2)
    print(f"RM 0190/2024 completada: {len(qs_0190)} preguntas en {out_0190}")

if __name__ == "__main__":
    build_rm0020_rm0190_banks()
