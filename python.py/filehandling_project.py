# FILE HANDLING ACTIVITY

# 1. Create a file and write data using 'w' mode
file = open("student.txt", "w")
file.write("Name: Saketh\n")
file.write("Class: 9\n")
file.write("Subject: Computer Science\n")
file.close()

print("File created and data written successfully.\n")


# 2. Read the file using 'r' mode
file = open("student.txt", "r")
print("Reading file content:")
print(file.read())
file.close()


# 3. Append new data using 'a' mode
file = open("student.txt", "a")
file.write("School: ABC Public School\n")
file.close()

print("\nNew data appended successfully.\n")


# 4. Read and update file using 'r+' mode
file = open("student.txt", "r+")
content = file.read()
file.write("Year: 2025\n")
file.close()

print("File updated using r+ mode.\n")


# 5. Final file content
file = open("student.txt", "r")
print("Final file content:")
print(file.read())
file.close()
