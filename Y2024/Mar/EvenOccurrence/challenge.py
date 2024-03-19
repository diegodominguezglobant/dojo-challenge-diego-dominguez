def even_occurrence(numbers):
    occurrences = {}
    for num in numbers:
        occurrences[num] = occurrences.get(num, 0) + 1

    for k, v in occurrences.items():
        if v % 2 == 0:
            return k
    return None




