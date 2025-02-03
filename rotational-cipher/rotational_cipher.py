import string

def rotate(text, key):
    new_text = ""
    alph_list = list(string.ascii_uppercase)
    for character in text:
        if character.upper() in alph_list:
            index = alph_list.index(character.upper())
            if character.isupper():
                new_text += alph_list[((key + index) % 26)]
            else:
                new_text += alph_list[((key + index) % 26)].lower()
        else:
            new_text += character
    return new_text

# ABC
# DEF
# GIH
# JKL
# MNO
# PQR
# STU
# VWX
# YZ