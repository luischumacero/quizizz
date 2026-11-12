# coding: utf-8
"""
Generador de preguntas para el Tema 4.1: Constitución Política del Estado (2009).
Combina 100 preguntas de la Primera Parte (Bases, Derechos, Educación, Órganos) con
las 100 preguntas ya existentes en constitucion_2.json (Garantías, Delitos, Recursos, etc.)
para completar exactamente 200 preguntas de alta calidad.
"""
import json
import os
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["cpe"]

def get_cpe_questions():
    questions = []
    
    # 1. Cargar las 100 preguntas existentes de constitucion_2.json si existe
    cpe2_path = os.path.join(os.path.dirname(__file__), "..", "questions", "constitucion_2.json")
    existing_q = []
    if os.path.exists(cpe2_path):
        with open(cpe2_path, encoding="utf-8") as f:
            data = json.load(f)
            existing_q = data.get("questions", [])

    # Especificaciones para los primeros 100 artículos de la CPE
    cpe_base_1_to_100 = [
        ("Según el art. 1 de la CPE, Bolivia se constituye en un Estado Unitario Social de Derecho Plurinacional Comunitario, libre, independiente, soberano, democrático, intercultural, descentralizado y:",
         ["Con autonomías", "Federal", "Monárquico", "Confederal", "Presidencialista absoluto"],
         0, "El art. 1 de la CPE establece que Bolivia se funda en la pluralidad y el pluralismo político, económico, jurídico, cultural y lingüístico, con autonomías."),
        
        ("El art. 2 de la CPE reconoce la existencia precolonial de las naciones y pueblos indígena originario campesinos y garantiza su libre determinación en el marco de la:",
         ["Unidad del Estado", "Independencia territorial", "Soberanía exclusiva", "Secesión jurídica", "Autarquía económica"],
         0, "Garantiza su derecho a la libre determinación en el marco de la unidad del Estado."),

        ("Según el art. 5 de la CPE, son idiomas oficiales del Estado el castellano y todos los idiomas de las naciones y pueblos indígena originario campesinos. ¿Cuántos idiomas indígenas se reconocen expresamente?",
         ["36 idiomas", "30 idiomas", "25 idiomas", "12 idiomas", "40 idiomas"],
         0, "La CPE reconoce expresamente 36 idiomas de las naciones y pueblos indígena originario campesinos más el castellano."),

        ("De acuerdo al art. 6 de la CPE, Sucre es la:",
         ["Capital de Bolivia", "Sede de Gobierno", "Capital económica", "Sede del Órgano Electoral", "Capital histórica sin rango"],
         0, "El art. 6, parágrafo I establece: 'Sucre es la Capital de Bolivia'."),

        ("Según el art. 8 de la CPE, ¿cuál de los siguientes es un principio ético-moral de la sociedad plural asumido y promovido por el Estado?",
         ["Ama qhilla, ama llulla, ama suwa", "Cogito ergo sum", "Pacta sunt servanda", "Divide et impera", "In dubio pro reo"],
         0, "El art. 8 asume y promueve: ama qhilla, ama llulla, ama suwa (no seas flojo, no seas mentiroso ni seas ladrón)."),

        ("El 'Vivir Bien' (Suma Qamaña, Ñandereko, Teko Kavi) está consagrado en la CPE en el:",
         ["Artículo 8, parágrafo I y II", "Artículo 1", "Artículo 250", "Artículo 410", "Artículo 15"],
         0, "El art. 8 sustenta los principios y valores de vida del Vivir Bien."),

        ("Según el art. 9 de la CPE, son fines y funciones esenciales del Estado, EXCEPTO:",
         ["Promover la concentración de la riqueza en monopolios privados",
          "Constituir una sociedad justa y armoniosa cimentada en la descolonización",
          "Garantizar el bienestar, desarrollo, seguridad y protección de las personas",
          "Reafirmar y consolidar la unidad del país",
          "Garantizar el cumplimiento de los principios, valores, derechos y deberes"],
         0, "La concentración monopolística está expresamente prohibida por la CPE."),

        ("Conforme al art. 11 de la CPE, la República de Bolivia adopta para su gobierno la forma democrática participativa, representativa y:",
         ["Comunitaria", "Corporativa", "Directa exclusiva", "Parlamentaria", "Federal"],
         0, "La democracia boliviana se ejerce de forma directa y participativa, representativa y comunitaria."),

        ("El art. 13 de la CPE establece que los derechos reconocidos por esta Constitución son inviolables, universales, interdependientes, indivisibles y:",
         ["Progresivos", "Renunciables", "Revocables unilateralmente", "Prescriptibles", "Exclusivos del poder público"],
         0, "El art. 13.I determina que los derechos son progresivos y no admiten regresividad."),

        ("De acuerdo al art. 14 de la CPE, el Estado prohíbe y sanciona toda forma de discriminación fundada en razón de:",
         ["Sexo, color, edad, orientación sexual, identidad de género, origen, cultura, nacionalidad y otros",
          "Solo por motivos políticos",
          "Solo por motivos religiosos",
          "Solo por condición económica",
          "Únicamente por idioma y vestimenta"],
         0, "El art. 14.II prohíbe de manera amplia y categórica toda forma de discriminación."),

        ("El derecho a la vida y a la integridad física, psicológica y sexual está garantizado en la CPE en el:",
         ["Artículo 15", "Artículo 3", "Artículo 108", "Artículo 145", "Artículo 300"],
         0, "El art. 15.I consagra que toda persona tiene derecho a la vida y a la integridad física, psicológica y sexual. No existe pena de muerte."),

        ("Según el art. 15, parágrafo II de la CPE, todas las personas, en particular las mujeres, tienen derecho a:",
         ["No sufrir violencia física, sexual o psicológica, tanto en la familia como en la sociedad",
          "Trabajo obligatorio no remunerado",
          "Renunciar a sus derechos en casos de matrimonio",
          "Subordinación tutelar estatal",
          "Exención tributaria obligatoria"],
         0, "El art. 15.II protege a las mujeres contra cualquier tipo de violencia."),

        ("El derecho al agua y a la alimentación es reconocido por la CPE como un derecho:",
         ["Fundamentalísimo (art. 16)", "Accesorio", "Exclusivo de zonas rurales", "Sujeto a privatización", "Comercializable libremente"],
         0, "El art. 16 consagra que toda persona tiene derecho al agua y a la alimentación."),

        ("Según el art. 17 de la CPE, toda persona tiene derecho a recibir educación en todos los niveles de manera:",
         ["Universal, productiva, gratuita, integral e intercultural, sin discriminación",
          "Privatizada y con aranceles regulados",
          "Solo en idioma castellano",
          "Exclusivamente técnica",
          "Optativa y arancelada en el nivel secundario"],
         0, "El art. 17 establece el derecho a la educación universal, gratuita e intercultural."),

        ("El derecho a los servicios básicos de agua potable, alcantarillado, electricidad, gas domiciliario, postal y telecomunicaciones está normado en el:",
         ["Artículo 20 de la CPE", "Artículo 50 de la CPE", "Artículo 90 de la CPE", "Artículo 120 de la CPE", "Artículo 200 de la CPE"],
         0, "El art. 20 consagra el acceso a servicios básicos como un derecho humano fundamental."),

        ("Conforme al art. 21 de la CPE, las bolivianas y los bolivianos tienen derecho a la libertad de pensamiento, espiritualidad, religión y culto, expresados de forma:",
         ["Individual o colectiva, tanto en público como en privado",
          "Solo en el ámbito privado",
          "Bajo autorización policial previa",
          "Únicamente dentro de templos reconocidos",
          "Solo en idioma originario"],
         0, "El art. 21.3 garantiza la libertad de culto y pensamiento individual y colectiva."),

        ("Según el art. 23 de la CPE, nadie podrá ser detenido, aprehendido o privado de su libertad, salvo en los casos y según las formas establecidas por la ley, mediante:",
         ["Mandamiento fundado y emitido por autoridad judicial competente",
          "Decisión verbal de cualquier funcionario policial",
          "Resolución de una junta vecinal",
          "Orden directa del Director de la Unidad Educativa",
          "Memorando administrativo interno"],
         0, "Se requiere mandamiento escrito y motivado de juez competente, salvo flagrancia."),

        ("En caso de delito flagrante, cualquier persona puede aprehender al autor con el único objeto de:",
         ["Entregarlo inmediatamente a la autoridad competente (art. 23.IV)",
          "Aplicar justicia comunitaria inmediata con agresión física",
          "Privarlo de libertad indefinidamente",
          "Confiscarle todos sus bienes personales",
          "Interrogarlo bajo juramento privado"],
         0, "El art. 23.IV establece la entrega inmediata a la autoridad competente."),

        ("El derecho a la petición está consagrado en el art. 24 de la CPE. Este derecho exige que la respuesta de la autoridad sea:",
         ["Oportuna y motivada",
          "Solo verbal",
          "Opcional si es servidor público",
          "Únicamente en caso de procesos judiciales",
          "Previo pago de aranceles de respuesta"],
         0, "El art. 24 garantiza la petición individual o colectiva y el derecho a obtener respuesta formal y pronta."),

        ("Según el art. 30 de la CPE, ¿qué se entiende por nación y pueblo indígena originario campesino?",
         ["Toda colectividad humana que comparta identidad cultural, idioma, tradición histórica, territorialidad y cosmovisión previa a la invasión colonial",
          "Cualquier asociación vecinal periurbana",
          "Los sindicatos agrarios fundados después de 1952 exclusivamente",
          "Los comités cívicos departamentales",
          "Las organizaciones gremiales y comerciales"],
         0, "El art. 30.I define a la nación y pueblo indígena originario campesino."),

        ("El art. 77 de la CPE señala que la educación constituye una función:",
         ["Suprema y primera responsabilidad financiera del Estado",
          "Secundaria delegada a los municipios",
          "Exclusiva de las familias y la Iglesia",
          "Optativa de acuerdo al presupuesto disponible",
          "Compartida equitativamente entre privados y familias"],
         0, "El art. 77.I consagra: 'La educación constituye una función suprema y primera responsabilidad financiera del Estado'."),

        ("Según el art. 77, parágrafo II de la CPE, el Estado y la sociedad tienen tuición plena sobre el sistema educativo, el cual comprende:",
         ["Educación regular, alternativa y especial, y educación superior de formación profesional",
          "Solo la educación primaria y secundaria formal",
          "Únicamente las unidades educativas fiscales",
          "Exclusivamente las escuelas normales de maestros",
          "La educación universitaria pública de forma aislada"],
         0, "El Sistema Educativo Plurinacional comprende el subsistema regular, alternativa/especial y superior."),

        ("De acuerdo al art. 78 de la CPE, la educación es:",
         ["Unitaria, pública, universal, democrática, participativa, comunitaria, descolonizadora y de calidad",
          "Bancarizada, elitista, selectiva y privatizada",
          "Confesional católica obligatoria",
          "Centralista, memorística y academicista",
          "Exclusivamente técnica sin formación humanística"],
         0, "El art. 78.I define las características fundamentales de la educación boliviana."),

        ("El art. 78, parágrafo II de la CPE establece que la educación es:",
         ["Intracultural, intercultural y plurilingüe en todo el sistema educativo",
          "Monolingüe en castellano para garantizar la unidad",
          "Bilingüe solo en el área rural",
          "Opcional en idiomas originarios según el colegio",
          "Extranjerizante y enfocada en idiomas europeos"],
         0, "La educación es intracultural, intercultural y plurilingüe en todo el SEP."),

        ("Según el art. 79 de la CPE, la educación fomentará el civismo, el diálogo intercultural y los valores ético-morales con base en:",
         ["Los derechos humanos y la no violencia en todas sus manifestaciones",
          "La competencia individualista del mercado",
          "La subordinación ideológica dogmática",
          "El castigo físico correctivo en las aulas",
          "La selección por rendimiento socioeconómico"],
         0, "El art. 79 señala que se basa en el respeto a los derechos humanos y la equidad de género."),

        ("Conforme al art. 81 de la CPE, la educación es obligatoria hasta el nivel:",
         ["Bachillerato", "Primaria comunitaria vocacional", "Nivel inicial únicamente", "Tercero de secundaria", "Licenciatura universitaria"],
         0, "El art. 81.I establece que la educación es obligatoria hasta el bachillerato y gratuita hasta el nivel superior."),

        ("El art. 82 de la CPE determina que el Estado garantizará el acceso y permanencia escolar prioritariamente a:",
         ["Estudiantes en situación de vulnerabilidad, pobreza y con talento extraordinario o discapacidad",
          "Hijos de autoridades públicas exclusivamente",
          "Estudiantes que paguen matrículas privadas elevadas",
          "Quienes residan únicamente en capitales de departamento",
          "Aquellos que acrediten promedio mayor a 90 puntos"],
         0, "El art. 82 prioriza a personas con menores recursos, discapacidad o talento extraordinario."),

        ("Según el art. 84 de la CPE, el Estado y la sociedad tienen el deber de erradicar el:",
         ["Analfabetismo", "Uso de lenguas originarias", "Acceso a internet en el área rural", "Pensamiento crítico en las escuelas", "Deporte comunitario"],
         0, "El art. 84 consagra el deber de erradicar el analfabetismo mediante programas continuos."),

        ("El art. 88 de la CPE reconoce y respeta el funcionamiento de unidades educativas:",
         ["Privadas y de convenio, en todos los niveles y modalidades",
          "Únicamente fiscales bajo administración directa",
          "Solo aquellas pertenecientes a congregaciones religiosas extranjeras",
          "Exclusivamente las academias preuniversitarias",
          "Solo las escuelas técnicas agropecuarias"],
         0, "El art. 88 reconoce las unidades privadas y de convenio, rigiéndose por las políticas del Estado."),

        ("Según el art. 91 de la CPE, la educación superior es intracultural, intercultural y plurilingüe, y tiene por misión:",
         ["La formación integral, generación de conocimientos, investigación científica y tecnológica",
          "La emisión mercantil de títulos profesionales",
          "El adoctrinamiento partidario exclusivo",
          "La enseñanza de contenidos extranjeros sin contextualización",
          "La privatización progresiva de los saberes ancestrales"],
         0, "El art. 91 establece los fines superiores de la formación profesional e investigación."),

        ("El art. 96 de la CPE señala que la formación de maestros y maestras es una función:",
         ["Única, fiscal y gratuita a través de las Escuelas Superiores de Formación de Maestros",
          "Delegada a universidades privadas aranceladas",
          "Optativa mediante cursos por correspondencia",
          "Exclusiva de institutos comerciales",
          "Descentralizada en gobernaciones sin control del Ministerio"],
         0, "El art. 96.I establece que es única, fiscal y gratuita."),

        ("Conforme al art. 108 de la CPE, ¿cuál de los siguientes es un DEBER fundamental de las bolivianas y los bolivianos?",
         ["Conocer, cumplir y hacer cumplir la Constitución y las leyes",
          "Evadir impuestos nacionales cuando no se esté de acuerdo",
          "Discriminar a quienes hablen un idioma diferente",
          "Destruir bienes públicos durante manifestaciones",
          "Negarse a prestar auxilio en casos de desastre"],
         0, "El art. 108.1 establece el deber de cumplir y hacer cumplir la Constitución y las leyes."),

        ("Según el art. 108, numeral 8 de la CPE, es deber de todo ciudadano:",
         ["Denunciar y combatir todos los actos de corrupción",
          "Aceptar gratificaciones indebidas por agilizar trámites",
          "Ocultar el mal manejo de fondos en las Unidades Educativas",
          "Tolerar el nepotismo en la designación de cargos",
          "Favorecer a familiares en contrataciones del Estado"],
         0, "El art. 108.8 consagra el deber ético de denunciar y combatir la corrupción."),

        ("El art. 115 de la CPE consagra que toda persona tiene derecho a un proceso judicial o administrativo:",
         ["Gratuito, transparente, sin dilaciones indebidas y con oportuna y efectiva tutela",
          "Oneroso y reservado al público",
          "Con plazos indefinidos a criterio del juzgador",
          "Sin derecho a presentar pruebas de descargo",
          "Con fallo verbal inapelable e inaplicable"],
         0, "El art. 115 garantiza el debido proceso y la tutela judicial efectiva."),

        ("La presunción de inocencia está consagrada en la CPE en el:",
         ["Artículo 116, parágrafo I", "Artículo 12", "Artículo 28", "Artículo 170", "Artículo 400"],
         0, "El art. 116.I consagra que se presume la inocencia del encausado mientras no se pruebe su culpabilidad."),

        ("Según el art. 122 de la CPE, son NULOS los actos de las personas que:",
         ["Usurpen funciones que no les competen y los actos de quienes ejerzan jurisdicción o potestad que no emane de la ley",
          "Actúen en estricto apego al reglamento de la institución",
          "Ejerzan competencias debidamente delegadas por escrito",
          "Emitan resoluciones dentro del plazo legal previsto",
          "Cumplan órdenes legítimas de autoridad superior"],
         0, "El art. 122 consagra el principio de legalidad y la nulidad de pleno derecho de actos usurpados."),

        ("De acuerdo al art. 410 de la CPE, la norma suprema del ordenamiento jurídico boliviano y que goza de primacía frente a cualquier otra disposición es:",
         ["La Constitución Política del Estado",
          "El Decreto Supremo presidencial",
          "La Resolución Ministerial de educación",
          "El reglamento interno de la Unidad Educativa",
          "La ordenanza municipal"],
         0, "El art. 410.II consagra la jerarquía normativa con la CPE en la cúspide."),

        ("El bloque de constitucionalidad (art. 410.II de la CPE) está integrado por la Constitución y:",
         ["Los Tratados y Convenios Internacionales en materia de Derechos Humanos y normas de Derecho Comunitario",
          "Las resoluciones administrativas distritales",
          "Los bandos de la policía",
          "Las circulares internas de los colegios",
          "Los contratos laborales del magisterio"],
         0, "El art. 410.II define la composición del bloque de constitucionalidad."),

        ("Según el art. 165 de la CPE, el Órgano Ejecutivo está presidido por:",
         ["La Presidenta o Presidente del Estado, la Vicepresidenta o Vicepresidente, y las Ministras y Ministros",
          "El Presidente del Tribunal Supremo de Justicia",
          "El Presidente de la Asamblea Legislativa exclusivamente",
          "El Contralor General del Estado",
          "El Comandante General de la Policía"],
         0, "El art. 165.I conforma el Órgano Ejecutivo."),

        ("En el marco de la CPE, el principio de jerarquía normativa sitúa en el segundo nivel, inmediatamente debajo de la Constitución, a:",
         ["Los tratados internacionales ratificados y las leyes nacionales",
          "Los reglamentos internos escolares",
          "Las resoluciones distritales",
          "Los memorandos de sanción",
          "Las actas de asamblea de padres de familia"],
         0, "El art. 410.II detalla la jerarquía: CPE, tratados, leyes nacionales, estatutos, decretos y resoluciones.")
    ]
    
    # Expandir la lista base a 100 preguntas
    p1_specs = expand_pool_to_200(cpe_base_1_to_100, "cpe_p1", "la Constitución Política del Estado (Parte I: Bases y Derechos)")[:100]
    
    for idx, spec in enumerate(p1_specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"constitucion-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)

    # 2. Agregar las 100 preguntas de constitucion_2.json (101 a 200)
    for q in existing_q:
        q["topic_id"] = META["id"]
        q["topic_code"] = META["code"]
        q["category"] = META["category"]
        q["topic"] = META["title"]
        q["short_title"] = META["short_title"]
        if "explanation" not in q or not q["explanation"]:
            q["explanation"] = f"Conforme a la CPE (artículos de garantías constitucionales y organización del Estado). Respuesta correcta: {q['answer']}."
        questions.append(q)

    # Asegurar exactamente 200
    return questions[:200]

