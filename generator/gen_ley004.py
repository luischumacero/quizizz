# coding: utf-8
"""
Generador de preguntas para el Tema 4.8: Ley N° 004 Marcelo Quiroga Santa Cruz de Lucha Contra la Corrupción.
200 preguntas exhaustivas basadas en tipos penales, imprescriptibilidad, enriquecimiento ilícito, denuncias y transparencia.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley004"]

BASE_SPECS = [
    ("¿Cuál es el objeto de la Ley N° 004 de 31 de marzo de 2010 (Marcelo Quiroga Santa Cruz)?",
     ["Establecer mecanismos y procedimientos destinados a prevenir, investigar, procesar y sancionar actos de corrupción y recuperar el patrimonio del Estado",
      "Regular el comercio minorista en mercados cantonales",
      "Organizar el censo de población y vivienda",
      "Establecer la ley del deporte comunitario",
      "Administrar los parques nacionales protegidos"],
     0, "El art. 1 define el objeto central de erradicar la corrupción y recuperar bienes estatales."),

    ("Según el art. 2 de la Ley 004, se define 'Corrupción' como:",
     ["El requerimiento o aceptación, ofrecimiento u otorgamiento de cualquier beneficio indebido para realizar u omitir un acto en el ejercicio de funciones",
      "El debate político en una asamblea pública",
      "La fiscalización comunitaria de una obra escolar",
      "El cobro de impuestos legalmente aprobados",
      "La postulación libre a un cargo directivo"],
     0, "El art. 2 conceptualiza la corrupción vinculada al abuso de poder para beneficio propio o de terceros."),

    ("En virtud del art. 112 de la CPE y el art. 34 de la Ley 004, los delitos cometidos por servidores públicos que atenten contra el patrimonio del Estado y causen grave daño económico son:",
     ["IMPRESCRIPTIBLES y no admiten régimen de inmunidad",
      "Prescriptibles a los 2 años",
      "Prescriptibles a los 6 meses",
      "Extinguibles por simple cambio de gobierno",
      "Perdonables por acuerdo verbal de partes"],
     0, "La imprescriptibilidad constitucional garantiza que el Estado pueda perseguir penalmente la corrupción sin límite de tiempo."),

    ("El delito de 'Enriquecimiento Ilícito' (art. 27 de la Ley 004) sanciona a la servidora o servidor público que:",
     ["Hubiere incrementado desproporcionadamente su patrimonio respecto de sus ingresos legítimos y no pueda justificarlo",
      "Ahorre mensualmente parte de su salario oficial en el banco",
      "Reciba una herencia familiar debidamente declarada",
      "Compre un automóvil a plazos con crédito bancario",
      "Venda un inmueble propio con factura legal"],
     0, "Se sanciona el incremento patrimonial injustificado con privación de libertad de 5 a 10 años e inhabilitación."),

    ("La pena privativa de libertad para el delito de 'Enriquecimiento Ilícito' de servidor público es de:",
     ["Cinco (5) a diez (10) años de privación de libertad, decomiso de bienes e inhabilitación",
      "Uno (1) a dos (2) meses de arresto",
      "Quince (15) días de trabajo comunitario",
      "Multa de 50 bolivianos únicamente",
      "Treinta (30) años de presidio común"],
     0, "El art. 27 fija una pena de 5 a 10 años más el decomiso de los bienes ilícitos."),

    ("El delito de 'Uso Indebido de Influencias' (art. 26 de la Ley 004) ocurre cuando:",
     ["El servidor público aprovecha las funciones que ejerce para obtener ventajas patrimoniales indebidas para sí o un tercero",
      "Presenta su currículum vitae en una convocatoria pública",
      "Participa en una capacitación docente obligatoria",
      "Recomienda el estudio de la Constitución en clases",
      "Emite calificaciones conforme al reglamento"],
     0, "Castiga el tráfico de influencias desde el ejercicio del cargo público."),

    ("El delito de 'Conducta Antieconómica' (art. 224 del Código Penal modificado) se comete cuando el servidor público:",
     ["Por mala gestión, negligencia o dolo causa daños al patrimonio de la entidad pública o a los intereses del Estado",
      "Logra un ahorro presupuestario ejecutando obras a menor costo",
      "Exige calidad en los materiales escolares adquiridos",
      "Rinde cuentas documentadas cada mes",
      "Rechaza productos defectuosos de un proveedor"],
     0, "Sanciona el detrimento patrimonial del Estado por negligencia grave o acción deliberada."),

    ("El delito de 'Incumplimiento de Deberes' (art. 154 del Código Penal modificado) consiste en que la servidora o servidor público:",
     ["Ilegalmente omita, rehúse hacer o retarde un acto propio de sus funciones",
      "Llegue puntualmente a su fuente de trabajo",
      "Entregue notas en los plazos fijados por el Ministerio",
      "Denuncie de inmediato hechos de violencia física",
      "Realice inventarios de bienes del establecimiento"],
     0, "Tipifica la omisión, demora indebida o negativa injustificada a cumplir las obligaciones del cargo."),

    ("Según el art. 20 de la Ley 004, en las investigaciones por delitos de corrupción y legitimación de ganancias ilícitas:",
     ["NO rige el secreto bancario ni la confidencialidad financiera",
      "El secreto bancario es absoluto e inviolable para todos",
      "Se requiere permiso previo del investigado para revisar sus cuentas",
      "Solo pueden investigarse cuentas en moneda extranjera",
      "Las transferencias bancarias no pueden ser auditadas"],
     0, "El art. 20 levanta el secreto bancario para esclarecer actos de corrupción contra el Estado."),

    ("El Sistema de Protección a Denunciantes y Testigos (art. 17) de la Ley 004 tiene como fin:",
     ["Resguardar la seguridad física, laboral y jurídica de quienes denuncien o testifiquen sobre actos de corrupción",
      "Revelar la identidad del denunciante en medios de prensa",
      "Despedir al testigo de su trabajo de inmediato",
      "Sancionar al denunciante con multas escolares",
      "Detener preventivamente al denunciante"],
     0, "Garantiza reserva de identidad, protección laboral y seguridad personal a quienes combatan la corrupción."),

    ("En una Unidad Educativa, si el Director cobra 'aportes voluntarios' obligatorios para entregar libretas o inscribir alumnos, comete:",
     ["Delito de concusión y exacción ilegal, sancionable penal y administrativamente",
      "Una acción pedagógica comunitaria lícita",
      "Un trámite regular autorizado por la junta escolar",
      "Un acto amparado en la autonomía del colegio",
      "Una falta leve sin consecuencias legales"],
     0, "El cobro indebido bajo condición de otorgar servicios públicos gratuitos constituye delito penal flagrante."),

    ("La Declaración Jurada de Bienes y Rentas debe ser presentada obligatoriamente por las y los servidores públicos ante la:",
     ["Contraloría General del Estado",
      "Policía Nacional",
      "Alcaldía Municipal únicamente",
      "Asociación de Bancos Privados",
      "Junta Escolar de la zona"],
     0, "La Contraloría administra y custodia las declaraciones juradas de todo el sector público."),

    ("La no presentación oportuna o la falsedad en la Declaración Jurada de Bienes y Rentas da lugar a:",
     ["Proceso administrativo, suspensión o destitución y denuncia penal por falsedad",
      "Una felicitación por confidencialidad personal",
      "El archivo del legajo del funcionario",
      "La entrega de un premio a la discreción",
      "Ninguna consecuencia jurídica"],
     0, "La falsedad u omisión en la declaración patrimonial acarrea sanciones penales y disciplinarias."),

    ("El Consejo Nacional de Lucha contra la Corrupción está presidido por (art. 6):",
     ["El Ministerio de Justicia y Transparencia Institucional",
      "El Comandante de las Fuerzas Armadas",
      "El Presidente de la Confederación de Empresarios",
      "El Defensor del Pueblo",
      "El Contralor de manera aislada"],
     0, "El Ministerio cabeza de sector en transparencia y justicia lidera las políticas nacionales anticorrupción."),

    ("El principio ético 'Ama Llulla' consagrado en la CPE y Ley 004 significa:",
     ["No seas mentiroso", "No seas flojo", "No seas ladrón", "Vive en paz", "Ama a la naturaleza"],
     0, "'Ama Llulla' significa 'no seas mentiroso' y rige la probidad y veracidad pública."),

    ("El principio ético 'Ama Suwa' significa:",
     ["No seas ladrón", "No seas mentiroso", "No seas flojo", "Trabaja de noche", "No descanses"],
     0, "'Ama Suwa' significa 'no seas ladrón' y fundamenta la honestidad y protección de los bienes del Estado."),

    ("El principio ético 'Ama Qhilla' significa:",
     ["No seas flojo", "No seas ladrón", "No seas mentiroso", "Come bien", "No viajes solo"],
     0, "'Ama Qhilla' significa 'no seas flojo' y exige laboriosidad, compromiso y diligencia en el servicio público."),

    ("Si un Director de Unidad Educativa utiliza los pupitres, computadoras o vehículos asignados al colegio para su negocio privado familiar:",
     ["Comete el delito de 'Uso Indebido de Bienes y Servicios Públicos'",
      "Está optimizando el uso de recursos ociosos legítimamente",
      "Ejecuta una acción amparada en la costumbre docente",
      "Comete una falta leve que se subsana con devolverlos",
      "No incurre en ninguna falta porque el colegio le pertenece temporalmente"],
     0, "El art. 26 bis tipifica el uso indebido de bienes del Estado para beneficio particular."),

    ("La Ley 004 establece que la investigación y recuperación de fortunas de origen ilícito se aplicará a:",
     ["Servidores públicos, ex servidores públicos y particulares que hubieren afectado el patrimonio del Estado",
      "Únicamente a personas que vivan en el extranjero",
      "Solo a empresas extranjeras sin sucursal",
      "Exclusivamente a diplomáticos jubilados",
      "Personas menores de 18 años sin patrimonio"],
     0, "Alcanza a cualquier persona que se haya enriquecido ilícitamente a costa del erario público boliviano."),

    ("El Control Social en la lucha contra la corrupción (art. 7) faculta a la sociedad civil organizada a:",
     ["Fiscalizar la gestión pública, denunciar irregularidades y exigir transparencia y rendición de cuentas",
      "Dictar sentencias de cárcel sin jueces",
      "Confiscar bienes por mano propia",
      "Nombrar directores de colegios a dedo",
      "Cobrar sueldos como fiscales ad-honorem"],
     0, "El control social ejerce vigilancia comunitaria y promueve la transparencia institucional.")
]

def get_ley004_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley004", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley004-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

