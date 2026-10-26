import unittest
from analyzer import (
    analyze_text, is_palindrome, are_anagrams, duplicate_characters,
    first_non_repeating_character, compress_runs, expand_runs, normalize_text
)
from algorithms import naive_search, kmp_search
from regex_tools import extract_emails, extract_urls, extract_numbers, find_pattern

class TestAnalyzer(unittest.TestCase):
    def test_basic_statistics(self):
        report = analyze_text("Hi hi! 123")
        self.assertEqual(report["characters"], 10)
        self.assertEqual(report["words"], 3)
        self.assertEqual(report["digits"], 3)

    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(is_palindrome("Python"))

    def test_anagram(self):
        self.assertTrue(are_anagrams("Dormitory", "Dirty room!!"))
        self.assertFalse(are_anagrams("cat", "car"))

    def test_duplicate_and_first_unique(self):
        self.assertEqual(duplicate_characters("banana"), {"a": 3, "n": 2})
        self.assertEqual(first_non_repeating_character("aabbc"), "c")

    def test_compression(self):
        self.assertEqual(compress_runs("aaabbc"), "a3b2c1")
        self.assertEqual(expand_runs("a3b2c1"), "aaabbc")
        self.assertEqual(expand_runs(""), "")

    def test_normalization(self):
        self.assertEqual(normalize_text("  HELLO   World "), "hello world")

    def test_search_algorithms(self):
        text, pattern = "ababcabcabababd", "ababd"
        self.assertEqual(naive_search(text, pattern), [10])
        self.assertEqual(kmp_search(text, pattern), [10])
        self.assertEqual(kmp_search("aaaa", "aa"), [0, 1, 2])

    def test_regex(self):
        text = "Contact a@example.com, https://example.org and 42."
        self.assertEqual(extract_emails(text), ["a@example.com"])
        self.assertEqual(extract_urls(text), ["https://example.org"])
        self.assertEqual(extract_numbers(text), ["42"])
        self.assertEqual(find_pattern("cat CAT", "cat", True)[1]["match"], "CAT")

if __name__ == "__main__":
    unittest.main()
