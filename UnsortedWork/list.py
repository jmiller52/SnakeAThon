# lists always contain square brackets surrounding the "list of values"
# There is also a list function
# lists always start at index 0

tasks = list(range(10))
# output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

items = [1,"two", 3, "four"]
# This is also a list

print(items[0]) # prints out 1 from the list
print(items[1]) # prints out "two" from the list

# can check if a value is in a list
friends = ["Trevor", "Vong", "Austin"]

"Austin" in friends # Trude
"Colt" in friends # False

# Something that can be done
if "Trevor" in friends:
    print("You have a friend!")
else:
    print("No Friends For You!")