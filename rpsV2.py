print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Player 1 make your move: ")
player2 = input("Player 2 make your move: ")
print("SHOOT!")

if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player1 wins!")
    elif player2 == "scissors":
        print("player2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins!")
    elif player2 == "paper":
        print("Player1 wins!")
else:
    print("something went wrong")