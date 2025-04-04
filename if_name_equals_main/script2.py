from script1 import *

# print(__name__)

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("Pizza")
    favorite_drink("Redbull")
    print("Goodbye")

if __name__ == "__main__":
    main()