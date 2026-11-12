# coding: utf-8
"""
Generador de preguntas para el Tema 4.6: Ley N° 223 General para Personas con Discapacidad.
200 preguntas exhaustivas basadas en tipos de discapacidad, inclusión educativa, adaptaciones, cuotas y CONALPEDIS.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley223"]

BASE_SPECS = [
    ("¿Cuál es el objeto de la Ley N° 223 de 2 de marzo de 2012?",
     ["Garantizar a las personas con discapacidad el ejercicio pleno de sus derechos y deberes en igualdad de condiciones y equiparación de oportunidades",
      "Crear impuestos especiales para el transporte urbano",
      "Regular las pensiones de vejez de los jubilados",
      "Organizar competencias olímpicas internacionales",
      "Establecer aranceles consulares"],
     0, "El art. 1 consagra el mandato de garantizar los derechos plenos de las personas con discapacidad."),

    ("Según el art. 5 de la Ley 223, ¿cuáles son los tipos o clasificaciones de discapacidad reconocidos?",
     ["Física-motora, visual, auditiva, intelectual, mental o psíquica, y múltiple",
      "Temporal y definitiva únicamente",
      "Leve y grave sin subcategorías",
      "Infantil y adulta",
      "Urbana y rural"],
     0, "El art. 5 clasifica técnicamente los tipos de discapacidad en el marco biopsicosocial."),

    ("El documento oficial que acredita legalmente la condición y grado de discapacidad en Bolivia es:",
     ["El Carnet de Discapacidad emitido por el Ministerio de Salud / CODEPEDIS",
      "El certificado de notas del colegio",
      "La cédula de identidad común sin registro médico",
      "Una carta notariada firmada por un familiar",
      "El carnet de vacunas escolar"],
     0, "El carnet de discapacidad es emitido por los equipos de calificación biopsicosocial autorizados."),

    ("En el ámbito de la EDUCACIÓN (art. 10), la Ley 223 establece que el Sistema Educativo Plurinacional debe garantizar:",
     ["La educación inclusiva, oportuna y pertinente, con adaptaciones curriculares y materiales adecuados",
      "La reclusión de estudiantes con discapacidad en escuelas aisladas",
      "El rechazo de inscripción si el colegio no tiene ascensor",
      "El cobro de pensiones dobles por alumno con discapacidad",
      "La exención total de aprender a leer y escribir"],
     0, "El art. 10 consagra el derecho a la educación inclusiva en el subsistema regular y especial."),

    ("¿Qué prohíbe expresamente la Ley 223 a las Unidades Educativas públicas, privadas y de convenio?",
     ["Rechazar la inscripción o permanencia de estudiantes por motivos de su discapacidad",
      "Construir rampas de acceso en los ingresos",
      "Capacitar a los maestros en lenguaje de señas",
      "Proveer textos en sistema Braille",
      "Organizar olimpiadas científicas inclusivas"],
     0, "El rechazo de matrícula a personas con discapacidad constituye un acto discriminatorio grave penado por ley."),

    ("El lenguaje oficial de comunicación para la comunidad sorda reconocido por el Estado y el SEP es:",
     ["La Lengua de Señas Boliviana (LSB)",
      "El código Morse",
      "El lenguaje gestual internacional exclusivamente",
      "La dactilología francesa",
      "El esperanto sonoro"],
     0, "La Ley 223 y normativas complementarias reconocen formalmente la Lengua de Señas Boliviana (LSB)."),

    ("Para las personas con discapacidad visual, el sistema oficial de lectura y escritura táctil garantizado es:",
     ["El Sistema Braille", "El alfabeto cirílico", "Los pictogramas", "El código binario", "El taquigráfico"],
     0, "El Sistema Braille es el medio fundamental para la alfabetización y acceso a la información visual."),

    ("Según el art. 34 de la Ley 223, ¿cuál es el porcentaje MÍNIMO de inserción laboral obligatoria para personas con discapacidad en entidades públicas?",
     ["No menor al 4% del total de su personal",
      "No menor al 10%",
      "Exactamente el 1%",
      "El 0.5%",
      "No existe cuota obligatoria"],
     0, "El art. 34 establece una cuota obligatoria preferente del 4% en el sector público y 2% en el privado."),

    ("El beneficio de la INAMOVILIDAD LABORAL protege a:",
     ["Las personas con discapacidad y a los padres, madres o cónyuges que tengan bajo su dependencia a personas con discapacidad",
      "Únicamente a directores de colegios privados",
      "Exclusivamente a funcionarios diplomáticos",
      "A contratados temporales por 15 días",
      "A trabajadores que incurran en faltas gravísimas reiteradas"],
     0, "Garantiza estabilidad e inamovilidad laboral tanto al titular como a sus tutores directos."),

    ("La máxima entidad plurinacional de defensa y promoción de los derechos de las personas con discapacidad es (art. 38):",
     ["CONALPEDIS (Comité Nacional de Personas con Discapacidad)",
      "SENASIR", "ASFI", "COB", "INRA"],
     0, "El CONALPEDIS diseña y fiscaliza el cumplimiento de las políticas públicas inclusivas."),

    ("A nivel departamental, las entidades operativas encargadas de la temática de discapacidad son los:",
     ["CODEPEDIS (Comités Departamentales de Personas con Discapacidad)",
      "SEDES exclusivamente",
      "Comités Cívicos",
      "Consejos Universitarios",
      "Tribunales de Sentencia"],
     0, "Los CODEPEDIS funcionan bajo la tuición de los Gobiernos Autónomos Departamentales."),

    ("En cuanto a la infraestructura escolar, el principio de 'Accesibilidad' (art. 21) exige que los colegios:",
     ["Eliminen barreras arquitectónicas construyendo rampas, pasamanos y baños adaptados",
      "Instalen únicamente escaleras de caracol",
      "Coloquen puertas angostas de menos de 60 cm",
      "Eliminen la señalética visual y sonora",
      "Prohíban la entrada de sillas de ruedas al aula"],
     0, "La accesibilidad física y arquitectónica es un derecho fundamental para la libre movilidad."),

    ("Las 'Adaptaciones Curriculares' en el aula regular para un estudiante con discapacidad implican:",
     ["Ajustes no significativos o significativos en metodologías, recursos, tiempos y evaluación para responder a sus necesidades",
      "Hacer que el estudiante copie textos sin comprender nada",
      "Excluir al estudiante de todas las clases teóricas",
      "Aprobarlo automáticamente con 100 puntos sin enseñarle",
      "Obligarlo a rendir el mismo examen memorístico estándar sin apoyo"],
     0, "Las adaptaciones curriculares adecúan los contenidos y estrategias pedagógicas a la realidad del estudiante."),

    ("El rol del Director de Unidad Educativa frente a un estudiante con discapacidad inscrita en su plantel es:",
     ["Coordinar con los maestros y centros de educación especial la implementación efectiva de adaptaciones curriculares",
      "Sugerir a los padres que no manden a su hijo al colegio",
      "Aislar al estudiante en una sala vacía",
      "Delegar el caso exclusivamente al portero",
      "Exigir un pago adicional a los padres para contratar un tutor privado"],
     0, "El Director debe liderar y monitorear la inclusión pedagógica efectiva en la comunidad educativa."),

    ("Los 'Centros de Educación Especial' (CEE) en articulación con las unidades educativas regulares brindan:",
     ["Apoyo técnico-pedagógico, asesoramiento interdisciplinario y recursos adaptados en la modalidad indirecta",
      "Internamiento cerrado forzoso",
      "Educación militarizada",
      "Tratamiento psiquiátrico de reclusión",
      "Exámenes de expulsión escolar"],
     0, "Articulan con la educación regular para fortalecer los procesos inclusivos mediante la modalidad indirecta."),

    ("El principio de 'Equiparación de Oportunidades' en la Ley 223 busca:",
     ["Garantizar que los diversos sistemas de la sociedad estén a disposición de todos, eliminando discriminaciones",
      "Dar ventajas injustas a quienes no las necesitan",
      "Hacer que todos piensen de la misma manera",
      "Impedir que las personas sobresalgan en sus estudios",
      "Cobrar impuestos especiales a las familias"],
     0, "Busca compensar y superar las desventajas sociales y estructurales para garantizar igualdad real."),

    ("Si un colegio privado niega el cupo a un niño con síndrome de Down alegando 'falta de preparación':",
     ["Incurre en infracción grave sancionada por el Ministerio de Educación con multas y proceso penal por discriminación",
      "Actúa en el marco de la libertad de empresa protegida legalmente",
      "Tiene la razón absoluta porque es un negocio privado",
      "Solo recibe una felicitación distrital",
      "Puede cobrarle el triple de matrícula para aceptarlo"],
     0, "La negativa de inscripción por motivos de discapacidad es una falta muy grave y delito tipificado."),

    ("En las pruebas de evaluación escolar, los estudiantes con discapacidad sensorial (visual o auditiva) tienen derecho a:",
     ["Formatos accesibles, tiempo razonable y uso de apoyos técnicos (intérprete LSB, textos Braille o lupas)",
      "Ser reprobados de oficio",
      "Rendir la prueba a oscuras o en silencio absoluto sin mediación",
      "Examen verbal en idioma extranjero",
      "No tener ninguna constancia de evaluación"],
     0, "La evaluación debe ser inclusiva, pertinente y en formatos totalmente accesibles."),

    ("La 'Discapacidad Múltiple' se refiere a:",
     ["La presencia de dos o más discapacidades (física, sensorial, intelectual) en una misma persona",
      "Tener más de 3 fracturas óseas temporales",
      "Enfermedades comunes como gripe o tos",
      "Reprobar más de tres materias en el colegio",
      "Vivir en más de dos ciudades"],
     0, "La combinación de distintas discapacidades requiere apoyos interdisciplinarios intensivos."),

    ("El principio de 'Autonomía Personal' reconoce a las personas con discapacidad el derecho a:",
     ["Tomar sus propias decisiones, ser oídas y participar activamente en su proyecto de vida",
      "Vivir siempre bajo tutela obligatoria de terceros",
      "No opinar en las decisiones que afecten su salud o educación",
      "Ser consideradas legalmente incapaces en todo momento",
      "No tener bienes a su nombre"],
     0, "Reconoce la dignidad intrínseca y capacidad de decidir con apoyos y salvaguardias adecuadas.")
]

def get_ley223_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley223", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley223-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

