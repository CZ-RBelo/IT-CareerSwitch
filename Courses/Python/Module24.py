# Using Math and Random Modules

import math
import random

print("\n### Using Math Module ###")


print("\n-> Finding the square root for a given number")


num = int(input("Give me a number to find the square root for "))
print(math.sqrt(num))


print("\n### Using Random Module ###")

print("\nPrinting random number")
print(random.random())


print("\n### Generate Random Integers ###")

print("\nPrinting random integer ", random.randint(0,1000))
print("\nPrinting random integer ", random.randrange(0,500, 2))