def find_the_shortest_path_between_two_nodes(matrix, start_node, end_node):
    n = len(matrix)
    seen = [False] * n
    weight = [float('inf')] * n
    weight[start_node] = 0

    for _ in range(n):
        min_weight = float('inf')
        for i in range(n):
            if not seen[i] and weight[i] < min_weight:
                min_weight = weight[i]
                current_node = i

        seen[current_node] = True

        if current_node == end_node:
            break

        for i in range(n):
            if matrix[current_node][i] != 0 and not seen[i]:
                new_weight = weight[current_node] + matrix[current_node][i]
                if new_weight < weight[i]:
                    weight[i] = new_weight

    path = []
    node = end_node
    while node != start_node:
        path.append(node)
        min_weight = float('inf')
        for i in range(n):
            if matrix[i][node] != 0 and weight[node] == weight[i] + matrix[i][node]:
                if weight[i] < min_weight:
                    min_weight = weight[i]
                    prev_node = i
        node = prev_node
    path.append(start_node)

    return path[::-1]
