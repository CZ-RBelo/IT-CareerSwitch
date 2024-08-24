# Using Default Arguments

print("\n-> Using Default Arguments")

def student(fisrtname, lastname = "Bigger", major = "Information Technology"):
    print(fisrtname,lastname, "majors in", major )

# 1 argument

student("Tony")

# 3 arguments

student("Tony", "Stark", "Physics")

# 2 arguments

student("Stan", "Lee")