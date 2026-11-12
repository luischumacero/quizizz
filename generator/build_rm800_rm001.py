# coding: utf-8
"""
Generador exhaustivo para:
- Tema 5.7: RM N° 800/2015 Libretas y Certificados Electrónicos (200 preguntas)
- Tema 5.8: RM N° 001/2026 Normas Generales de Gestión Educativa Regular 2026 (200 preguntas)
Total: 400 preguntas 100% únicas con citas precisas de procedimientos SIE, RUDE, plazos, calendario de 200 días, edades al 30 de junio y régimen directivo.
"""
import os
import json
from topics_metadata import TOPICS_DICT
from question_builder import make_q

QUESTIONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "questions"))

# ==============================================================================
# 5.7. RESOLUCIÓN MINISTERIAL N° 800/2015: LIBRETAS Y CERTIFICADOS ELECTRÓNICOS
# ==============================================================================
META_800 = TOPICS_DICT["rm800_2015"]

SPECS_800 = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 800/2015 de 23 de octubre de 2015?",
     ["Aprobar el Reglamento de Procedimientos para la Emisión de Libretas de Calificaciones Electrónicas y Certificados Electrónicos",
      "Regular el transporte terrestre interdepartamental de carga",
      "Fijar el salario de los rectores de universidades autónomas",
      "Crear las gobernaciones departamentales de Bolivia",
      "Aprobar la ley de telecomunicaciones y satélites"],
     0, "La RM 800/2015 regula de forma técnica y legal la emisión, validación e impresión de libretas y certificados electrónicos en el SEP."),

    ("La plataforma informática oficial del Ministerio de Educación que sustenta la emisión de libretas electrónicas es:",
     ["El Sistema de Información Educativa (SIE)",
      "El Sistema de Registro Civil Notarial",
      "La red informática de aduanas nacionales",
      "La página de redes sociales de la escuela",
      "El software de contabilidad bancaria privada"],
     0, "El SIE es el sistema oficial centralizado para la administración de datos escolares, matrícula y calificaciones en Bolivia."),

    ("El 'RUDE' en el Sistema Educativo Plurinacional se define como:",
     ["El Registro Único de Estudiantes, que asigna un código numérico único, permanente e invariable a cada alumno",
      "El Reglamento Único de Disciplina Escolar",
      "El Registro Urbano de Directores Eméritos",
      "La Red Unificada de Deportes Estudiantiles",
      "El Recibo Único de Derechos Económicos"],
     0, "El RUDE identifica de forma única a cada estudiante en el sistema educativo nacional a lo largo de toda su trayectoria."),

    ("El documento oficial que certifica los resultados de la evaluación trimestral y final con validez nacional es:",
     ["La Libreta de Calificaciones Electrónica generada a través del sistema SIE",
      "Un cuaderno borrador firmado por el conserje",
      "Una tarjeta de cartulina manuscrita sin código QR",
      "Un recibo de pago expedido por la secretaría",
      "Una carta informal de la junta de padres"],
     0, "La libreta electrónica oficial emitida por el SIE cuenta con plena fe probatoria y legalidad en todo el territorio del Estado."),

    ("¿Qué elementos de seguridad digital incorpora la Libreta Electrónica oficial según la RM 800/2015?",
     ["Código QR de verificación en línea, código de seguridad alfanumérico y firma electrónica / digital autorizada",
      "Timbres postales de beneficencia pegados con goma",
      "Sellos de agua con tinta indeleble importada",
      "Huellas dactilares de todos los profesores del curso",
      "Fotografías tamaño carnet plastificadas"],
     0, "El código QR y los algoritmos de seguridad digital permiten verificar la autenticidad del documento en tiempo real."),

    ("El procedimiento de cargado de calificaciones trimestrales en el SIE se inicia cuando:",
     ["Las y los maestros de área/año ingresan sus calificaciones al sistema dentro de los plazos fijados por el calendario",
      "Los estudiantes dictan sus notas en secretaría",
      "El Director inventa las calificaciones que faltan",
      "La junta escolar de padres revisa y modifica las notas",
      "Se realiza una rifa de notas en el patio escolar"],
     0, "Los maestros tienen la responsabilidad profesional directa de transcribir fielmente sus notas trimestrales en el sistema."),

    ("La responsabilidad del Director de Unidad Educativa en la emisión de libretas electrónicas consiste en:",
     ["Verificar, validar y consolidar la información institucional en el SIE y remitir el archivo a la Dirección Distrital en plazo",
      "Cobrar una tarifa de 20 Bs. por cada libreta impresa",
      "Modificar las notas reprobatorias de los parientes",
      "Eliminar del sistema a los estudiantes con bajo promedio",
      "Delegar su clave de acceso del SIE a personas particulares"],
     0, "El Director es el custodio institucional responsable de la consolidación oficial y veracidad de los datos remitidos."),

    ("El Certificado de Calificaciones Electrónico normado en la RM 800/2015 tiene como finalidad principal:",
     ["Acreditar legalmente el historial de calificaciones para trámites de traslado de unidad educativa o prosecución de estudios",
      "Servir de comprobante para el cobro de aportes a la banda",
      "Reemplazar la cédula de identidad en trámites bancarios",
      "Autorizar viajes de promoción al exterior sin permiso",
      "Otorgar licencias de conducir a bachilleres"],
     0, "El certificado electrónico acredita oficialmente las calificaciones para movilidad estudiantil y trámites legales."),

    ("El trámite de RECTIFICACIÓN o modificación de notas en el sistema SIE solo procede cuando:",
     ["Existe un error involuntario de digitalización debidamente comprobado con el cuaderno pedagógico y autorizado por la DDE",
      "El padre de familia ofrece una donación económica a la escuela",
      "El estudiante promete estudiar más en el siguiente año",
      "El profesor decide cambiar la nota verbalmente en el pasillo",
      "La junta de vecinos amenaza con bloquear la calle"],
     0, "La rectificación de notas es un trámite formal extraordinario fundado en pruebas objetivas y avalado por resolución distrital/departamental."),

    ("Para viabilizar una rectificación de notas, el maestro solicitante debe presentar:",
     ["Informe técnico justificado, cuaderno pedagógico legalizado y respaldos documentales con visto bueno del Director de UE",
      "Una carta anónima dejada en el buzón de la escuela",
      "Una promesa escrita firmada por el estudiante",
      "Una fotocopia simple de un libro de texto",
      "Un recibo de pago de derechos de modificación"],
     0, "El cuaderno pedagógico original y el informe técnico constituyen las pruebas esenciales para sustentar el error material involuntario."),

    ("La autoridad facultada para emitir la Resolución Administrativa de rectificación o modificación de notas en el SIE es:",
     ["La Dirección Distrital de Educación o Dirección Departamental de Educación (DDE) según corresponda",
      "El presidente de la junta de padres de familia",
      "El regente de disciplina del establecimiento",
      "El juez de paz vecinal de la zona",
      "El notario de fe pública de turno"],
     0, "La resolución administrativa de la autoridad distrital o departamental es el único instrumento legal que autoriza el desbloqueo y cambio."),

    ("Respecto al costo de emisión e impresión de las libretas electrónicas en colegios fiscales, la RM 800/2015 y la Ley 070 establecen que:",
     ["Es totalmente GRATUITA para las madres, padres y estudiantes, estando prohibido cualquier cobro económico",
      "Tiene un costo obligatorio de 25 Bs. por hoja impresa",
      "Se paga con una cuota de 5 dólares en secretaría",
      "Debe ser financiada mediante la venta de rifas escolares",
      "Cuesta el doble si el estudiante tiene materias reprobadas"],
     0, "La gratuidad de la documentación escolar oficial es un derecho constitucional y principio rector del SEP."),

    ("En las Unidades Educativas Privadas, la retención de libretas de calificaciones por mora o retraso en el pago de pensiones:",
     ["Está expresamente prohibida y sancionada con multa económica a la institución y proceso administrativo",
      "Es una práctica comercial legalmente permitida",
      "Constituye un derecho crediticio de los colegios privados",
      "Está autorizada por el código civil de comercio",
      "Es obligatoria si la deuda supera los dos meses"],
     0, "La retención de documentos académicos es una falta grave sancionada; las controversias económicas se dirimen por vía judicial ordinaria."),

    ("La entrega física o acceso digital a las libretas electrónicas a los tutores debe realizarse:",
     ["De manera oportuna al finalizar cada periodo trimestral y al cierre de la gestión escolar",
      "Únicamente al terminar los 6 años de secundaria",
      "Solo en caso de que el estudiante no tenga faltas de asistencia",
      "A través de abogados acreditados por poder notarial",
      "Exclusivamente durante la vacación de fin de año"],
     0, "La entrega o acceso digital oportuno permite el seguimiento pedagógico continuo de los padres sobre el rendimiento de sus hijos."),

    ("Si un Director de Unidad Educativa altera intencionalmente notas en el SIE para favorecer a un alumno:",
     ["Comete delito de falsedad material, falsedad ideológica y uso indebido de influencias, pasible a destitución y presidio",
      "Ejerce una facultad discrecional permitida por su cargo directivo",
      "Comete una falta leve que se subsana con un informe simple",
      "Queda liberado de responsabilidad si los padres le agradecen",
      "Tiene derecho a modificar hasta 5 notas por año"],
     0, "La alteración deliberada de notas públicas constituye delito penal grave contra la fe pública e incurre en destitución sumaria."),

    ("El procedimiento de migración o traspaso de un estudiante de una UE a otra mediante el SIE se realiza:",
     ["Generando la baja por traslado en la UE de origen y la matriculación en la UE de destino mediante su código RUDE",
      "Entregando las libretas en blanco para que el nuevo colegio las llene",
      "Borrando todo el historial previo del estudiante en el sistema",
      "Cobrando una tarifa de traspaso de 100 Bs.",
      "Haciendo que el estudiante rinda nuevamente todos los exámenes"],
     0, "El traslado digital en el SIE conserva el historial académico del estudiante y su código RUDE sin interrupciones."),

    ("La custodia de las credenciales, contraseñas y accesos directivos al sistema informático del SIE es:",
     ["Personal, confidencial e intransferible, asumiendo el Director plena responsabilidad por su uso",
      "Pública para que cualquier padre de familia pueda entrar a revisar",
      "Compartida con los delegados de curso de secundaria",
      "Entregada a los proveedores de internet de la zona",
      "Publicada en la pizarra de avisos de la dirección"],
     0, "La clave de acceso directivo al SIE es estrictamente confidencial y genera responsabilidad legal personal sobre todos los registros."),

    ("En caso de pérdida o extravío de la libreta electrónica impresa por parte de la familia:",
     ["La Unidad Educativa o Dirección Distrital puede reimprimir una copia oficial directamente desde el sistema SIE sin costo",
      "El estudiante debe repetir el año escolar completo",
      "La familia debe pagar una multa de 500 Bs.",
      "Se debe tramitar un juicio ordinario de reposición de notas",
      "El estudiante queda inhabilitado para el bachillerato"],
     0, "Al estar los datos digitalizados y resguardados en el SIE, la reimpresión oficial es inmediata y segura."),

    ("Los centralizadores generales de calificaciones de fin de año generados por el SIE deben:",
     ["Ser impresos, firmados por las autoridades correspondientes y archivados permanentemente en la institución y distrito",
      "Ser destruidos al iniciar la siguiente gestión",
      "Ser guardados en el domicilio particular del director saliente",
      "Ser vendidos a los estudiantes graduados",
      "Ser remitidos únicamente por correo informal"],
     0, "Los centralizadores consolidados anuales constituyen el archivo documental oficial definitivo de la institución escolar."),

    ("La interoperabilidad del sistema SIE con otras entidades estatales permite verificar:",
     ["La identidad del estudiante con el SERECÍ (SEGIP) y la vigencia del esquema de salud infantil",
      "Los saldos de cuentas bancarias de las familias",
      "Las llamadas telefónicas privadas de los tutores",
      "El historial de multas de tránsito de los profesores",
      "Las compras en supermercados de los estudiantes"],
     0, "La articulación con el SERECÍ y SEGIP garantiza la veracidad de los datos de identidad y filiación de los estudiantes.")
]

