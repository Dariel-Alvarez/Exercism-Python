def square_root(number):

    if number == 1:
        return number
    
    left, right = 1, number

    while left <= right:
        mid = (left + right) // 2

        squared_mid = mid * mid

        if squared_mid == number:
            return mid
        
        if squared_mid < number:
            left = mid + 1
        
        else:
            right = mid - 1
    
    raise ValueError("Value does not exist.")
