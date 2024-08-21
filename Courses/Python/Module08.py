# Slincing Lists

# Present nums from the index 2 (value 3) to index 5 (value 5)

print("\n-> Slincing Lists")
nums = [1,2,3,4,5,6]

print("\n-> Original list")
print(nums)
print("\n-> Present nums from the index 2 (value 3) to index 5 (value 5)")
print(nums[2:5])

# Slicing with Loop

print("\n-> Slicing with Loop")
players = ["Bob", "Steve", "Michael", "Tom", "Eli"]
print("\n-> Original list")
print(players)

print("\n-> Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n-> Here are the last two players on my team:")
for player in players[3:5]:
    print(player.title())

# Slicing with Increment

print("\n-> Slicing with Increment")
nums = [1,2,3,4,5,6,7,8,9]
print(nums[1:8:3])


# Pratice Time

print("\n-> Pratice Time")
nums = [1,2,3,4,5,6,7,8,9]
print(nums)
print(nums[2:5])
print(nums[0:10:2])

