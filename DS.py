# Data structures in Python

# sorting in python

items = [
    ("product1", 10),
    ("product2", 0),
    ("product3", 100),
    ("product4", 90),
]

prices = []


# A good way of mapping
for item in items:
    prices.append(item[1])

# A better way of mapping
for val in check:
    print(val)

# kinda the best way
check = list(map(lambda item: item[1], items))

print(check)
