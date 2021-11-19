from time import time


def generate_number(min_num, max_num):
    diff = max_num - min_num
    if diff <= 0:
        raise ValueError('max_num must be greater then min_num')
    random_number = int(str(time())[-3:])**2 / 10**6
    random_value = random_number * diff
    return min_num + random_value


if __name__ == '__main__':
    random_list = [generate_number(-1000, 1000) for i in range(10)]
    random_dict = {f'elem_{i}': generate_number(-1000, 1000) for i in range(10)}

