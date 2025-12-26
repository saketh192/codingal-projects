# Open the file in read mode
file = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

print("1. Read the entire file using read():")
print(file.read())

file.close()


# Open again because the file pointer is at the end
file = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

print("\n2. Read one line using readline():")
print(file.readline())

file.close()


# Open again
file = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

print("\n3. Read all lines using readlines():")
lines = file.readlines()
print(lines)

file.close()


# Open again
file = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

print("\n4. Read line by line using a loop:")
for line in file:
    print(line, end="")

file.close()
