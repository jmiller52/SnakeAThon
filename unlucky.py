# Loop through numbers 1-20
# for 4 and 13 print "x is unlucky"
# for even numbers print "x is even"
# for odd numbers print "x is odd"

for num in range(1,21):
    if num == 4 or num == 13:
        state = "unlucky"
        # print("{} is unlucky".format(num)) # .format for udemy
        # print(f"{num} is unlucky") #newer f string format which is faster and less characters
    elif num % 2 != 0:
        state = "odd"
        # print("{} is odd".format(num))
        # print(f"{num} is odd")
    else:
        state = "even"
        # print("{} is even".format(num))
        # print(f"{num} is even")
    print(f"{num} is {state}")