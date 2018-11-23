import os
import re


def get_files_list():
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    list_file = os.listdir(path=os.path.join(current_dir, 'migrations'))
    return list_file


def find_procedure():
    list_file = get_files_list()
    while True:
        user_input = input('Введите строку:').lower()
        file_list_after_search = []
        i = 0
        for files in list_file:
            if re.search(user_input, files.lower()) and re.search('.sql', files):
                print(files)
                i += 1
                file_list_after_search.append(files)
        print('Всего найдено файлов: {}'.format(i))
        list_file = file_list_after_search


if __name__ == '__main__':
    find_procedure()
