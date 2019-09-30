import random

random_number = random.randint(1,10) # random numbers from 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#       otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

guess = None

# while guess != random_number:
#     if play_again == "y":
#         random_number = random.randint(1, 10)
#         guess = int(input("Please guess a number from 1 - 10: "))
#         if guess < random_number:
#             print("Your guess is too low")
#             guess = int(input("Guess again: "))
#         elif guess > random_number:
#             print("Your guess is too high")
#             guess = int(input("Guess again: "))
#         elif guess == random_number:
#             print("Great guess, you win!")
#             play_again = input("Would you like to play again (y/n) ")
#     else:
#         print("Thanks for playing")
#         break

# Revised order
while guess != random_number:
    guess = int(input("Please guess a number from 1 - 10: "))
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    else:
        print("You Got It!")
