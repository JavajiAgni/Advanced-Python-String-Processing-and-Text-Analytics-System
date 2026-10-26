# Advanced Text Intelligence and String Analytics System

**Level:** M.Tech CSE  
**Language:** Python 3.10+  
**Dependencies:** Python standard library only

## Features
- Character, word, sentence, punctuation, digit, vowel and consonant statistics
- Word and character frequencies
- Palindrome, anagram, duplicate-character and first-unique-character analysis
- Longest-word detection and run-length encoding
- Naive string search, KMP string search, built-in search comparison
- Regex extraction of emails, URLs and numbers; custom regex matching
- Text normalization and JSON report export
- Automated unit tests

## Project structure
```text
advanced_text_intelligence_project/
├── main.py
├── analyzer.py
├── algorithms.py
├── regex_tools.py
├── sample_text.txt
├── README.md
├── PROJECT_REPORT.md
└── tests/
    └── test_analyzer.py
```

## Run
Check Python:
```bash
python --version
```
Start with sample text:
```bash
python main.py --file sample_text.txt
```
Enter text manually:
```bash
python main.py
```
Paste text and type `END` on its own line to finish input.

Save report to JSON:
```bash
python main.py --file sample_text.txt --json report.json
```
The program also provides a menu option to export a JSON report.

## Run tests
From the project root:
```bash
python -m unittest discover -s tests -v
```

## Design
- `analyzer.py`: statistics and general string operations
- `algorithms.py`: search algorithms and timing
- `regex_tools.py`: regex-based extraction and matching
- `main.py`: command-line interface and report export
- `tests/`: regression tests

## Important limitations
- Email and URL regular expressions are practical extractors, not complete standards validators.
- The simple sentence count is heuristic and may not handle every abbreviation or language.
- Run-length encoding is intended for demonstrations; the format is ambiguous if the original text contains digits. Avoid using it as a lossless general-purpose compression format without an escaping scheme.
- Timing results depend on hardware, text size, Python version and system load. Repeat measurements and use large inputs for meaningful comparisons.
