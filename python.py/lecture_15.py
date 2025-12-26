# Activity_1 and 2
file = open(
    r"D:\\OneDrive - SBaisakh\\OneDrive\Documents\\codingal-projects\\python.py\\New folder (2)\Codingal.txt",
    "w",
)
file.write(
    "Python is easy to learn\nFile handling is important\nSplit method is useful"
)
file.close()


file = open(
    r"D:\\OneDrive - SBaisakh\\OneDrive\Documents\\codingal-projects\\python.py\\New folder (2)\\Codingal.txt",
    "r",
)
content = file.read()
print("File Content:")
print(content)
file.close()

file = open(
    r"D:\\OneDrive - SBaisakh\\OneDrive\Documents\\codingal-projects\\python.py\\New folder (2)\\Codingal.txt",
    "r",
)
words = content.split()
print("\nWords after split:")
print(words)
