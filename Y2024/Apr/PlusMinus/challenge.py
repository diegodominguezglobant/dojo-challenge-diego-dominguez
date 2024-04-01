def plus_minus(arr_n):
    len_n = len(arr_n)
    neg = 0
    pos = 0
    zero = 0
    for n in arr_n:
        if n < 0:
            neg += 1
        elif n > 0:
            pos += 1
        else:
            zero += 1

    print(round(neg/len_n, 6))
    print(round(pos/len_n, 6))
    print(round(zero/len_n, 6))
