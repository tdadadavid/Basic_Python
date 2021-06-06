class Product:
    def __init__(self, price):
        self.setPrice(price)

    def getPrice(self):
        return self.__price

    def setPrice(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product1 = Product(-30)
print(product1.price)
