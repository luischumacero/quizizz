# coding: utf-8
"""
Generador de preguntas para el Tema 4.4: Ley N° 348 Integral para Garantizar a las Mujeres una Vida Libre de Violencia.
200 preguntas exhaustivas basadas en tipos de violencia, deber de denuncia en educación, medidas de protección y feminicidio.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley348"]

BASE_SPECS = [
    ("¿Cuál es el objeto de la Ley N° 348 de 9 de marzo de 2013?",
     ["Establecer mecanismos, medidas y políticas integrales de prevención, atención, protección y reparación a las mujeres en situación de violencia",
      "Regular el divorcio voluntario ante notario de fe pública",
      "Crear cooperativas de ahorro y crédito para mujeres rurales",
      "Administrar el registro biométrico electoral",
      "Determinar los horarios de trabajo en fábricas textiles"],
     0, "El art. 1 consagra el mandato de garantizar una vida libre de violencia a las mujeres."),

    ("Según el art. 7 de la Ley 348, ¿cuántos tipos de violencia contra las mujeres se definen y tipifican expresamente?",
     ["16 tipos de violencia", "5 tipos de violencia", "8 tipos de violencia", "10 tipos de violencia", "25 tipos de violencia"],
     0, "El art. 7 describe 16 formas o tipos de violencia reconocidas por la ley."),

    ("El art. 7, numeral 12 de la Ley 348 define la 'Violencia en el Sistema Educativo' como:",
     ["Todo acto de agresión física, psicológica o sexual cometido contra las mujeres por personal docente, administrativo o pares en el ámbito escolar",
      "La exigencia de rendir exámenes bimestrales",
      "El control estricto de asistencia al colegio",
      "El uso del uniforme escolar reglamentario",
      "La asignación de tareas académicas para el fin de semana"],
     0, "El art. 7.12 protege a las estudiantes y docentes de agresiones dentro de la comunidad educativa."),

    ("La 'Violencia Feminicida' se define en la Ley 348 (art. 7.2) como:",
     ["La acción de extrema violencia que viola el derecho fundamental a la vida y causa la muerte de la mujer por su condición de tal",
      "El acoso laboral sin consecuencias físicas",
      "La disputa verbal sobre tareas del hogar",
      "La negativa a otorgar un permiso de vacaciones",
      "El atraso en el pago de pensiones escolares"],
     0, "Es la forma más extrema de violencia basada en género que culmina en el asesinato de la mujer."),

    ("El delito de 'Feminicidio' incorporado al Código Penal por la Ley 348 (art. 252 bis) se sanciona con una pena de:",
     ["30 años de presidio sin derecho a indulto",
      "10 a 15 años de prisión",
      "20 años con posibilidad de libertad condicional a los 5 años",
      "5 a 8 años de arresto domiciliario",
      "1 a 3 años de trabajo comunitario"],
     0, "El feminicidio conlleva la pena máxima del ordenamiento penal boliviano: 30 años sin indulto."),

    ("La 'Violencia Psicológica' (art. 7.3) comprende:",
     ["Toda acción u omisión destinada a degradar, controlar o aislar a la mujer, causándole daño emocional o disminuyendo su autoestima",
      "Un debate respetuoso en una asamblea de docentes",
      "La corrección pedagógica de errores ortográficos",
      "El desacuerdo fundamentado en una reunión directiva",
      "La entrega puntual de informes escolares"],
     0, "Abarca desvalorización, intimidación, insultos, amenazas y manipulación psicológica."),

    ("La 'Violencia Patrimonial y Económica' (art. 7.10) se manifiesta mediante:",
     ["El control, despojo o retención indebida de bienes, ingresos o documentos personales de la mujer",
      "La apertura voluntaria de una cuenta de ahorros compartida",
      "El pago puntual del salario docente",
      "La compra conjunta de útiles escolares",
      "La rendición pública de cuentas de la Unidad Educativa"],
     0, "Consiste en la privación o limitación ilegítima de los recursos económicos o patrimoniales de la mujer."),

    ("Según el art. 42 de la Ley 348, ¿qué OBLIGACIÓN tienen las y los educadores y directores de Unidades Educativas que tomen conocimiento de un hecho de violencia contra una mujer o niña?",
     ["Denunciar el hecho obligatoriamente e inmediatamente ante la FELCV, SLIM, DNA o Ministerio Público en el plazo máximo de 24 horas",
      "Convocar a una reunión secreta para obligar a conciliar",
      "Esperar a que termine la gestión escolar para informar",
      "Desestimar la denuncia si la estudiante no tiene marcas físicas visibles",
      "Sancionar a la estudiante por difamación"],
     0, "El art. 42 establece la obligación ineludible de denunciar en 24 horas; omitirlo constituye delito penal."),

    ("¿Qué establece el art. 46 de la Ley 348 respecto a la CONCILIACIÓN en hechos de violencia hacia las mujeres?",
     ["Está expresamente PROHIBIDA toda forma de conciliación en hechos de violencia física o sexual y en casos graves o reincidentes",
      "La conciliación es obligatoria antes de iniciar cualquier trámite penal",
      "El Director de la UE debe obligar a las partes a firmar un acuerdo de perdón",
      "La junta escolar decide si se concilia o no",
      "Se permite la conciliación económica libremente en todos los casos"],
     0, "El art. 46 prohíbe categóricamente conciliar en hechos de violencia que comprometan la integridad física o sexual."),

    ("La entidad policial especializada encargada de recibir denuncias, investigar y proteger a víctimas de violencia según la Ley 348 es la:",
     ["FELCV (Fuerza Especial de Lucha Contra la Violencia)",
      "FELCC (Fuerza Especial de Lucha Contra el Crimen)",
      "Policía Caminera",
      "Interpol Bolivia",
      "Policía Turística"],
     0, "La FELCV es la unidad especializada creada para atender exclusivamente casos bajo la Ley 348."),

    ("Los SLIM son servicios municipales fundamentales en la estructura de la Ley 348. ¿Qué significan las siglas SLIM?",
     ["Servicios Legales Integrales Municipales",
      "Sistemas Locales de Información Magisterial",
      "Sociedades Libres de Integración de la Mujer",
      "Servicios Laborales para la Infancia y la Madre",
      "Secciones Legales de Inspección Municipal"],
     0, "Los SLIM brindan atención legal, psicológica y social gratuita en cada municipio."),

    ("El Sistema Integral de Registro de Casos de Violencia en razón de Género creado por la Ley 348 (art. 11) se denomina:",
     ["SIPPASE (Sistema Integral Plurinacional de Prevención, Atención, Sanción y Erradicación de la Violencia)",
      "RUDE", "SIE", "SIGEP", "SENASIR"],
     0, "El SIPPASE centraliza la información y emite los certificados de no violencia."),

    ("Según el art. 13 de la Ley 348, para el ejercicio de la función pública en cualquier nivel del Estado, es requisito indispensable:",
     ["No contar con antecedentes de violencia ejercida contra una mujer o cualquier miembro de su familia (Certificado SIPPASE)",
      "Tener libreta de ahorros en un banco estatal",
      "Ser propietario de bienes inmuebles",
      "Haber sido dirigente sindical durante 5 años",
      "Contar con recomendación de una junta de vecinos"],
     0, "El certificado de no antecedentes de violencia emitido por el SIPPASE es requisito obligatorio para todo servidor público."),

    ("En una Unidad Educativa, si un docente es denunciado penalmente con imputación formal por violencia sexual contra una estudiante, el Director debe:",
     ["Suspenderlo inmediatamente del contacto con estudiantes y ponerlo a disposición de la Dirección Distrital",
      "Cambiarlo a otro curso para que siga dictando clases",
      "Aconsejar a la familia que no denuncie a la policía",
      "Esperar la sentencia ejecutoriada de 10 años para tomar medidas administrativas",
      "Pagarle un bono especial de defensa legal"],
     0, "Las medidas cautelares y administrativas exigen la separación inmediata del contacto con menores."),

    ("Las 'Medidas de Protección Inmediata' previstas en el art. 35 de la Ley 348 pueden ser ordenadas por la autoridad competente para:",
     ["Evitar que el agresor se acerque, amenace, intimide o ingrese al lugar de estudio, trabajo o domicilio de la víctima",
      "Obligar a la víctima a abandonar la ciudad",
      "Retener el sueldo de la víctima",
      "Prohibir que la víctima continúe estudiando",
      "Entregar a los hijos al agresor"],
     0, "Las medidas de protección resguardan de forma urgente la seguridad y vida de la mujer y sus dependientes."),

    ("El art. 9 de la Ley 348 prohíbe en todos los niveles educativos:",
     ["Toda forma de violencia, acoso escolar sexista, tocamientos impúdicos y discriminación por razones de género",
      "La enseñanza de ciencias naturales y biología",
      "Los recreos deportivos mixtos",
      "La conformación de centros de estudiantes",
      "El uso de libros de texto actualizados"],
     0, "Garantiza espacios escolares seguros, inclusivos y libres de cualquier expresión de violencia sexista."),

    ("La 'Violencia Mediática' (art. 7.4) sanciona:",
     ["La difusión de imágenes, mensajes o textos que cosifiquen, difamen o degraden a las mujeres en medios de comunicación",
      "La publicación de notas y promedios escolares en el sistema oficial",
      "La emisión de noticias sobre eventos cívicos",
      "La publicidad de útiles escolares",
      "La transmisión de programas educativos infantiles"],
     0, "Sanciona la reproducción de estereotipos denigrantes y la exposición humillante de la mujer en medios."),

    ("Si un Director de Unidad Educativa encubre a un funcionario o docente que cometió abuso o violencia física en el colegio, incurre en el delito de:",
     ["Encubrimiento e incumplimiento de deberes formales (agravado por la Ley 348)",
      "Falta leve sin sanción",
      "Simple error administrativo subsanable",
      "Acto de solidaridad laboral justificado",
      "Uso de legítima defensa"],
     0, "El encubrimiento de delitos de violencia constituye una falta gravísima y un delito penal tipificado."),

    ("En el marco de la prevención, la Ley 348 dispone que el Ministerio de Educación incorpore en los planes de estudio:",
     ["Contenidos de equidad de género, derechos humanos, despatriarcalización y resolución no violenta de conflictos",
      "Cursos obligatorios de artes marciales agresivas",
      "Contenidos que justifiquen la superioridad masculina",
      "Reglas de sumisión femenina tradicional",
      "Exámenes de ingreso selectivos por género"],
     0, "Establece la obligatoriedad de la formación en valores de respeto, igualdad y despatriarcalización."),

    ("El principio de 'No Revictimización' en la atención de casos de violencia hacia las mujeres exige:",
     ["Evitar que la víctima deba relatar reiteradamente los hechos traumáticos ante distintas instancias innecesariamente",
      "Negarle asistencia legal gratuita",
      "Obligarla a carearse con su agresor en público",
      "Cuestionar su vestimenta y conducta moral",
      "Archivar su testimonio por falta de peritaje privado"],
     0, "La no revictimización protege la dignidad y estabilidad emocional de la persona afectada.")
]

def get_ley348_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley348", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley348-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

