# function = A block of reusable code
# place () after the function name to invoke it

def happy_birthday(name, age):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday to {name}")
    print("Happy birthday to you!")
    print(f"You're {age} years old!")
    print()

happy_birthday("BroCode", 25)

def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${float(amount):.2f} is due {due_date}")

display_invoice("brocode", "42.50", "05/01/25")
print()


# return = statement used to end a function
# and send a result back to the caller

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Spongebob", "Squarepants")
print(full_name)