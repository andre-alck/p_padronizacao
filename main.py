from operator import index
import random
import string
from os import mkdir, listdir, rename, walk
from os.path import isdir, join, isfile
from shutil import rmtree

main_folder = "C:\\Users\\User\\Desktop\\main_folder\\"
if isdir(main_folder):
    rmtree(main_folder)
mkdir(main_folder)

for i in range(0, 10):
    random_int = random.randint(1, 10)
    new_file_name = string.ascii_letters[0:random_int] + \
        string.digits[0:random_int] + " " + \
        string.ascii_letters[random.randint(1, 5)] + '.txt'

    f = open(join(main_folder, new_file_name), "w")
    f.close()

# new_folder = join(main_folder, "new folder")
# mkdir(new_folder)
# f = open(join(new_folder, 'teste .txt'), 'x')
# f.close()

# content = []

print(f'listdir(main_folder) - b: {listdir(main_folder)}')

for main_folder, directories, files in walk(main_folder):
    for directory in directories:
        # content.append(join(main_folder, directory))
        new_name = join(main_folder, directory).replace(' ', '_')
        rename(join(main_folder, directory), new_name)
    for file in files:
        # content.append(join(main_folder, file))
        new_name = join(main_folder, file).replace(' ', '_')
        rename(join(main_folder, file), new_name)

print(f'listdir(main_folder) - a: {listdir(main_folder)}')

# for index in content:
#     new_name = index.replace(' ', '_')
#     rename(index, new_name)
#     print(new_name)
