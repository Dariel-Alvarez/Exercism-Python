def is_paired(input_string):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    for character in input_string:
        if character in brackets:
            stack.append(character)
        elif character in brackets.values():
            if not stack or brackets[stack.pop()] != character:
                return False
    return not stack