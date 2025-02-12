def find(search_list, value):
    low, high = 0, len(search_list) - 1

    while low <= high:

        mid_index = (low + high) // 2

        if value == search_list[mid_index]:
            return mid_index

        if value > search_list[mid_index]:
            low = mid_index + 1

        else:
            high = mid_index - 1

    raise ValueError("value not in array")