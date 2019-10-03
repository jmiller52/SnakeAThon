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

# accessing all values in a list
# one way

numbers = [1, 2, 3, 4]

for number in numbers: 
#number automatically stores the value in each index of the numbers list one at a time
    print(number)
# this prints all values in the list


# now with a while loop
i = 0 #required for the while loop. This case used to keep track of what index we are at in the list
while i < len(numbers):
    print(numbers[i])
    i += 1