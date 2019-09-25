# first we want to get input so we ask a question
msg = input("What are you up to? ")

# start a loop with the input and check if it is equal to "stop copying me"
# if not print the msg and then ask for input again (not text question required this time)
while msg != "stop copying me":
    print(msg)
    msg = input()
print("UGH FINE YOU WIN")
