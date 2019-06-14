# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if actually_sick == True and sick_days > 0:
    calling_in_sick = True
    print("I am sick so I am staying home. You have {} sick days left.".format(sick_days))
elif (kinda_sick == True and hate_your_job == True) and sick_days > 0:
    calling_in_sick = True
    print("I'm not feeling up to working today. You have {} sick days left.".format(sick_days))
elif sick_days == 0:
    print("You are out of sick days!")
else:
    calling_in_sick = False
    print("Heading into")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
