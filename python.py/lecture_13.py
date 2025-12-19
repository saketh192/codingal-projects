# File handling
# Acitivity_1 and 2
file_read = open("Codingal.txt", "r")
print("File in read mode - ")
print(file_read.read())
file_read.close()
file_write = open("Codingal.txt", "w")
file_write.write("File in mode ....")
file_write.write("Hi i am penguin  , I am 1 year old")
file_write.close()
file_append = open("Codingal.txt", "a")
file_append.write("\n File in append mode ....")
file_append.write("Hi i am penguin  , I am 1 year old")
file_append.close()

# Acitivity_3
file = open("Codingal.txt", "r")
counter = 0
content = file.read()
colist = content.split("\n")

for i in colist:
    if i:
        counter += 1

print("this is the number of lines in the file")
print(counter)

# Activity_4
firstfile = input("Enter the first file")
secondfile = input("Enter the first file")

f1 = open(firstfile, "r")
f2 = open(secondfile, "r")

f1.close()
f2.close()

f1 = open(firstfile, "a+")
f2 = open(secondfile, "r")

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("content of firstfile before appending - \n", f1.read())
print("content of secondfile before appending - \n", f2.read())
