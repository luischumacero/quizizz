# coding: utf-8
"""
Utilidades para validar y estructurar bancos de preguntas de opción múltiple (a-e).
"""

def make_q(qid, topic_meta, question, options_list, correct_idx, explanation=""):
    """
    Crea un objeto de pregunta estructurado.
    options_list: lista de 5 opciones (strings)
    correct_idx: índice 0..4 (0=a, 1=b, 2=c, 3=d, 4=e)
    """
    letters = ["a", "b", "c", "d", "e"]
    assert len(options_list) == 5, f"Debe tener exactamente 5 opciones para {qid}"
    assert 0 <= correct_idx < 5, f"Índice correcto inválido {correct_idx} para {qid}"

    opts = {letters[i]: options_list[i].strip() for i in range(5)}
    
    return {
        "id": qid,
        "topic_id": topic_meta["id"],
        "topic_code": topic_meta["code"],
        "category": topic_meta["category"],
        "topic": topic_meta["title"],
        "short_title": topic_meta["short_title"],
        "question": question.strip(),
        "options": opts,
        "answer": letters[correct_idx],
        "explanation": explanation.strip() if explanation else f"Respuesta correcta: inciso {letters[correct_idx]}."
    }

