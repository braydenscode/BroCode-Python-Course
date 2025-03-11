# This is my first Python program

print("I like pizza!")
print("It's really good")

#Strings
first_name = "Brayden"
food = "pizza"
email = "fake@email.com"

#Integers
age = 18
quantity = 3
num_of_students = 30

#Floats
price = 10.99
gpa = 3.2
distance = 5.5

#Booleans
is_student = True
for_sale = False
is_online = True

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance}km")
print(f"Are you a student? {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("You are offline")


# Learned to print text to console, 4 basic data types, and if statements