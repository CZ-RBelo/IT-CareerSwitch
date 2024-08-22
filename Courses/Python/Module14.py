# Working with NESTING FOR Loops


print("\n-> NESTING FOR Loops Statement - Example 1")

outer = ['outer1', 'outer2', 'outer3']
nest = ['nest1', 'nest2', 'nest3']

for x in outer:
    print("\n"+x)
    for y in nest:
        print(x, y)

print("\n-> NESTING FOR Loops Statement - Example 2")

numbers = [1,2,3]
letters = ['a','b','c']

for x in numbers:
    print(x)
    for y in letters:
        print(y)
    print("\n")