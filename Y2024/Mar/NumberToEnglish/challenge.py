number_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen'
}

dec_map = {
    1: ' thousand',
    2: ' million',
    3: ' billion'
}

def number_to_english(number):
    number = list(str(number))[::-1]
    word = ''
    hundred_pos = 0
    while number:
        digits = number[:3][::-1]

        hundred_group = ''

        if len(digits) < 3:
            digits = list(''.join(digits).zfill(3))
        if digits[0] != '0':
            hundred_group += f'{number_map[int(digits[0])]} hundred '

        if dec_ans := number_map.get(int(digits[1] + digits[2])):
            hundred_group += dec_ans

        elif int(digits[1]) < 2:
            hundred_group += f'{number_map.get(int(digits[0]))}teen '

        else:
            hundred_group += f'{number_map.get(int(digits[1]))}ty-{number_map.get(int(digits[2]))}'

        hundred_group += dec_map.get(hundred_pos, '')

        word = hundred_group + ' ' + word
        hundred_pos += 1
        number[:] = number[3:]


    return word.strip()


