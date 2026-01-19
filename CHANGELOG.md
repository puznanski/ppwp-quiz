## v0.1.0 - 2026-01-19

### Changes since v0.0.3:
- QZ-12 Wydzielenie funkcji LLM do osobnych plików (#17)
- QZ-19 Wyświetlanie wyniku po skończeniu gry
- QZ-12 QZ-17 Wysyłanie requestu do Gemini i sprawdzanie poprawnej odpowiedzi
- Merge branch 'main' into QZ-18
- QZ-14 Przyjmowanie argumentów od użytkownika (#14)
- QZ-18 Liczenie poprawnych odpowiedzi
- QZ-15 Klasa na pytania i odpowiedzi
- QZ-17,5 Sprawdzanie poprawnej odpowiedzi
- QZ-17,5 Sprawdzanie poprawnej odpowiedzi
- QZ-11 Ustalić format zwracanego JSONa z pytaniami (#12)

### File changes summary:

Added:
- `.env.example`
- `src/config.py`
- `src/llm_gemini.py`
- `src/llm_openai.py`

Modified:
- `src/quizcli.py`


## v0.0.3 - 2026-01-18

### Changes since v0.0.2:
- Updated workflow with new action version (#13)
- QZ-10 Wymyślić prompt z zapytaniem do OpenAI (#11)
- QZ-9 Funkcja przygotowująca prompt (#10)

### File changes summary:

Modified:
- `.github/workflows/release.yml`
- `src/quizcli.py`


## v0.0.2 - 2025-11-29

### Changes since v0.0.1:
- QZ-4 Basic project structure and description (#1)

### File changes summary:

Added:
- `src/quizcli.py`

Modified:
- `.github/workflows/release.yml`
- `.gitignore`
- `CHANGELOG.md`
- `README.md`


## v0.0.1 - 2025-11-29

### Initial release:
- QZ-5 Fixed versioning workflow (#8)
- QZ-5 Fixed versioning workflow (#7)
- QZ-5 Updated versioning workflow token acquiring (#6)
- QZ-5 Updated versioning workflow (#5)
- QZ-5 Updated versioning workflow permissions (#4)
- QZ-5 Created github versioning workflow (#3)
- Initial commit

### File changes summary:

Added:
- `.github/workflows/release-label-check.yml`
- `.github/workflows/release.yml`
- `.gitignore`
- `LICENSE`
- `README.md`


