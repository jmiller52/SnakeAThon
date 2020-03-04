# Dictionary format: Variable = {"Key": "Value"}
# Key and value can be a string or number

cat = {"name": "blue", "age": 3.5, "isCute": True}
print(cat)

cat2 = dict(name="kitty", age=0.5)
print(cat2)

# Accessing a specific bit of information in a dictionary
cat["name"] # this would result in "blue" being referenced

# access all values in a dictionary
# Use .values() can also use .keys() for the keys side
# To access both we use .items()
# To access in a for loop you provide 2 variables (for k,v in instructor.items())
# Example:
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "His Favorite Number!"
}

for value in instructor.values():
    print(value)
# "Colt"
# True
# 4
# "Python"
# False
# "His Favorite Number!"

# Testing for the presence of a Key in a dictionary you use the keyword "in"
# "key" in dictionary_name
"name" in instructor

# if you wanted to test for a Value you need to use the .values() as well:
"num_courses" in instructor.values()

# DICTIONARY METHODS
# clear()  empties out the dictionary
# copy()   make a copy of the dictionary but the variables that are used are not the same.  They are differnt values in memory c is d = False
# fromkeys()  usually called on an empty dictionary. Often used to create default dictionaries.  new_user = {}.fromkeys(['name', 'email'], 'unknown')
# This would create a dictionary new_user with {'name': 'unknown', 'email': 'unknown'}
# get()  Retrieves a key in an object and return None instead of a KeyError if the key does not exist.