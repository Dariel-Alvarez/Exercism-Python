def flatten(iterable):

    final_list = []

    for item in iterable:
        if type(item) == list:
            final_list.extend(flatten(item))
        elif item != None:
            final_list.append(item)
            
    return final_list