# Reading Console Inputs

print("\n-> Reading Console Inputs")

txt = input("Can you see this? Yes or No")
print("You said ", txt)


print("\n-> Input with Numbers")

txt = input("Give me a number:")
num = int(txt)
print("The number you gave is: ", num)

txt = int(input("Give me a number:"))
print("The number you gave is: ", txt)



print("\n-> Errors")

txt = input("Give me a number:")
try:
    num = int(txt)
    print("The number you gave is:", num)
except ValueError:
    print("Please put in a real number, not a tring or text")


print("\n-> Formatting Output")

salary = 44000
txt = "You make {} dollars a year"
print(txt.format(salary))


print("\n-> Curly Bracket Parameters")

string = "Dave teachs {} {}, and has {} {}."
print(string.format("cyber", "security", 14, "certifications"))


print("\n-> Curly Bracket Parameters - Referencing Variable Substitutions")

string = "Dave loves {1} {3}, and has {2} {0}."
print(string.format("kids", "cyber", 7, "security"))


print("\n-> Curly Bracket Parameters - Named indexes")

string = "Bob like to play {act}, and eat {1} {0}."
print(string.format("dogs", "hot", act="games"))

print("Bob like to play {act}, and eat {1} {0}.".format("dogs", "hot", act="games"))