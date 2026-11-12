# coding: utf-8
"""
Generador de preguntas para el Tema 4.5: Ley N° 548 Código Niña, Niño y Adolescente.
200 preguntas exhaustivas basadas en derechos, interés superior, acoso escolar, trabajo infantil y SIPPROINA.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley548"]

BASE_SPECS = [
    ("Según el art. 5 de la Ley 548 (Código Niña, Niño y Adolescente), se considera niña o niño a la persona desde:",
     ["La concepción hasta los 12 años cumplidos",
      "El nacimiento hasta los 18 años",
      "Los 5 años hasta los 15 años",
      "Los 3 años hasta los 10 años",
      "El bautismo hasta la mayoría de edad"],
     0, "El art. 5 define niña/niño hasta los 12 años cumplidos, y adolescente desde los 12 hasta los 18 años cumplidos."),

    ("Se considera ADOLESCENTE a la persona humana comprendida entre (art. 5):",
     ["Las edades de 12 a 18 años cumplidos",
      "Las edades de 10 a 16 años",
      "Las edades de 14 a 21 años",
      "Las edades de 15 a 18 años exclusivamente",
      "Las edades de 8 a 14 años"],
     0, "La etapa de la adolescencia comprende desde los 12 hasta cumplir los 18 años."),

    ("El principio del 'Interés Superior de la Niña, Niño y Adolescente' (art. 12) determina que:",
     ["Toda decisión que les concierna debe velar primordialmente por la satisfacción integral de sus derechos",
      "Los intereses económicos de la escuela priman sobre el estudiante",
      "Las decisiones de los adultos son incuestionables sin oír al menor",
      "Se debe priorizar el prestigio de la institución educativa",
      "Los derechos de los padres anulan los derechos de los hijos"],
     0, "El interés superior es un principio de orden público y cumplimiento obligatorio prioritario."),

    ("El principio de 'Prioridad Absoluta' (art. 13) implica que niñas, niños y adolescentes tienen preferencia en:",
     ["La atención en los servicios públicos, protección en desastres y asignación de recursos",
      "El pago de aranceles y multas",
      "La comparecencia ante tribunales penales",
      "El servicio militar obligatorio anticipado",
      "La contratación en empleos nocturnos"],
     0, "El art. 13 consagra la primacía y atención preferente en toda política pública."),

    ("El derecho a la integridad personal (art. 145) protege a las niñas, niños y adolescentes contra:",
     ["Cualquier forma de castigo corporal, trato humillante, abuso físico, psicológico o sexual",
      "La asistencia regular a la escuela",
      "La práctica de actividades deportivas supervisadas",
      "El aprendizaje de ciencias y matemáticas",
      "El cumplimiento de deberes escolares razonables"],
     0, "Está terminantemente prohibido el castigo corporal o cualquier trato degradante o violento."),

    ("En cuanto al derecho a la educación (art. 114), el Estado garantiza una educación:",
     ["Intracultural, intercultural y plurilingüe, gratuita, obligatoria y libre de discriminación",
      "Arancelada y condicionada a pruebas de ingreso selectivas",
      "Exclusiva para familias con vivienda propia",
      "Monolingüe sin contenidos indígenas",
      "Sujeta a donaciones obligatorias"],
     0, "El art. 114 garantiza la educación como derecho humano universal en el SEP."),

    ("El art. 152 de la Ley 548 define el 'Acoso Escolar' (Bullying) como:",
     ["Toda forma de violencia física, psicológica, verbal o cibernética reiterada entre pares en el ámbito escolar",
      "Una llamada de atención por llegar tarde",
      "El debate de ideas en el consejo de curso",
      "La calificación de una prueba de conocimientos",
      "El préstamo de libros de la biblioteca"],
     0, "Es la agresión reiterada, hostigamiento o exclusión entre estudiantes que crea un entorno intimidatorio."),

    ("Ante un caso confirmado de acoso escolar (bullying) grave en la Unidad Educativa, la dirección debe:",
     ["Activar el protocolo de atención inmediata, brindar apoyo psicosocial y coordinar con la DNA si es necesario",
      "Expulsar a la víctima para evitar problemas",
      "Ignorar la situación calificándola como simple 'juego de niños'",
      "Exigir pago monetario entre familias en la dirección",
      "Sancionar a todo el curso con pérdida de año escolar"],
     0, "Corresponde activar medidas de protección, mediación pedagógica y derivación a las DNAs."),

    ("¿Qué son las Defensorías de la Niñez y Adolescencia (DNA) según el art. 185?",
     ["Servicios municipales permanentes y gratuitos de defensa psico-socio-jurídica de los derechos de NNA",
      "Juzgados penales de sentencia",
      "Comisarías de detención policial",
      "Centros de internamiento cerrado",
      "Empresas privadas de seguridad escolar"],
     0, "Las DNAs dependen de los Gobiernos Autónomos Municipales y actúan de oficio o por denuncia."),

    ("El Sistema Plurinacional de Protección Integral de la Niña, Niño y Adolescente se conoce como (art. 165):",
     ["SIPPROINA", "SENASIR", "SEDEM", "SINAE", "SICOES"],
     0, "El SIPPROINA es el conjunto articulado de órganos, entidades y servicios encargados de proteger a la niñez."),

    ("Respecto a la EDAD MÍNIMA para trabajar en Bolivia (art. 126 modificado):",
     ["La edad mínima legal es 14 años, garantizándose la protección contra cualquier forma de explotación",
      "Los niños pueden trabajar en minas desde los 8 años",
      "No existe límite de edad para el trabajo nocturno",
      "Los 10 años en cualquier industria pesada",
      "Los 18 años cumplidos sin excepción alguna"],
     0, "La edad mínima general es de 14 años, asegurando derecho a la educación y prohibiendo trabajos peligrosos."),

    ("El art. 134 de la Ley 548 prohíbe taxativamente que niñas, niños o adolescentes realicen trabajos que:",
     ["Sean peligrosos, insalubres, atenten contra su dignidad o impidan su asistencia regular a la escuela",
      "Se realicen dentro del hogar colaborando en tareas familiares livianas",
      "Consistan en pasantías educativas supervisadas",
      "Se vinculen a prácticas deportivas o artísticas",
      "Sean voluntariados ecológicos escolares"],
     0, "Se prohíbe todo trabajo nocivo para el desarrollo físico, mental, moral o educativo del menor."),

    ("En cuanto al derecho a la familia (art. 35), la falta o carencia de recursos materiales o económicos:",
     ["En ningún caso constituye por sí sola motivo suficiente para la pérdida o suspensión de la autoridad materna o paterna",
      "Es causa directa de adopción forzada inmediata",
      "Impide la matriculación del niño en el colegio",
      "Permite la expulsión del hogar por orden policial",
      "Autoriza el internamiento en un orfanato"],
     0, "La pobreza económica jamás puede ser causal para separar a un niño de su núcleo familiar."),

    ("El art. 158 de la Ley 548 establece entre los DEBERES de las niñas, niños y adolescentes:",
     ["Respetar a sus padres, maestros, autoridades y cumplir responsablemente con sus deberes educativos",
      "Contribuir económicamente con un salario al colegio",
      "Aceptar castigos físicos sin quejarse",
      "Trabajar en jornadas laborales completas",
      "Renunciar a su idioma originario"],
     0, "Establece el deber de respetar a la comunidad, la patria, sus educadores y dedicarse al estudio."),

    ("El Sistema Penal para Adolescentes (art. 257) se aplica a personas que tengan entre:",
     ["14 y menos de 18 años al momento de cometer una infracción penal",
      "8 y 12 años",
      "10 y 14 años",
      "18 y 21 años",
      "Cualquier edad desde la concepción"],
     0, "La responsabilidad penal para adolescentes se aplica exclusivamente a partir de los 14 años."),

    ("Las sanciones aplicables a adolescentes en conflicto con la ley tienen una finalidad primordialmente (art. 258):",
     ["Socioeducativa, reparadora y de reinserción social",
      "Punitiva, ejemplificadora y de castigo carcelario común",
      "Económica mediante multas elevadas",
      "De aislamiento perpetuo",
      "De pérdida de ciudadanía boliviana"],
     0, "El sistema de justicia juvenil prioriza medidas socioeducativas en libertad o semilibertad."),

    ("Si un docente ejerce violencia física o psicológica (castigo corporal) contra un alumno dentro del aula:",
     ["Comete una falta gravísima que amerita suspensión o destitución y remisión de antecedentes a la DNA y Ministerio Público",
      "Está ejerciendo su legítimo derecho disciplinario docente",
      "Debe ser felicitado por la dirección",
      "Solo se le descuenta 10 bolivianos de su salario",
      "Se le otorga una semana de vacaciones pagadas"],
     0, "El castigo corporal está expresamente prohibido y penado por la legislación boliviana."),

    ("El derecho a la identidad (art. 65) establece que todo niño tiene derecho a:",
     ["Un nombre propio, filiación respecto a sus progenitores y nacionalidad boliviana",
      "Cambiar de identidad cada año libremente",
      "No tener registro en el SERECI",
      "Tener un número de serie en lugar de nombre",
      "Adoptar apellidos extranjeros obligatorios"],
     0, "El registro civil de nacimiento es gratuito e inmediato desde el nacimiento."),

    ("En una Unidad Educativa, la retención de libretas escolares por deudas de pensiones o cuotas:",
     ["Está TERMINANTEMENTE PROHIBIDA por vulnerar el derecho fundamental a la educación de la niña o niño",
      "Es una medida legal permitida a colegios privados",
      "Es una atribución exclusiva del Director de UE",
      "Se autoriza si lo aprueba la junta de padres",
      "Es obligatoria para colegios de convenio"],
     0, "La retención de libretas de calificaciones está prohibida por la CPE, Ley 548 y resoluciones ministeriales."),

    ("El deber de protección hacia niñas, niños y adolescentes compete de manera corresponsable a:",
     ["La familia, la sociedad y el Estado Plurinacional",
      "Únicamente a la Policía Nacional",
      "Exclusivamente a los profesores de aula",
      "A las agencias internacionales de ayuda",
      "Solo a los propios menores"],
     0, "El art. 3 establece la corresponsabilidad ineludible de la familia, la sociedad y el Estado.")
]

def get_ley548_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley548", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley548-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

