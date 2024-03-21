def common_factors(num_1, num_2):
    min_num = min(num_1, num_2)
    ans = []
    for i in range(1, min_num + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            ans.append(i)
    return ans
