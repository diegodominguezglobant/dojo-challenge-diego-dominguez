def swapping_pairs(numbers, left_c=0):
    right_c = left_c + 1

    if right_c < len(numbers):
        numbers[right_c], numbers[left_c] = numbers[left_c], numbers[right_c]
        return swapping_pairs(numbers, left_c=left_c+2)

    return numbers
