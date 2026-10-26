# M.Tech CSE Project Report
## Advanced Text Intelligence and String Analytics System Using Python

### Abstract
Text is a common data format in software systems, digital libraries, search engines and information retrieval applications. This project implements a modular text-analysis system using Python. It measures text statistics, identifies character and word patterns, performs palindrome and anagram checks, extracts structured patterns with regular expressions, and compares naive string search with the Knuth-Morris-Pratt (KMP) algorithm. The implementation uses Python's standard library and includes automated unit tests and JSON report export. The project demonstrates how basic string methods, loops, conditional statements, collections and algorithm design can be integrated into a maintainable software application.

### 1. Introduction
String processing is a foundational task in computer science. It supports document analysis, search, validation, data cleaning and information extraction. The project brings these tasks into one menu-driven application and emphasizes correctness, modularity and algorithmic efficiency.

### 2. Problem statement
Manual inspection of text is slow and inconsistent. A compact application is needed to summarize text, find patterns, extract common entities, and illustrate how alternative string-search algorithms behave.

### 3. Objectives
1. Apply Python string indexing, slicing and built-in methods.
2. Compute character-, word- and sentence-level statistics.
3. Implement palindrome, anagram and character-frequency analysis.
4. Use regular expressions to extract emails, URLs and numbers.
5. Implement naive and KMP substring-search algorithms.
6. compare search results and execution times.
7. Export analysis results as JSON and validate functionality with unit tests.

### 4. Scope
The application processes UTF-8 text supplied through a file or interactive input. It is intended for educational analysis and small-to-medium text samples. It is not a full natural-language-processing engine and does not claim perfect sentence segmentation or standards-compliant email validation.

### 5. Requirements
**Hardware:** Any modern computer capable of running Python.  
**Software:** Python 3.10 or later; Windows, Linux or macOS; a terminal or IDE.  
**External packages:** None.

### 6. System modules
- **Input module:** reads UTF-8 files or multiline terminal input.
- **Statistics module:** counts characters, letters, digits, spaces, punctuation, vowels, consonants, words and sentences.
- **Frequency module:** reports frequent words and characters.
- **String operations module:** checks palindromes and anagrams, detects duplicates, identifies unique characters and compresses repeated runs.
- **Pattern search module:** compares naive search, KMP and Python's `find`.
- **Regex module:** extracts emails, URLs and numbers, and runs custom regular expressions.
- **Reporting module:** displays results and exports JSON.
- **Testing module:** checks core behaviors using `unittest`.

### 7. Methodology
1. Read source text.
2. Compute basic text statistics and frequencies.
3. Normalize case where comparison semantics require it.
4. Apply dedicated functions to palindrome, anagram and repetition tasks.
5. Search for a user-specified pattern with three methods.
6. Extract selected patterns using regular expressions.
7. Display or serialize results.
8. Run tests to detect regressions.

### 8. Algorithms and complexity
Let `n` be the text length and `m` the pattern length.

| Operation | Expected / worst-case complexity | Notes |
|---|---|---|
| Character frequency | O(n) expected | Hash-based counter |
| Word frequency | O(n) expected | Depends on tokenization and hashing |
| Palindrome check | O(n) | Builds a normalized candidate |
| Anagram check | O(n + m) expected | Frequency counters |
| Naive pattern search | O(nm) worst case | Straightforward comparison |
| KMP preprocessing | O(m) | Builds LPS table |
| KMP search | O(n + m) | Avoids repeated backtracking |
| Regex extraction | Pattern-dependent | Regex behavior depends on expression |

Python's built-in string search is implemented in optimized native code, so its observed speed may beat a pure-Python KMP implementation even when KMP has a favorable asymptotic bound. Timing should be interpreted alongside algorithmic complexity.

### 9. Testing strategy
Run `python -m unittest discover -s tests -v`. Tests cover statistics, palindrome checks, anagrams, duplicate characters, compression, normalization, search correctness and regex extraction. Add edge-case tests for empty text, repeated matches, punctuation, Unicode, invalid regular expressions and very large input.

### 10. Expected results
The application produces:
- A statistical profile of the input text
- Top words and character frequencies
- Results for palindrome, anagram and repetition checks
- Match positions and timing for each search implementation
- Extracted emails, URLs and numeric values
- A JSON file containing the main analysis report

### 11. Advantages
- Modular and easy to extend
- Uses only Python standard-library features
- Demonstrates both practical string processing and algorithm design
- Reproducible tests and machine-readable output
- Useful as a foundation for document analysis and search experiments

### 12. Limitations
- Sentence segmentation is heuristic.
- Regex extraction is not equivalent to complete standards validation.
- Run-length encoding is a teaching demonstration and is ambiguous for arbitrary digit-containing text.
- Benchmark results vary by environment.
- The application does not provide semantic understanding or multilingual linguistic analysis.

### 13. Future enhancements
- Add a graphical interface or web dashboard.
- Support CSV, PDF and DOCX text ingestion.
- Add stop-word filtering, n-gram analysis and TF-IDF.
- Add Boyer-Moore and Rabin-Karp search implementations.
- Generate charts and downloadable PDF reports.
- Add language-aware tokenization and Unicode normalization options.
- Evaluate search algorithms on generated corpora with repeated benchmark runs and statistical summaries.

### 14. Conclusion
The project integrates core Python string topics into a practical text intelligence application. It demonstrates string methods, loops, conditionals, regular expressions, frequency counting, testing and algorithmic complexity. The KMP comparison provides a bridge between introductory string programming and advanced algorithm analysis, making the project suitable as an M.Tech CSE educational prototype.

### 15. References
1. Python Software Foundation, *Python 3 Documentation*, https://docs.python.org/3/
2. Python Software Foundation, *Regular expression operations (`re`)*, https://docs.python.org/3/library/re.html
3. Knuth, D. E., Morris, J. H., and Pratt, V. R. (1977). “Fast Pattern Matching in Strings.” *SIAM Journal on Computing*, 6(2), 323–350.
4. Cormen, T. H. et al., *Introduction to Algorithms*, section on string matching.
