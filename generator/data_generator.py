# coding: utf-8
import json
import os
import random

from topics_metadata import TOPICS, TOPICS_DICT
from question_builder import make_q

def generate_topic_questions(topic_meta, question_specs):
    """
    question_specs es una lista de especificaciones de preguntas:
    (pregunta, [opcion_a, opcion_b, opcion_c, opcion_d, opcion_e], respuesta_index, explicacion)
    """
    questions = []
    tid = topic_meta["id"]
    for idx, spec in enumerate(question_specs, 1):
        q_text, opts, ans_idx, exp = spec
        qid = f"{tid}-{idx:03d}"
        q = make_q(qid, topic_meta, q_text, opts, ans_idx, exp)
        questions.append(q)
    return questions

