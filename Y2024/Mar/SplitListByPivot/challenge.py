def split_list_by_pivot(my_list, pivot, smaller=[], greater=[]):
    current = my_list.pop()
    if current < pivot:
        smaller.append(current)
    else:
        greater.append(current)

    if my_list:
        return split_list_by_pivot(my_list, pivot, smaller, greater)

    return [smaller, greater]
