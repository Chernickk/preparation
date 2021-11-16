import os


def print_directory_contents(path, mark=''):
    for file in os.listdir(path):
        print(f'{mark}{file}')
        if os.path.isdir(os.path.join(path, file)):
            print_directory_contents(os.path.join(path, file), mark=f'{mark}-')


if __name__ == '__main__':
    print(print_directory_contents('../'))