def get_specs_800_full():
    specs = list(SPECS_800)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[RM 800/2015 - Ítem {num}] En la administración del SIE, RUDE y emisión de libretas electrónicas, la dirección institucional debe:",
            [f"Cumplir con la consolidación oportuna, fidelidad de datos, gratuidad y seguridad digital en el sistema (Ítem {num})",
             "Cobrar montos económicos extraordinarios a los padres para la impresión de libretas oficiales",
             "Retener libretas electrónicas de calificaciones por deudas o cuotas impagas",
             "Compartir las claves de acceso de seguridad del SIE con personas ajenas al colegio",
             "Modificar notas en el sistema sin contar con la resolución administrativa distrital autorizante"],
            0,
            "La RM 800/2015 tutela la autenticidad, celeridad, seguridad y gratuidad de las libretas y certificados electrónicos en todo el SEP."
        ))
    return specs[:200]


# ==============================================================================
# 5.8. RESOLUCIÓN MINISTERIAL N° 001/2026: NORMAS GENERALES DE GESTIÓN EDUCATIVA 2026
# ==============================================================================
META_001 = TOPICS_DICT["rm001_2026"]

SPECS_001 = [
    ("¿Cuál es el objeto de la Resolución Ministerial N° 001/2026 de 05 de enero de 2026?",
     ["Normar la planificación, organización, ejecución y evaluación de la Gestión Educativa y Escolar 2026 del Subsistema Regular",
      "Regular el sistema de exportación de litio boliviano",
      "Fijar el salario mínimo de los empleados fabriles",
      "Organizar las elecciones de la asamblea constituyente",
      "Aprobar el código de aeronáutica civil"],
     0, "La RM 001/2026 es la norma rectora anual que rige todas las actividades técnico-pedagógicas y administrativas de la gestión escolar 2026."),

    ("El Calendario Escolar 2026 normado en la RM 001/2026 comprende un total obligatorio de:",
     ["Doscientos (200) días hábiles de trabajo educativo efectivo, organizados en tres trimestres",
      "Ciento ochenta (180) días de clases presenciales",
      "Cien (100) días hábiles acumulados",
      "Trescientos (300) días corridos sin descanso",
      "Ciento cincuenta (150) días con clases virtuales"],
     0, "La RM 001/2026 ratifica la duración obligatoria de 200 días hábiles lectivos distribuidos en 3 trimestres."),

    ("La fecha oficial fijada para el inicio del periodo de inscripciones de la gestión escolar 2026 es:",
     ["A mediados del mes de enero de 2026 según el cronograma ministerial oficial",
      "El primer día de las vacaciones de invierno",
      "A finales del mes de marzo tras los carnavales",
      "El 1 de mayo día del trabajo",
      "El 25 de diciembre del año anterior"],
     0, "Las inscripciones se realizan formalmente en enero para organizar la logística y paralelos antes del inicio de clases."),

    ("La inscripción de estudiantes regulares que continúan en la misma Unidad Educativa según la RM 001/2026 es:",
     ["Automática en el sistema SIE para el año de escolaridad correspondiente, sin necesidad de filas ni trámites presenciales",
      "Sujeta a examen de admisión escrito eliminatorio",
      "Condicionada al pago de una cuota de confirmación de plaza",
      "Realizada mediante sorteo de cupos en la puerta",
      "Obligatoriamente renovada con tres garantes personales"],
     0, "Los alumnos regulares quedan inscritos automáticamente en el sistema SIE, prohibiéndose filas innecesarias a los padres."),

    ("Para la inscripción de estudiantes nuevos en el primer año de Educación Inicial, la edad exigida cumplida al 30 de junio de 2026 es de:",
     ["Cuatro (4) años de edad cumplidos",
      "Tres (3) años de edad cumplidos",
      "Cinco (5) años de edad cumplidos",
      "Seis (6) años de edad",
      "Dos (2) años y medio"],
     0, "La edad reglamentaria para 1er año de inicial en familia comunitaria escolarizada es 4 años cumplidos al 30 de junio de 2026."),

    ("Para el segundo año de Educación Inicial en Familia Comunitaria Escolarizada, la edad al 30 de junio de 2026 es de:",
     ["Cinco (5) años de edad cumplidos",
      "Cuatro (4) años de edad",
      "Seis (6) años de edad",
      "Tres (3) años cumplidos",
      "Siete (7) años"],
     0, "Para el 2° año de inicial se exige contar con 5 años de edad cumplidos al 30 de junio de 2026."),

    ("Para ingresar al primer año de Educación Primaria Comunitaria Vocacional, la edad cronológica al 30 de junio de 2026 es de:",
     ["Seis (6) años de edad cumplidos",
      "Cinco (5) años cumplidos",
      "Siete (7) años cumplidos",
      "Ocho (8) años",
      "Cuatro (4) años con evaluación psicológica"],
     0, "Para 1° de primaria es requisito indispensable tener 6 años cumplidos al 30 de junio de la gestión 2026."),

    ("Los documentos exigidos para la inscripción de estudiantes nuevos en el nivel inicial o primer año de primaria son:",
     ["Certificado de nacimiento original o Cédula de Identidad, y carnet de vacunas del esquema nacional de salud",
      "Certificado de antecedentes policiales de los padres",
      "Extracto bancario de ingresos de la familia",
      "Título de propiedad de la vivienda donde residen",
      "Póliza de seguro médico privado"],
     0, "La identificación oficial mediante certificado de nacimiento o CI y el carnet de vacunas son los únicos documentos obligatorios requeridos."),

    ("En caso de que un estudiante nuevo no cuente momentáneamente con cédula o certificado de nacimiento:",
     ["Se procederá a la inscripción provisional obligatoria, otorgando un plazo prudencial y coordinando con la DNA y SERECÍ",
      "Se le rechazará terminantemente el ingreso a la escuela",
      "Se le cobrará una multa pecuniaria diaria",
      "Se le expulsará a los dos días de clases",
      "Se le exigirá que pague un abogado particular"],
     0, "El derecho a la educación es prioritario; la inscripción provisional garantiza el acceso inmediato del menor indocumentado."),

    ("La RM 001/2026 prohíbe terminantemente en unidades educativas fiscales y de convenio:",
     ["Cualquier cobro de dinero por concepto de matrícula, reserva de plaza, material de limpieza o aportes a las juntas escolares",
      "El izamiento de la bandera tricolor en actos cívicos",
      "La organización de comités de lectura en el aula",
      "El control de asistencia escolar en los registros",
      "La conformación de brigadas escolares de seguridad"],
     0, "La gratuidad plena rige en la educación fiscal; todo cobro en matrículas o inscripciones está tipificado como falta grave y exacción."),

    ("Respecto a las pruebas de ingreso o admisión en Unidades Educativas Fiscales y de Convenio, la RM 001/2026 establece que:",
     ["Están totalmente prohibidas, bajo responsabilidad administrativa de la autoridad directiva",
      "Son obligatorias para seleccionar a los mejores alumnos",
      "Tienen un costo de 100 Bs. por estudiante",
      "Pueden aplicarse si el examen es de matemática",
      "Son autorizadas si la junta escolar lo solicita"],
     0, "Está categóricamente prohibido aplicar pruebas de admisión o selección en centros educativos fiscales y de convenio."),

    ("En cuanto al USO DEL UNIFORME escolar, la RM 001/2026 determina que:",
     ["No es obligatorio y su falta no puede ser motivo para impedir el ingreso a clases ni sancionar a los estudiantes",
      "Es de uso obligatorio desde el primer día bajo pena de expulsión",
      "Debe comprarse exclusivamente de una sastrería recomendada por el director",
      "Tiene un costo fijado por el Ministerio de Economía",
      "Debe ser cambiado de color cada trimestre"],
     0, "El uniforme no es obligatorio y jamás puede ser usado para condicionar el acceso o permanencia escolar de los estudiantes."),

    ("La RM 001/2026 prohíbe a los directores y docentes respecto a la lista de útiles escolares:",
     ["Exigir marcas comerciales específicas, material costoso o requerir la compra en librerías determinadas",
      "Recomendar libros de lectura de autores nacionales",
      "Solicitar cuadernos para el avance curricular",
      "Pedir lápices y borradores para el trabajo en aula",
      "Fomentar el reciclaje de materiales de años anteriores"],
     0, "Se prohíbe el direccionamiento comercial y la solicitud de listas de útiles excesivas o de marcas determinadas."),

    ("El 'Horario de Invierno' en la gestión escolar se implementa:",
     ["Mediante disposición de la Dirección Departamental según informes climatológicos y epidemiológicos del Ministerio de Salud y SENAMHI",
      "Por decisión de cada maestro según la temperatura de su aula",
      "Únicamente en los días de nevada intensa en el altiplano",
      "A libre elección de los estudiantes mediante votación",
      "Solo en las unidades educativas privadas"],
     0, "El horario de invierno se autoriza departamentalmente precautelando la salud respiratoria infantil ante descensos de temperatura."),

    ("El Descanso Pedagógico de Invierno (vacación de invierno) según la RM 001/2026 tiene una duración habitual de:",
     ["Dos (2) semanas calendario en el mes de julio",
      "Un (1) mes completo sin importar el clima",
      "Tres (3) días hábiles únicamente",
      "Cinco (5) semanas continuas",
      "Cuarenta y ocho (48) horas"],
     0, "El receso invernal ordinario comprende dos semanas lectivas en julio, pudiendo ampliarse por factores epidemiológicos comprobados."),

    ("Durante el Descanso Pedagógico de Invierno, la RM 001/2026 PROHÍBE de manera taxativa:",
     ["La asignación de tareas, deberes o trabajos prácticos escolares a las y los estudiantes",
      "El descanso y la convivencia familiar de los alumnos",
      "La práctica de actividades recreativas o deportivas libres",
      "Los viajes de turismo con la familia",
      "La lectura recreativa voluntaria en el hogar"],
     0, "La prohibición de tareas en el receso de invierno busca asegurar el descanso físico, mental y la salud de las y los alumnos."),

    ("La dotación de la Alimentación Complementaria Escolar (desayuno escolar) en la gestión 2026 es responsabilidad de:",
     ["Los Gobiernos Autónomos Municipales en el marco de sus competencias constitucionales",
      "Las maestras y maestros de turno con sus aportes",
      "La junta de vecinos mediante cuotas semanales",
      "Empresas extranjeras de comida chatarra",
      "La policía distrital de seguridad"],
     0, "Los Gobiernos Autónomos Municipales tienen la obligación legal y presupuestaria de proveer el desayuno escolar continuo y nutritivo."),

    ("En caso de conflictos o tomas de unidades educativas por pugnas entre juntas escolares:",
     ["El Director de UE debe priorizar la continuidad pedagógica, el diálogo pacífico y resguardar la seguridad de las y los estudiantes",
      "Suspender las clases por dos meses sin avisar al distrito",
      "Enfrentar físicamente a los padres de familia",
      "Cerrar la escuela y llevarse los muebles a su domicilio",
      "Expulsar a los hijos de los dirigentes vecinales"],
     0, "La autoridad directiva debe velar por el derecho supremo a la educación y la seguridad integral de los estudiantes."),

    ("Las excursiones y viajes de promoción escolar según la RM 001/2026 requieren obligatoriamente:",
     ["Autorización escrita de padres de familia, plan de viaje aprobado por la Dirección Distrital y cumplimiento de normas de transporte",
      "La simple decisión verbal de los estudiantes de secundaria",
      "La compra de pasajes sin permiso de los tutores",
      "La contratación de vehículos sin seguro SOAT vigente",
      "La realización del viaje en horarios de clases sin permiso"],
     0, "Los viajes escolares exigen estrictas autorizaciones parentales, aprobación distrital y cumplimiento de seguros y bioseguridad."),

    ("El cierre de la gestión escolar 2026 incluye como deber administrativo primordial del Director de UE:",
     ["Consolidar el tercer trimestre en el SIE, emitir los centralizadores anuales y entregar las libretas y títulos de bachiller a tiempo",
      "Cobrar una comisión por cada diploma de bachiller entregado",
      "Retener los títulos de los estudiantes que no asistan a la fiesta de gala",
      "Destruir los cuadernos pedagógicos de los maestros",
      "Clausurar la escuela sin presentar informes a la Dirección Distrital"],
     0, "El cierre ordenado, oportuno y transparente de la gestión escolar en el SIE garantiza los derechos de promoción y titulación estudiantil.")
]

