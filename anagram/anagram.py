def find_anagrams(word, candidates):
    sorted_word = sorted(word.upper())
    anagrams = []

    for candidate in candidates:

        if word.upper() == candidate.upper():
            continue

        if sorted(candidate.upper()) == sorted_word:
            anagrams.append(candidate)

    return anagrams