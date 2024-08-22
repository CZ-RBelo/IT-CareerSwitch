# Working with Files


print("\n-> Reading Files - read()")

a = open("Module15.txt", "r")
print(a.read())
a.close()


print("\n-> Reading Files - Readline() - first line")

a = open("Module15.txt", "r")
print(a.readline())
a.close()


print("\n-> Reading Files - read() - first 7 characters")

a = open("Module15.txt", "r")
print(a.read(7))
a.close()


print("\n-> Reading Files - as myfile")

with open("Module15.txt") as myfile:
    contents = myfile.read()
    print(contents)
    a.close()


print("\n-> Writing Files: 'a' - Append")

a = open("Module15.txt", "a")
a.write("\nHere is another line in our text file")
a.close()

a = open("Module15.txt", "r")
print(a.read())
a.close()


print("\n-> Writing Files: 'w' - Overwrite")

a = open("Module15.txt", "w")
a.write("Hello Rui!")
a.write("\nHello World!")
a.close()


print("\n-> Creating Files: 'a' - Append")
print("\n-> Creating Files: 'w' - Write")
print("\n-> Creating Files: 'x' - Create")

y = open("Module15 - X iFile.txt", "x")
y.write("Hello Rui!")
y.write("\nHello World!")
y.close()

y = open("Module15 - X iFile.txt", "a")
b = 1
while b < 4:
    y.write("\nHere is line" + str(b))
    b +=1
y.close()

y = open("Module15 - X iFile.txt", "r")
print(y.read())
y.close()



