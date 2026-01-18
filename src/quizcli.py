import os
import json
from config import get_llm


def clear_screen():
    if os.environ.get('TERM'):
        clear_screen()
    else:
        print("\n" * 50)


class QuizQuestion:
    def __init__(self, question: str, options: list[str], correct_index: int):
        self.question = question
        self.options = options
        self.correct_index = correct_index


def build_prompt(topic: str, level: str, question_count: int) -> str:
    return (
        f'Przygotuj mi quiz na temat "{topic}".\n'
        f"Poziom trudności: {level}\n"
        f"Liczba pytań: {question_count}\n\n"
        "Wymagania:\n"
        "- 4 odpowiedzi (A, B, C, D)\n"
        "- dokładnie jedna odpowiedź jest poprawna\n"
        "- zwróć wyłącznie czysty JSON, bez komentarzy\n\n"
        "Format JSON:\n"
        '[\n'
        '  {"question": "...", "options": ["A) ...", "B) ...", "C) ...", "D) ..."], "correct_index": 0}\n'
        ']\n'
    )


def parse_response(response: str) -> list[QuizQuestion]:
    text = response.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:-1])

    json_data = json.loads(text)
    questions = []
    for item in json_data:
        q = QuizQuestion(
            question=item["question"],
            options=item["options"],
            correct_index=item["correct_index"]
        )
        questions.append(q)
    return questions


def ask_question(question: QuizQuestion, question_num: int, total: int) -> str:
    print(f"Pytanie {question_num}/{total}:")
    print(question.question)
    for option in question.options:
        print(f"  {option}")

    while True:
        answer = input("Twój wybór (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("Nieprawidłowy wybór. Wpisz A, B, C lub D.")


def main():
    clear_screen()
    llm = get_llm()

    print("=== QuizCLI ===\n")
    topic = input("Podaj temat quizu: ")
    level = input("Wybierz poziom trudności (easy/medium/hard): ")
    question_count = int(input("Ile pytań wygenerować? "))

    print("\nGeneruję pytania...\n")
    prompt = build_prompt(topic, level, question_count)
    response = llm.generate(prompt)
    questions = parse_response(response)

    clear_screen()
    score = 0
    total = len(questions)

    for i, question in enumerate(questions, start=1):
        user_answer = ask_question(question, i, total)
        correct_letter = ["A", "B", "C", "D"][question.correct_index]

        if user_answer == correct_letter:
            print("Poprawnie!\n")
            score += 1
        else:
            print(f"Błędnie! Poprawna odpowiedź: {correct_letter}\n")

        input("Naciśnij Enter, aby kontynuować...")
        clear_screen()

    percent = (score / total) * 100
    print(f"Twój wynik: {score}/{total} ({percent:.0f}%)")


if __name__ == "__main__":
    main()
