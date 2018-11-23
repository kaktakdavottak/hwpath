import subprocess
import os

def cut_picture():


        # Проверяем наличие директории, если нет - создаем ее
        if not os.path.exists('.\Result'):
                path = os.getcwd()
                os.mkdir(path + '\Result')

        # Директория с картинками, создание списка файлов
        result = 'Result'
        source = 'Source'
        current_dir = os.path.dirname(os.path.abspath(__file__))
        list_file = os.listdir(path=os.path.join(current_dir, 'source'))

        # Обрезка исходников в цикле
        for file in list_file:
                file_init_path = current_dir + '\\' +source + '\\' + file
                file_target_path = current_dir + '\\' + result + '\\' + file
                cmd = current_dir + '\convert ' + file_init_path + ' -resize 200 ' + file_target_path
                subprocess.call(cmd, shell=True)

cut_picture()

