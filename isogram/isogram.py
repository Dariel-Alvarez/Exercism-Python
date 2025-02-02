def is_isogram(string):
    letters = dict()
    string = string.upper()
    for letter in string:
        if letter.isalpha():
            if letter not in letters:
                letters[letter] = 1
            else:
                return False
    return True

