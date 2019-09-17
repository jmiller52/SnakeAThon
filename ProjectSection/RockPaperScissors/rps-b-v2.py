print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Make your move: ").lower()
print("*** NO CHEATING!\n\n" * 20)
player2 = input("Make your move: ").lower()

if player1 == player2:
    print("It's a TIE!")
elif player1 == "rock":
    if player2 == "scirrors":
        print("Player1 Wins!")
    elif player2 == "paper":
        print("Player2 Wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player1 Wins!")
    elif player2 == "scissors":
        print("Player2 Wins!")
elif player1 == " scissors":
    if player2 == "paper":
        print("Player1 Wins!")
    elif player2 == "rock":
        print("Player2 Wins!")
else:
    print("Something went wrong")
