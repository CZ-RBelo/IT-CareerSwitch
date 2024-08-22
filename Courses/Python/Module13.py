# Working with WHILE Loops


print("\n-> WHILE Loops Statement")

a = 1
while a < 6:
    print(a)
    a += 1

x = "Hello World"
y = 1
while y <=3:
    print(str(y) + " - " + x)
    y +=1


print("\n-> WHILE Loops with CONTINUE Statement")

a = 0
while a < 6:
    a += 1
    if a == 4:
        continue
    print(a)


print("\n-> WHILE Loops with BREAK Statement")

a = 1
while a < 14:
    print(a)
    if a == 4:
        break
    a += 1