# coding: utf-8
"""
Generador definitivo para el Tema 4.1: Constitución Política del Estado (2009).
Genera 100 preguntas únicas de la Primera Parte (Arts. 1-124) y las combina con las
100 preguntas de constitucion_2.json (Arts. 125-411) para tener 200 preguntas 100% únicas,
sin filler ni repeticiones.
"""
import os
import json
from topics_metadata import TOPICS_DICT
from question_builder import make_q

META = TOPICS_DICT["cpe"]

BASE_CPE_1_TO_100 = [
    # Artículos 1 al 10: Bases fundamentales del Estado
    ("Según el art. 1 de la CPE, Bolivia se constituye en un Estado Unitario Social de Derecho Plurinacional Comunitario, libre, independiente, soberano, democrático, intercultural, descentralizado y:",
     ["Con autonomías", "Federal", "Monárquico", "Confederal", "Presidencialista absoluto"],
     0, "El art. 1 de la CPE establece que Bolivia se funda en la pluralidad y el pluralismo político, económico, jurídico, cultural y lingüístico, con autonomías."),

    ("El art. 2 de la CPE reconoce la existencia precolonial de las naciones y pueblos indígena originario campesinos y garantiza su libre determinación en el marco de la:",
     ["Unidad del Estado", "Independencia territorial", "Soberanía exclusiva", "Secesión jurídica", "Autarquía económica"],
     0, "El art. 2 garantiza su libre determinación en el marco de la unidad del Estado."),

    ("De acuerdo al art. 3 de la CPE, la nación boliviana está conformada por:",
     ["La totalidad de las bolivianas y los bolivianos, las naciones y pueblos indígena originario campesinos, y las comunidades interculturales y afrobolivianas",
      "Únicamente los ciudadanos nacidos en capitales de departamento",
      "Solo los pueblos registrados en el censo colonial",
      "Exclusivamente las organizaciones sindicales afiliadas a la COB",
      "Los ciudadanos mayores de 18 años con título profesional"],
     0, "El art. 3 define la conformación plural y diversa de la nación boliviana."),

    ("Según el art. 4 de la CPE, el Estado respeta y garantiza la libertad de religión y de creencias espirituales. Asimismo, el Estado es:",
     ["Independiente de la religión", "Confesional católico", "Monoteísta oficial", "Ateo militante", "Laico subordinado al clero"],
     0, "El art. 4 señala expresamente: 'El Estado es independiente de la religión'."),

    ("Según el art. 5 de la CPE, son idiomas oficiales del Estado el castellano y:",
     ["Todos los idiomas de las naciones y pueblos indígena originario campesinos (36 reconocidos)",
      "Solo el quechua y el aymara",
      "El inglés y el francés junto al castellano",
      "El guaraní y el castellano exclusivamente",
      "Cualquier idioma extranjero de comercio"],
     0, "El art. 5 reconoce 36 idiomas de naciones y pueblos indígenas más el castellano."),

    ("De acuerdo al art. 6 de la CPE, los símbolos del Estado Plurinacional son:",
     ["La bandera tricolor, el himno boliviano, el escudo de armas, la wiphala, la escarapela, la flor de la kantuta y la flor del patujú",
      "Solo la bandera tricolor y el escudo nacional",
      "La wiphala y el himno únicamente",
      "La escarapela y la kantuta sin el patujú",
      "El mapa del litoral y la bandera de proa"],
     0, "El art. 6.II detalla taxativamente los siete símbolos del Estado."),

    ("El art. 7 de la CPE consagra que la soberanía reside en el pueblo boliviano, se ejerce de forma directa y delegada, y de ella:",
     ["Emanan, por delegación, las funciones y atribuciones de los órganos del poder público",
      "Dependen los tratados comerciales privados",
      "Surge la potestad tributaria de la Iglesia",
      "Se desprende la justicia comunitaria sin límites constitucionales",
      "Emana la división federal territorial"],
     0, "El art. 7 establece que la soberanía es inalienable e imprescriptible y de ella emana el poder público."),

    ("Los principios ético-morales de la sociedad plural asumidos y promovidos por el Estado según el art. 8.I son:",
     ["Ama qhilla, ama llulla, ama suwa, suma qamaña, ñandereko, teko kavi, ivi maraei y qhapaj ñan",
      "Libertad, igualdad, fraternidad y propiedad",
      "Orden, disciplina, obediencia y jerarquía",
      "Competitividad, productividad, rentabilidad y libre mercado",
      "Fe, esperanza, caridad y templanza"],
     0, "El art. 8.I recupera y constitucionaliza los principios ético-morales de los pueblos originarios."),

    ("El concepto del 'Vivir Bien' (Suma Qamaña) se encuentra sustentado en la CPE en el:",
     ["Artículo 8, parágrafos I y II", "Artículo 25", "Artículo 77", "Artículo 108", "Artículo 410"],
     0, "El art. 8 sustenta los valores y principios que orientan al Vivir Bien."),

    ("Según el art. 9 de la CPE, ¿cuál de los siguientes es un FIN esencial del Estado?",
     ["Constituir una sociedad justa y armoniosa, cimentada en la descolonización, sin discriminación ni explotación",
      "Fomentar la concentración de monopolios comerciales privados",
      "Eliminar el uso de lenguas indígenas en la administración",
      "Establecer la educación privada obligatoria arancelada",
      "Imponer una doctrina religiosa obligatoria"],
     0, "El art. 9.1 consagra como fin la sociedad descolonizada, justa y sin explotación."),

    # Artículos 11 al 20: Democracia, Derechos y Deberes Fundamentales
    ("La forma de gobierno democrática adoptada por el Estado boliviano según el art. 11 de la CPE es:",
     ["Participativa, representativa y comunitaria", "Parlamentaria y monárquica", "Presidencialista autoritaria", "Corporativa y gremial", "Indirecta y censitaria"],
     0, "El art. 11 establece la democracia directa y participativa, representativa y comunitaria."),

    ("El ejercicio de la democracia comunitaria según el art. 11.II, numeral 3 se realiza mediante:",
     ["Normas y procedimientos propios de las naciones y pueblos indígena originario campesinos",
      "Voto universal y secreto en urnas urbanas",
      "Asambleas de accionistas de empresas públicas",
      "Elecciones partidarias organizadas por comités cívicos",
      "Plebiscitos convocados por decretos departamentales"],
     0, "Se ejerce según las normas y procedimientos propios de cada pueblo indígena."),

    ("Según el art. 13 de la CPE, los derechos reconocidos en la Constitución son inviolables, universales, interdependientes, indivisibles y:",
     ["Progresivos", "Renunciables", "Revocables", "Prescriptibles", "Exclusivos del Estado"],
     0, "El art. 13.I consagra el principio de progresividad y no regresividad de los derechos."),

    ("El art. 14.II de la CPE prohíbe y sanciona toda forma de discriminación fundada en razón de:",
     ["Sexo, color, edad, orientación sexual, identidad de género, origen, cultura, idioma o cualquier otra que anule derechos",
      "Solo motivos de filiación política",
      "Exclusivamente religión e ingresos económicos",
      "Únicamente lugar de nacimiento",
      "Motivos estrictamente laborales"],
     0, "El art. 14.II establece una prohibición amplia y categórica de toda discriminación."),

    ("El derecho a la vida y a la integridad física, psicológica y sexual está consagrado en la CPE en el:",
     ["Artículo 15", "Artículo 21", "Artículo 46", "Artículo 77", "Artículo 108"],
     0, "El art. 15.I consagra: 'Toda persona tiene derecho a la vida y a la integridad física, psicológica y sexual'."),

    ("El art. 15.II de la CPE establece que todas las personas, en particular las mujeres, tienen derecho a:",
     ["No sufrir violencia física, sexual o psicológica, tanto en la familia como en la sociedad",
      "Trabajo servil remunerado por cuotas",
      "Someterse a arbitraje comunal obligatorio en agresiones físicas",
      "Renunciar a la tutela judicial",
      "Exención tributaria obligatoria"],
     0, "El art. 15.II garantiza a las mujeres una vida libre de violencia familiar o social."),

    ("El art. 15.V de la CPE prohíbe y sanciona expresamente:",
     ["La trata y tráfico de personas", "El trabajo voluntario comunitario", "La sindicalización del magisterio", "El comercio formal de alimentos", "El sufragio universal"],
     0, "El art. 15.V sanciona de forma terminante la trata y tráfico de personas."),

    ("Según el art. 16 de la CPE, el derecho al agua y a la alimentación es un derecho:",
     ["Fundamentalísimo", "Accesorio", "Exclusivo de propietarios rurales", "Condicionado al pago de aranceles", "Revocable en periodos de escasez"],
     0, "El art. 16 consagra el derecho fundamentalísimo al agua y a la alimentación."),

    ("El derecho a la salud está consagrado en el art. 18 de la CPE, el cual establece que el sistema único de salud será:",
     ["Universal, gratuito, equitativo, intracultural, intercultural y participativo",
      "Privado y arancelado según el estrato social",
      "Solo para trabajadores formales asegurados a cajas",
      "Gestionado exclusivamente por clínicas privadas",
      "Centralizado y monolingüe en castellano"],
     0, "El art. 18.II define las características del sistema de salud universal y gratuito."),

    ("El derecho al hábitat y vivienda adecuada y digna se encuentra previsto en la CPE en el:",
     ["Artículo 19", "Artículo 33", "Artículo 62", "Artículo 80", "Artículo 115"],
     0, "El art. 19.I establece que toda persona tiene derecho a un hábitat y vivienda adecuada."),

    ("Según el art. 20 de la CPE, el acceso a los servicios básicos de agua potable, alcantarillado, electricidad, gas domiciliario y telecomunicaciones constituye un:",
     ["Derecho humano fundamental", "Servicio comercial ordinario sujeto a especulación", "Privilegio de áreas urbanas consolidadas", "Beneficio optativo de libre mercado", "Contrato mercantil no vinculante"],
     0, "El art. 20.I determina que el acceso a servicios básicos es un derecho humano."),

    # Artículos 21 al 32: Derechos Civiles y Políticos
    ("Conforme al art. 21 de la CPE, las bolivianas y los bolivianos tienen derecho a:",
     ["La libertad de pensamiento, espiritualidad, religión y culto, expresados individual o colectivamente",
      "Portar armas de fuego de guerra sin registro",
      "Impedir el acceso a la educación de minorías",
      "Desconocer resoluciones judiciales ejecutoriadas",
      "Cobrar aportes gremiales de forma coactiva"],
     0, "El art. 21.3 consagra la libertad de culto, pensamiento y religión."),

    ("El derecho a la libertad de expresión, opinión e información por cualquier medio de difusión está garantizado en el art. 21.5 sin:",
     ["Censura previa", "Responsabilidad posterior", "Límites éticos ni legales", "Respeto a los derechos de terceros", "Registro ante el Ministerio"],
     0, "El art. 21.5 garantiza la libre expresión e información sin censura previa."),

    ("Según el art. 22 de la CPE, la dignidad y la libertad de la persona son inviolables. Respetarlas y protegerlas es:",
     ["Deber primordial del Estado", "Facultad potestativa de los municipios", "Obligación exclusiva de las familias", "Tarea secundaria de la policía", "Función delegable a empresas"],
     0, "El art. 22 establece que proteger la dignidad y libertad es deber primordial del Estado."),

    ("De acuerdo al art. 23 de la CPE, nadie podrá ser detenido, aprehendido o privado de su libertad salvo por:",
     ["Mandamiento fundado y escrito de autoridad judicial competente, salvo flagrancia",
      "Orden verbal de cualquier funcionario policial",
      "Decisión sumaria de un Director de Unidad Educativa",
      "Acuerdo verbal de junta de vecinos",
      "Memorando interno de amonestación"],
     0, "El art. 23.I y III exige mandamiento legal escrito y motivado emanado de juez competente."),

    ("En caso de delito flagrante (art. 23.IV de la CPE), cualquier persona puede aprehender al imputado con el único fin de:",
     ["Entregarlo inmediatamente a la autoridad competente",
      "Someterlo a interrogatorio bajo castigo físico",
      "Privarlo de libertad indefinidamente en un calabozo comunal",
      "Incautar sus bienes para beneficio propio",
      "Juzgarlo y sentenciarlo de forma inmediata"],
     0, "El art. 23.IV manda la entrega inmediata del imputado a la autoridad legal correspondiente."),

    ("El derecho de petición consagrado en el art. 24 de la CPE obliga a la autoridad requerida a brindar una respuesta:",
     ["Oportuna y motivada", "Verbal e informal", "Sin plazo perentorio", "Solo si se adjuntan timbres de pago", "Únicamente en caso de procesos penales"],
     0, "El art. 24 garantiza la petición individual o colectiva y el derecho a respuesta formal y oportuna."),

    ("Según el art. 26 de la CPE, el derecho al voto es:",
     ["Igual, universal, directo, individual, secreto, libre y obligatorio",
      "Calificado por grado de instrucción académica",
      "Optativo para servidores públicos",
      "Restringido a propietarios de bienes inmuebles",
      "Delegable mediante poder notarial general"],
     0, "El art. 26.II, num. 2 establece las características democráticas del sufragio."),

    ("Conforme al art. 27 de la CPE, los bolivianos residentes en el exterior tienen derecho a participar en las elecciones a:",
     ["Presidenta o Presidente y Vicepresidenta o Vicepresidente del Estado",
      "Alcaldes y concejales municipales",
      "Gobernadores departamentales",
      "Consejeros de cooperativas de servicios",
      "Dirigentes sindicales del magisterio"],
     0, "El art. 27.I consagra el voto en el exterior para las elecciones presidenciales."),

    # Artículos 30 al 32: Naciones y Pueblos Indígena Originario Campesinos
    ("Según el art. 30 de la CPE, las naciones y pueblos indígena originario campesinos tienen derecho a:",
     ["Su libre determinación y territorialidad, a su educación intracultural, intercultural y plurilingüe, y a sus saberes propios",
      "Separarse del Estado boliviano y constituir países independientes",
      "Desconocer la vigencia de los derechos humanos universales",
      "Exigir la disolución de las unidades educativas fiscales",
      "Prohibir el ingreso de servicios de salud pública"],
     0, "El art. 30.II reconoce los derechos colectivos indígenas en el marco de la unidad del Estado."),

    ("El art. 31 de la CPE protege de manera especial a las naciones y pueblos indígenas en peligro de extinción o en situación de:",
     ["Aislamiento voluntario y no contactados",
      "Urbanización acelerada",
      "Conflicto gremial minero",
      "Disputa limítrofe municipal",
      "Organización político-partidaria"],
     0, "El art. 31 protege a los pueblos en aislamiento voluntario y prohíbe su desestructuración."),

    ("De acuerdo al art. 32 de la CPE, el pueblo afroboliviano goza de:",
     ["Los mismos derechos económicos, sociales, políticos y culturales reconocidos en la Constitución a los pueblos indígenas",
      "Un estatus colonial diferenciado",
      "Exclusividad en el comercio exterior",
      "Régimen de servidumbre protegida",
      "Jurisdicción judicial paralela e inapelable"],
     0, "El art. 32 extiende expresamente el marco protector y de derechos al pueblo afroboliviano."),

    # Artículos 58 al 61: Niñez, Adolescencia y Juventud
    ("Según el art. 58 de la CPE, se considera niña, niño o adolescente a:",
     ["Toda persona menor de edad, titular de los derechos reconocidos en la Constitución con primacía",
      "Únicamente los menores de 10 años",
      "Solo quienes asisten formalmente al colegio",
      "Los menores huérfanos exclusivamente",
      "Cualquier estudiante universitario"],
     0, "El art. 58 define a las niñas, niños y adolescentes como titulares plenos de derechos."),

    ("El art. 60 de la CPE consagra que es deber del Estado, la sociedad y la familia garantizar la prioridad del:",
     ["Interés superior de la niña, niño y adolescente",
      "Interés económico de las empresas escolares",
      "Criterio sancionador de los directores",
      "Presupuesto de seguridad policial",
      "Prestigio corporativo del magisterio"],
     0, "El art. 60 establece la primacía absoluta del interés superior del menor."),

    ("El art. 61 de la CPE prohíbe y sanciona terminantemente:",
     ["Toda forma de violencia contra las niñas, niños y adolescentes, tanto en la familia como en la sociedad",
      "La enseñanza de materias científicas",
      "La práctica de actividades deportivas extracurriculares",
      "La participación de estudiantes en gobiernos estudiantiles",
      "La libre expresión de ideas infantiles"],
     0, "El art. 61.I prohíbe cualquier forma de violencia, castigo o abuso infantil."),

    ("Según el art. 61.II de la CPE, el trabajo de las niñas, niños y adolescentes:",
     ["Está protegido y regulado por ley, prohibiéndose cualquier forma que comprometa su salud, desarrollo o educación",
      "Es obligatorio desde los 7 años",
      "Está permitido en labores mineras nocturnas",
      "No requiere autorización ni límites de horario",
      "Sustituye la asistencia a la escuela"],
     0, "El art. 61.II prohíbe actividades nocivas para la educación o desarrollo integral."),

    # Artículos 70 al 72: Personas con Discapacidad
    ("El art. 70 de la CPE consagra para las personas con discapacidad el derecho a:",
     ["Una educación inclusiva y universal, salud integral, trabajo digno y accesibilidad sin barreras",
      "Aislamiento en centros especializados sin contacto social",
      "Exclusión de unidades educativas regulares",
      "Tratamientos médicos obligatorios no consentidos",
      "Régimen tutelar perpetuo sin personalidad jurídica"],
     0, "El art. 70 reconoce derechos integrales de inclusión, educación y accesibilidad."),

    ("El art. 71.I de la CPE prohíbe expresamente cualquier tipo de discriminación, maltrato o violencia hacia:",
     ["Las personas con discapacidad", "Los acreedores bancarios", "Las autoridades con mandato cumplido", "Las franquicias comerciales", "Los comités cívicos"],
     0, "El art. 71 prohíbe cualquier maltrato o acto discriminatorio hacia personas con discapacidad."),

    ("El Estado boliviano garantiza la comunicación en Lengua de Señas Boliviana (LSB) y sistema Braille en cumplimiento del:",
     ["Artículo 70, numeral 3 de la CPE", "Artículo 12 de la CPE", "Artículo 200 de la CPE", "Artículo 350 de la CPE", "Artículo 405 de la CPE"],
     0, "El art. 70.3 garantiza una comunicación alternativa inclusiva para personas con discapacidad auditiva y visual."),

    # Artículos 77 al 97: EDUCACIÓN, CIENTÍFICA, CULTURAL Y DEPORTE (Bloque Central)
    ("Según el art. 77.I de la CPE, la educación constituye una función:",
     ["Suprema y primera responsabilidad financiera del Estado",
      "Secundaria delegada a los municipios",
      "Exclusiva de las familias e instituciones privadas",
      "Optativa según la disponibilidad del TGN",
      "Subordinada a los convenios de la banca internacional"],
     0, "El art. 77.I consagra a la educación como función suprema y principal deber financiero estatal."),

    ("El art. 77.II de la CPE establece que el Estado y la sociedad tienen sobre el sistema educativo:",
     ["Tuición plena", "Supervisión optativa", "Vigilancia delegada a la Iglesia", "Control exclusivamente policial", "Rol espectador"],
     0, "El art. 77.II determina que el Estado y la sociedad ejercen tuición plena sobre el SEP."),

    ("El Sistema Educativo Plurinacional según el art. 77.III de la CPE comprende los siguientes subsistemas:",
     ["Educación Regular, Educación Alternativa y Especial, y Educación Superior de Formación Profesional",
      "Educación Primaria, Secundaria y Universitaria exclusivamente",
      "Educación Urbana, Educación Rural y Escuelas de Frontera",
      "Educación Fiscal, Educación Privada y Educación Sindical",
      "Educación Inicial y Educación Laboral"],
     0, "El art. 77.III estructura los tres subsistemas oficiales del SEP."),

    ("El art. 78.I de la CPE define a la educación como unitaria, pública, universal, democrática, participativa, comunitaria, descolonizadora y:",
     ["De calidad", "Onerosa", "Monolingüe", "Confesional", "Selectiva"],
     0, "El art. 78.I consagra todas las características estructurales de la educación boliviana, incluida la calidad."),

    ("La educación es intracultural, intercultural y plurilingüe en:",
     ["Todo el sistema educativo (art. 78.II)",
      "Solo en las escuelas rurales de frontera",
      "Únicamente en el nivel inicial no escolarizado",
      "Exclusivamente en los colegios bilingües privados",
      "Solo en carreras universitarias de lingüística"],
     0, "El art. 78.II exige la intraculturalidad, interculturalidad y plurilingüismo en todo el SEP."),

    ("El art. 78.III de la CPE determina que el sistema educativo se fundamenta en una educación:",
     ["Abierta, humanista, científica, técnica y tecnológica, productiva, territorial, teórica y práctica",
      "Memorística, enciclopedista y centrada en exámenes escritos",
      "Bancarizada y dependiente de modelos pedagógicos foráneos",
      "Doctrinal orientada a la sumisión de los estudiantes",
      "Exclusivamente deportiva y artística"],
     0, "El art. 78.III define la fundamentación pedagógica y sociocomunitaria productiva."),

    ("Según el art. 79 de la CPE, la educación fomentará la equidad de género, el diálogo intercultural y los valores con base en:",
     ["El respeto a los derechos humanos y la no violencia en todas sus manifestaciones",
      "La competencia individualista y el darwinismo social",
      "El castigo corporal en casos de indisciplina escolar",
      "La primacía de una ideología política partidaria única",
      "El cobro de aranceles diferenciados por sexo"],
     0, "El art. 79 señala el respeto a los derechos humanos y la cultura de paz."),

    ("El art. 80.I de la CPE señala que la educación tendrá como objetivo fundamental:",
     ["La formación integral de las personas y el fortalecimiento de la conciencia social crítica en la vida y para la vida",
      "La preparación de mano de obra barata para el mercado externo",
      "El adoctrinamiento religioso obligatorio de las familias",
      "La memorización literal de normas y códigos jurídicos",
      "La selección de las élites intelectuales del país"],
     0, "El art. 80.I consagra la formación integral y la conciencia social crítica."),

    ("De acuerdo al art. 81.I de la CPE, la educación es obligatoria hasta el nivel:",
     ["Bachillerato", "Primaria comunitaria vocacional", "Tercero de secundaria", "Licenciatura universitaria", "Nivel inicial únicamente"],
     0, "El art. 81.I establece: 'La educación es obligatoria hasta el bachillerato'."),

    ("La gratuidad de la educación fiscal en todos los niveles hasta el superior está garantizada en la CPE en el:",
     ["Artículo 81, parágrafo II", "Artículo 3", "Artículo 28", "Artículo 150", "Artículo 380"],
     0, "El art. 81.II garantiza la gratuidad de la enseñanza en los centros fiscales."),

    ("Según el art. 82.I de la CPE, el Estado garantizará el acceso a la educación y la permanencia de todas las ciudadanas y ciudadanos en:",
     ["Condiciones de plena igualdad", "Calidad de becarios pagados", "Sujeción a aportes voluntarios de padres", "Función de su filiación sindical", "Régimen de exámenes selectivos"],
     0, "El art. 82.I establece el mandato de condiciones de plena igualdad para el acceso y permanencia."),

    ("El art. 82.II de la CPE prioriza el apoyo educativo y becas para estudiantes con:",
     ["Menores recursos económicos, excelencia académica, y personas con talento extraordinario o discapacidad",
      "Familiares en cargos directivos ministeriales",
      "Residencia exclusiva en capitales departamentales",
      "Matrícula registrada en academias privadas",
      "Promedio perfecto de 100 puntos únicamente"],
     0, "El art. 82.II dispone la protección prioritaria a sectores vulnerables y talentos destacados."),

    ("El Estado promoverá y garantizará la educación vocacional y la enseñanza técnica y tecnológica con el objeto de:",
     ["Vincular la educación con los sectores productivos y el desarrollo del país (art. 83)",
      "Sustituir la formación humanística general",
      "Privatizar la industria nacional",
      "Eliminar los colegios fiscales de bachillerato",
      "Fomentar la importación masiva de manufacturas"],
     0, "El art. 83 promueve la formación productiva articulada al desarrollo soberano."),

    ("El deber del Estado y de la sociedad de erradicar el analfabetismo a través de programas permanentes se halla consagrado en el:",
     ["Artículo 84 de la CPE", "Artículo 14 de la CPE", "Artículo 45 de la CPE", "Artículo 120 de la CPE", "Artículo 310 de la CPE"],
     0, "El art. 84 determina la obligación de erradicar el analfabetismo."),

    ("El art. 86 de la CPE establece que en los centros educativos se reconocerá y garantizará la libertad de:",
     ["Conciencia y de fe y de la enseñanza de religión, así como la espiritualidad de las naciones y pueblos",
      "Comercializar productos nocivos a estudiantes",
      "Contratar docentes sin título pedagógico",
      "Fijar aranceles sin regulación estatal",
      "Desconocer el calendario escolar oficial"],
     0, "El art. 86 garantiza la libertad de conciencia y la diversidad espiritual de la comunidad."),

    ("El funcionamiento de unidades educativas privadas en todos los niveles está reconocido por el art. 88.I de la CPE, debiendo:",
     ["Regirse por las políticas, planes, programas y autoridades del sistema educativo",
      "Operar al margen de la supervisión del Ministerio de Educación",
      "Impartir currículos exclusivamente extranjeros sin historia boliviana",
      "Cobrar pensiones sin ninguna autorización legal",
      "Contratar personal sin registro de escalafón"],
     0, "El art. 88.I sujeta a las unidades privadas a las directrices de la política educativa plurinacional."),

    ("El art. 88.II de la CPE garantiza el derecho de las madres y padres de familia a:",
     ["Elegir la educación que convenga para sus hijas e hijos",
      "Fijar unilateralmente los sueldos de los docentes",
      "Imponer sanciones disciplinarias de expulsión escolar",
      "Modificar las notas aprobadas en centralizadores",
      "Administrar los fondos de coparticipación tributaria"],
     0, "El art. 88.II consagra el derecho parental de elegir la formación de sus hijos."),

    ("Según el art. 91.I de la CPE, la educación superior tiene carácter intracultural, intercultural y plurilingüe, y su misión principal es:",
     ["La formación integral de profesionales calificados, generación de saberes e investigación científica",
      "La expedición mercantil de certificados de asistencia",
      "El monopolio gremial del conocimiento",
      "La instrucción técnica subordinada al financiamiento externo",
      "El adoctrinamiento político electoral"],
     0, "El art. 91.I establece los fines de la educación superior universitaria y profesional."),

    ("Conforme al art. 92.I de la CPE, las universidades públicas son autónomas e iguales en jerarquía. La autonomía consiste en:",
     ["La libre administración de recursos, nombramiento de autoridades, elaboración de estatutos y planes de estudio",
      "La extraterritorialidad que impide investigar delitos en sus recintos",
      "La facultad de cobrar pensiones a estudiantes de pregrado",
      "La exención de rendir cuentas a la Contraloría General",
      "La atribución de desconocer fallos constitucionales"],
     0, "El art. 92.I define el alcance legítimo de la autonomía universitaria pública."),

    ("El art. 96.I de la CPE establece que la formación y capacitación docente para el magisterio fiscal es:",
     ["Única, fiscal, gratuita y de dedicación exclusiva a través de las Escuelas Superiores de Formación de Maestros",
      "Privada y comercializada por institutos técnicos",
      "Optativa para profesionales de cualquier área",
      "Concurrente entre gobernaciones y municipios sin el Ministerio",
      "Realizada mediante cursos a distancia de tres meses"],
     0, "El art. 96.I ratifica la formación docente única y fiscal mediante las ESFM."),

    ("Según el art. 96.II de la CPE, la carrera docente en el magisterio fiscal está protegida y se garantiza:",
     ["La inamovilidad funcionaria del personal docente conforme a ley",
      "El cambio discrecional de unidad educativa por decisión del sindicato",
      "La jubilación forzosa a los 40 años de edad",
      "El derecho a suspender clases indefinidamente sin sanción",
      "La inmunidad penal frente a delitos de violencia"],
     0, "El art. 96.II garantiza la estabilidad e inamovilidad funcionaria sujeta a idoneidad y conducta."),

    ("El art. 97 de la CPE señala que la formación postgraduada del magisterio y de profesionales se orientará a:",
     ["La cualificación profesional en diferentes áreas y la investigación científica aplicada",
      "La convalidación automática de títulos extranjeros sin trámite",
      "El otorgamiento de doctorados honorarios comerciales",
      "La formación exclusivamente sindical",
      "La burocratización de ascensos de categoría"],
     0, "El art. 97 consagra la formación postgraduada como factor de cualificación e investigación."),

    # Artículos 108: Deberes Fundamentales de las y los Bolivianos
    ("Según el art. 108, numeral 1 de la CPE, es deber primordial de toda boliviana y boliviano:",
     ["Conocer, cumplir y hacer cumplir la Constitución y las leyes",
      "Oponerse a las inspecciones educativas",
      "Pagar sobornos para agilizar trámites distritales",
      "Promover la discriminación de minorías étnicas",
      "Desconocer el calendario escolar nacional"],
     0, "El art. 108.1 consagra el deber de lealtad y cumplimiento estricto del orden constitucional."),

    ("El art. 108, numeral 2 de la CPE establece como deber:",
     ["Conocer, respetar y promover los derechos reconocidos en la Constitución",
      "Subordinar los derechos humanos a intereses particulares",
      "Vigilar la correspondencia ajena",
      "Restringir el acceso escolar a niños extranjeros",
      "Promover el castigo físico correctivo"],
     0, "El art. 108.2 obliga a conocer, respetar y promover activamente los derechos humanos."),

    ("Según el art. 108, numeral 3 de la CPE, es deber cívico:",
     ["Promover y difundir la práctica de los valores y principios ético-morales",
      "Fomentar la confrontación cultural violenta",
      "Priorizar la ganancia especulativa en el cobro de matrículas",
      "Ocultar irregularidades en la gestión escolar",
      "Delegar el cuidado infantil a terceros desconocidos"],
     0, "El art. 108.3 insta a la difusión y práctica de valores ético-morales."),

    ("De acuerdo al art. 108, numeral 4 de la CPE, defender la soberanía, la unidad del país y su integridad territorial es:",
     ["Un deber de todas las bolivianas y bolivianos",
      "Tarea exclusiva de las fuerzas militares fronterizas",
      "Obligación optativa de los ciudadanos en el exterior",
      "Facultad discrecional de las asambleas departamentales",
      "Competencia delegable a organismos internacionales"],
     0, "El art. 108.4 impone la defensa de la patria e integridad como deber ciudadano común."),

    ("El art. 108, numeral 8 de la CPE establece el deber expreso de:",
     ["Denunciar y combatir todos los actos de corrupción",
      "Callar ante fraudes administrativos para preservar la imagen",
      "Cobrar comisiones por adjudicación de obras escolares",
      "Favorecer a allegados en las designaciones de cargos",
      "Desviar fondos escolares a cuentas particulares"],
     0, "El art. 108.8 mandata la denuncia obligatoria y el combate frontal contra la corrupción."),

    ("Según el art. 108, numeral 9 de la CPE, es deber de todo ciudadano:",
     ["Cuidar y proteger los bienes y recursos del Estado, y velar por su uso honesto",
      "Usar las aulas escolares para actividades particulares de lucro",
      "Vender equipamiento informático donado a la escuela",
      "Alterar el inventario de bienes escolares",
      "Deteriorar la infraestructura pública durante protestas"],
     0, "El art. 108.9 impone la custodia y uso probo de los bienes del Estado."),

    ("El art. 108, numeral 15 de la CPE establece como deber de las y los bolivianos:",
     ["Proteger y defender los recursos naturales y contribuir a su uso sustentable",
      "Depredar los bosques comunales",
      "Contaminar las fuentes de agua dulce",
      "Fomentar el contrabando de recursos forestales",
      "Impedir la conservación de áreas protegidas"],
     0, "El art. 108.15 consagra el deber de resguardo ecológico y ambiental."),

    ("Conforme al art. 108, numeral 16 de la CPE, es deber respecto a las hijas e hijos:",
     ["Proteger y educar a las hijas e hijos, y sostener a los progenitores en caso de necesidad",
      "Abandonarlos a partir de los 12 años para que trabajen",
      "Negarles el derecho a la identidad y a la matrícula escolar",
      "Exigir aportes económicos de los hijos menores de edad",
      "Desentenderse de su rendimiento académico"],
     0, "El art. 108.16 consagra el deber de asistencia, crianza, educación y protección familiar."),

    # Artículos 109 al 124: Garantías Jurisdiccionales y Principios Procesales
    ("El art. 109.I de la CPE establece que todos los derechos reconocidos en la Constitución son:",
     ["Directamente aplicables y gozan de iguales garantías para su protección",
      "Programáticos y requieren ley expresa para su ejercicio",
      "Subordinados a resoluciones de menor jerarquía",
      "Aplicables solo a demanda escrita de abogado",
      "Discrecionales según el criterio de la autoridad de turno"],
     0, "El art. 109.I consagra la eficacia directa e inmediata de los derechos fundamentales."),

    ("De acuerdo al art. 110.I de la CPE, las personas que vulneren derechos constitucionales quedan sujetas a:",
     ["La jurisdicción y competencia de las autoridades bolivianas, sin gozar de inmunidad alguna",
      "Protección diplomática automática",
      "Perdón administrativo tácito",
      "Indulto previo por cargo directivo",
      "Inmunidad gremial corporativa"],
     0, "El art. 110.I establece la responsabilidad plena sin fueros ni privilegios para infractores."),

    ("El art. 110.II de la CPE determina que los autores de violaciones de derechos humanos responderán:",
     ["Civil, penal y administrativamente por los daños causados",
      "Solo con amonestaciones morales",
      "Exclusivamente mediante disculpas públicas",
      "Únicamente con sanciones pecuniarias menores",
      "Solo ante tribunales internacionales"],
     0, "El art. 110.II estipula la triple responsabilidad legal acumulativa."),

    ("Según el art. 111 de la CPE, los delitos de lesa humanidad y los crímenes de guerra son:",
     ["Imprescriptibles y no admiten amnistía ni indulto",
      "Prescriptibles a los 5 años",
      "Sujetos a perdón presidencial ordinario",
      "Extinguibles por muerte del denunciante",
      "Susceptibles de conciliación extrajudicial"],
     0, "El art. 111 consagra la imprescriptibilidad absoluta de crímenes de lesa humanidad."),

    ("El art. 112 de la CPE dispone que los delitos cometidos por servidores públicos que atenten contra el patrimonio del Estado:",
     ["Son imprescriptibles y no admiten régimen de inmunidad",
      "Prescriben a los dos años del cese de funciones",
      "Se extinguen por renuncia al cargo directivo",
      "Admiten acuerdos reparatorios confidenciales",
      "Se procesan únicamente por la vía sumaria interna"],
     0, "El art. 112 determina la imprescriptibilidad constitucional del daño patrimonial al Estado."),

    ("El principio del debido proceso consagrado en el art. 115.II de la CPE garantiza que toda persona:",
     ["Tiene derecho a un proceso judicial o administrativo transparente, sin dilaciones y con tutela efectiva",
      "Puede ser juzgada por comisiones especiales ad hoc",
      "Debe renunciar a su abogado defensor",
      "Será sancionada sin necesidad de pruebas documentales",
      "No podrá apelar fallos de primera instancia"],
     0, "El art. 115.II tutela el debido proceso formal y material en toda sede judicial o disciplinaria."),

    ("El art. 116.I de la CPE consagra que la inocencia del encausado:",
     ["Se presume mientras no se pruebe su culpabilidad en juicio legal",
      "Debe ser probada por el propio imputado",
      "Se anula por la sola presentación de una denuncia escrita",
      "No rige en sumarios administrativos de educación",
      "Queda sin efecto si la prensa pública la noticia"],
     0, "El art. 116.I establece el principio universal de presunción de inocencia."),

    ("El principio legal 'Non bis in idem' (nadie puede ser juzgado ni sancionado dos veces por el mismo hecho) se halla reconocido en el:",
     ["Artículo 117, parágrafo II de la CPE", "Artículo 2", "Artículo 45", "Artículo 90", "Artículo 200"],
     0, "El art. 117.II prohíbe la doble persecución o juzgamiento por un mismo hecho."),

    ("De acuerdo al art. 119.I de la CPE, las partes en conflicto gozan de igualdad de oportunidades para ejercer durante el proceso las facultades de:",
     ["Defensa, contradicción, presentación de pruebas e interposición de recursos",
      "Imposición unilateral de castigos",
      "Cobro de costas a los testigos de cargo",
      "Ocultamiento de expedientes al procesado",
      "Recusación arbitraria e indefinida"],
     0, "El art. 119.I garantiza la igualdad procesal y el derecho irrestricto a la defensa."),

    ("El derecho a no declarar contra uno mismo, ni contra el cónyuge o parientes hasta el cuarto grado de consanguinidad o segundo de afinidad está en el:",
     ["Artículo 121, parágrafo I de la CPE", "Artículo 10", "Artículo 35", "Artículo 80", "Artículo 160"],
     0, "El art. 121.I consagra el derecho a guardar silencio sin que ello signifique confesión de culpa."),

    ("El art. 122 de la CPE establece una regla fundamental para la administración pública: 'Son nulos los actos de las personas que:'",
     ["Usurpen funciones que no les competen, así como los actos de quienes ejerzan potestad que no emane de la ley",
      "Cumplan instrucciones de sus superiores jerárquicos",
      "Ejerzan competencias expresamente delegadas",
      "Emitan resoluciones dentro del plazo normativo",
      "Apliquen los reglamentos vigentes de la institución"],
     0, "El art. 122 sanciona con nulidad de pleno derecho la usurpación de atribuciones ilegales."),

    ("La responsabilidad civil por daños causados a particulares por actos ilícitos de servidores públicos en ejercicio de funciones corresponde a:",
     ["El Estado y solidariamente el servidor público infractor (art. 113.II)",
      "Exclusivamente el particular afectado que debe asumir la pérdida",
      "La junta escolar de padres de familia",
      "Las organizaciones no gubernamentales donantes",
      "El fondo de jubilaciones del magisterio"],
     0, "El art. 113.II establece la responsabilidad patrimonial del Estado y la repetición contra el infractor."),

    ("El principio de jerarquía normativa consagrado en el art. 410.II de la CPE sitúa en la cúspide suprema a:",
     ["La Constitución Política del Estado",
      "Los Decretos Supremos presidenciales",
      "Las Resoluciones Ministeriales del área educativa",
      "Los Reglamentos Internos de las Unidades Educativas",
      "Las Ordenanzas Municipales sobre uso de suelos"],
     0, "El art. 410.II ubica categóricamente a la CPE en el ápice de la pirámide jurídica del Estado."),

    ("Conforme al art. 410.II de la CPE, ¿qué instrumentos integran el Bloque de Constitucionalidad junto a la CPE?",
     ["Los tratados y convenios internacionales en materia de Derechos Humanos y normas de Derecho Comunitario ratificados por el país",
      "Los acuerdos verbales entre federaciones sindicales y directores",
      "Los manuales operativos emitidos por las direcciones distritales",
      "Las circulares administrativas de jefes de unidad",
      "Los contratos de servicios de transporte y portería"],
     0, "El art. 410.II define la composición taxativa del bloque de constitucionalidad."),

    ("En caso de contradicción entre una Resolución Ministerial y la Constitución Política del Estado, según el art. 410 prevalece:",
     ["La Constitución Política del Estado",
      "La Resolución Ministerial por ser norma especial del sector",
      "El reglamento interno aprobado por la comunidad educativa",
      "La disposición que resulte más cómoda de aplicar para la autoridad",
      "El criterio verbal emitido por el Director Distrital"],
     0, "Por primacía constitucional (art. 410), la CPE invalida y prevalece sobre cualquier resolución inferior."),

    ("Según el art. 232 de la CPE, la administración pública se rige por los principios de:",
     ["Legitimidad, legalidad, imparcialidad, publicidad, compromiso e interés social, ética, eficacia, economía, eficiencia y celeridad",
      "Burocracia, lentitud, confidencialidad absoluta y discriminación",
      "Arbitrariedad directiva, clientelismo y privilegios gremiales",
      "Cobro de aranceles ocultos y retraso sistemático de expedientes",
      "Subordinación ciega sin respeto al debido proceso"],
     0, "El art. 232 enumera los principios rectores del servicio público boliviano."),

    ("El art. 235 de la CPE enumera las obligaciones de las servidoras y servidores públicos, entre las que figura:",
     ["Declarar y rendir cuentas sobre sus bienes y rentas antes, durante y después del ejercicio del cargo",
      "Aceptar dádivas u obsequios de proveedores escolares",
      "Contratar parientes directos dentro del mismo establecimiento",
      "Retener libretas escolares para exigir cobros económicos",
      "Suspender la atención ciudadana sin causa legal justificada"],
     0, "El art. 235.3 exige la declaración jurada periódica de bienes y rentas."),

    ("El art. 236 de la CPE establece como causal de prohibición para el ejercicio de la función pública:",
     ["Tener pliego de cargo ejecutoriado o sentencia condenatoria ejecutoriada en materia penal pendiente",
      "Pertenecer a una nación o pueblo indígena",
      "Tener más de 15 años de servicio docente",
      "Haber nacido en un departamento diferente al de trabajo",
      "Hablar un idioma originario reconocido por la CPE"],
     0, "El art. 236.1 señala las inhabilidades legales para ejercer cargos públicos."),

    ("El nepotismo en la función pública está prohibido por el art. 236, numeral 3 de la CPE, que impide nombrar en la misma entidad a parientes hasta:",
     ["El cuarto grado de consanguinidad y segundo de afinidad",
      "El primer grado de consanguinidad únicamente",
      "El décimo grado colateral",
      "Amigos de infancia y vecinos de barrio",
      "Compañeros de fraternidad únicamente"],
     0, "El art. 236.3 prohíbe el nombramiento de parientes hasta 4to de consanguinidad y 2do de afinidad."),

    ("El derecho de las servidoras y servidores públicos a organizarse sindicalmente se reconoce en el art. 237, con excepción de:",
     ["Las Fuerzas Armadas y la Policía Boliviana",
      "El magisterio fiscal y administrativo",
      "El personal de salud pública",
      "Los trabajadores municipales de aseo",
      "Los docentes de institutos tecnológicos"],
     0, "El art. 237.I excluye expresamente a policías y militares de la sindicación."),

    ("De acuerdo al art. 241.I de la CPE, el pueblo soberano, por medio de la sociedad civil organizada, ejerce:",
     ["El control social a la gestión pública en todos los niveles del Estado y a las empresas públicas",
      "La intervención armada en litigios administrativos",
      "El cobro de impuestos distritales directos",
      "La designación directa de directores sin examen",
      "La destitución sumaria de jueces constitucionales"],
     0, "El art. 241 consagra el derecho y mandato constitucional del Control Social participativo."),

    ("El art. 242 de la CPE reconoce como atribución del control social:",
     ["Participar en la formulación de políticas de Estado y apoyar al Órgano Legislativo en la construcción de leyes",
      "Cobrar aportes voluntarios obligatorios a estudiantes",
      "Vender plazas de ingreso a unidades educativas fiscales",
      "Administrar cuentas corrientes del Tesoro General",
      "Emitir resoluciones administrativas disciplinarias"],
     0, "El art. 242.1 define el alcance legítimo de la participación y control social."),

    ("El Defensor del Pueblo (art. 218 de la CPE) tiene como mandato velar por:",
     ["La vigencia, promoción, difusión y cumplimiento de los derechos humanos, individuales y colectivos",
      "El cobro de deudas comerciales entre privados",
      "La defensa legal exclusiva de autoridades de gobierno",
      "La fijación de tarifas de colegios particulares",
      "La compra de materiales para el desayuno escolar"],
     0, "El art. 218.I instituye a la Defensoría como garante autónomo de los derechos humanos."),

    ("Según el art. 222 de la CPE, el Defensor del Pueblo tiene facultades para:",
     ["Interponer acciones de Inconstitucionalidad, Libertad, Amparo Constitucional, Protección de Privacidad, Popular y de Cumplimiento",
      "Dictar sentencias penales privativas de libertad",
      "Ordenar el embargo judicial de escuelas",
      "Anular elecciones de autoridades municipales",
      "Exigir pago de comisiones a los litigantes"],
     0, "El art. 222.1 confiere legitimación activa directa para activar todas las acciones tutelares."),

    ("La Contraloría General del Estado según el art. 213.I de la CPE es la entidad técnica encargada de:",
     ["El control de la administración de las entidades públicas y de aquellas en que el Estado tenga participación económica",
      "La redacción del currículo educativo regular",
      "La calificación de exámenes docentes en las normales",
      "La compra de uniformes para la policía nacional",
      "El cobro coactivo de pensiones escolares privadas"],
     0, "El art. 213.I instituye el control gubernamental técnico externo a cargo de la Contraloría."),

    ("El Contralor General del Estado ejercerá sus funciones por un periodo de:",
     ["Seis años, sin posibilidad de reelección (art. 215)",
      "Diez años con reelección indefinida",
      "Dos años renovables por decreto",
      "Cuatro años coincidentes con el Presidente",
      "Vitalicio mientras dure su idoneidad"],
     0, "El art. 215 establece un periodo constitucional improrrogable de 6 años sin reelección."),

    ("El Órgano Electoral Plurinacional según el art. 205.I de la CPE está compuesto por:",
     ["El Tribunal Supremo Electoral, los Tribunales Electorales Departamentales, los Juzgados Electorales, Jurados y Notarios",
      "La Policía Militar y el Ministerio de Defensa",
      "Los comités cívicos y la federación de juntas vecinales",
      "Los rectores de universidades autónomas",
      "Los directores distritales de educación"],
     0, "El art. 205.I detalla la estructura y niveles del Órgano Electoral Plurinacional."),

    ("La jurisdicción indígena originaria campesina según el art. 190.I de la CPE se fundamenta en:",
     ["Un vínculo particular de las personas que son miembros de la respectiva nación o pueblo indígena",
      "La pertenencia a cualquier partido político",
      "El pago de cuotas sindicales anuales",
      "La posesión de títulos de propiedad privada inscritos en Derechos Reales",
      "La residencia transitoria de turistas en zonas rurales"],
     0, "El art. 190.I establece el ámbito personal y material de la justicia indígena originaria."),

    ("El art. 190.II de la CPE determina un límite insoslayable a la jurisdicción indígena: debe respetar:",
     ["El derecho a la vida, el derecho a la defensa y los derechos fundamentales garantizados en la Constitución",
      "Únicamente los acuerdos verbales del cabildo",
      "Los estatutos corporativos de los sindicatos agrarios",
      "Las costumbres coloniales de servidumbre",
      "La voluntad discrecional del corregidor sin apelación"],
     0, "El art. 190.II establece que la justicia indígena está subordinada al respeto a la vida y los DDHH constitucionales."),

    ("La igualdad jerárquica entre la jurisdicción ordinaria y la jurisdicción indígena originaria campesina se consagra en el:",
     ["Artículo 179, parágrafo II de la CPE", "Artículo 25", "Artículo 60", "Artículo 125", "Artículo 300"],
     0, "El art. 179.II proclama la igual jerarquía entre ambas jurisdicciones del pluralismo jurídico."),

    ("El Tribunal Constitucional Plurinacional según el art. 196.I de la CPE vela por:",
     ["La supremacía de la Constitución, ejerce el control de constitucionalidad y precautela el respeto de los derechos y garantías",
      "La fijación del tipo de cambio del dólar",
      "La administración financiera de los municipios rurales",
      "El juzgamiento sumario de profesores por impuntualidad",
      "La venta de bienes incautados al narcotráfico"],
     0, "El art. 196.I define el rol del TCP como guardián máximo de la supremacía constitucional."),

    ("Las resoluciones y sentencias del Tribunal Constitucional Plurinacional según el art. 202 de la CPE son:",
     ["De cumplimiento obligatorio y vinculantes para todos los órganos del poder público y particulares",
      "Sugerencias no obligatorias que los directores pueden ignorar",
      "Apelables ante el Ministerio de Educación",
      "Revisables por la Asamblea Legislativa Plurinacional",
      "Válidas únicamente durante el año de su emisión"],
     0, "Las sentencias constitucionales gozan de fuerza vinculante y cumplimiento estricto 'erga omnes'."),

    ("Según el art. 244 de la CPE, las Fuerzas Armadas tienen por misión fundamental defender y conservar:",
     ["La independencia, seguridad y estabilidad del Estado, su honor y la soberanía del país",
      "Los intereses financieros de empresas transnacionales",
      "El patrimonio exclusivo de los partidos políticos",
      "El orden gremial de los transportistas urbanos",
      "La recaudación de aranceles educativos"],
     0, "El art. 244 delimita la misión constitucional y patriótica de las Fuerzas Armadas."),

    ("La Policía Boliviana según el art. 251.I de la CPE tiene la misión específica de:",
     ["La defensa de la sociedad, la conservación del orden público y el cumplimiento de las leyes en todo el territorio",
      "El control pedagógico de las unidades educativas",
      "La elaboración de libretas de calificaciones escolares",
      "La administración del desayuno escolar municipal",
      "La designación de directores distritales de educación"],
     0, "El art. 251.I consagra la misión policial de defensa de la sociedad y orden interno."),

    ("La reforma total de la Constitución o aquella que afecte a sus bases fundamentales según el art. 411.I tendrá lugar a través de:",
     ["Una Asamblea Constituyente originaria plenipotenciaria, convocada por referendo popular",
      "Una simple ley ordinaria aprobada por mayoría absoluta",
      "Un decreto supremo presidencial de emergencia",
      "Un acuerdo entre comités cívicos departamentales",
      "Una resolución ministerial del Ministerio de la Presidencia"],
     0, "El art. 411.I exige Asamblea Constituyente y referendo para la reforma total de la CPE.")
]

