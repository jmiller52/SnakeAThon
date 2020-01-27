import random

print("rock...")
print("paper...")
print("scissors...")

comp_number = random.randint(0,2)
if comp_number == 0:
    computer = "rock"
elif comp_number == 1:
    computer = "paper"
else:
    computer = "scissors"

player = input("Please enter your choice: ").lower()
print(f"Computer chose: {computer.capitalize()}")

if player == computer:
    print("It's a draw!")
elif player == "rock":
    if computer == "paper":
        print("Computer Wins!")
    else:
        print("Player Wins!")
elif player == "paper":
    if computer == "scissors":
        print("Computer Wins!")
    else:
        print("Player Wins!")
elif player == "scissors":
    if computer == "rock":
        print("Computer Wins!")
    else:
        print("Player Wins!")
else:
    print("Please make a valid choice")
