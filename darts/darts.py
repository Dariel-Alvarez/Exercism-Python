import math

def score(x, y):
    hypotenuse = calculate_hypotenuse(x, y)
    if hypotenuse <= 1:
        return 10
    if hypotenuse <= 5:
        return 5
    if hypotenuse <= 10:
        return 1
    return 0

def calculate_hypotenuse(x, y):
    return math.sqrt(x ** 2 + y ** 2)
