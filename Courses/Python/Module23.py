# Handling Exceptions

print("\n-> Handling Exceptions - Example 1")


try:
    print(0/0)

except ZeroDivisionError:
    print("You can't divide by zero!")


print("\n-> Handling Exceptions - Example 2")

import sys

try:
    number = int(input("Enter a number between 1-10 : "))
except ValueError:
        print("Please use numbers only")
        sys.exit() #Foces program to stop gracefully after the error

print("You entered the number ", number)


print("\n-> Handling Exceptions - Example 3")

import sys

try:
    number = int(input("Enter a number between 1-10 : "))
except ValueError:
        print("Please use numbers only")
        sys.exit() #Foces program to stop gracefully after the error
else:
     print("You entered the number ", number)
finally:
     print("The End.")