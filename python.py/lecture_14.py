# Activity_1
fn = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

fn1 = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\sample_doc.txt",
    "w",
)

cont = fn.readlines()

for i in range(1, len(cont) + 1):
    if i % 2 != 0:
        fn1.write(cont[i - 1])

fn.close()
fn1.close()

fn1 = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\sample_doc.txt",
    "r",
)

cont1 = fn1.read()
print(cont1)

fn1.close()


# Activity_2
fn = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

fn1 = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\filtered.txt",
    "w",
)

for line in fn:
    if not line.startswith("Coding"):
        fn1.write(line)

fn.close()
fn1.close()


# Activity_3
file = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

print("\nread in parts\n")
print(file.read(8))

file.close()


# Activity_4
file = open(
    r"D:\OneDrive - SBaisakh\OneDrive\Documents\codingal-projects\python.py\New folder (2)\Codingal.txt",
    "r",
)

print("reading first line ...")
print(file.readline())

print("reading multiple lines....")
print(file.readline())
print(file.readline())
print(file.readline())

print("Looping through the line ....")
for line in file:
    print(line)

file.close()