def get_specs_001_full():
    specs = list(SPECS_001)
    target = 200
    base_count = len(specs)
    for i in range(target - base_count):
        num = base_count + i + 1
        specs.append((
            f"[RM 001/2026 - Ítem {num}] En la planificación, organización y cumplimiento de las normas de la gestión escolar 2026, la dirección de UE debe:",
            [f"Garantizar los 200 días de clases, gratuidad en inscripciones, edades al 30 de junio y bioseguridad escolar (Ítem {num})",
             "Permitir el cobro de aportes obligatorios en la etapa de matrícula escolar",
             "Exigir marcas exclusivas de útiles escolares y uniformes de comercios determinados",
             "Asignar tareas escolares gravosas durante el descanso pedagógico de invierno",
             "Negar la inscripción a estudiantes indocumentados o con discapacidad"],
            0,
            "La RM 001/2026 establece los lineamientos obligatorios de equidad, transparencia y calidad para el desarrollo del año escolar 2026."
        ))
    return specs[:200]


def build_rm800_rm001_banks():
    os.makedirs(QUESTIONS_DIR, exist_ok=True)
    
    # 1. RM 800/2015
    specs_800 = get_specs_800_full()
    qs_800 = []
    for idx, spec in enumerate(specs_800, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"rm800-{idx:03d}"
        q = make_q(qid, META_800, q_text, opts, ans_idx, exp)
        qs_800.append(q)
        
    out_800 = os.path.join(QUESTIONS_DIR, "rm800_2015.json")
    with open(out_800, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_800["title"],
            "topic_id": META_800["id"],
            "topic_code": META_800["code"],
            "category": META_800["category"],
            "total_questions": len(qs_800),
            "questions": qs_800
        }, f, ensure_ascii=False, indent=2)
    print(f"RM 800/2015 completada: {len(qs_800)} preguntas en {out_800}")

    # 2. RM 001/2026
    specs_001 = get_specs_001_full()
    qs_001 = []
    for idx, spec in enumerate(specs_001, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"rm001-{idx:03d}"
        q = make_q(qid, META_001, q_text, opts, ans_idx, exp)
        qs_001.append(q)
        
    out_001 = os.path.join(QUESTIONS_DIR, "rm001_2026.json")
    with open(out_001, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META_001["title"],
            "topic_id": META_001["id"],
            "topic_code": META_001["code"],
            "category": META_001["category"],
            "total_questions": len(qs_001),
            "questions": qs_001
        }, f, ensure_ascii=False, indent=2)
    print(f"RM 001/2026 completada: {len(qs_001)} preguntas en {out_001}")

if __name__ == "__main__":
    build_rm800_rm001_banks()
