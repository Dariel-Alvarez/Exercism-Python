def append(list1, list2):
    return list1 + list2


def concat(lists):
    single_list = []
    for lst in lists:
        single_list += lst
    return single_list


def filter(function, list):
    predicate_list = []
    for item in list:
        if function(item):
            predicate_list.append(item)
    return predicate_list


def length(list):
    counter = 0
    for _ in list:
        counter += 1
    return counter


def map(function, list):
    function_list = []
    for item in list:
        function_list.append(function(item))
    return function_list


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    list = reverse(list)
    return foldl(function, list, initial)


def reverse(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list
