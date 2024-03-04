def letter_tally(word, tally: dict = {}):
    if isinstance(word, str):
        word = list(word)

    letter = word.pop(0)
    letter_count = tally.get(letter, 0)
    tally[letter] = letter_count + 1

    if word:
        tally = letter_tally(word, tally)

    return tally
