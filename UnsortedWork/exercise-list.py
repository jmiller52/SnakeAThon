sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""
# for i in sounds:
#     result += i.upper()

# result starts as an empty sring
# as you iterate through the list in the for loop you update "result" with its current value + the value currently being evaluated by the loop

i = 0
while i < len(sounds):
    result += sounds[i].upper()
    i += 1