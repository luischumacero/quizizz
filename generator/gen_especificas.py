# coding: utf-8
"""
Generador de preguntas para Normativa Específica (8 temas x 200 preguntas = 1,600 preguntas):
- 5.1. DS 4688: Escalafón Nacional del Magisterio
- 5.2. RS 212414: Faltas y Sanciones del Magisterio
- 5.3. RM 864/2019: Protocolo Prevención Violencia en UEs
- 5.4. RM 069/2025: Educación Inclusiva en el SEP
- 5.5. RM 0020-0022/2024 y RM 534/2025: Apertura/Cierre de UEs
- 5.6. RM 0190/2024: Evaluación del Desarrollo Curricular
- 5.7. RM 800/2015: Libretas y Certificados Electrónicos
- 5.8. RM 001/2026: Normas Generales Subsistema Regular 2026
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

# ----------------- 5.1. DS 4688: ESCALAFÓN NACIONAL -----------------
DS4688_SPECS = [
    ("¿Cuál es el objeto del Decreto Supremo N° 4688 de 18 de julio de 1957?",
     ["Aprobar el Reglamento del Escalafón Nacional del Servicio de Educación y normar la carrera docente y administrativa",
      "Fijar el presupuesto nacional de defensa",
      "Crear las alcaldías municipales en Bolivia",
      "Regular el transporte terrestre interdepartamental",
      "Organizar las elecciones sindicales de la COB"],
     0, "El DS 4688 es el instrumento fundamental que norma la jerarquía, categorías y carrera del magisterio boliviano."),

    ("Según el DS 4688, el Escalafón Nacional del Servicio de Educación es:",
     ["El registro sistemático, permanente y centralizado de los datos y méritos profesionales del personal docente y administrativo",
      "Un listado confidencial de sanciones políticas",
      "El registro de propiedad vehicular del Ministerio",
      "La nómina de directores jubilados",
      "El padrón biométrico electoral"],
     0, "El art. 1 del DS 4688 define el escalafón como el registro y calificación de la carrera profesional."),

    ("¿Cuántas CATEGORÍAS contempla el Escalafón del Magisterio para el ascenso jerárquico docente?",
     ["Cinco categorías (5ta, 4ta, 3ra, 2da, 1ra) más la categoría al Mérito",
      "Tres categorías únicamente (A, B y C)",
      "Diez categorías numéricas",
      "Dos categorías: inicial y final",
      "Siete categorías rotativas"],
     0, "El sistema de categorías comprende desde la 5ta categoría hasta la 1ra categoría y el Mérito."),

    ("El ascenso de una categoría a la inmediata superior en el Magisterio boliviano se realiza cada:",
     ["Cinco (5) años de servicio acreditado y aprobación del examen o calificación de méritos",
      "Un (1) año de servicio",
      "Diez (10) años obligatorios sin examen",
      "Dos (2) años por simple solicitud verbal",
      "Quince (15) años"],
     0, "El ascenso de categoría se cumple por quinquenios (cada 5 años) previo cumplimiento de requisitos."),

    ("Para el ingreso al Escalafón Nacional en el servicio docente fiscal es requisito INDISPENSABLE:",
     ["Título pedagógico de Maestra o Maestro otorgado por las Escuelas Superiores de Formación de Maestros (ESFM)",
      "Título de bachiller en humanidades únicamente",
      "Haber sido dirigente de junta vecinal",
      "Recomendación política de una autoridad municipal",
      "Haber trabajado en un colegio privado por 10 años sin título"],
     0, "El título pedagógico emitido por las ESFM es el requisito legal habilitante para la docencia fiscal."),

    ("El personal 'Titular' según el Escalafón es aquel que:",
     ["Posee título profesional pedagógico en provisión nacional y está debidamente inscrito en el escalafón",
      "Trabaja temporalmente por invitación verbal",
      "Es estudiante de secundaria contratado como auxiliar",
      "Posee cualquier título técnico sin relación con la educación",
      "Tiene nombramiento provisional de 3 meses"],
     0, "La titularidad docente exige título pedagógico oficial e inscripción en el registro nacional."),

    ("El personal 'Interino' en el magisterio corresponde a:",
     ["Docentes que ejercen funciones sin poseer título pedagógico específico, de forma supletoria o transitoria",
      "Docentes con más de 30 años de servicio en categoría al mérito",
      "Directores distritales con doctorado",
      "Profesores eméritos jubilados",
      "Catedráticos de la Universidad Pedagógica"],
     0, "La condición de interino se aplica a quienes no tienen formación normalista pedagógica regular."),

    ("La inamovilidad y estabilidad docente en sus cargos, según el Escalafón y la CPE, está garantizada mientras:",
     ["Mantengan buena conducta, idoneidad profesional y no incurran en faltas sancionadas con destitución",
      "Pertenezcan al partido político de gobierno",
      "No tengan alumnos aplazados",
      "Paguen aportes mensuales a la dirección",
      "Tengan menos de 30 años de edad"],
     0, "La estabilidad docente está protegida por ley, sujeta únicamente a la idoneidad y el cumplimiento de deberes."),

    ("El 'Bono de Antigüedad' o porcentaje de categoría en el magisterio se calcula en función de:",
     ["La categoría alcanzada en el escalafón y los años de servicio docente acumulados",
      "El número de estudiantes que aprueben el curso",
      "La distancia física entre el colegio y la plaza principal",
      "La marca del vehículo del maestro",
      "El color del aula asignada"],
     0, "El bono de categoría incrementa porcentualmente la remuneración en cada ascenso quinquenal."),

    ("Las 'Permutas' en el magisterio consisten en:",
     ["El intercambio voluntario y concertado de funciones y plazas entre dos maestros de igual nivel y especialidad",
      "El traslado forzoso de un maestro como castigo",
      "La renuncia definitiva a la carrera docente",
      "El despido intempestivo de un maestro titular",
      "La venta económica de una plaza escolar"],
     0, "La permuta es el cambio concertado y reglamentado entre dos servidores del mismo nivel y especialidad.")
]

# ----------------- 5.2. RS 212414: FALTAS Y SANCIONES -----------------
RS212414_SPECS = [
    ("¿Cuál es el objeto de la Resolución Suprema N° 212414 de 21 de abril de 1993?",
     ["Aprobar el Reglamento de Faltas y Sanciones Disciplinarias del Magisterio y Personal Docente y Administrativo",
      "Crear el subsidio de lactancia escolar",
      "Reglamentar el uso de vehículos oficiales del Estado",
      "Normar el descanso pedagógico de invierno únicamente",
      "Establecer la libreta militar para maestros"],
     0, "La RS 212414 regula el régimen disciplinario, tipos de faltas, sanciones y tribunales en el servicio educativo."),

    ("Según la RS 212414, las faltas disciplinarias cometidas por el personal del magisterio se clasifican en tres grados:",
     ["Faltas Leves, Faltas Graves y Faltas Gravísimas",
      "Faltas Simples y Faltas Complejas",
      "Faltas Morales, Civiles y Penales",
      "Faltas Escolares y Faltas Distritales",
      "Faltas de Primer Grado y Faltas de Segundo Grado"],
     0, "El art. 2 clasifica taxativamente las faltas en leves, graves y gravísimas."),

    ("¿Cuál de las siguientes constituye una FALTA LEVE según el art. 6 de la RS 212414?",
     ["La impuntualidad reiterada en el ingreso a clases y actos oficiales de la Unidad Educativa",
      "El cobro de sobornos para alterar calificaciones",
      "La agresión sexual contra estudiantes",
      "La falsificación de títulos profesionales",
      "El abandono del servicio docente por más de 10 días continuos"],
     0, "Los atrasos menores y negligencia leve en el cumplimiento de horarios son consideradas faltas leves."),

    ("Constituyen FALTAS GRAVES según el art. 8 de la RS 212414:",
     ["La reincidencia voluntaria en faltas leves, el abandono del aula sin causa justificada y el maltrato físico o verbal moderado",
      "Llegar 3 minutos tarde un día de lluvia",
      "Usar bolígrafo de tinta azul en vez de negra",
      "Solicitar permiso por duelo familiar con justificativo",
      "Organizar un festival de danzas autóctonas"],
     0, "Las faltas graves implican transgresiones intencionales, desobediencia manifiesta o reincidencia en faltas leves."),

    ("Constituye una FALTA GRAVÍSIMA (art. 10 de la RS 212414) que da lugar a DESTITUCIÓN definitiva del magisterio:",
     ["La venta o alteración de notas, la extorsión económica, la violencia sexual y el abandono de funciones por más de 6 días hábiles continuos",
      "Olvidar el libro de firmas en la dirección un día viernes",
      "No asistir a una reunión por causa médica justificada",
      "Tener divergencias pedagógicas con el director",
      "Vestir traje formal en lugar de guardapolvo"],
     0, "Las faltas gravísimas comprometen gravemente la ética, integridad de estudiantes o patrimonio, sancionadas con destitución."),

    ("Las SANCIONES para las Faltas Leves son aplicadas por:",
     ["El Director de la Unidad Educativa mediante amonestación verbal o escrita en memorando",
      "El Tribunal Supremo de Justicia",
      "La Policía Nacional con arresto carcelario",
      "El Ministro de Educación en persona",
      "La Asamblea Legislativa Plurinacional"],
     0, "El Director de UE tiene potestad sancionatoria directa sobre faltas leves mediante memorando de llamada de atención."),

    ("Las sanciones para las Faltas Graves y Gravísimas requieren obligatoriamente:",
     ["Proceso previo sumario disciplinario ante el Tribunal Disciplinario con derecho a la defensa",
      "Decisión verbal unilateral del portero de la escuela",
      "Un linchamiento comunitario en la plaza",
      "La expulsión inmediata sin escuchar al denunciado",
      "Una encuesta en redes sociales escolares"],
     0, "El debido proceso constitucional exige sumario disciplinario contradictorio ante tribunal competente."),

    ("La sanción aplicable ante la comisión de una FALTA GRAVÍSIMA comprobada en proceso es:",
     ["Destitución del cargo y retiro definitivo del ejercicio de la docencia en el servicio público",
      "Descuento de medio día de haber",
      "Una llamada de atención privada",
      "Cambio a un colegio más céntrico",
      "Un curso de actualización de 2 horas"],
     0, "Las faltas gravísimas conllevan la expulsión y exoneración definitiva del Escalafón del Magisterio."),

    ("El recurso que puede interponer la servidora o servidor sancionado contra el fallo de primera instancia del Tribunal Disciplinario es:",
     ["El Recurso de Apelación ante el Tribunal Disciplinario Superior",
      "El recurso de queja verbal ante el portero",
      "Una carta a la federación de fútbol",
      "El juicio civil ordinario",
      "No existe ningún recurso"],
     0, "Garantiza el derecho a la doble instancia mediante el recurso de apelación."),

    ("La prescripción de la acción disciplinaria para faltas leves, según la normativa procesal administrativa, opera a los:",
     ["Treinta (30) a sesenta (60) días de conocido el hecho sin que la autoridad hubiese iniciado acción",
      "Diez (10) años",
      "Nunca prescribe",
      "Veinticuatro (24) horas",
      "Cinco (5) años"],
     0, "Las faltas leves deben ser sancionadas oportunamente por la autoridad inmediata dentro de plazos perentorios.")
]

# ----------------- 5.3. RM 864/2019: PROTOCOLO VIOLENCIA EN UES -----------------
RM864_SPECS = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 864/2019 de 9 de agosto de 2019?",
     ["Aprobar el 'Protocolo de Prevención, Actuación y Denuncia en Casos de Violencia Física, Psicológica y Sexual en Unidades Educativas y CEEs'",
      "Normar las tarifas del transporte escolar privado",
      "Establecer el menú obligatorio del desayuno escolar",
      "Fijar el horario de los exámenes finales de diciembre",
      "Autorizar viajes de promoción al extranjero"],
     0, "La RM 864/2019 establece la ruta única, obligatoria y estandarizada de prevención, actuación y denuncia ante violencia en escuelas."),

    ("El Protocolo de la RM 864/2019 se aplica de forma OBLIGATORIA en:",
     ["Todas las unidades educativas fiscales, privadas y de convenio, y centros de educación especial de Bolivia",
      "Únicamente en unidades educativas del área rural",
      "Solo en colegios privados de convenio",
      "Exclusivamente en las escuelas normales",
      "Solo en colegios de varones"],
     0, "Su alcance es universal y vinculante para todas las modalidades y tipos de administración en el SEP."),

    ("Ante la sospecha o revelación de un hecho de VIOLENCIA SEXUAL contra un estudiante en la UE, la primera acción inmediata del Director es:",
     ["Brindar contención emocional y protección prioritaria a la víctima, sin interrogarla de forma revictimizante ni buscar careos",
      "Exigir que la víctima demuestre físicamente lo sucedido delante del agresor",
      "Llamar al acusado para que convenza a la familia de retirar la queja",
      "Publicar la fotografía de la víctima en el periódico mural",
      "Expulsar a la víctima por generar desorden"],
     0, "El principio de protección y no revictimización exige acoger, resguardar y abstenerse de investigaciones invasivas."),

    ("¿En qué plazo MÁXIMO debe el Director de la UE presentar la denuncia formal ante la DNA, FELCV o Ministerio Público (RM 864/2019)?",
     ["Dentro de las 24 horas siguientes a tomar conocimiento del hecho",
      "En el plazo de 15 días hábiles",
      "Al finalizar el trimestre escolar",
      "Dentro de los 6 meses posteriores",
      "Cuando la junta escolar emita su autorización por escrito"],
     0, "La ley y el protocolo exigen denuncia inmediata en un plazo perentorio no mayor a 24 horas."),

    ("¿Qué prohíbe terminantemente la RM 864/2019 a directores y docentes en casos de violencia contra niñas, niños y adolescentes?",
     ["PROHIBIDA absolutamente cualquier forma de conciliación, mediación, transacción o acuerdo entre partes",
      "Elaborar un acta informativa de derivación",
      "Coordinar con la Defensoría de la Niñez",
      "Separar al denunciado de sus funciones con menores",
      "Comunicar de inmediato el hecho a los padres o tutores de la víctima"],
     0, "Está expresamente prohibido promover o suscribir conciliaciones o acuerdos de perdón en hechos de violencia."),

    ("Si el agresor denunciado de violencia física grave o sexual es un DOCENTE de la misma Unidad Educativa, la autoridad debe:",
     ["Separar inmediatamente al docente del contacto directo con estudiantes y remitir informe urgente a la Dirección Distrital",
      "Mantener al docente en su aula como si nada hubiera pasado",
      "Permitirle que tome examen a solas con la víctima",
      "Darle un permiso verbal para que viaje de vacaciones",
      "Amenazar a la víctima con reprobarla"],
     0, "La medida de protección cautelar exige apartar al sindicado de toda labor en aula con menores de edad."),

    ("La omisión de denuncia por parte del Director o personal educativo ante un hecho de violencia sexual contra menores constituye:",
     ["Delito penal de Encubrimiento e Incumplimiento de Deberes, con sanción penal y destitución del magisterio",
      "Una falta leve sancionada con llamada de atención verbal",
      "Un acto de prudencia administrativa justificado",
      "Una falta que prescribe en 24 horas",
      "Un trámite optativo sin consecuencias"],
     0, "La omisión es sancionada penalmente conforme al Código Penal y administrativamente como falta gravísima."),

    ("En cuanto al principio de CONFIDENCIALIDAD, el protocolo de la RM 864/2019 exige que:",
     ["Se resguarde con absoluta reserva la identidad, imagen y datos personales de las niñas, niños o adolescentes víctimas",
      "Se publique el acta en el grupo de WhatsApp de todos los padres de familia",
      "Se anuncie el caso por el altavoz escolar en formación matinal",
      "Se envíen fotografías a los medios televisivos",
      "Se comparta en redes sociales institucionales"],
     0, "La reserva de identidad y dignidad del menor es un derecho humano supremo tutelado por ley."),

    ("El 'Plan de Convivencia Pacífica y Armónica' en la Unidad Educativa es:",
     ["Un instrumento institucional de prevención y resolución pacífica de conflictos elaborado participativamente por toda la comunidad escolar",
      "Un examen teórico de castigo para alumnos reprobados",
      "Un reglamento comercial de venta de quioscos",
      "Una lista de expulsiones anticipadas",
      "Un contrato de alquiler de canchas deportivas"],
     0, "El Plan de Convivencia es el pilar preventivo obligatorio en cada establecimiento escolar."),

    ("Las medidas de restitución del derecho a la educación garantizan que la víctima de violencia:",
     ["Pueda continuar sus estudios regulares con apoyo psicopedagógico y flexibilidad académica sin discriminación alguna",
      "Sea transferida forzosamente a una escuela nocturna lejana",
      "Repruebe automáticamente el año lectivo por inasistencias debidas al proceso",
      "Pague una multa por los trámites judiciales",
      "Tenga prohibido el ingreso a las bibliotecas escolares"],
     0, "El Estado y la escuela deben garantizar la permanencia, contención y restitución plena de sus derechos educativos.")
]

# ----------------- 5.4. RM 069/2025: EDUCACIÓN INCLUSIVA SEP -----------------
RM069_SPECS = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 069/2025 de 07 de febrero de 2025?",
     ["Aprobar el 'Reglamento para el Fortalecimiento de la Educación Inclusiva en el Sistema Educativo Plurinacional'",
      "Suspender las clases presenciales de forma definitiva",
      "Crear un impuesto al material escolar importado",
      "Fijar el costo de los uniformes de desfile",
      "Regular las vacaciones docentes de fin de año"],
     0, "La RM 069/2025 aprueba el reglamento integral para consolidar y operativizar la educación inclusiva en el SEP."),

    ("La RM 069/2025 define la 'Educación Inclusiva' como:",
     ["El proceso transformador que garantiza el acceso, permanencia y aprendizaje de todos los estudiantes, eliminando barreras y valorando la diversidad",
      "Un curso optativo dictado solo los días sábados",
      "La concentración de estudiantes con discapacidad en aulas aisladas",
      "La entrega gratuita de útiles escolares una sola vez al año",
      "Un programa exclusivo para universidades extranjeras"],
     0, "La inclusión es un enfoque pedagógico que adapta el sistema a la diversidad de todos los educandos."),

    ("Según la RM 069/2025, las 'Barreras para el Aprendizaje y la Participación' (BAP) se originan en:",
     ["Los contextos culturales, actitudinales, pedagógicos, físicos y organizacionales que limitan el pleno desarrollo del educando",
      "El coeficiente intelectual individual únicamente",
      "La falta de uniformes escolares idénticos",
      "El clima meteorológico de la región",
      "La distancia física entre el colegio y el banco"],
     0, "El modelo inclusivo sitúa las barreras en el entorno y la escuela, y no como defecto de la persona."),

    ("Las modalidades de atención educativa inclusiva en el SEP son:",
     ["Modalidad Directa (en Centros de Educación Especial) y Modalidad Indirecta (en Unidades Educativas Regulares con apoyos)",
      "Modalidad Virtual y Modalidad Presencial únicamente",
      "Modalidad Matutina y Modalidad Vespertina",
      "Modalidad Fiscal y Modalidad Privada",
      "Modalidad Teórica y Modalidad Práctica"],
     0, "La modalidad indirecta articula la inclusión en escuelas regulares y la directa atiende requerimientos específicos intensivos."),

    ("El instrumento técnico-pedagógico fundamental para adecuar objetivos, contenidos y evaluación a las particularidades de un estudiante inclusivo es:",
     ["La Adaptación Curricular Individualizada (ACI)",
      "El libro de caja de la dirección",
      "El parte mensual de inasistencias",
      "El memorando de sanción disciplinaria",
      "El recibo de alquiler de fotocopiadora"],
     0, "La ACI planifica ajustes curriculares individualizados y pertinentes para el estudiante."),

    ("En la evaluación de estudiantes con adaptaciones curriculares significativas, la RM 069/2025 dispone que:",
     ["Se evalúe en función del logro de los objetivos específicos adaptados establecidos en su Plan Curricular Inclusivo",
      "Se aplique exactamente el mismo examen estándar que al resto sin ningún ajuste",
      "Se les califique siempre con 100 puntos por lástima",
      "Se les prohíba dar evaluaciones y no tengan libreta",
      "Se les asigne automáticamente nota de reprobación"],
     0, "La evaluación inclusiva valora el progreso real conforme a los objetivos de su adaptación curricular."),

    ("El rol del Director de la Unidad Educativa en el fortalecimiento de la educación inclusiva (RM 069/2025) incluye:",
     ["Liderar la conformación del equipo de apoyo, coordinar con CEEs y garantizar la matrícula y permanencia sin discriminación",
      "Rechazar la inscripción de estudiantes en silla de ruedas por falta de rampas",
      "Cobrar cuotas adicionales a las familias para contratar sombras",
      "Obligar al estudiante a abandonar el colegio a medio año",
      "Ocultar a los estudiantes inclusivos en las visitas distritales"],
     0, "El Director debe liderar la cultura, política y práctica inclusiva en su comunidad educativa."),

    ("La 'Comisión Técnico-Pedagógica' (CTP) de la Unidad Educativa en relación a la educación inclusiva tiene la tarea de:",
     ["Asesorar, acompañar y validar las adaptaciones curriculares elaboradas por las y los maestros de aula",
      "Decidir qué alumnos son expulsados del colegio",
      "Fijar el precio de las cuotas del aniversario",
      "Administrar los fondos de la cantina escolar",
      "Comprar uniformes deportivos para la selección"],
     0, "La CTP brinda soporte pedagógico y orientación para la atención a la diversidad."),

    ("Para estudiantes con TALENTO EXTRAORDINARIO, la normativa de educación inclusiva contempla:",
     ["Estrategias de enriquecimiento curricular, aceleración o promoción anticipada de grado previo informe psicopedagógico",
      "Retenerlos en el mismo curso repitiendo lo ya aprendido",
      "Prohibirles leer libros avanzados",
      "Obligarlos a rendir exámenes con notas disminuidas",
      "Expulsarlos por saber más que el maestro"],
     0, "El SEP promueve la detección y potenciación de talentos extraordinarios con flexibilización y enriquecimiento curricular."),

    ("El principio de 'Corresponsabilidad Familiar' en la educación inclusiva establece que:",
     ["La familia es parte activa en el proceso educativo, debiendo coordinar, apoyar y dar seguimiento a las adaptaciones de su hijo/a",
      "La familia debe desentenderse por completo una vez matriculado el alumno",
      "La escuela asume el costo de vivienda y alimentación familiar",
      "Los padres no tienen derecho a conocer las notas del alumno",
      "La junta vecinal decide los castigos en el hogar"],
     0, "La articulación activa escuela-familia es indispensable para el éxito pedagógico inclusivo.")
]

# ----------------- 5.5. RM 0020-0022/2024 Y MODIF. RM 534/2025: APERTURA/CIERRE -----------------
RM0020_SPECS = [
    ("¿Qué aprueban las Resoluciones Ministeriales N° 0020/2024, 0021/2024 y 0022/2024 de 9 de enero de 2024?",
     ["Los Reglamentos de Apertura, Modificación y Cierre de Unidades Educativas Fiscales, de Convenio y Privadas del SEP",
      "El calendario del censo nacional de población",
      "La tabla de sueldos de la administración pública central",
      "El reglamento de pasajes aéreos internacionales",
      "La creación de nuevas universidades privadas en el país"],
     0, "Estas resoluciones norman de forma específica los requisitos y trámites para crear, modificar o cerrar colegios fiscales, convenio y privados."),

    ("La Resolución Ministerial N° 534/2025 aprobó:",
     ["Modificaciones y precisiones técnicas a los reglamentos de apertura, legalización de infraestructura y funcionamiento de UEs",
      "La derogación completa de la Ley 070",
      "El cierre de todas las unidades educativas de convenio",
      "La privatización del subsistema regular",
      "La eliminación de los trámites de RUE"],
     0, "La RM 534/2025 actualiza y optimiza los trámites administrativos de apertura, modificación y cierre de UEs."),

    ("El código alfanumérico único oficial asignado por el Ministerio de Educación a cada Unidad Educativa autorizada se denomina:",
     ["Código RUE (Registro de Unidades Educativas)",
      "Código RUDE", "Código RDA", "Código NIT", "Código SIE del estudiante"],
     0, "El RUE es el registro oficial que legaliza la existencia jurídica y pedagógica de la Unidad Educativa."),

    ("Para la APERTURA de una nueva Unidad Educativa Fiscal o Privada, uno de los requisitos técnicos indispensables es:",
     ["Contar con infraestructura propia adecuada, segura, equipamiento pedagógico y certificación de necesidad social",
      "Tener una carta de recomendación de un diputado",
      "Poseer 10 canchas de fútbol con césped sintético",
      "Tener contratados docentes extranjeros exclusivamente",
      "Cobrar aportes anticipados antes de obtener la resolución"],
     0, "Exige infraestructura reglamentaria, salubridad, seguridad y justificación sociodemográfica de demanda educativa."),

    ("La 'Modificación' de una Unidad Educativa según el reglamento comprende trámites tales como:",
     ["Ampliación de niveles o grados, cambio de nombre, traslado de infraestructura o cambio de dependencia",
      "Cambio de portero o regente",
      "Pintado anual de la fachada del colegio",
      "Elección de la reina escolar de primavera",
      "Reorganización del horario de recreo"],
     0, "Las modificaciones oficiales requieren resolución administrativa departamental para tener validez jurídica."),

    ("El CIERRE DEFINITIVO de una Unidad Educativa privada o fiscal puede ser dispuesto por la autoridad ministerial por:",
     ["Incumplimiento reiterado de normas, falta de estudiantes, infraestructura riesgosa o funcionamiento ilegal sin RUE",
      "Haber ganado un concurso de bandas estudiantiles",
      "Tener estudiantes con promedio destacado",
      "Cambiar el color de las cortinas del aula",
      "Realizar ferias productivas comunitarias"],
     0, "El cierre sancionatorio o técnico protege la seguridad y derecho a educación de calidad de los estudiantes."),

    ("En caso de CIERRE de una Unidad Educativa, la autoridad directiva tiene la obligación legal de:",
     ["Resguardar, ordenar y entregar todos los libros matrices, archivos y documentación escolar a la Dirección Distrital",
      "Quemar todos los papeles y libretas en el patio",
      "Llevarse los archivos a su domicilio particular para siempre",
      "Vender las libretas a los estudiantes",
      "Botar los registros a la basura"],
     0, "Los archivos históricos y libros matrices son bienes públicos bajo custodia distrital garantizada."),

    ("Las Unidades Educativas de CONVENIO se caracterizan según el reglamento por:",
     ["Ser administradas por instituciones sin fines de lucro (Iglesias u ONGs) con financiamiento docente a cargo del Estado",
      "Cobrar pensiones comerciales con fines de lucro empresarial",
      "No regirse por el currículo oficial del Estado Plurinacional",
      "Seleccionar alumnos por posición económica exclusiva",
      "Pertenecer a empresas transnacionales extranjeras"],
     0, "Las unidades de convenio brindan servicio social sin fines de lucro con ítems fiscales financiados por el TGN."),

    ("La 'Resolución Administrativa de Autorización de Apertura y Funcionamiento' es emitida formalmente por:",
     ["La Dirección Departamental de Educación (DDE) respectiva",
      "El presidente de la junta vecinal del barrio",
      "La comisaría policial más cercana",
      "El sindicato de choferes de la zona",
      "El párroco de la iglesia local"],
     0, "La DDE es la instancia facultada para emitir la resolución administrativa con validez legal del RUE."),

    ("El funcionamiento de una Unidad Educativa privada sin contar previamente con la Resolución Administrativa de apertura da lugar a:",
     ["Clausura inmediata, sanción pecuniaria y remisión de antecedentes por estafa al Ministerio Público",
      "Una felicitación por emprendimiento privado",
      "La regularización automática sin requisitos",
      "Un premio municipal",
      "Un préstamo bancario estatal"],
     0, "El funcionamiento clandestino o sin resolución es ilegal y sancionado con clausura y proceso penal.")
]

# ----------------- 5.6. RM 0190/2024: EVALUACIÓN DESARROLLO CURRICULAR -----------------
RM0190_SPECS = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 0190/2024 de 12 de marzo de 2024?",
     ["Aprobar el nuevo 'Reglamento de Evaluación del Desarrollo Curricular del Subsistema de Educación Regular'",
      "Suspender el Bachillerato Técnico Humanístico",
      "Fijar el precio de las pensiones en colegios privados",
      "Eliminar las calificaciones numéricas en secundaria",
      "Autorizar la promoción automática universal en todos los cursos"],
     0, "La RM 0190/2024 actualiza integralmente el régimen de evaluación cuantitativa y cualitativa en educación regular."),

    ("Según la RM 0190/2024, la evaluación de los procesos de aprendizaje en el SEP se sustenta en cuatro dimensiones holísticas:",
     ["SER, SABER, HACER y DECIDIR",
      "Ver, Oír, Callar y Repetir",
      "Teoría, Práctica, Memoria y Examen",
      "Entrada, Proceso, Salida y Retroalimentación",
      "Cognitiva, Afectiva, Psicomotriz y Social"],
     0, "El modelo sociocomunitario productivo evalúa integralmente el Ser, Saber, Hacer y Decidir."),

    ("La escala de calificación cuantitativa en los niveles de Educación Primaria y Secundaria Regular es sobre:",
     ["1 a 100 puntos", "1 a 10 puntos", "1 a 7 puntos", "1 a 20 puntos", "1 a 50 puntos"],
     0, "La escala numérica oficial en el SEP es de 1 a 100 puntos."),

    ("La nota mínima de APROBACIÓN trimestral y final en Educación Primaria y Secundaria es de:",
     ["51 puntos", "50 puntos", "60 puntos", "70 puntos", "45 puntos"],
     0, "La calificación de aprobación se consolida a partir de 51 sobre 100 puntos."),

    ("En el Nivel de Educación INICIAL en Familia Comunitaria Escolarizada, la evaluación es:",
     ["Exclusivamente CUALITATIVA y procesual, sin calificación numérica",
      "Numérica sobre 100 puntos con exámenes escritos",
      "Con aplazos y repitencia obligatoria",
      "Mediante pruebas de selección múltiple con tiempo",
      "Con notas del 1 al 10 en acta notariada"],
     0, "En inicial la evaluación es estrictamente cualitativa y formativa, descriptiva del desarrollo de capacidades."),

    ("El 'Apoyo y Seguimiento Pedagógico Continuo' (reforzamiento pedagógico continuo) según la RM 0190/2024:",
     ["Es permanente, obligatorio y debe aplicarse inmediatamente durante todo el trimestre a estudiantes con dificultades",
      "Se realiza únicamente la última media hora del último día del año",
      "Es optativo solo si los padres pagan clases particulares al maestro",
      "Se prohíbe en colegios fiscales",
      "Es exclusivo para estudiantes con notas mayores a 90"],
     0, "El reforzamiento debe ser permanente y oportuno en el proceso de aula para evitar el fracaso escolar."),

    ("La AUTOEVALUACIÓN comunitaria de las y los estudiantes valora fundamentalmente:",
     ["El desarrollo de las dimensiones del SER y del DECIDIR con honestidad, responsabilidad y autocrítica",
      "La nota más alta posible para subir el promedio sin importar el aprendizaje",
      "La copia de tareas entre compañeros",
      "El costo de los útiles escolares comprados",
      "La puntualidad de los profesores"],
     0, "La autoevaluación reflexiona sobre valores, actitudes, compromiso social y toma de decisiones éticas."),

    ("La 'Comisión Técnico-Pedagógica' (CTP) según el reglamento de evaluación tiene entre sus funciones:",
     ["Analizar casos de estudiantes con dificultades persistentes, coordinar adaptaciones y orientar estrategias de superación",
      "Vender uniformes escolares y cobrar rifas",
      "Sancionar a los padres de familia que reclaman notas",
      "Cambiar notas en el sistema a cambio de dinero",
      "Suspender las clases los días lunes"],
     0, "La CTP es el órgano pedagógico consultivo y de acompañamiento docente en la Unidad Educativa."),

    ("Respecto a la REPROBACIÓN de año de un estudiante, la RM 0190/2024 exige que la Unidad Educativa cuente con:",
     ["Documentación fehaciente que demuestre que el docente brindó los apoyos pedagógicos continuos y notificó oportunamente a los tutores",
      "Solo una nota de 50 en el último examen sin registros previos",
      "Una decisión verbal del director sin actas",
      "Un mensaje de texto enviado a fin de año",
      "La firma del portero del establecimiento"],
     0, "Para consolidar una reprobación se requiere respaldo documental del proceso continuo de reforzamiento y comunicación oportuna."),

    ("El reporte trimestral y final de calificaciones se comunica a madres, padres o tutores a través de:",
     ["La Libreta Electrónica de Calificaciones oficial del Ministerio de Educación",
      "Un cuaderno borrador informal sin firmas",
      "Llamadas telefónicas de los compañeros de curso",
      "Una lista pegada en la puerta del colegio con nombres y notas",
      "Rumores en la asamblea de barrio"],
     0, "La libreta electrónica descargable y verificable en el SIE es el único instrumento oficial de reporte.")
]

# ----------------- 5.7. RM 800/2015: LIBRETAS Y CERTIFICADOS ELECTRÓNICOS -----------------
RM800_SPECS = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 800/2015 de 23 de octubre de 2015?",
     ["Aprobar el Reglamento de Procedimientos para la Emisión de Libretas de Calificaciones Electrónicas y Certificados Electrónicos",
      "Comprar computadoras portátiles para el magisterio",
      "Normar las olimpiadas plurinacionales deportivas",
      "Regular el subsidio de frontera",
      "Establecer el día del estudiante boliviano"],
     0, "La RM 800/2015 implementó la digitalización oficial y modernización del sistema de libretas y certificaciones en el SIE."),

    ("La Libreta Escolar Electrónica emitida a través del Sistema de Información Educativa (SIE) cuenta con:",
     ["Código QR, código de barras y firma electrónica/digital que garantizan su autenticidad e inalterabilidad",
      "Sellos de agua hechos a mano por el docente",
      "Firma manuscrita del presidente de la junta vecinal obligatoria",
      "Fotografía tamaño carnet pegada con pegamento escolar",
      "Timbres fiscales comprados en la policía"],
     0, "La modernización tecnológica confiere validez legal inmediata mediante código QR y validación digital centralizada."),

    ("En cuanto al costo para las familias, la emisión y entrega de la Libreta Electrónica de Calificaciones es:",
     ["TOTALMENTE GRATUITA en unidades educativas fiscales, de convenio y privadas",
      "Arancelada con un costo de 100 bolivianos por libreta",
      "Pagada con un aporte obligatorio a la junta de padres",
      "Gratuita solo para el primer hijo y pagada para los demás",
      "Sujeta a compra de timbres notariales"],
     0, "La normativa prohíbe cualquier cobro directo o indirecto por la impresión o entrega de la libreta electrónica."),

    ("El 'Libro Centralizador de Calificaciones' generado por el sistema SIE al finalizar la gestión escolar constituye:",
     ["El documento público matriz oficial e histórico que respalda legalmente la promoción o reprobación de los estudiantes",
      "Un borrador provisional que se destruye al año siguiente",
      "Un registro opcional que los colegios pueden no tener",
      "Un inventario de bienes materiales del colegio",
      "Un catálogo de libros de la biblioteca"],
     0, "El centralizador anual del SIE es el documento legal maestro definitivo del historial escolar."),

    ("Para la rectificación o corrección de una calificación en el sistema después del cierre oficial de trimestre, se requiere:",
     ["Trámite formal fundamentado con informe técnico, actas de examen y autorización expresa de la Dirección Distrital",
      "Que el docente cambie la nota con borrador de tinta",
      "Una llamada telefónica informal al técnico informático",
      "La solicitud de cualquier alumno en ventanilla",
      "Pagar una multa económica en caja del colegio"],
     0, "La rectificación de notas es un trámite reglado y auditado que exige resolución o autorización de la autoridad competente."),

    ("¿Qué prohíbe taxativamente la RM 800/2015 a directores y directores de colegios privados respecto a la libreta escolar?",
     ["PROHIBIDA la retención de libretas escolares bajo pretexto de mora en el pago de pensiones o cuotas escolares",
      "Entregar la libreta en formato digital PDF",
      "Permitir que los padres descarguen la libreta desde la plataforma oficial",
      "Imprimir la libreta en papel bond blanco",
      "Revisar las notas con los docentes antes del cierre"],
     0, "Retener libretas vulnera el derecho al acceso a la educación y genera severas sanciones a colegios privados."),

    ("El 'Certificado de Calificaciones Electrónico' para trámites de legalización o traslados al exterior es emitido por:",
     ["El sistema oficial del Ministerio de Educación y legalizado por la Dirección Departamental de Educación correspondiente",
      "Cualquier imprenta autorizada de la calle",
      "El notario de fe pública de forma unilateral",
      "El presidente del curso",
      "El portero del establecimiento"],
     0, "La DDE legaliza y valida con firma institucional las certificaciones generadas por el SIE."),

    ("El plazo para que las y los maestros entreguen sus calificaciones trimestrales al Director de la UE se rige por:",
     ["El cronograma oficial establecido por el Ministerio y la Dirección Distrital antes del cierre del sistema",
      "La voluntad de cada profesor cuando tenga tiempo libre",
      "El último día de vacaciones de verano",
      "El día del cumpleaños del director",
      "No existe plazo alguno"],
     0, "El cumplimiento de plazos del calendario del SIE es de estricta responsabilidad directiva y docente."),

    ("El código RUDE (Registro Único de Estudiantes) que figura en la libreta electrónica sirve para:",
     ["Identificar de forma única y realizar el seguimiento pedagógico y de movilidad del estudiante en todo el SEP",
      "Controlar las cuentas bancarias de los padres de familia",
      "Registrar compras en supermercados",
      "Asignar la libreta de servicio militar",
      "Sortear premios en ferias escolares"],
     0, "El RUDE es la clave alfanumérica única que acompaña la trayectoria del estudiante en el SEP."),

    ("El Director de Unidad Educativa que no consolide los datos de calificaciones en los plazos fijados por el Ministerio:",
     ["Incurre en incumplimiento de deberes administrativos pasible a proceso sumario y sanciones del Escalafón",
      "Recibe una felicitación distrital por tomarse su tiempo",
      "Queda automáticamente promovido de categoría",
      "Puede culpar al clima y deslindar responsabilidad",
      "No recibe ninguna sanción por ser autoridad"],
     0, "La consolidación extemporánea perjudica los trámites de estudiantes e infringe los deberes de gestión.")
]

# ----------------- 5.8. RM 001/2026: NORMAS GENERALES GESTIÓN 2026 -----------------
RM001_SPECS = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 001/2026 de 05 de enero de 2026?",
     ["Aprobar las 'Normas Generales para la Gestión Educativa 2026 del Subsistema de Educación Regular'",
      "Organizar el desfile del 6 de agosto de 2026",
      "Aprobar el presupuesto del Ministerio de Obras Públicas",
      "Crear nuevas escuelas de formación militar",
      "Regular el transporte escolar internacional"],
     0, "La RM 001 es la norma directriz anual de mayor jerarquía operativa para la planificación y desarrollo escolar en regular."),

    ("Según la RM 001/2026, la gestión escolar en Educación Regular se organiza en:",
     ["Tres trimestres con un mínimo de 200 días hábiles de trabajo pedagógico",
      "Dos semestres de 80 días hábiles",
      "Cuatro bimestres sin vacaciones de invierno",
      "Diez módulos mensuales",
      "Un periodo único de 100 días"],
     0, "El calendario escolar oficial comprende 200 días hábiles obligatorios divididos en tres trimestres."),

    ("Respecto a las INSCRIPCIONES de estudiantes antiguos para la gestión escolar, la RM 001/2026 establece que:",
     ["La inscripción es AUTOMÁTICA para el año de escolaridad que les corresponda, sin exigir ratificación presencial",
      "Deben hacer filas nocturnas durante tres días",
      "Deben pagar una cuota de reserva obligatoria",
      "Deben rendir un examen de admisión eliminatorio",
      "Requiere una entrevista psicológica obligatoria de 2 horas"],
     0, "La inscripción de estudiantes continuos es automática para erradicar filas y cobros irregulares."),

    ("Para el primer año de Educación Inicial en Familia Comunitaria Escolarizada (prekínder), la edad mínima cumplida al 30 de junio es de:",
     ["4 años cumplidos", "3 años cumplidos", "5 años cumplidos", "6 años cumplidos", "2 años cumplidos"],
     0, "La edad reglamentaria para inicial 1ra sección es de 4 años cumplidos hasta el 30 de junio de la gestión."),

    ("Para el primer año de Educación Primaria Comunitaria Vocacional, la edad requerida al 30 de junio es de:",
     ["6 años cumplidos", "5 años cumplidos", "7 años cumplidos", "4 años cumplidos", "8 años cumplidos"],
     0, "Para 1ro de primaria se exige contar con 6 años cumplidos hasta el 30 de junio de la gestión escolar."),

    ("En cuanto al UNIFORME escolar en unidades educativas fiscales, de convenio y privadas, la RM 001/2026 dispone:",
     ["El uso de uniforme NO es obligatorio y su falta no impedirá el ingreso ni la permanencia en clases",
      "El uniforme es obligatorio y quien no lo tenga debe ser expulsado inmediatamente",
      "El uniforme debe comprarse exclusivamente del proveedor que designe el Director",
      "El uniforme debe cambiarse cada dos meses",
      "Se debe cobrar multa diaria de 20 Bs a quien no lleve corbata"],
     0, "El uso de uniforme no es obligatorio y jamás puede ser causal de discriminación o negación de ingreso."),

    ("Respecto a las listas de ÚTILES ESCOLARES, la normativa anual prohíbe terminantemente:",
     ["Exigir marcas específicas de materiales, materiales en cantidades abusivas o comprar en lugares determinados",
      "Pedir un cuaderno y lápices básicos",
      "Recomendar el uso de textos de la biblioteca del colegio",
      "Sugerir el forrado de cuadernos para su cuidado",
      "Utilizar materiales reciclables"],
     0, "Las listas abusivas, con marcas exclusivas o compras direccionadas están prohibidas y sancionadas."),

    ("En colegios PRIVADOS, la RM 001/2026 prohíbe taxativamente:",
     ["El cobro de matrícula adicional, reserva de plaza, aguinaldo para profesores o cualquier cobro camuflado fuera de las 10 pensiones anuales",
      "Cobrar pensiones mensuales bancarizadas",
      "Tener canchas deportivas",
      "Emitir facturas tributarias legales",
      "Tener docentes con título profesional normalista"],
     0, "Los colegios privados se financian exclusivamente en diez mensualidades iguales, prohibiéndose cobros extras."),

    ("El 'Descanso Pedagógico' de medio año (vacaciones de invierno) tiene como propósito principal:",
     ["Proteger la salud de estudiantes ante bajas temperaturas y prevenir infecciones respiratorias agudas",
      "Dar tiempo libre para que los estudiantes trabajen en fábricas",
      "Permitir la venta de uniformes de gala",
      "Cobrar pensiones por adelantado",
      "Aumentar las tareas escolares domiciliarias obligatorias"],
     0, "El descanso pedagógico responde a criterios epidemiológicos y climáticos de salud infantil."),

    ("Durante el Descanso Pedagógico de invierno, la RM 001/2026 establece expresamente que:",
     ["Queda terminantemente PROHIBIDA la asignación de tareas escolares para las vacaciones",
      "Los estudiantes deben rendir exámenes diarios virtuales",
      "Se debe avanzar el 50% de la materia pendiente",
      "Los docentes deben tomar pruebas escritas el primer día de retorno",
      "Es obligatorio asistir a clases de nivelación pagadas"],
     0, "Las vacaciones son un descanso efectivo para precautelar la salud y recreación de las y los estudiantes.")
]

def get_normativa_especifica_questions():
    """Genera 200 preguntas para cada uno de los 8 temas de Normativa Específica."""
    results = {}
    
    topics_map = [
        ("ds4688", DS4688_SPECS),
        ("rs212414", RS212414_SPECS),
        ("rm864_2019", RM864_SPECS),
        ("rm069_2025", RM069_SPECS),
        ("rm0020_2024", RM0020_SPECS),
        ("rm0190_2024", RM0190_SPECS),
        ("rm800_2015", RM800_SPECS),
        ("rm001_2026", RM001_SPECS)
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

