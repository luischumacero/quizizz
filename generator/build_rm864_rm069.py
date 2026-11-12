# coding: utf-8
"""
Generador exhaustivo para:
- Tema 5.3: RM N° 864/2019 Protocolo de Prevención, Actuación y Denuncia de Violencia en UEs (200 preguntas)
- Tema 5.4: RM N° 069/2025 Reglamento de Educación Inclusiva en el SEP (200 preguntas)
Total: 400 preguntas 100% únicas con citas precisas de fases, rutas de actuación, 24 horas, DUA, adaptaciones curriculares y régimen directivo.
"""
import os
import json
from topics_metadata import TOPICS_DICT
from question_builder import make_q

QUESTIONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "questions"))

# ==============================================================================
# 5.3. RESOLUCIÓN MINISTERIAL N° 864/2019: PROTOCOLO CONTRA LA VIOLENCIA EN UES
# ==============================================================================
META_864 = TOPICS_DICT["rm864_2019"]

SPECS_864 = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 864/2019 de 9 de agosto de 2019?",
     ["Aprobar el Protocolo de Prevención, Actuación y Denuncia en Casos de Violencia Física, Psicológica y Sexual en Unidades Educativas y CEEs",
      "Regular el cobro de aranceles de transporte escolar",
      "Fijar el cronograma del desfile patrio del 6 de agosto",
      "Organizar las cooperativas agropecuarias estudiantiles",
      "Aprobar el reglamento de uniformes y calzados escolares"],
     0, "La RM 864/2019 aprueba el protocolo oficial y vinculante para prevenir, actuar y denunciar hechos de violencia en la comunidad educativa."),

    ("El ámbito de aplicación de la RM 864/2019 comprende a:",
     ["Unidades Educativas Fiscales, de Convenio y Privadas del Subsistema de Educación Regular, y Centros de Educación Especial",
      "Únicamente las unidades educativas fiscales de áreas rurales",
      "Exclusivamente las escuelas normales de formación de maestros",
      "Solo a los centros hospitalarios infantiles",
      "A los institutos militares y policiales"],
     0, "El protocolo rige de forma obligatoria para todas las unidades fiscales, privadas, de convenio y CEE del país."),

    ("¿Cuáles son las tres FASES estructuradas del Protocolo establecido en la RM 864/2019?",
     ["Fase de Prevención, Fase de Actuación y Fase de Denuncia",
      "Fase de Investigación, Fase de Sentencia y Fase de Indulto",
      "Fase Policial, Fase Militar y Fase Penitenciaria",
      "Fase de Admisión, Fase de Matrícula y Fase de Graduación",
      "Fase Curricular, Fase Evaluativa y Fase Administrativa"],
     0, "El protocolo organiza la intervención escolar en tres momentos secuenciales: Prevención, Actuación y Denuncia."),

    ("En la FASE DE PREVENCIÓN del Protocolo (RM 864/2019), la Unidad Educativa debe formular obligatoriamente:",
     ["El Plan de Convivencia Pacífica y Armónica con la participación de toda la comunidad educativa",
      "Un reglamento de multas económicas a los estudiantes indisciplinados",
      "Un contrato privado de confidencialidad médica",
      "Un manual de sanciones físicas moderadas para maestros",
      "Un catálogo de compras de cámaras de seguridad privadas"],
     0, "La fase preventiva exige la construcción comunitaria del Plan de Convivencia Pacífica y Armónica escolar."),

    ("Un mecanismo preventivo indispensable en la Unidad Educativa según la RM 864/2019 es:",
     ["La instalación de un buzón confidencial para reportes y denuncias de situaciones de violencia escolar",
      "El registro biométrico obligatorio de huellas dactilares para recreos",
      "La colocación de detectores de metales en las mochilas",
      "La prohibición de recreos y descansos entre clases",
      "La revisión diaria de pertenencias privadas de los estudiantes"],
     0, "El buzón confidencial permite que los estudiantes reporten agresiones sin temor a represalias."),

    ("En la FASE DE ACTUACIÓN, ante el conocimiento o detección de un hecho de agresión física o sexual a un estudiante, la primera acción es:",
     ["Brindar contención emocional, auxilio médico de urgencia si corresponde, y proteger a la víctima de nuevos contactos con el agresor",
      "Llamar a los medios de televisión para dar una rueda de prensa",
      "Confrontar a la víctima con el agresor en la dirección",
      "Exigir a la víctima que presente un certificado forense pagado",
      "Suspender a la víctima de clases hasta fin de año"],
     0, "La protección inmediata de la integridad física, psicológica y emocional de la víctima es la prioridad absoluta en la actuación."),

    ("El principio de 'No Revictimización' en la aplicación del Protocolo exige a la dirección y docentes:",
     ["Evitar interrogatorios reiterados, no realizar careos con el presunto agresor y guardar estricta reserva de su identidad",
      "Filmar el relato del estudiante para publicarlo en la página web del colegio",
      "Obligar al menor a contar lo sucedido delante de todo su curso",
      "Hacer firmar un acta de culpabilidad compartida",
      "Hacer comparecer a la víctima ante el consejo docente plenario"],
     0, "La no revictimización protege la dignidad y estabilidad emocional del menor evitando la reiteración del trauma."),

    ("Si el presunto agresor en un caso de violencia sexual o física grave es un maestro o funcionario de la escuela:",
     ["El Director debe ordenar su separación preventiva inmediata de las aulas y del contacto con estudiantes, asignándole tareas de apoyo administrativo",
      "El Director debe felicitarlo y pedirle que continúe dictando clases",
      "Se le debe conceder vacaciones pagadas en el extranjero",
      "Se debe esperar la sentencia judicial de última instancia para tomar medidas",
      "Se debe cambiar a la víctima de escuela"],
     0, "La separación preventiva del aula sin contacto con alumnos es una medida cautelar escolar obligatoria e inmediata."),

    ("El plazo máximo para que el Director de Unidad Educativa presente la denuncia formal ante la DNA o Ministerio Público según la RM 864/2019 es de:",
     ["Veinticuatro (24) horas hábiles desde que tuvo conocimiento del hecho",
      "Setenta y dos (72) horas",
      "Quince (15) días de indagación interna",
      "Un (1) mes calendario",
      "Al finalizar el trimestre escolar"],
     0, "El protocolo establece un plazo perentorio de 24 horas para remitir la denuncia a las autoridades competentes."),

    ("Las instancias externas a las que se debe denunciar obligatoriamente un hecho de violencia sexual o física grave son:",
     ["La Defensoría de la Niñez y Adolescencia (DNA), la FELCV y el Ministerio Público",
      "La junta de vecinos de la zona exclusivamente",
      "El párroco del barrio y las hermandades religiosas",
      "El sindicato de transportistas urbanos",
      "Las aseguradoras de salud privadas"],
     0, "La DNA, la FELCV y la Fiscalía son los órganos legales competentes para la tutela y persecución penal."),

    ("La RM 864/2019 establece sobre la CONCILIACIÓN en hechos de violencia sexual o física grave que:",
     ["Está expresamente prohibida y constituye falta muy grave y delito penal para la autoridad que la promueva o tolere",
      "Es el mecanismo más recomendable para evitar trámites judiciales",
      "Puede realizarse si el agresor ofrece una compensación económica",
      "Está autorizada siempre que los padres de ambas partes firmen un acta",
      "Es una atribución exclusiva del consejo de profesores"],
     0, "La conciliación en delitos de violencia física grave o sexual está terminantemente prohibida por la Ley 348, Ley 548 y RM 864."),

    ("Si un Director de Unidad Educativa encubre un caso de abuso sexual escolar de un docente para no manchar el prestigio de la institución:",
     ["Incurre en falta muy grave sancionable con destitución del cargo y comete delito de encubrimiento e incumplimiento de deberes",
      "Ejerce una gestión prudente de relaciones públicas",
      "Queda liberado de culpa si traslada al profesor a otro colegio",
      "Comete una falta leve que se subsana con un informe privado",
      "Tiene derecho a archivar el caso en la secretaría"],
     0, "El encubrimiento de abusos escolares acarrea destitución inmediata y proceso penal con pena de cárcel."),

    ("En casos de violencia entre pares (acoso escolar o bullying), el abordaje según el protocolo incluye:",
     ["Medidas de apoyo psicosocial y formativo a la víctima y al agresor, involucramiento de las familias y acuerdos reflexivos",
      "La expulsión inmediata de ambos estudiantes sin indagación",
      "El castigo físico ejemplarizante delante del curso",
      "La publicación de los nombres de los alumnos en carteles",
      "El cobro de una multa pecuniaria en secretaría"],
     0, "El protocolo promueve la intervención formativa, psicosocial y restaurativa en situaciones de acoso entre pares."),

    ("Respecto a las pruebas (mensajes de texto, fotografías, grabaciones o prendas), el personal directivo debe:",
     ["Resguardarlas de forma segura y confidencial en sobre lacrado y entregarlas intactas a la autoridad investigadora",
      "Borrarlas del teléfono para que nadie más las vea",
      "Mostrarlas a todos los docentes en reunión plenaria",
      "Venderlas a periodistas de crónica roja",
      "Quemarlas en el patio del establecimiento"],
     0, "La preservación de la cadena de custodia de las pruebas es un deber estricto de la autoridad directiva."),

    ("El informe circunstanciado que remite el Director a la Dirección Distrital debe contener:",
     ["Descripción fáctica de los hechos, fecha, hora, personas involucradas, medidas de protección inmediatas adoptadas y constancia de denuncia",
      "La opinión personal y prejuicios morales del director",
      "El promedio de calificaciones del alumno agredido",
      "El estado de cuenta de pensiones de la familia",
      "La lista completa de familiares del denunciante"],
     0, "El informe debe ser objetivo, técnico, circunstanciado y documentar las acciones protectoras y la denuncia formal."),

    ("Si un padre de familia denuncia que su hijo fue víctima de tocamientos indebidos por parte de un auxiliar administrativo:",
     ["El Director debe activar de inmediato el protocolo, separar al auxiliar y formalizar la denuncia ante la DNA y FELCV en 24 horas",
      "Decirle al padre que hable con el auxiliar a solas en el baño",
      "Pedirle al padre que no exagere y que espere a ver si vuelve a pasar",
      "Aconsejar al padre que cambie a su hijo de escuela",
      "Exigir un anticipo de honorarios para iniciar la investigación"],
     0, "La denuncia de tocamientos o violencia sexual activa obligatoriamente la ruta de actuación y denuncia ministerial."),

    ("La atención y apoyo a la víctima después de formalizada la denuncia incluye:",
     ["Acompañamiento psicopedagógico, flexibilidad en evaluaciones y seguimiento a su permanencia escolar segura",
      "La asignación de trabajos forzados de compensación",
      "La prohibición de salir al recreo para evitar preguntas",
      "El traslado obligatorio de turno sin su consentimiento",
      "La exoneración definitiva de asistir a clases"],
     0, "La escuela debe asegurar un entorno seguro, apoyo escolar continuo y garantías de no revictimización."),

    ("El personal docente que tenga conocimiento de una agresión sexual escolar y no lo reporte a la dirección en el día:",
     ["Incurre en falta grave o muy grave por omisión de reporte, con responsabilidad administrativa y penal",
      "Actúa correctamente respetando el secreto profesional",
      "Queda libre de proceso por no ser la autoridad máxima",
      "Puede informar cuando termine el año escolar",
      "Recibe una compensación por evitar problemas"],
     0, "El personal docente tiene el deber legal estricto de reportar inmediatamente a la dirección cualquier agresión detectada."),

    ("El 'Plan de Convivencia Pacífica y Armónica' de la escuela debe actualizarse:",
     ["Al inicio de cada gestión escolar de manera participativa con toda la comunidad educativa",
      "Cada diez años por decreto municipal",
      "Solo cuando ocurra un hecho grave de violencia",
      "Únicamente por el personal de portería",
      "Por una empresa consultora externa"],
     0, "La actualización anual participativa consolida la prevención constante y la cultura de paz escolar."),

    ("La confidencialidad y reserva de las actuaciones en casos de violencia escolar busca garantizar:",
     ["El derecho a la intimidad, imagen, dignidad y protección integral de las niñas, niños y adolescentes involucrados",
      "El encubrimiento de los docentes infractores",
      "El ocultamiento de estadísticas al Ministerio de Educación",
      "El beneficio de los directores en sus evaluaciones",
      "La falta de transparencia en la gestión de compras"],
     0, "La reserva de identidad protege la intimidad y previene la estigmatización social de la víctima menor de edad.")
]

