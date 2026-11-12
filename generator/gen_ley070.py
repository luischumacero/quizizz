# coding: utf-8
"""
Generador de preguntas para el Tema 4.2: Ley N° 070 de la Educación "Avelino Siñani–Elizardo Pérez".
200 preguntas exhaustivas basadas en los artículos, principios, subsistemas y estructura curricular.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley070"]

BASE_SPECS = [
    ("Según el art. 1 de la Ley 070, toda persona tiene derecho a recibir educación en todos los niveles de manera:",
     ["Universal, productiva, gratuita, integral e intercultural, sin discriminación",
      "Arancelada y sujeta a examen de ingreso socioeconómico",
      "Exclusivamente urbana y bilingüe en inglés",
      "Optativa para mujeres y obligatoria para varones",
      "Regulada por el mercado privado"],
     0, "El art. 1.1 ratifica el mandato constitucional de educación universal, productiva, gratuita e intercultural."),

    ("¿Qué nombre lleva la Ley de la Educación promulgada el 20 de diciembre de 2010?",
     ["Avelino Siñani – Elizardo Pérez", "Simón Bolívar", "Franz Tamayo", "Jaime Escalante", "Marcelo Quiroga Santa Cruz"],
     0, "Lleva el nombre de los pioneros de la Escuela Ayllu de Warisata: Avelino Siñani y Elizardo Pérez."),

    ("Según el art. 1, numeral 3 de la Ley 070, la educación es una función suprema y primera responsabilidad financiera del Estado, que tiene la obligación indeclinable de:",
     ["Sostenerla, garantizarla y gestionarla",
      "Privatizarla gradualmente",
      "Traspasarla a ONGs internacionales",
      "Limitarla a las áreas urbanas",
      "Cobrar aportes obligatorios a los padres de familia"],
     0, "El Estado Plurinacional tiene la obligación indeclinable de sostenerla, garantizarla y gestionarla."),

    ("El art. 2 de la Ley 070 establece que el Sistema Educativo Plurinacional reconoce tres tipos de instituciones educativas:",
     ["Fiscales y gratuitas, privadas, y de convenio",
      "Solo fiscales",
      "Municipales, departamentales y nacionales",
      "Laicas, religiosas y militares",
      "Urbanas, rurales y fronterizas"],
     0, "El art. 2.I reconoce unidades fiscales y gratuitas, privadas y de convenio sin fines de lucro."),

    ("De acuerdo al art. 3 de la Ley 070, ¿cuál de las siguientes es una BASE fundamental de la educación boliviana?",
     ["Es descolonizadora, liberadora, revolucionaria, antiimperialista y transformadora",
      "Es eurocéntrica, memorística y enciclopedista",
      "Es homogeneizadora y castellanizante",
      "Es selectiva y meritocrática individualista",
      "Es confesional católica obligatoria"],
     0, "El art. 3.1 define la educación descolonizadora como primera base del modelo sociocomunitario productivo."),

    ("La educación es comunitaria, democrática, participativa y de consensos según el art. 3 porque:",
     ["Se fundamenta en la vivencia y la participación social en la toma de decisiones educativas",
      "Es dirigida exclusivamente por el Director sin consultar a nadie",
      "Los estudiantes deciden sus propias notas sin evaluación",
      "Sigue el modelo de empresas privadas",
      "Solo participan los maestros federados"],
     0, "El art. 3.2 establece el carácter comunitario y participativo de consensos."),

    ("Según el art. 3, numeral 4 de la Ley 070, la educación es universal porque:",
     ["Atiende a todas y todos los habitantes del Estado Plurinacional sin distinción alguna",
      "Enseña únicamente contenidos internacionales",
      "Se imparte en idioma inglés en todos los colegios",
      "Exige pasaporte para ingresar a clases",
      "Está reservada para quienes viven en el territorio urbano"],
     0, "Es universal porque se extiende a todas las bolivianas y bolivianos en todo el territorio."),

    ("El art. 3, numeral 8 consagra que la educación es intracultural, intercultural y plurilingüe. La intraculturalidad promueve:",
     ["La recuperación, fortalecimiento, desarrollo y cohesión al interior de las culturas indígenas",
      "El desprecio de las culturas extranjeras",
      "La mezcla forzada de idiomas sin identidad",
      "El aislamiento total de las comunidades",
      "La prohibición de aprender castellano"],
     0, "La intraculturalidad fortalece y desarrolla la propia identidad cultural de cada pueblo."),

    ("La interculturalidad en la Ley 070 se define como:",
     ["La interacción, reciprocidad y convivencia armónica entre diferentes culturas en igualdad de condiciones",
      "La imposición de la cultura dominante sobre las minoritarias",
      "La asimilación de los pueblos indígenas a la cultura occidental",
      "La separación física de estudiantes según su idioma",
      "El intercambio comercial de bienes escolares"],
     0, "El art. 3.8 define la interculturalidad como el diálogo, convivencia y aprendizaje mutuo sin discriminación."),

    ("Según el art. 3, numeral 9, la educación es productiva y territorial porque:",
     ["Se orienta al trabajo creador y al desarrollo sostenible en armonía con la Madre Tierra",
      "Obliga a los estudiantes a trabajar en fábricas sin estudiar",
      "Vende productos escolares para autofinanciar la UE",
      "Se limita a la agricultura tradicional sin ciencia",
      "Prohíbe el uso de tecnología moderna"],
     0, "Articula la teoría con la práctica, la producción material e intelectual y el cuidado de la naturaleza."),

    ("El art. 4 de la Ley 070 establece como FIN de la educación:",
     ["Contribuir a la consolidación de la educación descolonizada y al Vivir Bien",
      "Promover la emigración de profesionales al extranjero",
      "Fomentar la acumulación individual de capital económico",
      "Sustituir las lenguas originarias por lenguas extranjeras",
      "Aislar a Bolivia del contexto internacional"],
     0, "El art. 4.1 busca consolidar una sociedad descolonizada para el Vivir Bien."),

    ("¿Qué artículo de la Ley 070 establece los OBJETIVOS de la educación boliviana?",
     ["Artículo 5", "Artículo 1", "Artículo 25", "Artículo 77", "Artículo 100"],
     0, "El art. 5 enumera los objetivos centrales de la educación en el Estado Plurinacional."),

    ("Según el art. 6 de la Ley 070, la educación es intracultural, intercultural y plurilingüe. En el currículo del SEP se enseña:",
     ["Una lengua originaria, el castellano y una lengua extranjera",
      "Únicamente castellano y latín",
      "Solo la lengua originaria del contexto sin castellano",
      "Tres lenguas extranjeras obligatorias",
      "Solo castellano en primaria y originario en secundaria"],
     0, "El art. 7 establece la obligatoriedad del aprendizaje de la lengua originaria, castellano y una extranjera."),

    ("De acuerdo al art. 7 de la Ley 070, en poblaciones o comunidades monolingües castellano-hablantes, la lengua originaria es:",
     ["Materia de aprendizaje obligatoria",
      "Optativa fuera de horario",
      "Prohibida en el aula",
      "Reemplazada por francés",
      "Exclusiva para personal administrativo"],
     0, "El art. 7.1 establece que en comunidades monolingües se aprende la lengua originaria como segunda lengua."),

    ("El Sistema Educativo Plurinacional (SEP) comprende tres subsistemas (art. 8):",
     ["Educación Regular, Educación Alternativa y Especial, y Educación Superior de Formación Profesional",
      "Educación Inicial, Primaria y Secundaria",
      "Educación Formal, No Formal e Informal",
      "Educación Fiscal, Privada y de Convenio",
      "Educación Urbana, Rural e Intercultural"],
     0, "El art. 8 estructura el SEP en estos tres grandes subsistemas."),

    ("El Subsistema de Educación Regular (art. 11) comprende los niveles:",
     ["Educación Inicial en Familia Comunitaria, Educación Primaria Comunitaria Vocacional y Educación Secundaria Comunitaria Productiva",
      "Prekínder, Primaria y Bachillerato Humanístico",
      "Guardería, Escuela Básica y Colegio Secundario",
      "Básica, Intermedia y Media",
      "Nivel Uno, Nivel Dos y Nivel Tres"],
     0, "El art. 11 define con precisión los tres niveles de la Educación Regular."),

    ("La Educación Inicial en Familia Comunitaria consta de dos etapas (art. 12):",
     ["No escolarizada (de 0 a 3 años) y escolarizada (de 4 a 5 años)",
      "Maternal y Prekínder",
      "Familiar y Barrial",
      "Comunitaria y Urbana",
      "De 1 a 2 años y de 3 a 6 años"],
     0, "El art. 12.1 distingue la etapa no escolarizada (0 a 3 años) y la escolarizada (4 y 5 años)."),

    ("La Educación Primaria Comunitaria Vocacional comprende (art. 13):",
     ["Seis años de escolaridad", "Cinco años de escolaridad", "Ocho años de escolaridad", "Cuatro años de escolaridad", "Siete años de escolaridad"],
     0, "Comprende 6 años de escolaridad orientados a la formación básica y desarrollo de vocaciones."),

    ("La Educación Secundaria Comunitaria Productiva (art. 14) comprende:",
     ["Seis años de escolaridad y otorga el diploma de bachiller técnico humanístico",
      "Cuatro años y título de bachiller en humanidades",
      "Cinco años sin especialidad técnica",
      "Tres años de ciclo diversificado",
      "Siete años de formación"],
     0, "Comprende 6 años y articula la formación humanística con la formación técnica con título BTH."),

    ("El Subsistema de Educación Alternativa y Especial (art. 16) tiene como áreas:",
     ["Educación Alternativa y Educación Especial",
      "Educación Nocturna y Educación Rural",
      "Educación Técnica y Educación Agraria",
      "Alfabetización y Cursos Rápidos",
      "Educación Inicial y Educación de Adultos"],
     0, "El art. 16 organiza el subsistema en Educación Alternativa y Educación Especial."),

    ("La Educación de Personas Jóvenes y Adultas (EPJA) corresponde al área de:",
     ["Educación Alternativa", "Educación Regular", "Educación Superior", "Educación Extraescolar", "Educación Municipal"],
     0, "La EPJA forma parte sustancial de la Educación Alternativa."),

    ("El área de Educación Especial (art. 25) atiende a estudiantes con:",
     ["Discapacidad, dificultades en el aprendizaje y talento extraordinario",
      "Únicamente ceguera o sordera",
      "Exclusivamente problemas de conducta",
      "Estudiantes repitentes de secundaria",
      "Personas mayores de 60 años"],
     0, "El art. 25 clasifica la Educación Especial en: personas con discapacidad, dificultades en el aprendizaje y talento extraordinario."),

    ("La formación de maestras y maestros en Bolivia es (art. 31):",
     ["Única, fiscal, gratuita y diversificada",
      "Privatizada y arancelada",
      "Exclusiva de las universidades autónomas",
      "Optativa para profesionales de otras ramas sin título pedagógico",
      "Descentralizada en los municipios"],
     0, "El art. 31 establece que la formación es única, fiscal y gratuita."),

    ("Las instituciones autorizadas para la formación inicial de maestros son (art. 35):",
     ["Las Escuelas Superiores de Formación de Maestras y Maestros (ESFM)",
      "Las academias pedagógicas privadas",
      "Los institutos técnicos departamentales",
      "Los colegios profesionales",
      "Las direcciones distritales de educación"],
     0, "Las ESFM y sus Unidades Académicas son las únicas facultadas para formar maestros."),

    ("El postgrado y la actualización continua de maestras y maestros en ejercicio se realiza a través de (art. 40):",
     ["La Universidad Pedagógica", "El Instituto Normal Superior", "Las gobernaciones", "Los sindicatos de maestros", "Empresas consultoras externas"],
     0, "La Universidad Pedagógica es la institución responsable de la formación postgradual del magisterio."),

    ("La estructura curricular en la Ley 070 (art. 69) se compone de:",
     ["Currículo Base, Currículo Regionalizado y Currículo Diversificado",
      "Currículo Oficial y Currículo Oculto",
      "Currículo Nacional y Currículo Extranjero",
      "Currículo Básico, Intermedio y Avanzado",
      "Currículo Teórico y Currículo Práctico"],
     0, "El art. 69 articula el Currículo Base plurinacional, los currículos regionalizados y el diversificado."),

    ("El Currículo Regionalizado (art. 70) es elaborado por:",
     ["Las naciones y pueblos indígena originario campesinos en coordinación con el Ministerio",
      "Los directores de unidades educativas de forma aislada",
      "El Banco Mundial y la UNESCO",
      "Las empresas editoriales escolares",
      "Los consejos municipales exclusivamente"],
     0, "Expresa la identidad, territorialidad, lengua y saberes de las naciones y pueblos originarios."),

    ("El Currículo Diversificado (art. 70) es formulado por:",
     ["La comunidad educativa de la Unidad Educativa para responder a su contexto local inmediato",
      "La Asamblea Legislativa Plurinacional mediante ley",
      "El Viceministro de Educación de forma unilateral",
      "La Junta Escolar sin los docentes",
      "El Ministerio de Economía"],
     0, "Recoge las particularidades del contexto local de la Unidad Educativa."),

    ("La gestión institucional del SEP se organiza en cuatro niveles de administración (art. 76):",
     ["Nivel Central, Nivel Departamental, Nivel Distrital y Nivel de Unidad Educativa",
      "Nivel Presidencial, Nivel Ministerial, Nivel Prefectural y Nivel Comunal",
      "Nivel Nacional, Nivel Regional, Nivel Cantonal y Nivel Escolar",
      "Nivel Macro, Nivel Meso, Nivel Micro y Nivel Nano",
      "Nivel Directivo, Nivel Docente, Nivel Administrativo y Nivel Estudiantil"],
     0, "El art. 76 establece los cuatro niveles de gestión y administración del SEP."),

    ("En el Nivel de Unidad Educativa (art. 83), la máxima autoridad responsable de la gestión técnico-pedagógica y administrativa es:",
     ["La Directora o el Director de la Unidad Educativa",
      "El Presidente del Consejo Educativo de Padres de Familia",
      "El Alcalde del Gobierno Autónomo Municipal",
      "El docente más antiguo del colegio",
      "El portero o regente de la UE"],
     0, "La Directora o Director es la máxima autoridad de la Unidad Educativa."),

    ("La Participación Social Comunitaria en educación (art. 90) tiene como instancia representativa de padres y madres en la UE a:",
     ["El Consejo Educativo Social Comunitario",
      "El Comité Cívico",
      "La Federación de Juntas Vecinales",
      "El Club de Madres",
      "La Asociación de Exalumnos"],
     0, "El Consejo Educativo Social Comunitario ejerce el control y apoyo social comunitario."),

    ("Según el art. 92 de la Ley 070, la participación social comunitaria NO tiene atribuciones para:",
     ["Imponer sanciones disciplinarias al personal docente ni interferir en la labor pedagógica de aula",
      "Participar en el diseño de planes educativos de la UE",
      "Promover el mantenimiento de la infraestructura escolar",
      "Coadyuvar en la seguridad alimentaria escolar (desayuno)",
      "Apoyar en actividades culturales y cívicas"],
     0, "El art. 92 delimita claramente las atribuciones de la participación social comunitaria."),

    ("El Observatorio Plurinacional de la Calidad Educativa (OPCE) fue creado por la Ley 070 (art. 89) para:",
     ["Hacer seguimiento, medición, evaluación y acreditación de la calidad del sistema educativo",
      "Sancionar económicamente a los maestros reprobados",
      "Cobrar licencias de funcionamiento a los colegios",
      "Comprar material escolar",
      "Dirigir el sindicato docente"],
     0, "El OPCE es la institución pública descentralizada de evaluación de la calidad del SEP."),

    ("El Instituto Plurinacional de Estudio de Lenguas y Culturas (IPELC) fue creado por la Ley 070 (art. 88) para:",
     ["Desarrollar procesos de investigación lingüística y cultural de las naciones y pueblos originarios",
      "Enseñar únicamente idiomas extranjeros modernos",
      "Supervisar la venta de uniformes escolares",
      "Otorgar becas de posgrado en el exterior",
      "Organizar desfiles escolares"],
     0, "El IPELC investiga, normaliza y promociona las lenguas y culturas del Estado Plurinacional."),

    ("El Bachillerato Técnico Humanístico (BTH) busca que las y los estudiantes al egresar de secundaria cuenten con:",
     ["Diploma de Bachiller y Título de Técnico Medio",
      "Solo certificado de egreso escolar",
      "Licenciatura en pedagogía",
      "Libreta de servicio militar",
      "Certificado de suficiencia en mecanografía"],
     0, "El BTH confiere formación integral humanística y técnica a nivel de Técnico Medio.")
]

def get_ley070_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley070", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley070-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

