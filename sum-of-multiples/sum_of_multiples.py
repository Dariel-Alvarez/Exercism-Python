def sum_of_multiples(limit, multiples):
    
    factors = set()

    for number in multiples:
        
        if number == 0:
            continue

        for factor in range(number, limit, number):
            factors.add(factor)

    return sum(factors)