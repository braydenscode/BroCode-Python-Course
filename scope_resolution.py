# variable scope = when a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

#Showcasing LEGB order

# def func1():
#     x = 1
#
#     def func2():
#         x = 2
#         print(x)
#     func2()
#
# func1()

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

x = 3

func1()
func2()

from math import e

def func3():
    print(e)

e = 3

print(e)