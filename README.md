# QuizCLI — Generator quizów z wykorzystaniem LLM

## Skład zespołu
* Kinga Chachulska
* Mateusz Rosloniec
* Piotr Uznański

## Opis funkcjonalny
**QuizCLI** to aplikacja terminalowa generująca interaktywne quizy za pomocą modelu językowego (LLM).
Program pobiera od użytkownika:
* temat quizu, 
* poziom trudności (`easy`/`medium`/`hard`),
* liczbę pytań.

Następnie tworzy prompt dla LLM, odbiera wygenerowaną listę pytań w formacie JSON i prezentuje je użytkownikowi w 
formie testu wielokrotnego wyboru.

### Aplikacja:
* waliduje odpowiedzi,
* liczy wynik i procent poprawnych odpowiedzi,
* obsługuje błędy parsowania JSON,
* (opcjonalnie) zapisuje historię wyników do pliku `data/quiz_history.json`.

## Instrukcja uruchomienia
1. Zainstaluj zależności z pliku `requirements.txt`
2. Ustaw zmienną środowiskową z kluczem API

### Tryb CLI
   3. Uruchom aplikację komendą
       ```aiignore
       python quizcli.py
       ```
   4. Postępuj zgodnie z instrukcjami wyświetlanymi w terminalu

### Tryb GUI
   TBD

## Ograniczenia rozwiązania
* Poprawność działania zależy od jakości odpowiedzi LLM.
* Model może generować błędny lub nieparsowalny JSON.
* Wymaga aktywnego połączenia z API OpenAI.
* Nie ma zaawansowanej walidacji logiki pytań (np. sensowność odpowiedzi).