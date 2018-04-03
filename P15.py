import os
import shutil


class File(object):

    def __init__(self, file_name, method, work_in_temp_dir=False, temp_dir=os.path.join(os.getcwd(), 'temp')):

        self.file_dir = os.path.dirname(file_name) if os.path.dirname(file_name) else os.getcwd()
        self.temp_dir = temp_dir if os.path.dirname(temp_dir) else os.path.join(os.getcwd(), temp_dir)
        self.home_dir = os.getcwd()
        if method != 'r' and method != 'rb' and work_in_temp_dir:
            self.create_temp_dir()
            shutil.copy2(file_name, self.temp_dir)
            os.chdir(self.temp_dir)
        file_name = os.path.split(file_name)[1]

        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        os.chdir(self.home_dir)

    def create_temp_dir(self):
        try:
            os.makedirs(self.temp_dir)
        except WindowsError:
            pass


with File('123.txt', 'w', work_in_temp_dir=True, temp_dir='Temp') as file_object:
    file_object.write('333333')

