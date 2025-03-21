# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")

# print(fruits[0])
# print(fruits[::-1])

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("coconut"))


# view possible methods
# print(dir(fruits))

# explanation of possible methods
# print(help(fruits))


# print(len(fruits))

# fruits[0] = "pineapple"

# fruits.append("pineapple")
# print("pineapple" in fruits)
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.count("banana"))

print(fruits)

for fruit in fruits:
    print(fruit)