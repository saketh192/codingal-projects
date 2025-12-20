# Activity_1
fn = open(
    r"D:\\OneDrive - SBaisakh\\OneDrive\Documents\\codingal-projects\\python.py\\New folder (2)\\Codingal.txt",
    "r",
)
fn1 = open(
    r"D:\\OneDrive - SBaisakh\\OneDrive\Documents\\codingal-projects\\python.py\\New folder (2)\\sample_doc.txt",
    "w",
)
cont = fn.readlines()
type(cont)
for i in range(1, len(cont) + 1):
    if i % 2 != 0:
        fn1.write(cont[i - 1])
    else:
        pass

fn1.close()
fn1 = open(
    r"D:\\OneDrive - SBaisakh\\OneDrive\Documents\\codingal-projects\\python.py\\New folder (2)\\sample_doc.txt",
    "r",
)
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()

# Activity_2
for line in fn.readlines():
    if not (line.startswith("Coding")):
        print(line)
        fn1.write(line)

fn.close()
fn1.close()
