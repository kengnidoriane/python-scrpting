import os
os.remove("novel.txt")
os.rename("spider.txt", "arachnid.txt")
# the os module provides functions for interacting with the operating system. The remove() function is used to delete a file, and the rename() function is used to rename a file. In this example, we are deleting the "novel.txt" file and renaming the "spider.txt" file to "arachnid.txt".
os.path.exists("novel.txt")
os.path.exists("arachnid.txt")
#