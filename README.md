# Word Frequency (Python)

A command-line tool that counts how many times each word appears in a block of text. Built as a beginner Python project to practice strings, dictionaries and sorting.

## Features
- Counts every word in the text you enter
- Ignores upper and lower case, so `The` and `the` count as the same word
- Removes punctuation before counting
- Shows results with the most frequent word first, and ties in A-Z order
- Shows a message if no words are found
- Runs in a loop until you type `q`
- Includes tests using `assert`

## How it works
1. **Clean:** the text is made lowercase and punctuation is removed with `string.punctuation`.
2. **Split:** `.split()` cuts the cleaned text into single words.
3. **Count:** a dictionary stores each word and how many times it was seen.
4. **Sort:** `sorted()` orders the words by count (highest first), then A-Z for ties.

Example of the counting step for `the cat and the hat`:

```
the  -> 2
cat  -> 1
and  -> 1
hat  -> 1
```

## Requirements
- Python 3.6 or newer (no extra libraries needed)

## How to run
```
python word_frequency.py
```
Type some text and press Enter. Type `q` to quit.

## Example
```
Enter text (or q to quit): the cat and the hat
the: 2
and: 1
cat: 1
hat: 1

Enter text (or q to quit): Hello, hello! HELLO?
hello: 3

Enter text (or q to quit): !!!
No words found. Please enter some text.

Enter text (or q to quit): q
```

## Functions
| Function | What it does |
|---|---|
| `clean_text(text)` | Lowercases the text and removes punctuation |
| `count_words(text)` | Returns a dictionary of `{word: count}` |
| `sort_counts(counts)` | Returns `(word, count)` pairs, most frequent first |
| `main()` | Command-line menu that asks for text and prints the results |

## Run the tests
```
python test_word_frequency.py
```
If everything works, it prints `All tests passed`.

## Project structure
```
WordFrequency/
├── word_frequency.py        # counting logic and command-line menu
├── test_word_frequency.py   # tests using assert
├── .gitignore               # ignores __pycache__
└── README.md
```

## What I learned
- A dictionary stores a word and its count together, and I can add 1 each time a word appears again.
- `.split()` turns a block of text into separate words, and `string.punctuation` helps remove symbols.
- `sorted()` with a `lambda` key lets me sort by count first and alphabetically second.
- Cleaning the data first (lowercase, no punctuation) matters, because `The`, `the,` and `THE` should count as one word.
- Splitting the code into small functions makes it easier to test each part on its own.

## Limitations
- Words with apostrophes, like `don't`, become `dont` because the apostrophe is removed as punctuation.
- Only plain text typed into the terminal is supported (no files yet).

## Ideas for improvement
- Read text from a `.txt` file
- Show only the top 10 words
- Ignore common words like `the`, `and`, `a`