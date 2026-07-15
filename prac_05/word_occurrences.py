"""
CP1404 practical - word occurrences
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
WORD_TO_COUNT = {}
for word in words:
    word = word.lower()
    if word in WORD_TO_COUNT:
        WORD_TO_COUNT[word] += 1
    else:
        WORD_TO_COUNT[word] = 1

word_width = max([len(word) for word in WORD_TO_COUNT])

for word in sorted(WORD_TO_COUNT.keys()):
        print(f"{word:{word_width}} : {WORD_TO_COUNT[word]}")

