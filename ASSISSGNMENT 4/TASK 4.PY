def count_vowels(text):
    """
    Count the number of vowels in a string (a, e, i, o, u).
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)

if __name__ == "__main__":
    examples = ["Hello World", "Python Programming", "AEIOU", "rhythm", ""]
    for s in examples:
        print(f"'{s}' -> {count_vowels(s)}")