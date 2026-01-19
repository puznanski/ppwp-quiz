# QuizCLI — Generator quizów z wykorzystaniem LLM

## Skład zespołu
* Kinga Chachulska
* Mateusz Rosloniec
* Piotr Uznański

## Opis funkcjonalny
**QuizCLI** to aplikacja terminalowa generująca interaktywne quizy za pomocą modelu językowego (LLM).
Program pobiera od użytkownika:
* temat quizu, 
* poziom trudności (`łatwy`/`średni`/`trudny`),
* liczbę pytań.

Następnie tworzy prompt dla LLM, odbiera wygenerowaną listę pytań w formacie JSON i prezentuje je użytkownikowi w 
formie testu wielokrotnego wyboru.

W pliku konfiguracyjnym programu możemy wybrać providera LLM (OpenAI lub Google).

### Aplikacja:
* waliduje odpowiedzi,
* liczy wynik i procent poprawnych odpowiedzi,
* obsługuje błędy parsowania JSON,
* zapisuje historię wyników do pliku `data/quiz_history.json`,
* wyświetla historię gier wewnątrz aplikacji.

## Instrukcja uruchomienia
1. Zainstaluj zależności:
    ```bash
    pip install -r requirements.txt
    ```
2. Utwórz plik konfiguracyjny `.env` na podstawie pliku `.env.example`. Wybierz providera LLM i podaj klucz API.
3. Uruchom aplikację komendą
    ```bash
    python quizcli.py
    ```
   lub
    ```bash
    python3 quizcli.py
    ```
4. Postępuj zgodnie z instrukcjami wyświetlanymi w terminalu

## Ograniczenia rozwiązania
* Poprawność działania zależy od jakości odpowiedzi LLM.
* Model może generować błędny lub nieparsowalny JSON.
* Wymaga aktywnego połączenia z API OpenAI.
* Nie ma zaawansowanej walidacji logiki pytań (np. sensowność odpowiedzi).

## Wkład w projekt
* Kinga Chachulska — przyjmowanie argumentów od użytkownika, połączenie z Gemini, pętla gry, liczenie wyniku, wyświetlanie wyniku
* Mateusz Rosloniec — model i przygotowanie promptu dla LLM, ustalenie formatu JSON zwracanych pytań, walidacja argumentów, 'requirements.txt'
* Piotr Uznański — założenie projektu na Githubie i Jirze, struktura projektu, połączenie z OpenAI, plik konfiguracyjny, zapisywanie i wyświetlanie historii gier