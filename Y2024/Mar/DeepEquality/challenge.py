def deep_equality(x, y):
    return x == y


def deep_equality_recursive(first, second):
    for k, v in first.items():
        if second.get(k, None) != v:
            return False

        if isinstance(v, dict):
            return deep_equality_recursive(first[k], second[k])
    else:
        return True
