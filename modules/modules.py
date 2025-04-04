# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files

# print(help("modules"))
# print(help("math"))
# import math
# import math as m
# from math import pi

# It's a good habit to avoid using 'from' imports as you can override variables
# from math import e
# print(e)
# a, b, c, d, e = 1, 2, 3, 4, 5
# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)

import example

# result = example.pi
result = example.area(3)

print(result)