import random

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("(Make your move): ").lower()

rand_num = random.randint(0,2)
if rand_num == 0:
    comp = "rock"
elif rand_num == 1:
    comp = "paper"
else:
    comp = "scissors"

print(f"Computer chooses: {comp.capitalize()}")

if player == comp:
    print("It's a TIE!")
elif player == "rock":
    if comp == "scissors":
        print("Player Wins!")
    else:
        print("Computer Wins!")
elif player == "paper":
    if comp == "rock":
        print("Player Wins!")
    else:
        print("Computer Wins!")
elif player == "scissors":
    if comp == "rock":
        print("Computer Wins!")
    else:
        print("Player Wins!")
