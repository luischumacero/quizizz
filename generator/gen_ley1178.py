# coding: utf-8
"""
Generador de preguntas para el Tema 4.7: Ley N° 1178 de Administración y Control Gubernamentales (SAFCO).
200 preguntas exhaustivas sobre los 8 sistemas SAFCO, responsabilidades administrativa, ejecutiva, civil y penal.
"""
from topics_metadata import TOPICS_DICT
from question_builder import make_q
from builder_helpers import expand_pool_to_200

META = TOPICS_DICT["ley1178"]

BASE_SPECS = [
    ("¿Cuál es el objeto primordial de la Ley N° 1178 (SAFCO) promulgada el 20 de julio de 1990?",
     ["Regular los sistemas de administración y de control de los recursos del Estado y su relación con los sistemas nacionales de planificación e inversión",
      "Fijar precios máximos de la canasta familiar",
      "Organizar las elecciones de los poderes públicos",
      "Regular el matrimonio civil y la herencia",
      "Establecer la política arancelaria aduanera"],
     0, "El art. 1 de la Ley 1178 establece el marco de administración de recursos públicos y responsabilidad."),

    ("Según el art. 2 de la Ley 1178, ¿cuántos sistemas de administración y control regula esta ley?",
     ["Ocho (8) sistemas", "Cinco (5) sistemas", "Tres (3) sistemas", "Doce (12) sistemas", "Quince (15) sistemas"],
     0, "La Ley 1178 establece 8 sistemas agrupados en tres categorías: programar/organizar, ejecutar y controlar."),

    ("Los sistemas para PROGRAMAR y ORGANIZAR las actividades son (art. 2.a):",
     ["Sistema de Programación de Operaciones (SPO), Organización Administrativa (SOA) y Presupuesto (SP)",
      "Sistema de Personal, Bienes y Servicios, y Tesorería",
      "Sistema de Control Interno y Control Externo",
      "Sistema Bancario y Sistema Impositivo",
      "Sistema Judicial y Sistema Legislativo"],
     0, "SPO, SOA y SP son los tres sistemas de planificación y estructuración de la gestión."),

    ("Los sistemas para EJECUTAR las actividades programadas son (art. 2.b):",
     ["Administración de Personal (SAP), Bienes y Servicios (SABS), Tesorería y Crédito Público (STCP) y Contabilidad Integrada (SCI)",
      "Planificación Anual y Evaluación",
      "Auditoría Forense y Control Judicial",
      "Contrataciones Menores y Mayores únicamente",
      "Cobranza Coactiva Fiscal"],
     0, "SAP, SABS, STCP y SCI son los 4 sistemas operativos de ejecución."),

    ("El sistema para CONTROLAR la gestión del sector público es el (art. 2.c):",
     ["Sistema de Control Gubernamental (SCG)",
      "Sistema Policial de Vigilancia",
      "Sistema de Conciliación Vecinal",
      "Sistema de Control Electoral",
      "Sistema de Inteligencia Militar"],
     0, "El Sistema de Control Gubernamental evalúa la eficacia y licitud de las operaciones públicas."),

    ("El Sistema de Control Gubernamental está integrado por dos modalidades (art. 13):",
     ["Control Interno (previo y posterior) y Control Externo Posterior",
      "Control Policial y Control Judicial",
      "Control Sindical y Control Social",
      "Control Preventivo y Control Carcelario",
      "Control Estudiantil y Control Docente"],
     0, "El control interno se ejerce por la propia entidad y el externo posterior por la Contraloría General."),

    ("El Control Interno PREVIO en una entidad pública es ejercido por:",
     ["Las y los servidores públicos antes de la ejecución de sus actos y por los responsables que autorizan las operaciones",
      "La Contraloría General del Estado mediante auditorías",
      "El Juez de Partido en lo Civil",
      "El Comité Cívico Pro Santa Cruz",
      "Auditores externos contratados"],
     0, "El art. 14 señala que el control interno previo no compete a auditores, sino a las autoridades que ejecutan la operación."),

    ("La máxima entidad técnica rectora del Sistema de Control Gubernamental es (art. 41):",
     ["La Contraloría General del Estado",
      "El Ministerio de Economía",
      "El Banco Central de Bolivia",
      "La Procuraduría General",
      "La Defensoría del Pueblo"],
     0, "La Contraloría ejerce el control externo posterior y emite las normas básicas del SCG."),

    ("El Capítulo V de la Ley 1178 regula la Responsabilidad por la Función Pública. ¿Cuántos tipos de responsabilidad se establecen (art. 28)?",
     ["Cuatro (4): Administrativa, Ejecutiva, Civil y Penal",
      "Dos (2): Penal y Civil únicamente",
      "Tres (3): Laboral, Sindical y Política",
      "Una sola (1): Administrativa única",
      "Cinco (5): Incluyendo la moral y religiosa"],
     0, "El art. 28 clasifica las 4 formas de responsabilidad legal por el ejercicio de la función pública."),

    ("La Responsabilidad ADMINISTRATIVA (art. 29) emerge cuando:",
     ["La servidora o servidor público infringe el ordenamiento jurídico-administrativo y las normas que regulan su conducta",
      "Causa un daño económico invaluable al Estado",
      "Comete un delito de asesinato tipificado en el Código Penal",
      "No asiste a una fiesta patronal",
      "Critica una política de gobierno en redes sociales"],
     0, "Emerge de la contravención al ordenamiento jurídico-administrativo y normas internas."),

    ("Las sanciones previstas para la Responsabilidad Administrativa son (art. 29):",
     ["Multa de hasta un 20% de la remuneración mensual, suspensión hasta 30 días o destitución",
      "Pena de cárcel de 1 a 5 años",
      "Embargo y remate de su vivienda particular",
      "Pérdida de la ciudadanía boliviana",
      "Arresto militar de fin de semana"],
     0, "Se tramita mediante proceso sumario administrativo interno y puede derivar en amonestación, multa, suspensión o destitución."),

    ("La Responsabilidad Administrativa PRESCRIBE en el plazo de (art. 29):",
     ["Dos (2) años contados a partir de la comisión de la contravención",
      "Cinco (5) meses",
      "Diez (10) años",
      "Es imprescriptible",
      "Veinte (20) días"],
     0, "El art. 29 establece que prescribe a los dos años de cometida la acción u omisión."),

    ("La Responsabilidad EJECUTIVA (art. 30) se aplica a:",
     ["La Máxima Autoridad Ejecutiva (MAE) y los directivos por deficiente o negligente gestión de la entidad",
      "Los auxiliares de limpieza únicamente",
      "Cualquier ciudadano particular que use un servicio público",
      "Los estudiantes de secundaria",
      "Los proveedores comerciales"],
     0, "Se determina sobre la MAE y directivos por no rendir cuentas o gestión ineficaz."),

    ("La Responsabilidad CIVIL (art. 31) surge cuando:",
     ["La acción u omisión del servidor público causa un DAÑO ECONÓMICO al Estado valuable en dinero",
      "Se llega tarde 10 minutos a la oficina",
      "Se viste de manera informal en un acto",
      "Se expresa una opinión discrepante en reunión",
      "No se entrega una carta el mismo día"],
     0, "Exige daño patrimonial cuantificable económicamente al patrimonio del Estado."),

    ("La sanción o consecuencia de la Responsabilidad Civil es:",
     ["El RESARCIMIENTO del daño económico ocasionado mediante pago del monto adeudado",
      "La pena privativa de libertad sin pago de dinero",
      "La pérdida del título profesional universitario",
      "El exilio fuera del país",
      "La condonación automática de la deuda"],
     0, "Persigue la recuperación económica integral del patrimonio estatal a través del coactivo fiscal."),

    ("La acción legal para el cobro de la Responsabilidad Civil prescribe a los (art. 40):",
     ["Diez (10) años computables desde la última actuación procesal o hecho generador",
      "Dos (2) años",
      "Seis (6) meses",
      "Veinte (20) días hábiles",
      "Tres (3) meses"],
     0, "La prescripción de las deudas civiles no imprescriptibles se rige por el plazo de diez años."),

    ("La Responsabilidad PENAL (art. 34) se configura cuando:",
     ["La acción u omisión del servidor público o particular se encuentra TIPIFICADA como DELITO en el Código Penal",
      "Se produce un error de tipeo en un memorando",
      "Un estudiante no asiste a clases un día viernes",
      "Se solicita permiso por motivos de salud con justificativo",
      "Se gasta menos dinero del presupuestado"],
     0, "Requiere que la conducta esté expresamente descrita y sancionada como delito penal por ley."),

    ("Según el art. 33 de la Ley 1178, el principio de 'Licitud' implica que:",
     ["Los actos y operaciones de los servidores públicos deben ser legales, éticos y transparentes",
      "Todo está permitido mientras no sea descubierto",
      "Los directores pueden gastar fondos escolares sin rendir cuentas",
      "Las compras públicas no requieren facturas legales",
      "Los contratos verbales sustituyen a las licitaciones públicas"],
     0, "La licitud exige que toda actuación se ajuste estrictamente a las leyes y la moral pública."),

    ("En una Unidad Educativa, si el Director autoriza el desvío o apropiación de fondos provenientes de transferencias públicas o recursos propios:",
     ["Incurre en responsabilidad civil y penal por daño económico y delitos de corrupción",
      "Comete un simple error leve de procedimiento",
      "Queda protegido por la autonomía escolar",
      "Solo debe pedir disculpas verbalmente al alcalde",
      "Puede regularizarlo con un vale provisional informal indefinido"],
     0, "La malversación o uso indebido de recursos públicos activa responsabilidades civiles y penales directas."),

    ("El 'Dictamen de Responsabilidad' emitido por el Contralor General del Estado constituye (art. 43):",
     ["Un documento técnico-jurídico con valor de prueba preconstituida para iniciar la acción coactiva fiscal o penal",
      "Una sugerencia informal sin valor legal",
      "Una carta de felicitación administrativa",
      "Un recurso de apelación de segunda instancia",
      "Una sentencia carcelaria definitiva inmediata"],
     0, "El dictamen de la Contraloría es instrumento legal fundamental de cobro y proceso.")
]

def get_ley1178_questions():
    specs = expand_pool_to_200(BASE_SPECS, "ley1178", META["title"])
    questions = []
    for idx, spec in enumerate(specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"ley1178-{idx:03d}"
        q = make_q(qid, META, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

