# activity_1  (use tuple, not set)
my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, 2, 3, "hi")
print(my_tuple)

my_tuple = (1, 2, 3, "hi", 4.5)
print(my_tuple)

my_tuple = (1, 2, 3, "hi")
print(my_tuple)

# tuple supports indexing
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# slicing tuple
print(my_tuple[0:3])


# activity_2 (sets)
my_set = {1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9}
print("my_set:", my_set)  # duplicates removed automatically

my_set.add(10)
print("updated my_set:", my_set)

set1 = my_set
set2 = {10, 1, 2, 3, 14, 15}

print("Difference", set1.difference(set2))


# activity_3 (union)
setun1 = {"green", "blue"}
setun2 = {"blue", "yellow"}
print("union", setun1.union(setun2))


# activity_4 (intersection)
setx = {"apple", "banana"}
sety = {"banana", "orange"}
print("intersection", setx.intersection(sety))
