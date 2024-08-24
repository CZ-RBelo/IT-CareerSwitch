# Using Keyword and Positional Arguments

print("\n-> Using Keyword and Positional Arguments")



print("\n-> 1 keyword arguments")
def greet(name, msg = "How are you today?"):
    print("Hey", name + ", " + msg)


print("\n-> 2 keyword arguments")
greet(name = "Dave", msg = "How are you today?")


print("\n-> 2 keyword arguments (out of order)")
greet(msg = "How do you do?", name = "Dave")


print("\n-> 1 positional, 1 keyword arguments")
greet("Dave", msg = "How you doing?")