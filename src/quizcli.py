import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, model_validator
from typing_extensions import Self
from json import JSONDecoder

class GeminiConfig(BaseModel):
    model: str
    temperature: float
    top_p: float
    top_k: int
    api_key: str

class QuizQuestion(BaseModel):
    id: int
    question: str
    options: list[str]
    answer: str
    explanation: str

class InputConfig(BaseModel):
    level: str
    topic: str
    question_count: int


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
class QuizQuestion:
    def __init__(self, config: GeminiConfig):
        self.config = config
        self.prompt = ""

    def __str__(self):
        return f"Q{self.id}: {self.question} | Options: {self.options} | Answer: {self.answer}"

    def ask_user_for_answer(self, question):
        print(f"Q{question.id}: {question.question}")
        for idx, option in enumerate(question.options, start=1):
            print(f"  {idx}. {option}")
        return input("Your answer (enter the option number): ")
    
def main():
    load_dotenv()
    os.system('clear')
    gemini_config = GeminiConfig(
        model=os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'),
        temperature=float(os.getenv('GEMINI_TEMPERATURE', 0.7)),
        top_p=float(os.getenv('GEMINI_TOP_P', 0.9)),
        top_k=int(os.getenv('GEMINI_TOP_K', 40)),
        api_key=os.getenv('GEMINI_API_KEY'),
    )

    quiz_cli = QuizCLI(config=gemini_config)
    input_config = InputConfig(
        level=input("Enter difficulty level (easy, medium, hard): "),
        topic=input("Enter quiz topic: "),
        question_count=input("Enter number of questions: "),
    )
    os.system('clear')
    prompt = quiz_cli.create_prompt(input_config)
    response = quiz_cli.generate_response(prompt)
    json_response = quiz_cli.parse_response_as_json(response)
    quiz_questions = quiz_cli.extract_quiz_questions(json_response)

    score = 0
    for question in quiz_questions:
        user_answer = quiz_cli.ask_user_for_answer(question)
        correct_option_index = question.options.index(question.answer) + 1
        if str(correct_option_index) == user_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question.answer}\n")
            print(f"Explanation: {question.explanation}\n")
        os.system('clear')
    print(f"Liczba poprawnych odpowiedzi: {score}/{len(quiz_questions)}")

if __name__ == "__main__":
    main()