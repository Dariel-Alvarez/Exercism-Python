
import re

def count_words(sentence):

    Valid_Word_Pattern = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*")

    Valid_Words = Valid_Word_Pattern.findall(sentence)

    word_count = {}

    for word in Valid_Words:

        word = word.lower()

        if word not in word_count:
            word_count.update({word:1})
        else:
            word_count[word] += 1
    
    return word_count
