import random
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print("rock...")
    print("paper...")
    print("scissors...")

    player = input("Please enter your choice: ").lower()
    if player == "quit" or player == "q":
        break
    comp_number = random.randint(0,2)
    if comp_number == 0:
        computer = "rock"
    elif comp_number == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print(f"Computer chose: {computer.capitalize()}")

    if player == computer:
        print("It's a draw!")
    elif player == "rock":
        if computer == "paper":
            print("Computer Wins!")
            computer_wins += 1
        else:
            print("Player Wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "scissors":
            print("Computer Wins!")
            computer_wins += 1
        else:
            print("Player Wins!")
            player_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer Wins!")
            computer_wins += 1
        else:
            print("Player Wins!")
            player_wins += 1
    else:
        print("Please make a valid choice")
print(f"Final Scores... Player: {player_wins} Computer: {computer_wins}")
