# Working with operators

""" 
Identity Operators

is - True if both are same - Example: a is b
is not - True if both are not same - Example: a is not b

"""

print("\n-> IS")

a = 2
b = 6
c = a
print(a is b)
print(a is c)


print("\n-> IS NOT")

a = 2
b = 6
c = a
print(a is not b)
print(a is not c)


""" 
Membership Operators

in - True if a value is present - Example: a in b
not in - True if a value is not present - Example: a not in b

"""

print("\n-> IN")

numbers = [1,2,3,4]

print(1 in numbers)
print(5 in numbers)

print("\n-> NOT IN")

print(1 not in numbers)
print(5 not in numbers)

""" 
Bitwise Operators

& - AND
| - OR
^ - XOR (set 1 if only one is 1)

"""

print("\n-> Bitwise Operators")

a = 24
b = 60

print(bin(a))
print(bin(b))

print("\n-> Bitwise Operators: & (AND)")

a = 24
b = 60
print(a & b)

print("\n-> Bitwise Operators: | (OR)")

a = 24
b = 60
print(a | b)


print("\n-> Bitwise Operators: XOR")

a = 24
b = 60
print(a ^ b)

x = 223
y = 111
print(x ^ y)