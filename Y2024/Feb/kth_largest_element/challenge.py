def kth_largest(nums, k):
    processed = []
    while k:
        largest = float("-inf")
        index = -1
        for i, num in enumerate(nums):
            if num > largest:
                largest = num
                index = i

        processed.append(nums.pop(index))

        k -= 1
    return processed[-1]

