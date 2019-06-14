# In Python, the following operators can be used to make Boolean Logic comparisons
# and - both sides of the evaluation need to be true
# or - Either side of the evaluation needs to be true for the whole thing to be true
# not - Truthy if the opposite of a is true

city = input("Where do you live? ")

if city == "Broomfield" or city == "Boulder":
    print("You live in the best parts of Colorado!")
else:
    print("You live in the other parts of Colorado.")