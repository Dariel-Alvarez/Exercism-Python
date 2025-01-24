def is_armstrong_number(number):
    total = 0
    number_string = str(number)
    for x in number_string:
        total += int(x) ** len(number_string)
    return total == number