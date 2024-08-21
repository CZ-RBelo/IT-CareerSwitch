# Working with Multiple Assignment

a, b = 5, 10

c = d = 20

print("a: "+str(a))
print("b: "+str(b))
print("c: "+str(c))
print("d: "+str(d))

# Multiple Assignment in FOR LOOPS

numbers = {"First Num": '1', "Second Num": '2'}
for key, value in numbers.items():
    print(F"Key {key} has a value of {value}")


# Practice Time

int_1, int_2, int_3 = 10,20,30

print(int_1)
print(int_2)
print(int_3)

var_1, var_2, var_3, var_4 = (33, "car", 2.158, "hey")

print("var_1 value: " + str(var_1) + " type: " + str(type(var_1)))
print("var_2 value: " + str(var_2) + " type: " + str(type(var_2)))
print("var_3 value: " + str(var_3) + " type: " + str(type(var_3)))
print("var_4 value: " + str(var_4) + " type: " + str(type(var_4)))

loop_assignmet = {"Dave": '41', "Bob": '22', "Mark": '38'}
for key, value in loop_assignmet.items():
    print(F"{key} is {value} years old.")
