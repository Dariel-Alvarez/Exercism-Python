import string

alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]
translation = str.maketrans(alphabet, reversed_alphabet)
reverse_translation = str.maketrans(reversed_alphabet, alphabet)

def encode(plain_text):
    plain_text = plain_text.lower()
    filtered_text = ""
    for char in plain_text:
        if char.isalpha():
            filtered_text += char.translate(translation)
        elif char.isdigit():
            filtered_text += char
    grouped_cipher = []
    for i in range(0, len(filtered_text), 5):
        grouped_cipher.append(filtered_text[i:i+5])
    return " ".join(grouped_cipher)

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    filtered_text = ""
    for char in ciphered_text:
        if char.isalpha():
            filtered_text += char.translate(reverse_translation)
        elif char.isdigit():
            filtered_text += char
    return filtered_text