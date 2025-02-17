def transform(legacy_data):
    result = {}
    for key in legacy_data:
        letters, value = legacy_data[key], key
        for letter in letters:
            result[letter.lower()] = key
    return result