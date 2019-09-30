import random

random_number = random.randint(1, 10)  # random numbers from 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#       otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

while True: # This will loop forever. Careful!!
    guess = int(input("Please guess a number from 1 - 10: "))
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    else:
        print("You Got It!")
        play_again = input("Would you like to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1, 10)  # random numbers from 1 - 10
            guess = None
        else:
            print("Thank you for playing")
            break # Have to break out of the forever loop when player selects "n"
