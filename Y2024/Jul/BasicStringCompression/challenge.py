def basic_string_compression(string):
    if len(string) <= 1:
        return string
    string_list = list(string)

    compressed = ""
    compressed_dict = {}
    prev = string_list[0]
    max_count_flag = False
    for char in string_list:
        compressed_dict[char] = compressed_dict.get(char, 0) + 1
        if char != prev:
            max_count_flag = True if compressed_dict[prev] > 1 else False
            compressed = compressed + f"{prev}{compressed_dict[prev]}"
            del compressed_dict[prev]

            prev = char
    else:
        compressed = compressed + f"{char}{compressed_dict[char]}"

    return string if not max_count_flag else compressed
