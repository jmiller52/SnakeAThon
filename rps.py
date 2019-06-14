# print ...rock...
print("...rock...")
# print ...paper...
print("...paper...")
# print ...scissors...
print("...scissors...")
# get input from player 1
player1 = input("Player 1 make your move: ")
# get input from player 2
player2 = input("Player 2 make your move: ")
# print SHOOT!
print("SHOOT!")
# if rock vs paper - paper wins
if player1 == "rock" and player2 == "scissors":
    print("Player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong")
