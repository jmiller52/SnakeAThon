import random

# guess = int(input("Guess a number between 1 and 10: "))
# play = "y"

# while play == "y":
#     rnum = random.randint(1, 10)
#     while guess != None:
#         if guess == rnum:
#             print("You guessed it! You won!")
#             play = input("Do you want to play again? (y/n) ")
#             break
#         elif guess < rnum:
#             print("Too low, Try Again!")
#             guess = int(input("Guess a number between 1 and 10: "))
#         else:
#             print("Too high, Try again!")
#             guess = int(input("Guess a number between 1 and 10: "))


# rnum = random.randint(1, 10)
# guess = None

# while guess != rnum:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess == rnum:
#         print("You Win!")
#     elif guess > rnum:
#         print("Too High!")
#     else:
#         print("Too Low!")

# refined version again

rnum = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))    
    if guess < rnum:
        print("Too Low!")
    elif guess > rnum:
        print("Too High!")
    else:
        print("You Win!")
        play_again = input("Would you like to play again? (y/n)")
        if play_again == "y":
            rnum = random.randint(1, 10)
            guess == None
        else:
            print("Thank you for playing!")
            break
