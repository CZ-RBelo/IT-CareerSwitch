# Working with operators

""" 
Comparison Operators

== Equal
!= Not equel
> Greater Than
< Less Than
>= Greater Than or Equal To
<= Less Than or Equal To
"""

# Greater Than or Equal To Example
print("\n-> Greater Than or Equal To")

x = 10
y = 12

print(x >= y)

x = 12
y = 10

print(x >= y)

""" 
Logical Operators

and - True if both statements are true - Example: x < 3 and x < 6
or - True if either statements are true - Example: x < 3 or y > 4
not - Reverses the state of the operand - Example: not(x < 3 and x < 6)

"""

print("\n-> AND")
a = 5
print (a > 2 and a < 7)
print (a > 2 and a < 5)


print("\n-> NOT")
a = 4
print (not(a > 2 and a < 7))
print (not(a > 2 and a < 4))