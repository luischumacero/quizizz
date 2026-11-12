# coding: utf-8
"""
Compilador maestro del banco de preguntas:
- Lee los 20 archivos JSON individuales de questions/ (200 preguntas c/u = 4000 total)
- Valida que no haya filler, que las opciones sean a-e, que la respuesta sea válida
- Genera questions/all_questions.json
- Genera site/questions.json
- Genera site/questions_data.js (bundle JS para ejecución estática sin CORS)
- Copia los archivos actualizados a la raíz del repositorio para GitHub Pages
"""
import os
import json
import shutil
from topics_metadata import TOPICS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
QUESTIONS_DIR = os.path.join(BASE_DIR, "questions")
SITE_DIR = os.path.join(BASE_DIR, "site")

def compile_bank():
    print("=" * 60)
    print("COMPILANDO BANCO MAESTRO DE 4,000 PREGUNTAS ÚNICAS")
    print("=" * 60)

    all_questions_list = []
    total_q = 0

    for topic_meta in TOPICS:
        tid = topic_meta["id"]
        tfile = os.path.join(QUESTIONS_DIR, f"{tid}.json")
        assert os.path.exists(tfile), f"Falta el archivo {tfile}"

        with open(tfile, encoding="utf-8") as f:
            data = json.load(f)

        qs = data["questions"]
        count = len(qs)
        assert count == 200, f"El tema {tid} tiene {count} preguntas (se requieren 200)"
        total_q += count

        for q in qs:
            # Validaciones estrictas
            assert set(q["options"].keys()) == {"a", "b", "c", "d", "e"}, f"Opciones invalidas en {q['id']}"
            assert q["answer"] in {"a", "b", "c", "d", "e"}, f"Respuesta invalida en {q['id']}"
            assert "profundización" not in q["question"].lower(), f"Filler detectado en {q['id']}"
            assert "profundizaci" not in q["question"].lower(), f"Filler detectado en {q['id']}"
            all_questions_list.append(q)

        print(f" -> {topic_meta['code']} {topic_meta['id']}: 200 preguntas verificadas (0 filler)")

    print("-" * 60)
    print(f"TOTAL PREGUNTAS VERIFICADAS Y VALIDADAS: {total_q}")
    print("-" * 60)

    master_data = {
        "title": "Banco de Preguntas para Director de Unidad Educativa (Bolivia)",
        "total_topics": len(TOPICS),
        "total_questions": total_q,
        "topics": TOPICS,
        "questions": all_questions_list
    }

    # 1. Guardar questions/all_questions.json
    all_q_path = os.path.join(QUESTIONS_DIR, "all_questions.json")
    with open(all_q_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado: {all_q_path}")

    # 2. Guardar site/questions.json
    site_json_path = os.path.join(SITE_DIR, "questions.json")
    with open(site_json_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"Guardado: {site_json_path}")

    # 3. Guardar site/questions_data.js
    site_js_path = os.path.join(SITE_DIR, "questions_data.js")
    with open(site_js_path, "w", encoding="utf-8") as f:
        f.write("// Banco de preguntas empaquetado para ejecucion estatica local\n")
        f.write("window.QUIZ_DATA = ")
        json.dump(master_data, f, ensure_ascii=False)
        f.write(";\n")
    print(f"Guardado: {site_js_path}")

    # 4. Copiar a la raíz del repositorio para GitHub Pages
    root_files = ["index.html", "style.css", "app.js", "questions.json", "questions_data.js"]
    for fname in root_files:
        src = os.path.join(SITE_DIR, fname)
        dst = os.path.join(BASE_DIR, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copiado a raíz: {fname}")

    print("\nCOMPILACIÓN Y DESPLIEGUE LOCAL FINALIZADOS CON ÉXITO.")

if __name__ == "__main__":
    compile_bank()
