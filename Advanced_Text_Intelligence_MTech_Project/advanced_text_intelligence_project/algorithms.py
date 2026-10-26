"""String-search algorithms and simple performance measurements."""
from time import perf_counter

def naive_search(text: str, pattern: str) -> list[int]:
    """Return every start index where pattern occurs; O(n*m) worst case."""
    if pattern == "":
        return list(range(len(text) + 1))
    found = []
    for i in range(len(text) - len(pattern) + 1):
        matched = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                matched = False
                break
        if matched:
            found.append(i)
    return found

def build_lps(pattern: str) -> list[int]:
    """Build KMP longest-prefix-suffix table in O(m)."""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(text: str, pattern: str) -> list[int]:
    """Knuth-Morris-Pratt search; O(n+m) time."""
    if pattern == "":
        return list(range(len(text) + 1))
    lps = build_lps(pattern)
    found = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                found.append(i - j)
                j = lps[j - 1]
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return found

def benchmark_search(text: str, pattern: str) -> dict:
    results = {}
    expected = naive_search(text, pattern)
    for name, function in (("Naive", naive_search), ("KMP", kmp_search), ("Python find loop", _builtin_find_all)):
        start = perf_counter()
        matches = function(text, pattern)
        elapsed = perf_counter() - start
        results[name] = {
            "matches": len(matches),
            "positions": matches,
            "seconds": elapsed,
            "correct": matches == expected,
        }
    return results

def _builtin_find_all(text: str, pattern: str) -> list[int]:
    if pattern == "":
        return list(range(len(text) + 1))
    found, start = [], 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            return found
        found.append(index)
        start = index + 1
