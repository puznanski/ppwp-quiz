import os
import json
from datetime import datetime
from config import get_llm

HISTORY_FILE = os.path.join(os.path.dirname(_file_), "..", "data", "quiz_history.jsonl")


def clear_screen():
    if os.environ.get('TERM'):
        os.system('clear')
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


def save_history(topic: str, difficulty: str, score: int, total: int):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    record = {
        "ts": datetime.now().isoformat(),
        "topic": topic,
        "difficulty": difficulty,
        "score": score,
        "total": total
    }
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def view_history():
    clear_screen()
    print("=== Historia quizów ===\n")

    if not os.path.exists(HISTORY_FILE):
        print("Brak historii.\n")
        input("Naciśnij Enter, aby wrócić...")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Brak historii.\n")
        input("Naciśnij Enter, aby wrócić...")
        return

    for line in lines:
        record = json.loads(line.strip())
        ts = record["ts"][:16].replace("T", " ")
        topic = record["topic"]
        difficulty = record["difficulty"]
        score = record["score"]
        total = record["total"]
        percent = (score / total) * 100
        print(f"[{ts}] {topic} ({difficulty}) - {score}/{total} ({percent:.0f}%)")

    print()
    input("Naciśnij Enter, aby wrócić...")


def get_topic() -> str:
    while True:
        topic = input("Podaj temat quizu: ").strip()
        if topic:
            return topic
        print("Temat nie może być pusty.")


def get_difficulty() -> str:
    valid_levels = ["łatwy", "średni", "trudny"]
    while True:
        level = input("Wybierz poziom trudności (łatwy/średni/trudny): ").strip().lower()
        if level in valid_levels:
            return level
        print("Nieprawidłowy poziom. Wpisz: łatwy, średni lub trudny.")


def get_question_count() -> int:
    while True:
        try:
            count = int(input("Ile pytań wygenerować (1-20)? "))
            if 1 <= count <= 20:
                return count
            print("Liczba pytań musi być od 1 do 20.")
        except ValueError:
            print("Podaj liczbę całkowitą.")


def play_game():
    clear_screen()
    llm = get_llm()

    print("=== Nowy Quiz ===\n")
    topic = get_topic()
    level = get_difficulty()
    question_count = get_question_count()

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
    print(f"Twój wynik: {score}/{total} ({percent:.0f}%)\n")

    save_history(topic, level, score, total)
    input("Naciśnij Enter, aby wrócić do menu...")


def show_menu():
    print("=== QuizCLI ===\n")
    print("1. Zagraj w quiz")
    print("2. Zobacz historię")
    print("3. Wyjdź")
    print()

    while True:
        choice = input("Wybierz opcję (1/2/3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        print("Nieprawidłowy wybór. Wpisz 1, 2 lub 3.")


def main():
    while True:
        clear_screen()
        choice = show_menu()

        if choice == "1":
            play_game()
        elif choice == "2":
            view_history()
        elif choice == "3":
            clear_screen()
            print("Do zobaczenia!\n")
            break


if _name_ == "_main_":
    main()