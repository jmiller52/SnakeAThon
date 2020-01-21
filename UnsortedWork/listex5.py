answer = [[i for i in range(0,3)] for num in range(0,3)]

# first part creates the list with simple values
# i for i in range(0,3) gives you [1,2,3]

# the second part setups up the lists of lists
# [[] for num in range(0,3)] now gives you [[1,2,3],[1,2,3],[1,2,3]]
# the lists that was created in the inner part is then input into a list a number of times based on the range that was specified

answer = [[i for i in range(0,10)] for num in range(0, 10)]