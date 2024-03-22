def common_characters(characters_list: list)->list:
    characters_list = [list(char) for char in characters_list]

    larger = []
    for char in characters_list:
        if len(char) > len(larger):
            larger = char
    index = 0
    characters_list.remove(larger)

    ans = ''
    while index < len(larger) and all(characters_list):
        cur_char = larger[index]
        for i, char in enumerate(characters_list):
            if not cur_char in char:
                break
            else:
                char.remove(cur_char)
                characters_list[i] = char

        else:
            ans += cur_char

        index += 1

    return ans
