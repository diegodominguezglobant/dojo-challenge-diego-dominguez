def character_frequency(word)->list:
    frequency_map = {}
    for w in word:
        frequency_map[w] = frequency_map.get(w, 0) + 1

    ordered_list = list(frequency_map.items())
    left_c = 0
    right_c = 1
    while right_c < len(ordered_list):
        if ordered_list[right_c][1] > ordered_list[left_c][1]:
            ordered_list[right_c], ordered_list[left_c] = ordered_list[left_c], ordered_list[right_c]
        left_c += 1
        right_c += 1

    left_c = 0
    right_c = 1
    no_change = True
    while True:
        if left_c == 0:
            no_change = True
        if ordered_list[right_c][1] == ordered_list[left_c][1]:
            if ordered_list[right_c][0] < ordered_list[left_c][0]:
                no_change = False
                ordered_list[right_c], ordered_list[left_c] = ordered_list[left_c], ordered_list[right_c]
        left_c += 1
        right_c += 1
        if right_c == len(ordered_list):
            left_c = 0
            right_c = 1
            if no_change:
                break


    return ordered_list
