# Data structures in Python

# sorting in python

items = [
    ("product1", 10),
    ("product2", 0),
    ("product3", 100),
    ("product4", 90),
]


items.sort(key=lambda items: items[1], reverse=True)
print(items)
