import os.path

class File:
    def __init__(self, path):
        self.path = path

    def create(self):
        with open(self.path, 'w') as file:
            file.write('')
            file.close()

    def append(self, data):
        with open(self.path, 'a') as file:
            file.write(data + "\n")
            file.close()

    def clear(self):
        with open(self.path, 'w') as file:
            pass


def file_exist(file):
    return os.path.exists(file.path)