def multiply_string(num_1: str, num_2: str) -> str:
    if "0" in [num_1, num_2]:
        return "0"
    num_1 = num_1[::-1]
    num_2 = num_2[::-1]
    mult_res = []
    longest = 0
    carr = 0
    for idx, n1 in enumerate (num_1) :
        n1 = int(n1)
        _res = ["0" for _ in range(idx)]
        for n2 in num_2:
            n2 = int (n2)
            res = str((n1 * n2) + carr)
            carr = 0
            if len (res) > 1:
                carr, res = res
            _res. append (res)
        if carr:
            _res. append (carr)
            carr = 0
        mult_res.append (_res)
        longest = max(len(_res), longest)
    carr = 0
    col = 0
    sum_res = []
    while col < longest:
        res = 0
        for num in mult_res:
            res += int(carr)
            carr = 0
            if len (num) >= (col + 1):
                res += int (num[col])
        res = str(res)
        if len (res) > 1:
            carr, res = res
        sum_res.append(res)
        col += 1
    if carr:
        sum_res.append(carr)
    return "".join(sum_res[::-1])
