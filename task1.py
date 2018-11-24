import os


def get_files_list():
    migrations = 'Migrations'
    file_format = '.sql'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    list_file = []
    for sql_file in os.listdir(path=os.path.join(current_dir, 'migrations')):
        if file_format in sql_file:
            list_file.append(sql_file)
    return list_file


def find_procedure():
    list_file = get_files_list()
    while True:
        user_input = input('Введите строку:')
        file_list_after_search = []
        i = 0
        for files in list_file:
            with open(os.path.join('Migrations', files)) as file:
                if user_input in file.read():
                    print(files)
                    i += 1
                    file_list_after_search.append(files)
        print('Всего найдено файлов: {}'.format(i))
        list_file = file_list_after_search


if __name__ == '__main__':
    find_procedure()
