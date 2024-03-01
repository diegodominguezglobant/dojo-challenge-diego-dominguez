def diagonal_difference(matrix):
    diag_1 = 0
    diag_2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                diag_1 += matrix[i][j]
            if i + j == len(matrix)-1:
                diag_2 += matrix[i][j]

    ans = diag_1 - diag_2
    return ans if ans > -1 else ans * -1
