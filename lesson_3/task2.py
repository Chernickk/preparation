def compare_parts_of_num(num):
    try:
        float(num)
    except ValueError:
        return 'NaN'

    num_string = str(num)

    if '.' in num_string:
        int_part, fract_part = num_string.split('.')
    elif ',' in num_string:
        int_part, fract_part = num_string.split(',')
    else:
        return 'Integer'

    return True if int_part == fract_part else False


if __name__ == '__main__':
    print(compare_parts_of_num(123.342))
    print(compare_parts_of_num(123.123))
    print(compare_parts_of_num('string'))
    print(compare_parts_of_num(123))
