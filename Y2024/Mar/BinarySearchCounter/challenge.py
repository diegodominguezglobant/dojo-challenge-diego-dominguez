def binary_search_counter(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
