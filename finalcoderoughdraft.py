
import re
from collections import Counter

def analyze_text(text):
    # Split the text into words using regular expressions
    words = re.findall(r'\b\w+\b', text.lower())

    # Calculate word frequency
    word_freq = Counter(words)

    # Find the most common word and its frequency
    most_common = word_freq.most_common(1)
    if most_common:
        most_common_word, most_common_freq = most_common[0]
    else:
        most_common_word, most_common_freq = None, 0

    # Find the longest word
    longest_word = max(words, key=len) if words else ""

    return {
        "word_count": len(words),
        "unique_words": len(word_freq),
        "word_frequency": word_freq,
        "most_common_word": (most_common_word, most_common_freq),
        "longest_word": longest_word
    }

def run_tests():
    test_cases = [
        {"text": "This is a simple test. This test is simple.", "expected": {"word_count": 8, "unique_words": 5, "most_common_word": ("this", 2), "longest_word": "simple"}},
        {"text": "Another test, with punctuation! And more words.", "expected": {"word_count": 7, "unique_words": 7, "most_common_word": ("another", 1), "longest_word": "punctuation"}},
        {"text": "", "expected": {"word_count": 0, "unique_words": 0, "most_common_word": (None, 0), "longest_word": ""}},
        {"text": "One.", "expected": {"word_count": 1, "unique_words": 1, "most_common_word": ("one", 1), "longest_word": "one"}},
        {"text": "Go go go!", "expected": {"word_count": 3, "unique_words": 2, "most_common_word": ("go", 3), "longest_word": "go"}},
        {"text": "The quick brown fox jumps over the lazy dog.", "expected": {"word_count": 9, "unique_words": 8, "most_common_word": ("the", 2), "longest_word": "jumps"}},
        {"text": "A b c d e f g h i j k l m n o p q r s t u v w x y z", "expected": {"word_count": 26, "unique_words": 26, "most_common_word": ("a", 1), "longest_word": "a"}},
        {"text": "Testing with numbers 1 2 3.", "expected": {"word_count": 6, "unique_words": 6, "most_common_word": ("testing", 1), "longest_word": "testing"}},
        {"text": "  Extra   spaces  ", "expected": {"word_count": 2, "unique_words": 2, "most_common_word": ("extra", 1), "longest_word": "spaces"}},
        {"text": "Hyphenated-word and another-one.", "expected": {"word_count": 5, "unique_words": 5, "most_common_word": ("hyphenated", 1), "longest_word": "hyphenated"}}
    ]

    for i, test in enumerate(test_cases):
        result = analyze_text(test["text"])
        print(f"Test Case {i+1}:")
        print(f"  Input: '{test['text']}'")
        print(f"  Output: {result}")
        print("-" * 20)

if __name__ == "__main__":
    run_tests()
