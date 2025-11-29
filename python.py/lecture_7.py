# Activity_1
lst = ["apple", "banana", "fig", "grape", "cherry", "eldercherry"]
print("The original  list is :", lst)
print("Tthe length of the list is :", len(lst))

print("the first element of the list is :", lst[0])
print("the last element of the list is", lst[5])
print("the last element of the list is", lst[-1])

lst.append("Kiwi")
print("The list after adding Kiwi is :", lst)

lst.remove("fig")
print("The list after removing fig is", lst)

lst.sort()
print("The list after sorting is ;", lst)

lst.reverse()
print("The list after reversing is :", lst)

lst.clear()
print("The list after clearing is :", lst)
print(lst)

# Activity_2
my_dict = {
    "name": "john",
    "age": 29,
    "city": "Newyork",
    "country": "usa",
    "email ": "john@gmail.com",
    "phone": 1234567898,
}

print("the original dictionary is :", my_dict)
print("the value of the key name is :", my_dict["name"])
print("the value of the key age is :", my_dict["age"])

my_dict["state"] = "newyork"


# activity_3
def test(lst1):
    result = {}
    for item in lst1:
        result[item[0] == item[1:]]
    return result


student_list = [
    ("john", 35, "newyork"),
    ("jane", 30, "los angeles"),
    ("paul", 20, "chicago"),
]

print(test(student_list))
print("/n original list of lists is :", student_list)
print("convert the said list of list in the dictionary ;", student_list)
