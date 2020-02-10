import random

player_score = 0
comp_score = 0
winning_score = 2

while player_score < winning_score and comp_score < winning_score:
    print("Rock...\nPaper...\nScissors...")
    player = input("Please enter your choice: ").lower()

    rand_num = random.randint(0, 2)
    if rand_num == 0:
        comp = "rock"
    elif rand_num == 1:
        comp = "paper"
    else:
        comp = "scissors"
    print(f"The Computer chooses: {comp}")
    if player == comp:
        print("It's a Tie!")
    elif player == "rock":
        if comp == "paper":
            print("Computer Wins :(")
            comp_score += 1
        else:
            print("Player Wins!")
            player_score += 1
    elif player == "paper":
        if comp == "scissors":
            print("Computer Wins :(")
            comp_score += 1
        else:
            print("Player Wins!")
            player_score += 1
    elif player == "scissors":
        if comp == "rock":
            print("Computer Wins :(")
            comp_score += 1
        else:
            print("Player Wins!")
            player_score += 1
    else:
        print("Please make a valid selection: ")
