# coding: utf-8
"""
Utilidades para validar bancos de preguntas.
Ya no se usa el padding con filler: cada generador DEBE proveer 200+ preguntas únicas.
"""

def validate_pool(specs, topic_id, min_required=200):
    """
    Valida que la lista de especificaciones tenga al menos min_required preguntas.
    Si no las tiene, imprime un error y lanza excepción.
    """
    count = len(specs)
    if count < min_required:
        raise ValueError(
            f"ERROR: El tema '{topic_id}' tiene solo {count} preguntas únicas. "
            f"Se requieren al menos {min_required}. "
            f"Faltan {min_required - count} preguntas por generar."
        )
    return specs[:min_required]


# Mantener compatibilidad temporal durante la migración
def expand_pool_to_200(base_specs, topic_id, topic_title):
    """DEPRECADO: Solo devuelve las specs que haya. No añade filler."""
    return list(base_specs)[:200]
