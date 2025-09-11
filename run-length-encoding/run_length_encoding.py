def decode(string):

    counter = ""
    decoded_string = ""

    for character in string:
        if character.isdigit():
            counter += character
            continue
        if counter:
            decoded_string += int(counter) * character
            counter = ""
            continue
        decoded_string += character

    return decoded_string


def encode(string):

    if not string:
        return string
    
    previous_character = string[0]
    counter = 1
    encoded_string = ""

    for character in string[1:]:
        if character == previous_character:
            counter += 1
            continue
        if counter > 1:
            encoded_string += str(counter) + previous_character
            counter = 1
        else:
            encoded_string += previous_character
        previous_character = character
    #This is for appending the last character, since the loops doenst handle that
    #Theres definitely a better way to do this. (Could do a helper function)
    if counter > 1:
        encoded_string += str(counter) + previous_character
    else:
        encoded_string += previous_character

    return encoded_string
