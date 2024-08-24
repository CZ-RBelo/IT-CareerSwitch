# Reading Command Line Argument

print("\n-> Reading Command Line Argument")


import sys
print("The name our file is: ", (sys.argv[0]))
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))