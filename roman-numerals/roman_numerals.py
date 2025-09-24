def roman(number):
    Letters_Numbers = {"M":1000,
                       "CM": 900,
                       "D": 500,
                       "CD": 400,
                       "C": 100,
                       "XC": 90,
                       "L": 50,
                       "XL": 40,
                       "X": 10,
                       "IX": 9,
                       "V": 5,
                       "IV": 4,
                       "I": 1}
    
    roman_number = ""
    for key, value in Letters_Numbers.items():
        div = number // value
        if div > 0:
            roman_number += key * div
        number = number % value
    
    return roman_number
