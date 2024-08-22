# Working with IF Statements


print("\n-> IF Statement")
x = 1
y = 3
if x > y:
    print("X is greater than Y")


print("\n-> IF and ELSE Statement")
x = 1
y = 3
if x > y:
    print("X is greater than Y")
else:
    print("Y is greater than X")


print("\n-> ELSE IF Statement")
x = 3
y = 3
if x > y:
    print("X is greater than Y")
elif x == y:
    print("Y and X are equal")
else:
    print("Y is greater than X")


print("\n-> Working with IN statements")

requested_options = ['leather', 'sun roof']

if 'leather' in requested_options:
    print("Nice leather interior")
if 'alarm' in requested_options:
    print("Keeping the bad guys away!")
if 'sun roof' in requested_options:
    print("Letting the sun in")

print("\nFinished making your car!")