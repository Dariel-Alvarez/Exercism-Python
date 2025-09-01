def factors(value):
    
    factors = []
    i = 2

    while i < value:
        if value % i == 0:
            factors.append(i)
            value /= i        
        else:
            i += 1
    
    if value != 1: factors.append(value)
        
    return factors