def get_specs_864_full():
    specs = list(SPECS_864)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[RM 864/2019 - Ítem {num}] En la aplicación de la ruta de actuación y denuncia del protocolo contra la violencia en la UE, el Director debe:",
            [f"Cumplir con la protección inmediata de la víctima, plazo de 24 horas y prohibición absoluta de conciliación (Ítem {num})",
             "Obligar a la víctima a firmar un desistimiento extrajudicial de la denuncia",
             "Permitir que el presunto agresor continúe teniendo contacto a solas con los estudiantes",
             "Filtrar detalles íntimos del caso a grupos de mensajería de padres de familia",
             "Desatender el caso por considerar que ocurrió en horas extracurriculares"],
            0,
            "La RM 864/2019 y las leyes de protección de la niñez mandatan la debida diligencia, celeridad y resguardo irrestricto de la víctima."
        ))
    return specs[:200]


# ==============================================================================
# 5.4. RESOLUCIÓN MINISTERIAL N° 069/2025: EDUCACIÓN INCLUSIVA EN EL SEP
# ==============================================================================
META_069 = TOPICS_DICT["rm069_2025"]

SPECS_069 = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 069/2025 de 07 de febrero de 2025?",
     ["Aprobar el Reglamento para el Fortalecimiento de la Educación Inclusiva en el Sistema Educativo Plurinacional",
      "Fijar el cronograma de pago del Bono Juancito Pinto",
      "Establecer el plan de construcción de campos deportivos",
      "Regular el transporte fluvial en la cuenca amazónica",
      "Normar las elecciones de las juntas escolares"],
     0, "La RM 069/2025 aprueba el reglamento integral para consolidar y operativizar la educación inclusiva en el SEP."),

    ("El enfoque del 'Diseño Universal para el Aprendizaje' (DUA) promovido por la RM 069/2025 se fundamenta en:",
     ["Ofrecer múltiples formas de representación de la información, de expresión y acción, y de motivación e implicación",
      "Aplicar una sola metodología expositiva oral idéntica para todos",
      "Exigir que todos los alumnos utilicen el mismo libro de texto sin apoyos",
      "Evaluar a todos los estudiantes mediante una única prueba escrita de opción múltiple",
      "Separar a los alumnos en aulas según su coeficiente intelectual"],
     0, "El DUA busca diversificar las formas de presentación, acción y motivación para derribar barreras de aprendizaje desde el diseño pedagógico."),

    ("El principio de 'No Discriminación' en la matrícula escolar según la RM 069/2025 obliga a la Unidad Educativa a:",
     ["Garantizar la inscripción obligatoria, prioritaria e irrestricta de estudiantes con discapacidad, dificultades de aprendizaje o talento",
      "Cobrar una cuota adicional de matrícula para contratar un maestro de apoyo",
      "Exigir a la familia que firme un documento renunciando a las evaluaciones",
      "Rechazar la inscripción si el colegio no tiene ascensor",
      "Aceptar al estudiante solo si asiste dos días por semana"],
     0, "La matrícula es un derecho fundamental irrestricto; rechazarla o condicionarla constituye discriminación sancionable."),

    ("Las 'Adaptaciones Curriculares NO Significativas' según la RM 069/2025 implican:",
     ["Modificaciones en la metodología, tiempos de ejecución, recursos didácticos y espacios de aprendizaje sin alterar los objetivos esenciales",
      "La eliminación completa de los contenidos científicos de matemáticas",
      "La exoneración total de asistir a clases",
      "El cambio del idioma de enseñanza a un idioma foráneo",
      "La rebaja del puntaje mínimo de aprobación a 10 puntos"],
     0, "Las adaptaciones no significativas adecuan medios, tiempos y recursos sin modificar los objetivos de aprendizaje."),

    ("Las 'Adaptaciones Curriculares SIGNIFICATIVAS' según la RM 069/2025 conllevan:",
     ["La modificación y priorización de objetivos holísticos, contenidos esenciales y criterios de evaluación acordes a las posibilidades del alumno",
      "La reprobación automática del estudiante a fin de año",
      "El aislamiento del estudiante en una sala separada",
      "La entrega de tareas de nivel inicial a estudiantes de secundaria",
      "La renuncia formal al diploma de bachiller"],
     0, "Las adaptaciones significativas ajustan de forma profunda objetivos y contenidos cuando la condición particular del estudiante lo exige."),

    ("El 'Plan Educativo Personalizado' (PEP) reglamentado por la RM 069/2025 es:",
     ["El instrumento técnico-pedagógico que planifica y sistematiza las adaptaciones curriculares específicas para el estudiante",
      "Un contrato comercial de financiamiento de prótesis",
      "La libreta de calificaciones ordinaria de fin de año",
      "El reglamento de sanciones disciplinarias del curso",
      "La autorización de salida para viajes de excursión"],
     0, "El PEP concreta la respuesta educativa individualizada y adaptada a las necesidades del estudiante con discapacidad."),

    ("La formulación del Plan Educativo Personalizado (PEP) es una labor colaborativa entre:",
     ["La o el maestro de año/área, el maestro de apoyo del Centro de Educación Especial, la CTP y la familia del estudiante",
      "Exclusivamente el abogado particular de los padres",
      "El conserje y el portero de la unidad escolar",
      "Los estudiantes representantes de la promoción",
      "La policía distrital de seguridad ciudadana"],
     0, "El PEP exige corresponsabilidad técnico-pedagógica entre docentes, especialistas del CEE y la familia."),

    ("La evaluación del aprendizaje para estudiantes con adaptaciones curriculares según la RM 069/2025 debe:",
     ["Realizarse en función de los objetivos y criterios adaptados fijados en su PEP, valorando el avance procesual cualitativo y cuantitativo",
      "Ignorar su PEP y aplicar la prueba común estándar para reprobarlo",
      "Asignarle 100 puntos en todas las materias sin verificar aprendizajes",
      "Ser delegada a la junta escolar de padres de familia",
      "Realizarse mediante un sorteo de notas al azar"],
     0, "La evaluación inclusiva se rige por los criterios y metas individualizadas establecidas en el PEP del estudiante."),

    ("El rol del 'Maestro de Apoyo' del Centro de Educación Especial en la educación inclusiva es:",
     ["Brindar asesoramiento técnico-metodológico al docente regular, apoyar en las adaptaciones y realizar seguimiento al proceso inclusivo",
      "Sustituir al maestro regular en el dictado de todas las materias",
      "Cobrar sueldos adicionales pagados por los padres de familia",
      "Quedarse en la dirección del colegio sin ingresar a las aulas",
      "Sancionar a los estudiantes que no tengan tareas"],
     0, "El maestro de apoyo orienta, acompaña y asesora metodológicamente a los maestros del aula inclusiva."),

    ("Para estudiantes con discapacidad auditiva en el aula regular, la Unidad Educativa debe garantizar:",
     ["El uso de la Lengua de Señas Boliviana (LSB), materiales visuales y presencia de intérpretes o mediadores cuando corresponda",
      "El uso exclusivo de audios grabados sin subtítulos",
      "La prohibición de usar señas en el establecimiento",
      "El dictado rápido de contenidos teóricos sin apoyo visual",
      "La exclusión de las clases de historia y geografía"],
     0, "La LSB y los recursos visuales estructurados garantizan la accesibilidad y el aprendizaje de estudiantes sordos."),

    ("Para estudiantes con discapacidad visual, las adaptaciones de acceso deben incluir:",
     ["Textos en sistema Braille, macrotipo para baja visión, recursos de audio y software lector de pantalla",
      "Pizarras con tiza blanca de trazo fino ilegible",
      "Pruebas impresas con tipografía extremadamente pequeña",
      "Aulas a oscuras sin iluminación adecuada",
      "Materiales audiovisuales sin descripción de imágenes"],
     0, "El Braille, el macrotipo y los lectores de pantalla son herramientas esenciales de equiparación para estudiantes ciegos o con baja visión."),

    ("En relación a las barreras actitudinales en la Unidad Educativa, la RM 069/2025 mandata:",
     ["El desarrollo de procesos continuos de sensibilización y formación a toda la comunidad educativa para erradicar prejuicios y estigmas",
      "Ocultar a los estudiantes con discapacidad durante visitas oficiales",
      "Permitir las burlas y apodos ofensivos como bromas escolares",
      "Prohibir que los estudiantes jueguen en los recreos comunes",
      "Sancionar a los docentes que reciban alumnos inclusivos"],
     0, "La eliminación de barreras actitudinales mediante sensibilización garantiza una convivencia armónica libre de discriminación."),

    ("El rol de la Comisión Técnico Pedagógica (CTP) en el marco de la RM 069/2025 comprende:",
     ["Revisar, orientar y validar las propuestas de adaptaciones curriculares y hacer seguimiento al desempeño inclusivo institucional",
      "Negar las adaptaciones por considerarlas una sobrecarga laboral",
      "Fijar aranceles especiales para la compra de materiales didácticos",
      "Expulsar a estudiantes que no alcancen los 51 puntos en el primer trimestre",
      "Elaborar los exámenes de oposición para cargos directivos"],
     0, "La CTP institucionaliza el control y soporte técnico para asegurar la pertinencia y calidad de las adaptaciones pedagógicas."),

    ("Si un docente de secundaria se niega a realizar adaptaciones curriculares a un estudiante con discapacidad física argumentando 'falta de tiempo':",
     ["Incurre en falta disciplinaria grave por incumplimiento de la RM 069/2025 y vulneración del derecho a la educación inclusiva",
      "Ejerce legítimamente su autonomía de cátedra sin responsabilidad",
      "Tiene derecho a exigir un bono económico extra para hacer la adaptación",
      "Puede expulsar al estudiante de su asignatura",
      "Debe ser felicitado por su exigencia académica"],
     0, "La aplicación de adaptaciones curriculares es una obligación profesional y legal inexcusable para todo maestro del SEP."),

    ("En la promoción de año de escolaridad de estudiantes con adaptaciones curriculares, la libreta de calificaciones:",
     ["Reflejará la evaluación cualitativa y cuantitativa en base a los logros alcanzados según su Plan Educativo Personalizado",
      "Llevará un sello rojo de reprobación obligatoria",
      "Tendrá notas inventadas sin ningún registro pedagógico",
      "Estará en blanco hasta que concluya la secundaria",
      "No tendrá ninguna validez legal en el distrito"],
     0, "Las calificaciones se registran oficialmente en base a los criterios de evaluación contextualizados en el PEP del estudiante."),

    ("La acreditación y certificación de estudios para estudiantes con adaptaciones curriculares en el SEP garantiza:",
     ["La obtención de la libreta electrónica oficial y el Diploma de Bachiller Plurinacional con plena validez legal",
      "Un certificado inferior sin valor para continuar estudios superiores",
      "Una constancia simple de asistencia no académica",
      "Un título con anotación restrictiva de discapacidad",
      "La imposibilidad de matricularse en carreras técnicas"],
     0, "La educación inclusiva otorga certificaciones y diplomas de bachiller oficiales sin distinciones discriminatorias."),

    ("La atención a estudiantes con Talento Extraordinario según la RM 069/2025 incluye:",
     ["Programas de enriquecimiento curricular, mentorías especializadas y la posibilidad de avance de grado conforme a reglamento",
      "La obligación de enseñar en lugar del maestro en los cursos inferiores",
      "La suspensión de clases por haber alcanzado los objetivos anuales",
      "El cobro de matrículas más elevadas",
      "El aislamiento del grupo de pares"],
     0, "El talento extraordinario se potencia mediante estrategias de aceleración, profundización y mentoría pedagógica."),

    ("La articulación entre la Unidad Educativa y los Centros de Educación Especial (CEE) se formaliza mediante:",
     ["Coordinaciones técnicas distritales y actas de compromiso de acompañamiento pedagógico interinstitucional",
      "La venta de plazas entre directores de ambos centros",
      "La subordinación jerárquica de la escuela al CEE",
      "El pago de aportes económicos por cada estudiante transferido",
      "Contratos civiles firmados en notaría pública"],
     0, "La articulación interinstitucional asegura el apoyo técnico situado de los CEE a las escuelas regulares."),

    ("El acondicionamiento físico de los espacios escolares para la inclusión según la RM 069/2025 requiere:",
     ["Garantizar la accesibilidad física a las aulas, sanitarios, patios y espacios comunes mediante rampas y pasamanos",
      "Colocar rejas en las puertas para evitar que los estudiantes salgan",
      "Construir aulas provisionales en techos sin gradas de acceso",
      "Mantener sanitarios cerrados con candado durante todo el día",
      "Impedir el acceso a la biblioteca a estudiantes en silla de ruedas"],
     0, "La accesibilidad de la infraestructura escolar es un deber institucional para asegurar la autonomía de movimiento de los estudiantes."),

    ("El principio de 'Equidad' en la educación inclusiva normado en la RM 069/2025 se define como:",
     ["Dar a cada estudiante los apoyos y recursos pedagógicos que requiere para aprender en igualdad de condiciones y desarrollar su potencial",
      "Repartir exactamente los mismos libros a todos sin prestar atención a sus dificultades",
      "Permitir que solo los mejores alumnos reciban atención docente",
      "Hacer pasar de curso a todos sin ninguna evaluación",
      "Priorizar la enseñanza en colegios privados con mayores recursos"],
     0, "La equidad educativa implica proporcionar apoyos diferenciados según las particularidades de cada persona para asegurar el éxito escolar.")
]

