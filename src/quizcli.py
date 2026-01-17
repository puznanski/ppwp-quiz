def build_prompt(topic: str, difficulty: str, n_questions: int) -> str:
    return (
        f'Przygotuj mi quiz na temat "{topic}".\n'
        f"Poziom trudności: {difficulty}\n"
        f"Liczba pytań: {n_questions}\n\n"
        "Wymagania:\n"
        "- 4 odpowiedzi (A, B, C, D)\n"
        "- dokładnie jedna odpowiedź jest poprawna\n"
        "- zwróć wyłącznie czysty JSON, bez komentarzy\n\n"
        "Format JSON:\n"
        "[\n"
        "  {\n"
        '    "question": "",\n'
        '    "answers": [\n'
        '      {"key": "A", "text": ""},\n'
        '      {"key": "B", "text": ""},\n'
        '      {"key": "C", "text": ""},\n'
        '      {"key": "D", "text": ""}\n'
        "    ],\n"
        '    "correct_answer": "A"\n'
        "  }\n"
        "]\n"
    )