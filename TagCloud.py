class Product:
    def __init__(self,  price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # price = property(setPrice, getPrice)


product1 = Product(78)
product1.price = 2
print(product1.price)
