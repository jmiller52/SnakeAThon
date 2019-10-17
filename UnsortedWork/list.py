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


# List comprehension VS looping

# for loop
numbers = [1, 2, 3, 4, 5]
double_numbers = []

for num in numbers:
    double_number = num * 2
    double_numbers.append(double_number)

print(double_numbers) # [2. 4. 6. 8. 10]

# List Comprehension

numberss = [1, 2, 3, 4, 5]

double_numberss = [nums * 2 for nums in numberss]
print(double_numberss)

# more examples

numbs = [numb*10 for numb in range(1,6)] # [10, 20, 30, 40, 50]
print(numbs)

values = [bool(val) for val in [0, '', []]] # [false, false, false]
print(values)

# now with logic
numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0] # only the evens
odds = [num for num in numbers if num % 2 != 0] # only the odds

mix = [num*2 if num % 2 == 0 else num/2 for num in numbers]
# if the value is even it gets doubled otherwise it gets halved
print(mix)