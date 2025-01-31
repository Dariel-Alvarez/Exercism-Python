import string

def is_pangram(sentence):

    letters = set(string.ascii_uppercase)

    letters_in_sentence = set(sentence.upper())

    return letters.issubset(letters_in_sentence)