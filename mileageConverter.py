print("How many kilometers did you cycle today?")
kms = input() # Variable for the kilometers input
miles = float(kms)/1.60934 # Convert input to a float and perform math to change to miles
miles = round(miles, 2) # round the decimals down to 2 digits long
print(f"Your {kms}km ride was {miles}mi!") # prints the output and uses input value and miles(output) in a formated string (fstring)