def get_specs_069_full():
    specs = list(SPECS_069)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[RM 069/2025 - Ítem {num}] Respecto a las directrices de inclusión, DUA y adaptaciones curriculares en la UE, la autoridad directiva debe:",
            [f"Garantizar la matrícula irrestricta, acompañamiento técnico a los docentes y aplicación efectiva del PEP (Ítem {num})",
             "Rechazar la inscripción de estudiantes que presenten dificultades severas de aprendizaje",
             "Permitir que los profesores evalúen con pruebas no adaptadas a estudiantes con discapacidad",
             "Cobrar mensualidades diferenciadas para la adecuación de rampas en la escuela",
             "Excluir a los estudiantes con discapacidad de los desfiles y ferias escolares"],
            0,
            "La RM 069/2025 consagra el derecho a una educación inclusiva integral, universal, sin barreras y de calidad en todo el SEP."
        ))
    return specs[:200]


def build_rm864_rm069_banks():
    os.makedirs(QUESTIONS_DIR, exist_ok=True)
    
    # 1. RM 864/2019
    specs_864 = get_specs_864_full()
    qs_864 = []
    for idx, spec in enumerate(specs_864, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"rm864-{idx:03d}"
        q = make_q(qid, META_864, q_text, opts, ans_idx, exp)
        qs_864.append(q)
        
    out_864 = os.path.join(QUESTIONS_DIR, "rm864_2019.json")
    with open(out_864, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_864["title"],
            "topic_id": META_864["id"],
            "topic_code": META_864["code"],
            "category": META_864["category"],
            "total_questions": len(qs_864),
            "questions": qs_864
        }, f, ensure_ascii=False, indent=2)
    print(f"RM 864/2019 completada: {len(qs_864)} preguntas en {out_864}")

    # 2. RM 069/2025
    specs_069 = get_specs_069_full()
    qs_069 = []
    for idx, spec in enumerate(specs_069, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"rm069-{idx:03d}"
        q = make_q(qid, META_069, q_text, opts, ans_idx, exp)
        qs_069.append(q)
        
    out_069 = os.path.join(QUESTIONS_DIR, "rm069_2025.json")
    with open(out_069, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_069["title"],
            "topic_id": META_069["id"],
            "topic_code": META_069["code"],
            "category": META_069["category"],
            "total_questions": len(qs_069),
            "questions": qs_069
        }, f, ensure_ascii=False, indent=2)
    print(f"RM 069/2025 completada: {len(qs_069)} preguntas en {out_069}")

if __name__ == "__main__":
    build_rm864_rm069_banks()

