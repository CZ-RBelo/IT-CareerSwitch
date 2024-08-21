# Sorting and Reversing Lists

print("\n-> Original list")
colors = ["blue","red", "yellow", "green"]
print(colors)

# Sort the list ascending

print("\n-> Sort the list ascending")
colors = ["blue","red", "yellow", "green"]
colors.sort()
print(colors)

# Reverse that alphabetically

print("\n-> Reverse that alphabetically")
colors = ["blue","red", "yellow", "green"]
colors.sort(reverse=True)
print(colors)

# Just reverse the order

print("\n-> Just reverse the order")
colors = ["blue","red", "yellow", "green"]
colors.reverse()
print(colors)

# Order the list but doen's affect the actual order

print("\n-> Order the list but doen's affect the actual order")
colors = ["blue","red", "yellow", "green"]

print("\n-> Original List")
print(colors)

print("\n-> The Sorted List")
print(sorted(colors))

print("\n-> Original List, again")
print(colors)

