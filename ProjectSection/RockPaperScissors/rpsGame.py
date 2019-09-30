import random
mode = int(input(
    "ENTER 1 for 'Best out of how many'\nOR\nENTER 2 for 'First to how many'\nWhich Game Mode: "))

player_wins = 0
comp_wins = 0
if mode == 1:
    times = int(input("Out of how many: "))
    time = 1
    while time <= times:
        time += 1
        print(f"Player wins: {player_wins} Computer wins: {comp_wins}")
        print("...rock...")
        print("...paper...")
        print("...scissors...")

        player = input("(Make your move): ").lower()
        if player == "quit" or player == "q":
            break

        rand_num = random.randint(0, 2)
        if rand_num == 0:
            comp = "rock"
        elif rand_num == 1:
            comp = "paper"
        else:
            comp = "scissors"

        print(f"Computer chooses: {comp}")

        if player == comp:
            print("It's a TIE!")
        elif player == "rock":
            if comp == "scissors":
                print("Player Wins!")
                player_wins += 1
            else:
                print("Computer Wins!")
                comp_wins += 1
        elif player == "paper":
            if comp == "rock":
                print("Player Wins!")
                player_wins += 1
            else:
                print("Computer Wins!")
                comp_wins += 1
        elif player == "scissors":
            if comp == "rock":
                print("Computer Wins!")
                comp_wins += 1
            else:
                print("Player Wins!")
                player_wins += 1
        else:
            print("Please enter a valid move!")
    print(
        f"\n\nFINAL SCORES... \n Player:{player_wins} \n Computer {comp_wins}")
    if player_wins > comp_wins:
        print("Congratulations, You Win!!")
    elif player_wins == comp_wins:
        print("It's a TIE!")
    else:
        print("The Computer Wins!")
else:
    times = int(input("First to: "))
    while player_wins < times and comp_wins < times:
        print(f"Player wins: {player_wins} Computer wins: {comp_wins}")
        print("...rock...")
        print("...paper...")
        print("...scissors...")

        player = input("(Make your move): ").lower()
        if player == "quit" or player == "q":
            break

        rand_num = random.randint(0, 2)
        if rand_num == 0:
            comp = "rock"
        elif rand_num == 1:
            comp = "paper"
        else:
            comp = "scissors"

        print(f"Computer chooses: {comp}")

        if player == comp:
            print("It's a TIE!")
        elif player == "rock":
            if comp == "scissors":
                print("Player Wins!")
                player_wins += 1
            else:
                print("Computer Wins!")
                comp_wins += 1
        elif player == "paper":
            if comp == "rock":
                print("Player Wins!")
                player_wins += 1
            else:
                print("Computer Wins!")
                comp_wins += 1
        elif player == "scissors":
            if comp == "rock":
                print("Computer Wins!")
                comp_wins += 1
            else:
                print("Player Wins!")
                player_wins += 1
        else:
            print("Please enter a valid move!")
    print(
        f"\n\nFINAL SCORES... \n Player:{player_wins} \n Computer {comp_wins}")
    if player_wins > comp_wins:
        print("Congratulations, You Win!!")
    elif player_wins == comp_wins:
        print("It's a TIE!")
    else:
        print("The Computer Wins!")
