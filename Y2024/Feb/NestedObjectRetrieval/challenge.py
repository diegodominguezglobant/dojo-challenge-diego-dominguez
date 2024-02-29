def find_obj(texts):
    if isinstance(texts, dict):
        if 'textId' in texts:
            return texts['textId']
        else:
            for _, value in texts.items():
                result = find_obj(value)
                if result is not None:
                    return result
    elif isinstance(texts, (list, tuple)):
        for item in texts:
            result = find_obj(item)
            if result is not None:
                return result
    return None

