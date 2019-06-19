import random

# random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# This is my solution

# guess = int(input("Guess a number between 1 and 10: "))
# play = "y"
# while guess != random_number:
#     if play == "y":
#         if guess < random_number:
#             print("Too low, guess again")
#             guess = int(input())
#         elif guess > random_number:
#             print("Too high, guess again")
#             guess = int(input())
#         print("You guessed correct")
# # BONUS - let player play again if they want!
#     play = input("Would you like to play again (y/n) ")
#     if play == "n":
#         break
#     random_number = random.randint(1,10)
#     guess = int(input("Guess a number between 1 and 10: "))

# This is Colt's solution v1

# guess = None
# while guess != random_number:
#     guess = int(input("Pick a number from 1 to 10: "))
#     if guess > random_number:
#         print("Too High")
#     elif guess < random_number:
#         print("Too Low")
#     else:
#         print("You got it")

# This is Colt's solution v2
# This loops forever until you break out of the code by answering "n" to the play again question
random_number = random.randint(1,10)  # numbers 1 - 10

while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess > random_number:
        print("Too High")
    elif guess < random_number:
        print("Too Low")
    else:
        print("You got it")
        play_again = input("Do you want to play again (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing")
            break