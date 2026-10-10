from word_frequency import clean_text, count_words, sort_counts

assert clean_text("Hello, World! Hello...") == "hello world hello"
assert count_words("the cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
assert count_words("Hi, hi! HI?") == {"hi": 3}
assert count_words("") == {}
assert sort_counts({"b": 1, "a": 1, "the": 2}) == [("the", 2), ("a", 1), ("b", 1)]
print("All tests passed")