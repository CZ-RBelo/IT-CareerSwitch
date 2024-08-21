# Modifying Lists

employees = ["Sara", "Tammy", "Debbie", "John", "Carrie"]
print(employees[0])

print(" ")
print("---")
print(" ")

employees[0] = "Mark"
print(employees[0])

print(" ")
print("---")
print(" ")

employees = employees + ["Sara"]

print(employees[0])
print(employees[1])
print(employees[2])
print(employees[3])
print(employees[4])
print(employees[5])

print(" ")
print("---")
print(" ")

employees = ["Jim"] + employees
print(employees)

print(" ")
print("---")
print(" ")

employees.insert(1, "Dave")
print(employees)

print(" ")
print("---")
print(" ")

del employees[3]
print(employees)

print(" ")
print("---")
print(" ")

employees.remove("Carrie")
print(employees)

print(" ")
print("---")
print(" ")

for employees_names in employees:
    print(employees_names)

print(" ")
print("---")
print(" ")

if "Dave" in employees:
    print("Yes, Dave does work here!")

print(" ")
print("---")
print(" ")

print(len(employees))

print(" ")
print("---")
print(" ")