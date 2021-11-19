def multi_table(a, b):
    table = []
    for i in range(1, a + 1):
        table.append([])
        for j in range(1, b + 1):
            table[i - 1].append(i * j)

    return table


def print_table(a, b):
    table = multi_table(a, b)
    for line in table:
        print('\t'.join([f"{el}" for el in line]))


if __name__ == '__main__':
    print_table(10, 30)
