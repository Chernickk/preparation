def fill_dict(keys:list, values:list):
    result = {}
    for key in keys:
        try:
            result[key] = values.pop()
        except IndexError:
            result[key] = None
    return result


if __name__ == '__main__':
    values = [1, 2, 3, 4]
    keys = ['a', 'b', 'c', 'd', 'e', 'f']
    result = fill_dict(keys, values)
