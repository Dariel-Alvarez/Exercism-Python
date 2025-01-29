import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number == 1:
        return "deficient"
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = sum(findfactors(number))

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum < number:
        return "deficient"
    return "abundant"


def findfactors(number):
    factors = [1]
    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0:
            factors.append(index)
            if index != number // index:
                factors.append(number//index)
    return factors




