def find_string_and_return_textline(text, words):
    lines = text.split('\n')
    words = [word.strip() for word in words.split(',')]

    ans = []
    for word in words:
        for i, l in enumerate(lines):
            if word in l:
                ans.append(f"Line {i}: {l}")

    return "\n".join(ans)
