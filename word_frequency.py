import string


def clean_text(text):
    """Lowercase the text remove punctuation."""
    cleaned = ""
    for ch in text.lower():                     # lowercase so "The" and "the" match
        if ch not in string.punctuation:        # skip . , ! ? and so on
            cleaned += ch
    return cleaned


def count_words(text):
    """Return a dictionary like {"the": 2, "cat": 1}."""
    counts = {}
    for word in clean_text(text).split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def sort_counts(counts):
    """Return (word, count) pairs, most frequent first, ties in A-Z order."""
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def main():
    while True:
        text = input("Enter text (or q to quit): ").strip()
        if text.lower() == "q":
            break
        counts = count_words(text)
        if not counts:
            print("No words found. Please enter some text.")
            continue
        for word, count in sort_counts(counts):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()