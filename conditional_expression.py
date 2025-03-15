# conditional expression = A one line shortcut for the if-else statement AKA ternary operator
# print or assign ones of two values based on a condition

num = 6
a = 6
b = 7
age = 18
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(min_num)
print(max_num)
print(status)
print(weather)
print(access_level)