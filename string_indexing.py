# indexing = accessing elements of a sequence using [] (indexing operator)
#       [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[4]) # Print the character at index 4
print(credit_number[0:4]) # Print string from the 0 index to index 4
print(credit_number[5:]) # Print string from 5th index onward
print(credit_number[-1]) # Reverse index (find last character)
print(credit_number[::2]) # Increment index by 2

last_digits = credit_number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] # Easy way to reverse string
print(credit_number)