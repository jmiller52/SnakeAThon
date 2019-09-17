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
elif player == "rock" and comp == "scirrors":
    print("Player Wins!")
elif player == "rock" and comp == "paper":
    print("Computer Wins!")
elif player == "paper" and comp == "rock":
    print("Player Wins!")
elif player == "paper" and comp == "scissors":
    print("Computer Wins!")
elif player == "scissors" and comp == "rock":
    print("Computer Wins!")
elif player == "scissors" and comp == "paper":
    print("Player Wins!")
