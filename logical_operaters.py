# logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be true | and = both conditions must be true | not = inverts the condition

# or OPERATOR
temp = 20
is_raining = True
is_sunny = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor is event cancelled.")
else:
    print("The outdoor event is still scheduled.")

# and OPERATOR

if temp >= 28 and is_sunny:
    print("It is hot outside!")
    print("It is sunny!")
elif temp <= 0 and is_sunny:
    print("It is cold outside!")
    print("It is sunny!")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside.")
    print("It is sunny!")

# not OPERATOR

if temp >= 28 and not is_sunny:
    print("It is hot outside!")
    print("It is cloudy!")
elif temp <= 0 and not is_sunny:
    print("It is cold outside!")
    print("It is cloudy!")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside.")
    print("It is cloudy!")