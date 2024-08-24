# Defining functions

src_folder="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/"

print("\n-> Defining functions")

def first_function():
    print("Hello World!")

first_function()


def fname_function(fname):
    print("\nHello " + fname)

fname_function("Dave")
fname_function("Bob")
fname_function("Cindy")

#Calling the "Module20-Hello.py" module

import Module20_Hello
Module20_Hello.greet()