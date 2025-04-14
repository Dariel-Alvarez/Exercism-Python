import string

def rows(letter):

    letters = string.ascii_uppercase
    n = letters.index(letter)
    lines = []

    for i in range(n + 1):
        charac = letters[i]
        outer_spaces = ' ' * (n - i)
        if i == 0:
            line = outer_spaces + charac + outer_spaces
        else:
            inner_spaces = ' ' * (2 * i - 1)
            line = outer_spaces + charac + inner_spaces + charac + outer_spaces
        lines.append(line)

    diamond = lines + lines[:-1][::-1]

    return diamond
