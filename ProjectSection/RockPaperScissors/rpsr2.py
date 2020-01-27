print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter player 1's choice): ")
player2 = input("(enter player 2's choice): ")
print("SHOOT!")

if player1 == player2:
    print("It's a draw")
elif player1 == "rock":
    if player2 == "paper":
        print("player2 wins")
    else:
        print("player1 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    else:
        print("player2 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins")
    else:
        print("player1 wins")
else:
    print("Please enter a valid rock, paper or scissor choice.")