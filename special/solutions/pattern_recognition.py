"""
/**
 * 5 points
 * <p>
 * Given a pattern and a string str, find if str follows the same pattern.
 *
 * <p>
 * Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
 * <p>
 * <p>
 * Example 1:
 * Input: pattern = "abba", str = "dog cat cat dog"
 * Output: true
 * <p>
 * Input:pattern = "abba", str = "dog cat cat fish"
 * Output: false
 * <p>
 * Input: pattern = "aaaa", str = "dog cat cat dog"
 * Output: false
 * <p>
 * Input: pattern = "abba", str = "dog dog dog dog"
 * Output: false
 */
"""


def check_pattern(pattern: str, text: str) -> bool:
    words_of_text = text.split()

    if len(words_of_text) is not len(pattern):
        return False

    pattern_history = {}

    for word, pattern_letter in zip(words_of_text, pattern):
        word_corresponding_to_pattern = pattern_history.get(pattern_letter, None)
        if word_corresponding_to_pattern is None:
            if word in pattern_history.values():
                return False
            pattern_history[pattern_letter] = word
        elif word_corresponding_to_pattern is not word:
            return False

    return True
