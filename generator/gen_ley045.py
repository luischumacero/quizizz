# coding: utf-8
"""
Generador de preguntas para el Tema 4.3: Ley N° 045 Contra el Racismo y Toda Forma de Discriminación.
200 preguntas basadas en definiciones, tipos penales, agravantes, prevención escolar y sanciones.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley045"]

BASE_SPECS = [
    ("¿Cuál es el objeto de la Ley N° 045 de 8 de octubre de 2010?",
     ["Establecer mecanismos y procedimientos para la prevención y sanción de actos de racismo y toda forma de discriminación",
      "Regular el comercio exterior y aranceles aduaneros",
      "Administrar los recursos hidrocarburíferos del país",
      "Fijar el salario mínimo nacional de los trabajadores",
      "Organizar el régimen penitenciario y carcelario"],
     0, "El art. 1.I establece el objeto de prevenir y sancionar el racismo y toda forma de discriminación."),

    ("Según el art. 5 de la Ley 045, se define 'Discriminación' como toda distinción, exclusión, restricción o preferencia basada en motivos de:",
     ["Sexo, color, edad, orientación sexual, identidad de género, origen, cultura, nacionalidad, idioma o credo que tenga por objeto anular el goce de derechos",
      "Rendimiento exclusivamente académico en pruebas objetivas",
      "El cumplimiento del horario de entrada al establecimiento",
      "Portar el carnet de identidad para trámites oficiales",
      "La edad de jubilación fijada por ley"],
     0, "El art. 5.a define de manera integral la discriminación en concordancia con el art. 14 de la CPE."),

    ("La Ley 045 define 'Racismo' (art. 5.b) como:",
     ["Toda teoría o práctica que postula la superioridad o inferioridad de grupos raciales o étnicos",
      "El orgullo por las danzas tradicionales bolivianas",
      "El aprendizaje obligatorio de idiomas originarios",
      "La vestimenta tradicional en eventos cívicos",
      "La libre expresión de ideas científicas"],
     0, "El art. 5.b define el racismo como toda doctrina o práctica de superioridad fundada en diferencias biológicas o culturales."),

    ("Según el art. 5.d de la Ley 045, las 'Acciones Afirmativas' son:",
     ["Medidas temporales orientadas a corregir situaciones patentes de desigualdad o exclusión histórica de grupos vulnerables",
      "Sanciones penales de cárcel sin juicio previo",
      "Privilegios permanentes para familiares de directores",
      "Aumentos salariales automáticos por decreto",
      "Cobros de matrículas diferenciadas en colegios fiscales"],
     0, "Las acciones afirmativas son medidas correctivas temporales para nivelar desigualdades reales."),

    ("La 'Homofobia' es definida en la Ley 045 (art. 5.g) como:",
     ["La aversión, odio, prejuicio o discriminación contra personas homosexuales (lesbianas, gays)",
      "El miedo a espacios cerrados en el colegio",
      "La fobia a hablar en público",
      "El rechazo a aprender idiomas extranjeros",
      "La aversión a la tecnología digital"],
     0, "El art. 5.g tipifica y conceptualiza la homofobia como forma proscrita de discriminación."),

    ("La 'Transfobia' es conceptualizada en la Ley 045 (art. 5.h) como:",
     ["La discriminación, aversión o rechazo hacia las personas transgénero y transexuales",
      "El temor al transporte público escolar",
      "El rechazo a las transferencias bancarias",
      "La fobia a los cambios de curso o paralelo",
      "El miedo a la transición tecnológica"],
     0, "El art. 5.h define la transfobia protegiendo la identidad de género."),

    ("La 'Misoginia' se define en la Ley 045 (art. 5.i) como:",
     ["Cualquier conducta o práctica de odio, aversión o violencia hacia las mujeres por el solo hecho de serlo",
      "La amistad solidaria entre mujeres",
      "El liderazgo de mujeres en juntas escolares",
      "El acceso prioritario de niñas a la educación",
      "El permiso de maternidad laboral"],
     0, "El art. 5.i define la misoginia como el odio o aversión sistemática hacia las mujeres."),

    ("En el ámbito educativo, el art. 6 de la Ley 045 obliga al Sistema Educativo Plurinacional a:",
     ["Adoptar políticas de prevención, diseñar currículos con enfoque de derechos humanos y erradicar prácticas discriminatorias",
      "Expulsar a estudiantes de escasos recursos económicos",
      "Separar a estudiantes según su color de piel",
      "Prohibir que los estudiantes hablen lenguas originarias",
      "Cobrar multas a quienes lleven ropa tradicional"],
     0, "El art. 6 establece las medidas de prevención y educación en todos los niveles del SEP."),

    ("¿Qué prohíbe taxativamente la Ley 045 a las Unidades Educativas públicas, privadas y de convenio?",
     ["Rechazar la inscripción o permanencia escolar por razones de discriminación, apariencia, estado civil de los padres o embarazo",
      "Exigir certificado de nacimiento para la inscripción",
      "Establecer horarios de recreo escolar",
      "Enseñar el himno nacional",
      "Organizar ferias socioproductivas"],
     0, "Está terminantemente prohibida la exclusión o rechazo por motivos de discriminación o embarazo."),

    ("Según el art. 8 de la Ley 045, la instancia encargada de promover, diseñar y hacer seguimiento a las políticas públicas antirracistas es el:",
     ["Comité Nacional contra el Racismo y Toda Forma de Discriminación",
      "Tribunal Supremo Electoral",
      "Colegio Médico de Bolivia",
      "Consejo de la Judicatura",
      "Sindicato de Maestros Urbanos"],
     0, "El Comité Nacional contra el Racismo y Toda Forma de Discriminación depende del Ministerio de Culturas."),

    ("El Comité Nacional contra el Racismo está conformado por dos comisiones permanentes (art. 9):",
     ["Comisión de Lucha contra el Racismo y Comisión de Lucha contra la Discriminación",
      "Comisión Económica y Comisión Política",
      "Comisión de Primaria y Comisión de Secundaria",
      "Comisión de Docentes y Comisión de Padres",
      "Comisión Urbana y Comisión Rural"],
     0, "El art. 9 organiza el Comité en estas dos comisiones especializadas."),

    ("La Ley 045 incorpora al Código Penal el art. 281 bis, tipificando el delito de 'Racismo'. La pena privativa de libertad establecida es de:",
     ["1 a 5 años de prisión", "10 a 20 años", "30 años sin derecho a indulto", "1 a 3 meses", "Solo trabajo comunitario sin cárcel"],
     0, "El art. 281 bis sanciona el delito de racismo con privación de libertad de 1 a 5 años."),

    ("El art. 281 ter del Código Penal (incorporado por la Ley 045) tipifica el delito de 'Discriminación' con una pena de:",
     ["1 a 5 años de privación de libertad", "15 a 30 años", "6 meses de arresto de fin de semana", "5 a 10 años", "Solo fianza económica"],
     0, "El delito de discriminación tiene una pena base de 1 a 5 años de reclusión."),

    ("Según el Código Penal modificado por la Ley 045, ¿cuándo se AGRAVA la pena por delitos de racismo o discriminación en un tercio del mínimo y una mitad del máximo?",
     ["Cuando sea cometido por una servidora o servidor público en el ejercicio de sus funciones",
      "Cuando se cometa durante un día feriado",
      "Cuando el autor sea menor de 14 años",
      "Cuando se cometa a través de una llamada telefónica",
      "Cuando no existan testigos presenciales"],
     0, "La condición de servidora o servidor público constituye agravante específica expresa."),

    ("Constituye otra agravante en la Ley 045 cuando el acto racista o discriminatorio sea cometido contra:",
     ["Niñas, niños, adolescentes, mujeres embarazadas o personas con discapacidad",
      "Personas con título de maestría o doctorado",
      "Funcionarios diplomáticos extranjeros únicamente",
      "Comerciantes mayoristas",
      "Propietarios de inmuebles urbanos"],
     0, "La condición de vulnerabilidad de la víctima agrava penalmente la conducta."),

    ("El art. 281 quater del Código Penal sanciona la 'Difusión e Incitación al Racismo o a la Discriminación' cometida a través de:",
     ["Cualquier medio de comunicación impreso, radial, televisivo o informático (redes sociales)",
      "Solo conversaciones privadas en el hogar",
      "Cartas manuscritas confidenciales",
      "Murmullos en el aula",
      "Pensamientos no expresados"],
     0, "Sanciona a quien difunda o incite por cualquier medio de comunicación masivo o digital."),

    ("Según el art. 281 sexies del Código Penal, la persona que mediante expresiones verbales o insultos agravie a otra por motivos racistas será sancionada con:",
     ["Prestación de trabajo de 40 días a 18 meses y multa de 40 a 150 días",
      "Pena de presidio de 30 años",
      "Arresto domiciliario de por vida",
      "Pérdida definitiva de la nacionalidad",
      "Clausura de su cuenta bancaria"],
     0, "Las agresiones verbales e insultos racistas se sancionan con trabajo comunitario y multa."),

    ("En una Unidad Educativa, si un docente o directivo comete actos de discriminación contra un estudiante, además de la vía penal, corresponde:",
     ["Proceso disciplinario administrativo sancionatorio según el Reglamento del Magisterio",
      "Felicitarlo por imponer orden rígido",
      "Archivar la queja inmediatamente",
      "Cobrar una cuota extra a los padres de familia",
      "Cambiar a la víctima de colegio sin investigar"],
     0, "Corresponde el inicio inmediato de sumario administrativo disciplinario por faltas graves/gravísimas."),

    ("¿Qué deber tiene el Director de Unidad Educativa ante una denuncia comprobable de racismo o discriminación en su establecimiento?",
     ["Elevar informe inmediato a la Dirección Distrital y remitir antecedentes al Ministerio Público según corresponda",
      "Ocultar el hecho para proteger el prestigio del colegio",
      "Obligar a la víctima a pedir disculpas al agresor",
      "Expulsar a la víctima por quejarse",
      "Cobrar una multa privada para beneficio del colegio"],
     0, "El Director tiene la obligación legal de actuar de oficio y denunciar conforme a ley."),

    ("Conforme a la Ley 045, el principio de 'Interculturalidad' implica:",
     ["El reconocimiento a la coexistencia y convivencia recíproca entre todas las culturas sin discriminación",
      "La imposición forzada de una sola lengua en todo el país",
      "La prohibición de compartir tradiciones comunitarias",
      "El rechazo a la diversidad cultural en las escuelas",
      "La exclusión de saberes ancestrales"],
     0, "El art. 3 consagra la interculturalidad como base de armonía y reciprocidad entre culturas.")
]

def get_ley045_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley045", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley045-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

