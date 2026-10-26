"""Menu-driven command-line interface for Advanced Text Intelligence."""
import argparse
import json
from pathlib import Path

from analyzer import (
    analyze_text, is_palindrome, are_anagrams, duplicate_characters,
    first_non_repeating_character, compress_runs, normalize_text, get_words
)
from algorithms import benchmark_search
from regex_tools import extract_emails, extract_urls, extract_numbers, find_pattern

def read_text(path: str | None) -> str:
    if path:
        try:
            return Path(path).read_text(encoding="utf-8")
        except OSError as exc:
            raise SystemExit(f"Could not read file: {exc}")
    print("Enter/paste text. Finish with a line containing only END:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def show_report(text: str) -> None:
    report = analyze_text(text)
    print("\n--- TEXT ANALYSIS REPORT ---")
    for key, value in report.items():
        print(f"{key.replace('_', ' ').title():28}: {value}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Advanced Text Intelligence and String Analytics System")
    parser.add_argument("--file", help="UTF-8 text file to analyze")
    parser.add_argument("--json", dest="json_path", help="Save the analysis report as JSON")
    args = parser.parse_args()
    text = read_text(args.file)

    if not text:
        print("No text supplied. Exiting.")
        return

    while True:
        print("""
========== TEXT INTELLIGENCE MENU ==========
1. Complete text analysis
2. Palindrome checker
3. Anagram checker
4. Duplicate-character analysis
5. First non-repeating character
6. Longest word and run-length compression
7. Search a pattern (Naive vs KMP vs built-in)
8. Extract emails, URLs and numbers
9. Custom regular-expression search
10. Normalize text
11. Export full analysis as JSON
0. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_report(text)
        elif choice == "2":
            candidate = input("Text to check: ")
            print("Palindrome:", is_palindrome(candidate))
        elif choice == "3":
            first, second = input("First text: "), input("Second text: ")
            print("Anagrams:", are_anagrams(first, second))
        elif choice == "4":
            print(duplicate_characters(text))
        elif choice == "5":
            print("First non-repeating character:", repr(first_non_repeating_character(text)))
        elif choice == "6":
            print("Longest word:", max(get_words(text), key=len, default=""))
            candidate = input("Text to compress (press Enter to use the full text): ")
            print("Run-length compression:", compress_runs(candidate if candidate else text))
        elif choice == "7":
            pattern = input("Pattern to search (case-sensitive): ")
            for name, data in benchmark_search(text, pattern).items():
                print(f"{name}: {data['matches']} matches at {data['positions']}; "
                      f"{data['seconds']:.8f}s; correct={data['correct']}")
        elif choice == "8":
            print("Emails:", extract_emails(text))
            print("URLs:", extract_urls(text))
            print("Numbers:", extract_numbers(text))
        elif choice == "9":
            pattern = input("Enter regex pattern: ")
            try:
                print(find_pattern(text, pattern, ignore_case=True))
            except ValueError as exc:
                print(exc)
        elif choice == "10":
            print(normalize_text(text, casefold=True))
        elif choice == "11":
            report = analyze_text(text)
            output = args.json_path or input("Output JSON filename [analysis_report.json]: ").strip() or "analysis_report.json"
            Path(output).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"Report saved to {output}")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Select an option from 0 to 11.")

if __name__ == "__main__":
    main()
