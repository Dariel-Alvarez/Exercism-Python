def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10 or "X" in isbn[:-1]:
        return False
    total = 0
    counter = 10
    for digit in isbn:
        if digit.isalpha():
            if digit == "X":
                digit = 10
            else:
                return False
        total += int(digit) * counter
        counter -= 1
    return total % 11 == 0
