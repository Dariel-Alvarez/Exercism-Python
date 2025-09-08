def slices(series, length):

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if not series:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    substrings_arr = []

    for substring_start in range(len(series) - (length - 1)):
        substrings_arr.append(series[substring_start:substring_start + length])

    return substrings_arr




"""
If series length = 1
and slice = 1
1
lenght=     slice=      possible substrings:
2   1   2
2   2   1

3   1   3
3   2   2
3   3   1  

4   1   4
4   2   3
4   3   2
4   4   1

formula=
x - (slice - 1) = result

len(series) - (lenght - 1)



"""