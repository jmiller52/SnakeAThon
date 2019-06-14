from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print("The computer chooses {}".format(computer))
computer == rand_num
print("\nSHOOT!\n")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins!")
    else:
        print("Player wins!")
else:
    print("Please enter a valid move!")
