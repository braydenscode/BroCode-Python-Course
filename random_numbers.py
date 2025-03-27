import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(1,20)
# number = random.randint(low, high)
# number = random.random()              # random floating point number 0-1
option = random.choice(options)
random.shuffle(cards)

# print(number)
print(option)
print(cards)