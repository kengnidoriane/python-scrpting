file = open("spider.txt")
print(file.readline())
print(file.read())
file.close()

# another way to open a file is using with statement, it will automatically close the file after the block of code is executed
with open("spider.txt") as file:
    print(file.readline())
    print(file.read())

# reasons to always close a file:
# 1. It frees up system resources that are being used by the file.
# 2. It ensures that any changes made to the file are saved properly.
# 3. It prevents data corruption and loss of data.