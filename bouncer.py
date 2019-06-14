# ask for age
age = input("How old are you? ")
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         # 18-12 wristband
#         print("You may enter but need a wristband")
#     elif age >= 21:
#         # 21+ drink, normal entry
#         print("You are good to ender and are aloud to drink!")
#     else:
#         # too young, sorry
#         print("You can't come in, sorry little one! :P")
# else:
#     print("Please enter an age!")

# This is a cleaner way of writing the above code for checking age
if age:
    age = int(age)
    if age >= 21:
        print("You are good to ender and are aloud to drink!")
    elif age >= 18:
        print("You may enter but need a wristband")
    else:
        print("You can't come in, sorry little one! :P")
else:
    print("Please enter an age!")
