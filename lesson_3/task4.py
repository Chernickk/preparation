import os


def list_file(filename, template, include_all=False):
    with open(filename, 'r') as f:
        for line in f:
            if template in line:
                print(line)

            if not include_all:
                break


def create_file(filename):
    text = ['text' for i in range(5)]
    nums = [i if i % 2 else 'example234' for i in range(5)]

    result = list(zip(text, nums))

    if os.path.exists(filename):
        print('file already exists!')
    with open(filename, 'a') as f:
        for line in result:
            f.write(' '.join(str(x) for x in line) + '\n')

    list_file(filename, 'example', include_all=True)


if __name__ == '__main__':
    create_file('test.txt')
