ONES_TENS = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

SCALES = ["", "thousand", "million", "billion"]


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"
    
    words = []

    group_index = 0

    while number > 0:
        number, remainder = divmod(number, 1000)

        if remainder:
            chunk = say_core_digits_helper(remainder)

            if SCALES[group_index]:
                chunk += " " + SCALES[group_index]
            
            words.append(chunk)
        
        group_index += 1

    return " ".join(reversed(words))



def say_core_digits_helper (number: int) -> str:

    parts = []

    if number >= 100:
        parts.append(ONES_TENS[number//100] + " hundred")
        number %= 100

    if number >= 20:
        parts.append(TENS[number//10])
        if number % 10:
            parts[-1] += "-" + ONES_TENS[number%10]
    
    elif number > 0:
        parts.append(ONES_TENS[number])
    
    return " ".join(parts)