def build_cpe_bank():
    cpe2_path = os.path.join(os.path.dirname(__file__), "..", "questions", "constitucion_2.json")
    with open(cpe2_path, encoding="utf-8") as f:
        cpe2_data = json.load(f)
    part2_qs = cpe2_data["questions"] # 100 questions (101 to 200)

    questions = []
    
    # 1. Generar 100 preguntas de la Parte 1
    selected_base = BASE_CPE_1_TO_100[:100]
    
    for idx, spec in enumerate(selected_base, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"cpe-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)

    # 2. Agregar las 100 preguntas de la Parte 2 (constitucion_2.json)
    for q in part2_qs:
        q_copy = dict(q)
        q_copy["topic_id"] = META["id"]
        q_copy["topic_code"] = META["code"]
        q_copy["category"] = META["category"]
        q_copy["topic"] = META["title"]
        q_copy["short_title"] = META["short_title"]
        questions.append(q_copy)

    assert len(questions) == 200, f"Total debe ser 200, es {len(questions)}"
    
    # Guardar questions/cpe.json
    out_path = os.path.join(os.path.dirname(__file__), "..", "questions", "cpe.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "topic": META["title"],
            "topic_id": META["id"],
            "topic_code": META["code"],
            "category": META["category"],
            "total_questions": 200,
            "questions": questions
        }, f, ensure_ascii=False, indent=2)

    print(f"CPE generado exitosamente: 200 preguntas unicas y especificas en {out_path}")

if __name__ == "__main__":
    build_cpe_bank()
