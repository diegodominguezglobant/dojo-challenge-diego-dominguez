def sum_candidates(candidates, target):
    candidates = list(filter(lambda x: x<target, candidates))
    index = 0
    all_ans = []
    for i, cand in enumerate(candidates):
        deep = 0
        ans = []
        left_cur = 0
        left_candidates = candidates.copy()
        left_candidates.pop(i)
        ans.append(cand)
        if sum(ans) == target:
            ans.sort()
            if ans not in all_ans:
                all_ans.append(ans)
            continue
        while True:
            print(left_cur, deep)
            ans.append(left_candidates[left_cur])
            if sum(ans) == target:
                ans.sort()
                if ans not in all_ans:
                    all_ans.append(ans)
                break

            elif sum(ans) < target:
                left_cur += 1
                deep += 1

            elif sum(ans) > target:
                for _ in range(deep):
                    ans.pop()
                left_cur += 1
                if deep > 1:
                    left_cur -= 1
                    deep -= 0

    return all_ans
