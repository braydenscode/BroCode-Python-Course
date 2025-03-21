# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        prices.append(price)
        foods.append(food)

print()
print("------ YOUR CART ------")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")