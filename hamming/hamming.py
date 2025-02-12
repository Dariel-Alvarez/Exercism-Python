def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    hamming_distance = 0

    for char1, char2 in zip(strand_a, strand_b):
        if char1 != char2:
            hamming_distance += 1

    return hamming_distance