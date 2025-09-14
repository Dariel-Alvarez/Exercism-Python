
def is_prime(x):
        if x < 2:
            return False
        
        for i in range(2, int(x**0.5) + 1):
            
            if x % i == 0:
                return False
        
        return True


def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    
    count = 0
    candidate = 1

    while count < number:

        candidate += 1

        if is_prime(candidate):
            count += 1

    return candidate