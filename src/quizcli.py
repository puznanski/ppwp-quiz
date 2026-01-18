
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
def main():
    
    topic = input("Podaj temat quizu (np. 'Podstawy Pythona'): ").strip()
    level = input("Podaj poziom trudności (easy/medium/hard): ").strip().lower()
    question_count = input("Podaj liczbę pytań: ").strip()

    if not topic:
        print("Błąd: temat nie może być pusty!")
        return

    if level not in {"easy", "medium", "hard"}:
        print("Błąd: poziom trudności musi być 'easy', 'medium' lub 'hard'!")
        return

    if not question_count.isdigit() or int(question_count) <= 0:
        print("Błąd: liczba pytań musi być dodatnią liczbą całkowitą!")
        return

    question_count = int(question_count)

    print("\nDane wprowadzone przez użytkownika:")
    print(f"Temat: {topic}")
    print(f"Poziom trudności: {level}")
    print(f"Liczba pytań: {question_count}")


if __name__ == "__main__":
    main()
