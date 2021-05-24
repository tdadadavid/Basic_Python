# Data structures in Python

# sorting in python

items = [
    ("product1", 10),
    ("product2", 0),
    ("product3", 100),
    ("product4", 90),
]


def sort_item(items):
    return items[1]


items.sort(key=sort_item, reverse=True)
print(items)
