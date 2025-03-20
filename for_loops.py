# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# Can use continue to skip in a sequence and break to escape the loop

credit_card = "1234-5678-9012-3456"

for x in reversed(range(1, 11)):
    print(x)

print("Happy new year!")

print("\nCount in multiples of 3")
for x in range(0, 31, 3):
    print(x)

print("\nCredit card digits")
for x in credit_card:
    print(x)

print("\nSkip unlucky #13")
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)