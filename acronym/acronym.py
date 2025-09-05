import re

def abbreviate(words):

    words_no_punctuation = re.sub(r"[^A-Za-z\s-]", "", words)

    word = re.split(r"\s|-", words_no_punctuation)

    abbr = "".join(word[0].upper() for word in word if word)

    return abbr