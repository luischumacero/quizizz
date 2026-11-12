# coding: utf-8
"""
Compilador central del banco de preguntas.
Genera y valida 4,000 preguntas (200 preguntas x 20 temas oficiales).
Genera archivos JSON individuales, el archivo maestro y el bundle JavaScript para el cliente web.
"""
import os
import json
import sys

from topics_metadata import TOPICS, TOPICS_DICT
from gen_cpe import get_cpe_questions
from gen_ley070 import get_ley070_questions
from gen_ley045 import get_ley045_questions
from gen_ley348 import get_ley348_questions
from gen_ley548 import get_ley548_questions
from gen_ley223 import get_ley223_questions
from gen_ley1178 import get_ley1178_questions
from gen_ley004 import get_ley004_questions
from gen_especificas import get_normativa_especifica_questions
from gen_pedagogicas import get_tecnico_pedagogico_questions

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
QUESTIONS_DIR = os.path.join(BASE_DIR, "questions")
SITE_DIR = os.path.join(BASE_DIR, "site")

os.makedirs(QUESTIONS_DIR, exist_ok=True)
os.makedirs(SITE_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("CONSTRUCCIÓN DEL BANCO DE 4,000 PREGUNTAS (20 TEMAS x 200)")
    print("DIRECTOR DE UNIDAD EDUCATIVA - ESTADO PLURINACIONAL DE BOLIVIA")
    print("=" * 60)

    bank = {}

    # 1. Normativa General (8 temas)
    print("\n[1/3] Generando preguntas de Normativa General (Temas 4.1 a 4.8)...")
    bank["cpe"] = get_cpe_questions()
    print(f" -> 4.1 CPE: {len(bank['cpe'])} preguntas")

    bank["ley070"] = get_ley070_questions()
    print(f" -> 4.2 Ley 070: {len(bank['ley070'])} preguntas")

    bank["ley045"] = get_ley045_questions()
    print(f" -> 4.3 Ley 045: {len(bank['ley045'])} preguntas")

    bank["ley348"] = get_ley348_questions()
    print(f" -> 4.4 Ley 348: {len(bank['ley348'])} preguntas")

    bank["ley548"] = get_ley548_questions()
    print(f" -> 4.5 Ley 548: {len(bank['ley548'])} preguntas")

    bank["ley223"] = get_ley223_questions()
    print(f" -> 4.6 Ley 223: {len(bank['ley223'])} preguntas")

    bank["ley1178"] = get_ley1178_questions()
    print(f" -> 4.7 Ley 1178: {len(bank['ley1178'])} preguntas")

    bank["ley004"] = get_ley004_questions()
    print(f" -> 4.8 Ley 004: {len(bank['ley004'])} preguntas")

    # 2. Normativa Específica (8 temas)
    print("\n[2/3] Generando preguntas de Normativa Específica (Temas 5.1 a 5.8)...")
    esp_questions = get_normativa_especifica_questions()
    for tid, q_list in esp_questions.items():
        bank[tid] = q_list
        print(f" -> {TOPICS_DICT[tid]['code']} {TOPICS_DICT[tid]['id']}: {len(q_list)} preguntas")

    # 3. Técnico Pedagógico (4 temas)
    print("\n[3/3] Generando preguntas de Técnico Pedagógico (Temas 6.1 a 6.4)...")
    ped_questions = get_tecnico_pedagogico_questions()
    for tid, q_list in ped_questions.items():
        bank[tid] = q_list
        print(f" -> {TOPICS_DICT[tid]['code']} {TOPICS_DICT[tid]['id']}: {len(q_list)} preguntas")

    # Validaciones rigurosas
    total_q = 0
    all_questions_list = []
    
    for topic_meta in TOPICS:
        tid = topic_meta["id"]
        assert tid in bank, f"Falta el tema {tid} en el banco"
        q_list = bank[tid]
        count = len(q_list)
        total_q += count
        assert count >= 200, f"El tema {tid} tiene solo {count} preguntas (se requieren 200)"
        
        # Validar opciones A a E y respuesta válida en cada pregunta
        for q in q_list:
            opts = q["options"]
            assert set(opts.keys()) == {"a", "b", "c", "d", "e"}, f"Opciones inválidas en {q['id']}"
            assert q["answer"] in {"a", "b", "c", "d", "e"}, f"Respuesta inválida en {q['id']}"
            all_questions_list.append(q)

        # Guardar archivo JSON individual por tema
        topic_file = os.path.join(QUESTIONS_DIR, f"{tid}.json")
        with open(topic_file, "w", encoding="utf-8") as f:
            json.dump({
                "topic": topic_meta["title"],
                "topic_id": tid,
                "topic_code": topic_meta["code"],
                "category": topic_meta["category"],
                "total_questions": count,
                "questions": q_list
            }, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"VALIDACIÓN EXITOSA: {total_q} PREGUNTAS EN TOTAL GENERADAS.")
    print("=" * 60)

    # Guardar archivo maestro all_questions.json en questions/ y site/
    master_data = {
        "title": "Banco de Preguntas para Director de Unidad Educativa (Bolivia)",
        "total_topics": len(TOPICS),
        "total_questions": total_q,
        "topics": TOPICS,
        "questions": all_questions_list
    }

    all_q_path = os.path.join(QUESTIONS_DIR, "all_questions.json")
    with open(all_q_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado archivo maestro: {all_q_path}")

    site_json_path = os.path.join(SITE_DIR, "questions.json")
    with open(site_json_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado archivo web JSON: {site_json_path}")

    # Generar bundle JS para ejecución estática directa (sin CORS ni servidor web obligatorio)
    site_js_path = os.path.join(SITE_DIR, "questions_data.js")
    with open(site_js_path, "w", encoding="utf-8") as f:
        f.write("// Banco de preguntas empaquetado para ejecución estática local\n")
        f.write("window.QUIZ_DATA = ")
        json.dump(master_data, f, ensure_ascii=False)
        f.write(";\n")
    print(f"Guardado bundle JS para ejecución estática: {site_js_path}")
    print("\nPROCESO COMPLETADO EXITOSAMENTE.")

if __name__ == "__main__":
    main()
