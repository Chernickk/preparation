import os


def extract_filename(full_path:str):
    filename = os.path.basename(full_path).split('.')[0]
    return filename


if __name__ == '__main__':
    print(extract_filename('/home/nik/Documents/education/preparation/lesson_3/task1.py'))
