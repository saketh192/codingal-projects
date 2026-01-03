# File Operations in Python

# 1. Create and write to a file
file = open("sample.txt", "w")
file.write("Python is easy to learn.\n")
file.write("File handling is important.\n")
file.close()

print("File created and written successfully.\n")

# 2. Read the entire file
file = open("sample.txt", "r")
content = file.read()
print("Reading full content:")
print(content)
file.close()

# 3. Read file line by line
file = open("sample.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())
file.close()

# 4. Append new content to the file
file = open("sample.txt", "a")
file.write("This line is appended.\n")
file.close()

print("\nContent appended successfully.\n")

# 5. Count number of words in the file
file = open("sample.txt", "r")
text = file.read()
words = text.split()
print("Total number of words:", len(words))
file.close()
