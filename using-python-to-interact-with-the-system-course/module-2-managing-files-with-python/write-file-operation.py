with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night.")

# the "w" mode stands for "write". If the file already exists, it will be overwritten. If the file does not exist, it will be created. The write() method is used to write a string to the file. After the block of code is executed, the file is automatically closed.
#  the "a" mode stands for "append". If the file already exists, new content will be added to the end of the file. If the file does not exist, it will be created. The write() method is used to write a string to the file. After the block of code is executed, the file is automatically closed.
#  the "x" mode stands for "exclusive creation". It creates a new file and opens it for writing. If the file already exists, it raises a FileExistsError. The write() method is used to write a string to the file. After the block of code is executed, the file is automatically closed.
# the "r" mode stands for "read". It is the default mode when opening a file. It opens the file for reading and raises an error if the file does not exist. The read() method is used to read the entire contents of the file as a string. After the block of code is executed, the file is automatically closed.
# the "rt" mode stands for "read text". It is the same as "r" mode and is used to read text files. It opens the file for reading and raises an error if the file does not exist. The read() method is used to read the entire contents of the file as a string. After the block of code is executed, the file is automatically closed.
# the "+" mode stands for "update". It allows you to read and write to the file. If the file does not exist, it will be created. The read() method is used to read the entire contents of the file as a string, and the write() method is used to write a string to the file. After the block of code is executed, the file is automatically closed.

with open("novel.txt", "a") as file:
    file.write("\nThe rain was pouring down.")