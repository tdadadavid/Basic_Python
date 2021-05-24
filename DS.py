# Data structures in Python

# filtering in python

products = [
    ("product10", 2),
    ("product11", 90),
    ("product15", 267),
    ("product12", 30)
]

# list comprehension is a super
# cool way of mapping and filtering
# list comprehension syntax = [expression for..in loop]


# list comprehension for mapping
prices = [product[1] for product in products]
print(prices)
# the code above is far better the the best way of mapping


# list comprehension for filtering
filtered = [product[1] for product in products if product[1] >= 10]
print(filtered)
