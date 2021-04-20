import os

def search_file(path,str):
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            if str in file and os.path.splitext(file)[1] == '.py':
                print(filepath)
        else:
            search_file(filepath, str)

if __name__ == '__main__':
    path = input('Please enter the test path:')
    search_file(path, 'a')
            
