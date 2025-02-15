def square_of_sum(number):
    sums = 0
    for char in range(number + 1):
        sums += char
    return sums ** 2
        


def sum_of_squares(number):
    squares = 0
    for char in range(number + 1):
        squares += char ** 2
    return squares



def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
