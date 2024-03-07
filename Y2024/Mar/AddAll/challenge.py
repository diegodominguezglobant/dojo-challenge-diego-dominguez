def add_all(nums, cur_sum=0):
    if nums:
        num = nums.pop(0)
        cur_sum += num
        return add_all(nums, cur_sum)
    return cur_sum
