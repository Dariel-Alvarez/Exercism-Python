def pig_latin_(text):
    vowels = set("aeiou")

    if text[0] in vowels or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"
    
    if text[0] == 'y' and text[1] in vowels:
        return text[1:] + text[0] + "ay"
    
    consonant_cluster = ""
    while text[0] not in vowels and not (text[0] == 'y' and len(consonant_cluster) > 0):
        if text[0] == "q" and text[1] == "u":
            consonant_cluster += text[:2]
            text = text[2:]
            break
        consonant_cluster += text[0]
        text = text[1:]
        if len(text) == 0:
            break
    return text + consonant_cluster + "ay"

def translate(text):
    latin_words = []
    for word in text.split():
        latin_words.append(pig_latin_(word))
    return " ".join(latin_words)