# Data structures in Python


# matrix = [[0, 1], ["bola", "King"]]

# for items in matrix:
#     print(items[1])

# numbers = list(range(20))
# print(numbers[::-1])


letters = ["a", "b", "c", "d", "e", "f"]

# Add an element to a list
# Using append fnc or the insert fnc

# letters.append("D")
# letters.insert(6, "y")


# Remove element from a list
# Using pop fnc || remove fnc
# del keyword || clear fnc


letters.pop()
letters.remove("c")
del letters[0:2]
letters.clear()


print(letters)
