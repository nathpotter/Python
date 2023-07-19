import os
from pathlib import Path

# Specify the directory path
path = Path(r'C:/Users/nath_/OneDrive/Desktop/')
file_name = 'test3.txt'
abs_file_path = os.path.join(path, file_name)

print(path)
print(file_name)
print(abs_file_path)

# Creating a file at specified folder
# join directory and file path
if(os.path.exists(abs_file_path) != True):
# if(os.path.isfile(abs_file_path)):
    with open(os.path.join(path, file_name), 'w') as fp:
        # uncomment below line if you want to create an empty file
        fp.write('This is a new line')
        fp.write('This is a 2nd line')
else:
    # read file with absolute path
    try:
        fp = open(os.path.join(path, file_name), 'a')
        print(fp.read())
        fp.close()
    except FileNotFoundError:
        print("Please check the path")

