def spinner(players: list, k: int, index=0)->int:
    count = 0
    while count < k-1:
        index += 1
        count += 1
        if index > len(players):
            index = 1
        elif index == len(players):
            index = 0

    return index


def find_the_winner(n, k):
    index = 0
    while len(n) > 1:
        index = spinner(n, k, index)
        n.pop(index)

    return n[0]

