# *args = allows you to pass multiple non-key arguments
# kwargs = allows you to pass multiple keyword-arguments
#           * unpacking operator
#           1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
print()


print("Print address function")
print()
def print_address(**kwargs):
    for key,val in kwargs.items():
        print(f"{key}:{val}")

print_address(street="123 Fake Street",
              apt="#100",
              city="Detroit",
              state="Michigan",
              zip="54321")

print("Shipping label function")
print()
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake Street",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")