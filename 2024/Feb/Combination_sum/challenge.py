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


def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        print(start, target, path)
        # Si el target es 0, hemos encontrado una combinación válida
        if target == 0:
            results.append(path[:])  # Añade una copia de 'path' a 'results'
            return
        # Si el target es negativo, esta ruta no nos lleva a una solución
        if target < 0:
            return

        for i in range(start, len(candidates)):
            # Si el candidato actual es igual al anterior, lo saltamos para evitar duplicados
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # Añade el candidato actual a 'path' y realiza una llamada recursiva
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)

            # Deshace la última elección, permitiendo al backtracking probar la próxima opción
            path.pop()

    results = []
    candidates.sort()  # Ordena los candidatos para facilitar la eliminación de duplicados
    backtrack(0, target, [])
    return results

# Ejemplo de uso
candidates = [10,1,2,7,6,1,5]
target = 8
print("Resultados:")
combinationSum2(candidates, target)

