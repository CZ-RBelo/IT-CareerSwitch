# Working Margin Emails

src_folder="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/"

print("\n-> Margin Emails - open with statement")

with open(src_folder+"Hello.txt", "w") as file:
    file.write("Hey there!")

x = open(src_folder+"Hello.txt","r")
print(x.read())
x.close()

print("\n-> Margin Emails")

with open(src_folder+"Names.txt", "w") as file:
    file.write("Dave")
    file.write("\nBob")
    file.write("\nSara")
    file.write("\nMike")
    file.write("\nTerry")
    file.write("\nHenry")

with open(src_folder+"Message.txt", "w") as file:
    file.write("\n")
    file.write("Welcome to the party!")
    file.write("\nWe hope you can make it. Food, fun and friends!")

with open(src_folder+"Names.txt", "r") as n_file:
    with open(src_folder+"Message.txt", "r") as m_file:

        body = m_file.read()
        for name in n_file:

            mail = "Hello "+name+" "+body
            with open(src_folder+name.strip()+".txt", "w") as m_file:
                m_file.write(mail)

print("\n-> Names File")
names = open(src_folder+"Names.txt","r")
print(names.read())
names.close()

print("\n-> Message File")
message = open(src_folder+"Message.txt","r")
print(message.read())
message.close()

print("\n-> Bob File")
bob = open(src_folder+"Bob.txt","r")
print(bob.read())
bob.close()


# Deletes all created files

input() #Wait for a Keypress

print("\n-> Delete Files")
import os
os.remove(src_folder+"Hello.txt")
os.remove(src_folder+"Names.txt")
os.remove(src_folder+"Message.txt")
os.remove(src_folder+"Dave.txt")
os.remove(src_folder+"Bob.txt")
os.remove(src_folder+"Sara.txt")
os.remove(src_folder+"Mike.txt")
os.remove(src_folder+"Terry.txt")
os.remove(src_folder+"Henry.txt")