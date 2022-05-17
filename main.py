import random
import string
from os import listdir, mkdir, rename, walk
from os.path import isdir, isfile, join
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

# após a padronização do arquivo, new folder -> new_folder. portanto, o sistema não acha o caminho especificado.
new_folder = join(main_folder, "new folder")
mkdir(new_folder)
f = open(join(new_folder, 'teste .txt'), 'x')
f.close()

for main_folder, directories, files in walk(main_folder):
    for directory in directories:
        print(join(main_folder, directory))
        new_name = join(main_folder, directory).replace(' ', '_')
        rename(join(main_folder, directory), new_name)
    for file in files:
        print(join(main_folder, file))
        new_name = join(main_folder, file).replace(' ', '_')
        rename(join(main_folder, file), new_name)
