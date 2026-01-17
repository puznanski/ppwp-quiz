def build_prompt(topic: str, difficulty: str, n_questions: int) -> str:
    return (
        f'Przygotuj mi quiz na temat "{topic}".\n'
        f"Poziom trudności: {difficulty}\n"
        f"Liczba pytań: {n_questions}\n"
    )