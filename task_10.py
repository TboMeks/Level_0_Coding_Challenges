def output_common(word_i, word_ii):

    temp_string_i = word_i.lower()
    temp_string_ii = word_ii.lower()

    letters = (set(temp_string_i) & set(temp_string_ii))
    words = (letter for letter in letters)
    character = ", " .join(words)

    print(f"Common letters: {character}")


output_common("house", "computers")
