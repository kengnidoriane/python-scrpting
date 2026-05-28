# with open("spider.txt") as file:
#     for line in file:
#         print(line.strip().upper())


file = open("spider.txt") 
lines = file.readlines()
file.close()       
print(lines)
# when we use readlines() method, it reads the entire file and returns a list of lines. Each line is a string and includes the newline character at the end. We can use strip() method to remove the newline character and any leading or trailing whitespace from each line.